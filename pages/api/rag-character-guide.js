import mistbornData from '../../../rag_data/mistborn1.json';

// Mock GPT function (in production, we'd call OpenAI API)
async function generateGuide(chapters) {
  // In real RAG we'd send to GPT with instructions; here we just combine summaries
  const combined = chapters.map(ch => ch.summary).join(" ");
  return `**Spoiler-Free Character Guide (Prototype)**\n\nUsing the following chapters: ${combined}`;
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { series, book, chapter } = req.body;

  if (series !== 'Mistborn' || book !== 1) {
    return res.status(400).json({ error: 'RAG prototype only works for Mistborn Book 1.' });
  }

  // Get all summaries up to the requested chapter
  const chapters = mistbornData.filter(c => c.chapter <= chapter);
  const guide = await generateGuide(chapters);

  res.status(200).json({ guide });
}
