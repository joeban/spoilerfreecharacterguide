import { useState } from 'react';
import mistborn from '../../data/mistborn.json';
import stormlight from '../../data/stormlight.json';

const books = { mistborn, stormlight };

export default function BookPage({ bookData }) {
  const [chapter, setChapter] = useState(1);
  const [showRecap, setShowRecap] = useState(false);
  const { book, characters, recaps } = bookData;

  function getDescriptionForChapter(descriptions, chapter) {
    return descriptions.find(d => chapter >= d.startChapter && chapter <= d.endChapter)?.text;
  }

  const inChapter = characters.filter(c => c.featuredIn.includes(chapter));
  const othersSeen = characters.filter(
    c => c.firstAppearance <= chapter && !c.featuredIn.includes(chapter)
  );

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 flex flex-col justify-between">
      <div>
        <header className={\`border-b border-gray-200 p-4 text-center text-2xl font-semibold shadow-sm \${book.theme.backgroundEffect}\`}>
          <span className={book.theme.primaryColor}>Spoiler Free Character Guide</span>
          <div className={\`mt-2 w-32 mx-auto border-b-2 \${book.theme.underlineColor}\`}></div>
        </header>
        <main className="max-w-3xl mx-auto p-6">
          <h1 className="text-3xl font-light mb-2">{book.title}</h1>
          <a
            href={book.affiliateLink || "https://www.amazon.com?tag=profitfirstre-20"}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block mb-4 px-4 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-700 hover:bg-gray-200 transition"
          >
            Buy on Amazon
          </a>
          <p className="text-gray-600 mb-6">
            Choose your chapter to see only the characters you’ve met so far — no spoilers ahead.
          </p>
          <div className="mb-6">
            <select
              value={chapter}
              onChange={(e) => {setChapter(parseInt(e.target.value, 10)); setShowRecap(false);}}
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
            {!showRecap && (
              <button
                onClick={() => setShowRecap(true)}
                className="px-3 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-700 hover:bg-gray-200 transition"
              >
                Show Recap
              </button>
            )}
            {showRecap && (
              <div>
                <p className="text-gray-700 text-base mb-2">{recaps[chapter]}</p>
                <button
                  onClick={() => setShowRecap(false)}
                  className="px-3 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-700 hover:bg-gray-200 transition"
                >
                  Hide Recap
                </button>
              </div>
            )}
          </section>
          <section className="mb-6">
            <h2 className="text-xl font-semibold mb-3">Characters in Chapter {chapter}</h2>
            {inChapter.length === 0 && <p className="text-gray-500">No major characters appear in this chapter.</p>}
            {inChapter.map(char => (
              <div key={char.name} className="bg-white p-4 rounded-lg shadow mb-4">
                <div className="text-lg font-semibold">{char.name}</div>
                <div className="text-gray-700">{getDescriptionForChapter(char.descriptions, chapter)}</div>
              </div>
            ))}
          </section>
          <section>
            <h2 className="text-xl font-semibold mb-3">Other Characters Met So Far</h2>
            {othersSeen.length === 0 && <p className="text-gray-500">No other characters have been introduced yet.</p>}
            {othersSeen.map(char => (
              <div key={char.name} className="bg-white p-4 rounded-lg shadow mb-4">
                <div className="text-lg font-semibold">{char.name}</div>
                <div className="text-gray-700">{getDescriptionForChapter(char.descriptions, chapter)}</div>
              </div>
            ))}
          </section>
        </main>
      </div>
      <footer className="text-xs text-gray-500 mt-8 mb-4 text-center px-4">
        Disclosure: As an Amazon Associate, I earn from qualifying purchases.
      </footer>
    </div>
  );
}

export async function getStaticPaths() {
  return {
    paths: [{ params: { slug: 'mistborn' } }, { params: { slug: 'stormlight' } }],
    fallback: false
  };
}

export async function getStaticProps({ params }) {
  const slug = params.slug;
  const bookData = books[slug];
  return { props: { bookData } };
}