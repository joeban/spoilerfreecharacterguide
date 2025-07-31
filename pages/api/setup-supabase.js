import { createClient } from '@supabase/supabase-js';
import fs from 'fs';
import path from 'path';

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const SUPABASE_URL = process.env.SUPABASE_URL;
  const SUPABASE_SERVICE_KEY = process.env.SUPABASE_SERVICE_KEY;
  if (!SUPABASE_URL || !SUPABASE_SERVICE_KEY) {
    return res.status(500).json({ error: 'Missing Supabase credentials' });
  }

  const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY);

  try {
    // ✅ Load Mistborn1 JSON
    const filePath = path.join(process.cwd(), 'data', 'rag', 'mistborn1.json');
    const fileData = fs.readFileSync(filePath, 'utf8');
    const mistbornData = JSON.parse(fileData);

    // ✅ Prepare rows for insert
    const rows = mistbornData.map(ch => ({
      series: ch.series,
      book: ch.book,
      chapter: ch.chapter,
      text: ch.summary
    }));

    // ✅ Clear existing rows first
    await supabase.from('book_chunks').delete().neq('series', '');

    // ✅ Insert fresh 38 rows
    const { error } = await supabase.from('book_chunks').insert(rows);

    if (error) {
      console.error('Supabase insert error:', error);
      return res.status(500).json({ error: 'Bulk insert failed' });
    }

    return res.status(200).json({ message: `Inserted ${rows.length} chapters for Mistborn Book 1.` });
  } catch (err) {
    console.error('Setup error:', err);
    return res.status(500).json({ error: 'Setup route failed' });
  }
}
