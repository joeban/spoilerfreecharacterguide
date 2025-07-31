import { useRouter } from 'next/router';
import mistborn from '../data/mistborn.json';
import well from '../data/well-of-ascension.json';
import hero from '../data/hero-of-ages.json';

export default function Home() {
  const router = useRouter();
  const books = [
    { title: mistborn.book.title, slug: 'mistborn' },
    { title: well.book.title, slug: 'well-of-ascension' },
    { title: hero.book.title, slug: 'hero-of-ages' }
  ];

  const handleSelect = (e) => {
    const slug = e.target.value;
    if (slug) router.push(`/book/${slug}`);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-between bg-gray-50 text-gray-900">
      
<header className="w-full bg-white border-b border-gray-200 p-6 shadow-sm">
  <div className="flex flex-col items-center">
    <div className="flex items-center mb-2">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" className="w-8 h-8 mr-2 text-gray-700">
  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v12m-7-9h14M5 6h14a2 2 0 012 2v12a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2z" />
</svg>
      <h1 className="text-5xl font-bold text-gray-900">Spoiler Free Character Guide</h1>
    </div>
    <p className="text-lg text-gray-500 italic">Your safe guide to epic stories</p>
  </div>
</header>

      <div className="flex flex-col items-center mt-6">
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