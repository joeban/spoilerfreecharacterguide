import Link from 'next/link';
import { BookMeta } from '@/lib/types';
import BookSpine from './BookSpine';

interface SeriesBookshelfProps {
  books: Array<{ slug: string; book: BookMeta }>;
  seriesSlug: string;
}

export default function SeriesBookshelf({ books, seriesSlug }: SeriesBookshelfProps) {
  // Group books dynamically based on responsive breakpoints
  const groupBooksForBreakpoint = (booksPerRow: number) => {
    const rows = [];
    for (let i = 0; i < books.length; i += booksPerRow) {
      rows.push(books.slice(i, i + booksPerRow));
    }
    return rows;
  };

  // Create groups for each breakpoint
  const mobileRows = groupBooksForBreakpoint(2);     // < 640px
  const tabletRows = groupBooksForBreakpoint(3);     // 640px - 900px  
  const desktopRows = groupBooksForBreakpoint(4);    // 900px - 1200px
  const largeRows = groupBooksForBreakpoint(5);      // > 1200px

  return (
    <div className="max-w-6xl mx-auto px-4">
      {/* Mobile Layout (2 books per row) - visible < 640px */}
      <div className="sm:hidden space-y-8">
        {mobileRows.map((row, rowIndex) => (
          <div key={`mobile-${rowIndex}`} className="grid grid-cols-2 gap-4">
            {row.map(({ slug, book }) => (
              <Link key={slug} href={`/${seriesSlug}/${slug}`} className="block flex justify-center">
                <BookSpine
                  title={book.title}
                  author={`${book.published} • ${book.chapters} chapters`}
                  bookCount={book.chapters}
                  orientation="vertical"
                />
              </Link>
            ))}
            {row.length === 1 && <div />}
          </div>
        ))}
      </div>
      
      {/* Tablet Layout (3 books per row) - visible 640px to 900px */}
      <div className="hidden sm:block tablet-max:block desktop:hidden space-y-8">
        {tabletRows.map((row, rowIndex) => (
          <div key={`tablet-${rowIndex}`} className="grid grid-cols-3 gap-4">
            {row.map(({ slug, book }) => (
              <Link key={slug} href={`/${seriesSlug}/${slug}`} className="block flex justify-center">
                <BookSpine
                  title={book.title}
                  author={`${book.published} • ${book.chapters} chapters`}
                  bookCount={book.chapters}
                  orientation="vertical"
                />
              </Link>
            ))}
            {/* Fill empty spaces */}
            {Array.from({ length: 3 - row.length }).map((_, i) => (
              <div key={`empty-${i}`} />
            ))}
          </div>
        ))}
      </div>
      
      {/* Desktop Layout (4 books per row) - visible 900px to 1200px */}
      <div className="hidden desktop:block xl:hidden space-y-8">
        {desktopRows.map((row, rowIndex) => (
          <div key={`desktop-${rowIndex}`} className="grid grid-cols-4 gap-6">
            {row.map(({ slug, book }) => (
              <Link key={slug} href={`/${seriesSlug}/${slug}`} className="block flex justify-center">
                <BookSpine
                  title={book.title}
                  author={`${book.published} • ${book.chapters} chapters`}
                  bookCount={book.chapters}
                  orientation="vertical"
                />
              </Link>
            ))}
            {Array.from({ length: 4 - row.length }).map((_, i) => (
              <div key={`empty-${i}`} />
            ))}
          </div>
        ))}
      </div>
      
      {/* Large Desktop Layout (5 books per row) - visible > 1200px */}
      <div className="hidden xl:block space-y-8">
        {largeRows.map((row, rowIndex) => (
          <div key={`large-${rowIndex}`} className="grid grid-cols-5 gap-6">
            {row.map(({ slug, book }) => (
              <Link key={slug} href={`/${seriesSlug}/${slug}`} className="block flex justify-center">
                <BookSpine
                  title={book.title}
                  author={`${book.published} • ${book.chapters} chapters`}
                  bookCount={book.chapters}
                  orientation="vertical"
                />
              </Link>
            ))}
            {Array.from({ length: 5 - row.length }).map((_, i) => (
              <div key={`empty-${i}`} />
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}