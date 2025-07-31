// ⚠️ Book page: Styled view for chapters, characters, and recap.
import fs from 'fs';
import path from 'path';
import { useState } from 'react';

export default function BookPage({ bookData }) {
  const [selectedChapter, setSelectedChapter] = useState(1);
  const [showRecap, setShowRecap] = useState(false);

  const charactersInChapter = Object.keys(bookData.characters).filter(name =>
    bookData.characters[name].featuredIn.includes(selectedChapter)
  );

  const charactersSeenBefore = Object.keys(bookData.characters).filter(name =>
    !bookData.characters[name].featuredIn.includes(selectedChapter) &&
    bookData.characters[name].featuredIn.some(ch => ch < selectedChapter)
  );

  return (
    <div className="min-h-screen bg-[url('/textures/parchment.jpg')] bg-cover p-8">
      <div className="max-w-3xl mx-auto bg-white/80 p-6 rounded-lg shadow-md">
        <h1 className="text-3xl font-bold mb-4 text-center">{bookData.meta.title}</h1>
        
        {/* Chapter Selector */}
        <div className="mb-6 text-center">
          <label className="block text-lg font-semibold mb-2">Select Chapter:</label>
          <select
            value={selectedChapter}
            onChange={(e) => { setSelectedChapter(Number(e.target.value)); setShowRecap(false); }}
            className="border-2 border-yellow-900 rounded-md px-4 py-2 bg-yellow-50"
          >
            {Array.from({length: bookData.meta.totalChapters}, (_, i) => i + 1).map(ch => (
              <option key={ch} value={ch}>Chapter {ch}</option>
            ))}
          </select>
        </div>

        {/* Characters in this Chapter */}
        <section className="mb-6">
          <h2 className="text-2xl font-bold mb-2">Characters in this Chapter</h2>
          {charactersInChapter.length > 0 ? (
            <ul className="grid gap-3">
              {charactersInChapter.map(name => (
                <li key={name} className="bg-yellow-100 rounded-md shadow p-3">
                  <span className="font-semibold">{name}</span>
                </li>
              ))}
            </ul>
          ) : <p className="text-gray-700">No named characters appear in this chapter.</p>}
        </section>

        {/* Previously Seen Characters */}
        <section className="mb-6">
          <h2 className="text-2xl font-bold mb-2">Previously Seen Characters</h2>
          {charactersSeenBefore.length > 0 ? (
            <ul className="grid gap-3">
              {charactersSeenBefore.map(name => (
                <li key={name} className="bg-gray-100 rounded-md shadow p-3">
                  <span className="font-semibold">{name}</span>
                </li>
              ))}
            </ul>
          ) : <p className="text-gray-700">No previously seen characters yet.</p>}
        </section>

        {/* Recap Toggle */}
        <section className="mt-6">
          <button
            onClick={() => setShowRecap(!showRecap)}
            className="px-4 py-2 bg-yellow-700 text-white rounded hover:bg-yellow-800 transition"
          >
            {showRecap ? "Hide Recap" : "📜 Show Recap"}
          </button>
          {showRecap && (
            <div className="mt-3 p-4 bg-yellow-50 rounded border border-yellow-200 shadow-inner">
              <p>{bookData.recaps[String(selectedChapter)] || "No recap available."}</p>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

export async function getStaticPaths() {
  const indexPath = path.join(process.cwd(), 'data', 'index.json');
  const series = JSON.parse(fs.readFileSync(indexPath, 'utf-8'));
  const paths = [];
  Object.keys(series).forEach(name => {
    series[name].forEach(book => {
      paths.push({ params: { series: name.toLowerCase(), book: String(book.bookNumber) } });
    });
  });
  return { paths, fallback: false };
}

export async function getStaticProps({ params }) {
  const filePath = path.join(process.cwd(), 'data', `${params.series}${params.book}.json`);
  const bookData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  return { props: { bookData } };
}
