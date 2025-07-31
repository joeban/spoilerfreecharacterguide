import Link from 'next/link';
import mistborn from '../data/mistborn.json';
import well from '../data/well-of-ascension.json';
import hero from '../data/hero-of-ages.json';
import alloy from '../data/alloy-of-law.json';
import shadows from '../data/shadows-of-self.json';
import bands from '../data/bands-of-mourning.json';

export default function Home() {
  const books = [
    { title: mistborn.book.title, slug: 'mistborn' },
    { title: well.book.title, slug: 'well-of-ascension' },
    { title: hero.book.title, slug: 'hero-of-ages' },
    { title: alloy.book.title, slug: 'alloy-of-law' },
    { title: shadows.book.title, slug: 'shadows-of-self' },
    { title: bands.book.title, slug: 'bands-of-mourning' }
  ];

  return (
    <div className="min-h-screen bg-stone-50 p-6">
      <header className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800">Spoiler Free Character Guide</h1>
        <p className="text-lg text-gray-600">Your safe guide to epic stories</p>
      </header>

      <main className="max-w-xl mx-auto">
        <div className="bg-white shadow-md rounded-lg p-6">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">Choose a book to get started!</h2>
          <ul className="space-y-3">
            {books.map((book) => (
              <li key={book.slug}>
                <Link
                  href={`/book/${book.slug}`}
                  className="block p-3 rounded-lg border border-gray-200 hover:bg-gray-100 transition"
                >
                  {book.title}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </main>
    </div>
  );
}
