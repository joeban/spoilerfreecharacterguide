import { useState } from 'react';
import mistborn from '../../data/mistborn.json';
import well from '../../data/well-of-ascension.json';
import hero from '../../data/hero-of-ages.json';
import alloy from '../../data/alloy-of-law.json';
import shadows from '../../data/shadows-of-self.json';

const books = { mistborn, "well-of-ascension": well, "hero-of-ages": hero, "alloy-of-law": alloy, "shadows-of-self": shadows };

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
    <div className="min-h-screen bg-[#faf9f7] text-gray-900 flex flex-col justify-between">
      <div>
        
<header className="w-full bg-white border-b border-gray-200 p-6 shadow-sm mt-2">
  <div className="flex flex-col items-center">
    <h1 className="text-5xl font-bold text-gray-900 font-serif">Spoiler Free Character Guide</h1>
    <p className="text-lg text-gray-500 italic mt-1">Your safe guide to epic stories</p>
  </div>
</header>

        <main className="main-content">
          <h1 className="text-3xl font-serif mb-2">{book.title}</h1>
          <a
            href={book.affiliateLink}
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
              onChange={(e) => { setChapter(parseInt(e.target.value, 10)); setShowRecap(false); }}
              className="px-4 py-2 text-lg border border-gray-300 rounded-md shadow-sm w-full"
            >
              {[...Array(book.totalChapters)].map((_, idx) => (
                <option key={idx + 1} value={idx + 1}>Chapter {idx + 1}</option>
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
              <div key={char.name} className="bg-gray-50 p-4 rounded-lg shadow mb-4">
                <div className="text-lg font-semibold font-serif">{char.name}</div>
                <div className="text-gray-700">{getDescriptionForChapter(char.descriptions, chapter)}</div>
              </div>
            ))}
          </section>
          <section>
            <h2 className="text-xl font-semibold mb-3">Other Characters Met So Far</h2>
            {othersSeen.length === 0 && <p className="text-gray-500">No other characters have been introduced yet.</p>}
            {othersSeen.map(char => (
              <div key={char.name} className="bg-gray-50 p-4 rounded-lg shadow mb-4">
                <div className="text-lg font-semibold font-serif">{char.name}</div>
                <div className="text-gray-700">{getDescriptionForChapter(char.descriptions, chapter)}</div>
              </div>
            ))}
          </section>
        </main>
      </div>
      <footer className="text-xs text-gray-500 mt-8 mb-4 text-center px-4">
        Disclosure: As an Amazon Associate, I earn from qualifying purchases.<br/>
        <a href="mailto:spoilerfreecharacterguide@gmail.com" className="underline text-blue-700">Submit a correction</a>
      </footer>
    </div>
  );
}

export async function getStaticPaths() {
  return {
    paths: [
      { params: { slug: 'mistborn' } },
      { params: { slug: 'well-of-ascension' } },
      { params: { slug: 'hero-of-ages' } },
      { params: { slug: 'alloy-of-law' } },
      { params: { slug: 'shadows-of-self' } }
    ],
    fallback: false
  };
}

export async function getStaticProps({ params }) {
  const slug = params.slug;
  const bookData = books[slug];
  return { props: { bookData } };
}