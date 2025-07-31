import { useState } from 'react';

export default function Mistborn1Page() {
  const [chapter, setChapter] = useState(1);
  const [guide, setGuide] = useState('');

  async function fetchGuide(ch) {
    setGuide('Loading...');
    const response = await fetch('/api/rag-character-guide', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ series: 'Mistborn', book: 1, chapter: ch })
    });
    const data = await response.json();
    setGuide(data.guide);
  }

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-4">Mistborn: The Final Empire</h1>
      <label className="block mb-2">Select Chapter:</label>
      <select
        className="border p-2 mb-4"
        value={chapter}
        onChange={(e) => setChapter(Number(e.target.value))}
      >
        {Array.from({ length: 38 }, (_, i) => i + 1).map(num => (
          <option key={num} value={num}>Chapter {num}</option>
        ))}
      </select>
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded"
        onClick={() => fetchGuide(chapter)}
      >
        Generate Guide
      </button>
      <div className="mt-6 p-4 bg-stone-50 border rounded">
        {guide ? <pre className="whitespace-pre-wrap">{guide}</pre> : 'Select a chapter to generate a guide.'}
      </div>
    </div>
  );
}
