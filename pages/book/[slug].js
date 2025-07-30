import { useState } from 'react';
import mistborn from '../../data/mistborn.json';

const books = {
  mistborn
};

export default function BookPage({ bookData }) {
  const [chapter, setChapter] = useState(1);
  const { book, characters, recaps } = bookData;

  const visibleCharacters = characters.filter(c => c.firstAppearance <= chapter);

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <header className="bg-white border-b border-gray-200 p-4 text-center text-2xl font-semibold shadow-sm">
        Spoiler Free Character Guide
      </header>
      <main className="max-w-3xl mx-auto p-6">
        <h1 className="text-3xl font-light mb-2">{book.title}</h1>
        <p className="text-gray-600 mb-6">
          Choose your chapter to see only the characters you’ve met so far — no spoilers ahead.
        </p>
        <div className="mb-6">
          <select
            value={chapter}
            onChange={(e) => setChapter(parseInt(e.target.value, 10))}
            className="px-4 py-2 text-lg border border-gray-300 rounded-md shadow-sm"
          >
            {[...Array(book.totalChapters)].map((_, idx) => (
              <option key={idx + 1} value={idx + 1}>
                Chapter {idx + 1}
              </option>
            ))}
          </select>
        </div>
        <section className="bg-white p-5 rounded-lg shadow mb-6">
          <h2 className="text-xl font-medium mb-2">Recap through Chapter {chapter}</h2>
          <p className="text-gray-700 text-base">{recaps[chapter]}</p>
        </section>
        <section>
          <h2 className="text-xl font-medium mb-3">Characters Seen So Far</h2>
          {visibleCharacters.map(char => (
            <div key={char.name} className="bg-white p-4 rounded-lg shadow mb-4">
              <div className="text-lg font-semibold">{char.name}</div>
              <div className="text-gray-700">{char.description}</div>
            </div>
          ))}
        </section>
      </main>
    </div>
  );
}

export async function getStaticPaths() {
  return {
    paths: [{ params: { slug: 'mistborn' } }],
    fallback: false
  };
}

export async function getStaticProps({ params }) {
  const slug = params.slug;
  const bookData = books[slug];
  return {
    props: { bookData }
  };
}