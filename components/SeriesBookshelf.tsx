import Link from 'next/link';
import { BookMeta } from '@/lib/types';
import BookSpine from './BookSpine';

interface SeriesBookshelfProps {
  books: Array<{ slug: string; book: BookMeta }>;
  seriesSlug: string;
}

export default function SeriesBookshelf({ books, seriesSlug }: SeriesBookshelfProps) {
  return (
    <div className="max-w-6xl mx-auto px-4">
      {/* Responsive grid that adjusts columns based on screen size */}
      <div className="grid gap-4 sm:gap-6 grid-cols-2 sm:grid-cols-3 desktop:grid-cols-4 xl:grid-cols-5">
        {books.map(({ slug, book }) => (
          <Link key={slug} href={`/${seriesSlug}/${slug}`} className="block flex justify-center">
            <BookSpine
              title={book.title}
              author={`${book.published} • ${book.chapters} chapters`}
              bookCount={book.chapters}
              orientation="vertical"
            />
          </Link>
        ))}
      </div>
    </div>
  );
}