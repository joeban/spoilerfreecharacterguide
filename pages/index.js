import { useRouter } from 'next/router';
import mistborn from '../data/mistborn.json';
import stormlight from '../data/stormlight.json';

export default function Home() {
  const router = useRouter();
  const books = [
    { title: mistborn.book.title, slug: 'mistborn' },
    { title: stormlight.book.title, slug: 'stormlight' }
  ];

  const handleSelect = (e) => {
    const slug = e.target.value;
    if (slug) {
      router.push(`/book/${slug}`);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-between bg-gray-50 text-gray-900">
      <div className="flex flex-col items-center justify-center">
        <header className="text-3xl font-semibold mb-6">
          Spoiler Free Character Guide
        </header>
        <p className="text-lg text-gray-600 mb-4">Choose a book to get started</p>
        <select
          onChange={handleSelect}
          defaultValue=""
          className="px-4 py-2 text-lg border border-gray-300 rounded-md shadow-sm mb-4"
        >
          <option value="" disabled>Select a book...</option>
          {books.map((book) => (
            <option key={book.slug} value={book.slug}>{book.title}</option>
          ))}
        </select>
      </div>
      <footer className="text-xs text-gray-500 mt-8 mb-4 text-center px-4">
        Disclosure: As an Amazon Associate, I earn from qualifying purchases.
      </footer>
    </div>
  );
}