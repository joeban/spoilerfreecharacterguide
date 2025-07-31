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
    // ✅ Add unique constraint (series, book, chapter) if not already there
    const { error: constraintError } = await supabase.rpc('exec_sql', {
      sql: `ALTER TABLE book_chunks ADD CONSTRAINT IF NOT EXISTS unique_book_chunk UNIQUE (series, book, chapter);`
    });

    if (constraintError) {
      console.warn('Constraint creation may have failed (or already exists):', constraintError.message);
    }

    // ✅ Load Mistborn1 JSON
    const filePath = path.join(process.cwd(), 'data', 'rag', 'mistborn1.json');
    const fileData = fs.readFileSync(filePath, 'utf8');
    const mistbornData = JSON.parse(fileData);

    // ✅ Prepare rows for bulk insert
    const rows = mistbornData.map(ch => ({
      series: ch.series,
      book: ch.book,
      chapter: ch.chapter,
      text: ch.summary
    }));

    // ✅ Bulk upsert all 38 chapters
    const { data, error } = await supabase
      .from('book_chunks')
      .upsert(rows, { onConflict: ['series', 'book', 'chapter'] });

    if (error) {
      console.error('Supabase insert error:', error);
      return res.status(500).json({ error: 'Bulk insert failed' });
    }

    return res.status(200).json({ message: `Supabase setup complete. Inserted ${rows.length} chapters for Mistborn Book 1.` });
  } catch (err) {
    console.error('Setup error:', err);
    return res.status(500).json({ error: 'Setup route failed' });
  }
}
