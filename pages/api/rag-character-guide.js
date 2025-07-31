import { createClient } from '@supabase/supabase-js';
import OpenAI from 'openai';

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_KEY);

// ---- Basic in-memory rate limiter ----
const requests = {};
const LIMIT = 20;
const WINDOW = 60 * 60 * 1000;

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress || 'unknown';
  const now = Date.now();

  if (requests[ip]) {
    requests[ip] = requests[ip].filter(ts => now - ts < WINDOW);
  } else {
    requests[ip] = [];
  }

  if (requests[ip].length >= LIMIT) {
    return res.status(429).json({ error: 'Rate limit exceeded. Please wait before trying again.' });
  }
  requests[ip].push(now);

  const { series, book, chapter } = req.body;

  if (series !== 'Mistborn' || book !== 1) {
    return res.status(400).json({ error: 'RAG prototype only works for Mistborn Book 1.' });
  }

  try {
    // ✅ Query Supabase for all summaries up to the requested chapter
    const { data, error } = await supabase
      .from('book_chunks')
      .select('*')
      .eq('series', series)
      .eq('book', book)
      .lte('chapter', chapter)
      .order('chapter', { ascending: true });

    if (error) {
      console.error('Supabase error:', error);
      return res.status(500).json({ error: 'Database query failed' });
    }

    const combinedSummaries = data.map(c => `Chapter ${c.chapter}: ${c.text}`).join('\n');

    const prompt = `You are a spoiler-safe character guide writer.
Using only the provided summaries up to Chapter ${chapter} of Mistborn Book 1,
write a concise, spoiler-free character guide for the reader.
Never mention or hint at future plot events.
Always include basic context for each character mentioned so far, as if reminding a returning reader who they are.`;

    const completion = await client.chat.completions.create({
      model: "gpt-4o",
      messages: [
        { role: "system", content: "You write spoiler-safe character guides for fantasy and sci-fi books." },
        { role: "user", content: `${prompt}\n\nSummaries so far:\n${combinedSummaries}` }
      ],
      max_tokens: 700,
      temperature: 0.7
    });

    const guideText = completion.choices[0].message.content;
    res.status(200).json({ guide: guideText });
  } catch (err) {
    console.error('GPT API Error:', err);
    res.status(500).json({ error: 'Failed to generate guide' });
  }
}
