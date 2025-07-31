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

  try {
    // ✅ Supabase query for all chapters up to selected one
    const { data, error } = await supabase
      .from('book_chunks')
      .select('*')
      .eq('series', series)
      .eq('book', book)
      .lte('chapter', chapter)
      .order('chapter', { ascending: true });

    if (error) {
      console.error('❌ Supabase error:', error);
      return res.status(500).json({ error: `Supabase query failed: ${error.message}` });
    }
    if (!data || data.length === 0) {
      console.warn('⚠️ No chapter data found for query.');
      return res.status(404).json({ error: 'No summaries found in Supabase for this chapter selection.' });
    }

    console.log(`✅ Retrieved ${data.length} chapters from Supabase for ${series} Book ${book} up to Chapter ${chapter}`);

    // ✅ Combine summaries
    const combinedSummaries = data.map(c => `Chapter ${c.chapter}: ${c.text}`).join('\n');

    // ✅ GPT-4o call
    try {
      const completion = await client.chat.completions.create({
        model: "gpt-4o",
        messages: [
          { role: "system", content: "You write spoiler-safe character guides for fantasy and sci-fi books." },
          { role: "user", content: `Write a spoiler-free character guide for Mistborn Book 1 up to Chapter ${chapter} using these summaries:\n${combinedSummaries}` }
        ],
        max_tokens: 700,
        temperature: 0.7
      });

      const guideText = completion.choices[0].message.content;
      return res.status(200).json({ guide: guideText });
    } catch (gptError) {
      console.error('❌ OpenAI API error:', gptError);
      return res.status(500).json({ error: 'OpenAI API call failed. Check your API key or quota.' });
    }

  } catch (err) {
    console.error('❌ General handler error:', err);
    return res.status(500).json({ error: 'Unexpected error in rag-character-guide handler.' });
  }
}
