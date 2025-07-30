import { useState } from 'react';
import mistborn from '../../data/mistborn.json';
import stormlight from '../../data/stormlight.json';

const books = { mistborn, stormlight };

export default function BookPage({ bookData }) {
  const [chapter, setChapter] = useState(1);
  const [showRecap, setShowRecap] = useState(false);
  const { book, recaps } = bookData;

  // Determine if Mistborn theme for banner image
  const headerStyle = book.theme.backgroundEffect === 'mistborn-banner'
    ? {
        backgroundImage: 'url(/mistborn-header.png)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }
    : {};

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 flex flex-col justify-between">
      <div>
        <header
          className={"border-b border-gray-200 p-4 text-center text-2xl font-semibold shadow-sm " + book.theme.backgroundEffect}
          style={headerStyle}
        >
          <span className={book.theme.primaryColor + " drop-shadow-md"}>Spoiler Free Character Guide</span>
          <div className={"mt-2 w-32 mx-auto border-b-2 " + book.theme.underlineColor}></div>
        </header>
        <main className="max-w-3xl mx-auto p-6">
          <h1 className="text-3xl font-light mb-2">{book.title}</h1>
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
              className="px-4 py-2 text-lg border border-gray-300 rounded-md shadow-sm"
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
      { params: { slug: 'stormlight' } }
    ],
    fallback: false
  };
}

export async function getStaticProps({ params }) {
  const slug = params.slug;
  const bookData = books[slug];
  return { props: { bookData } };
}