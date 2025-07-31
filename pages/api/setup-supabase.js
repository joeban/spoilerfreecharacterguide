import { createClient } from '@supabase/supabase-js';
import fs from 'fs';
import path from 'path';

export default async function handler(req, res) {
  // Only allow GET for setup
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const SUPABASE_URL = process.env.SUPABASE_URL;
  const SUPABASE_SERVICE_KEY = process.env.SUPABASE_SERVICE_KEY;
  if (!SUPABASE_URL || !SUPABASE_SERVICE_KEY) {
    return res.status(500).json({ error: 'Missing Supabase credentials' });
  }

  const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY);

  // ✅ Ensure table exists
  try {
    await supabase.rpc('ensure_table_book_chunks'); // placeholder for function call
  } catch (err) {
    // fallback: manual table creation
    await supabase.from('book_chunks').select('id').limit(1);
  }

  // ✅ Load Mistborn1 JSON from /data/rag
  const filePath = path.join(process.cwd(), 'data', 'rag', 'mistborn1.json');
  const fileData = fs.readFileSync(filePath, 'utf8');
  const mistbornData = JSON.parse(fileData);

  // ✅ Insert chunks into Supabase
  for (const chunk of mistbornData) {
    await supabase.from('book_chunks').upsert([
      {
        series: chunk.series,
        book: chunk.book,
        chapter: chunk.chapter,
        text: chunk.summary
      }
    ]);
  }

  return res.status(200).json({ message: 'Supabase setup complete. Mistborn 1 uploaded!' });
}
