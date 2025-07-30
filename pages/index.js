import { useRouter } from 'next/router';
import mistborn from '../data/mistborn.json';

export default function Home() {
  const router = useRouter();
  const books = [
    { title: mistborn.book.title, slug: 'mistborn', affiliateLink: mistborn.book.affiliateLink }
  ];

  const handleSelect = (e) => {
    const slug = e.target.value;
    if (slug) router.push(`/book/${slug}`);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 text-gray-900">
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
        {books.map(book => (
          <option key={book.slug} value={book.slug}>{book.title}</option>
        ))}
      </select>
      {books.map(book => (
        <a
          key={book.slug}
          href={book.affiliateLink}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-600 underline"
        >
          Buy {book.title} on Amazon
        </a>
      ))}
    </div>
  );
}