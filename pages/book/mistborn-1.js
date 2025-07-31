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
    if (data.error) {
      setGuide(`Error: ${data.error}`);
    } else {
      setGuide(data.guide);
    }
  }

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">Mistborn: The Final Empire</h1>
      <p className="mb-4 text-gray-700">Select a chapter to generate a spoiler-free character guide powered by GPT-4o.</p>
      
      <label className="block mb-2 font-semibold">Select Chapter:</label>
      <select
        className="border p-2 mb-4 rounded w-full"
        value={chapter}
        onChange={(e) => setChapter(Number(e.target.value))}
      >
        {Array.from({ length: 38 }, (_, i) => i + 1).map(num => (
          <option key={num} value={num}>Chapter {num}</option>
        ))}
      </select>

      <button
        className="bg-green-700 hover:bg-green-800 text-white px-4 py-2 rounded"
        onClick={() => fetchGuide(chapter)}
      >
        Generate Guide
      </button>

      <div className="mt-6 p-4 bg-white border rounded shadow">
        {guide ? <pre className="whitespace-pre-wrap">{guide}</pre> : 'No guide generated yet.'}
      </div>
    </div>
  );
}
