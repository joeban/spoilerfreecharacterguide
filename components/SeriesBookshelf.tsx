import Link from 'next/link';
import { Book } from '@/lib/types';
import BookSpine from './BookSpine';

interface SeriesBookshelfProps {
  books: Array<{ slug: string; book: Book }>;
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
    <div className="bookshelf-container max-w-6xl mx-auto px-4">
      {/* Main bookcase frame */}
      <div className="wood-secondary rounded-xl relative"
           style={{
             boxShadow: `
               inset 0 0 50px rgba(0,0,0,0.5),
               0 10px 40px rgba(0,0,0,0.8)
             `
           }}>
        
        {/* Bookcase sides */}
        <div className="absolute left-0 top-0 bottom-0 w-8 bg-gradient-to-r from-black/30 to-transparent rounded-l-lg" />
        <div className="absolute right-0 top-0 bottom-0 w-8 bg-gradient-to-l from-black/30 to-transparent rounded-r-lg" />
        
        {/* Decorative top trim */}
        <div className="h-4 rounded-t-xl" style={{background: `linear-gradient(to bottom, #8b6f47, transparent)`}} />
        
        <div className="p-6">
          {/* Mobile Layout (2 books per row) - visible < 640px */}
          <div className="sm:hidden space-y-6">
            {mobileRows.map((row, rowIndex) => (
              <div key={`mobile-${rowIndex}`}>
                <div className="grid grid-cols-2 gap-3 mb-2">
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
                <div className="wooden-shelf h-4 rounded-md relative overflow-hidden">
                  <div className="absolute inset-0 bg-gradient-to-b from-amber-900/20 to-transparent" />
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-600/30 to-transparent" />
                </div>
              </div>
            ))}
          </div>
          
          {/* Tablet Layout (3 books per row) - visible 640px to 900px */}
          <div className="hidden sm:block tablet-max:block desktop:hidden space-y-6">
            {tabletRows.map((row, rowIndex) => (
              <div key={`tablet-${rowIndex}`}>
                <div className="grid grid-cols-3 gap-3 mb-2">
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
                <div className="wooden-shelf h-4 rounded-md relative overflow-hidden">
                  <div className="absolute inset-0 bg-gradient-to-b from-amber-900/20 to-transparent" />
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-600/30 to-transparent" />
                </div>
              </div>
            ))}
          </div>
          
          {/* Desktop Layout (4 books per row) - visible 900px to 1200px */}
          <div className="hidden desktop:block xl:hidden space-y-6">
            {desktopRows.map((row, rowIndex) => (
              <div key={`desktop-${rowIndex}`}>
                <div className="grid grid-cols-4 gap-4 mb-2">
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
                <div className="wooden-shelf h-4 rounded-md relative overflow-hidden">
                  <div className="absolute inset-0 bg-gradient-to-b from-amber-900/20 to-transparent" />
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-600/30 to-transparent" />
                </div>
              </div>
            ))}
          </div>
          
          {/* Large Desktop Layout (5 books per row) - visible > 1200px */}
          <div className="hidden xl:block space-y-6">
            {largeRows.map((row, rowIndex) => (
              <div key={`large-${rowIndex}`}>
                <div className="grid grid-cols-5 gap-4 mb-2">
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
                <div className="wooden-shelf h-4 rounded-md relative overflow-hidden">
                  <div className="absolute inset-0 bg-gradient-to-b from-amber-900/20 to-transparent" />
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-600/30 to-transparent" />
                </div>
              </div>
            ))}
          </div>
        </div>
        
        {/* Bottom decorative base */}
        <div className="h-12 bg-gradient-to-t from-black/50 to-transparent rounded-b-lg flex items-end justify-center pb-2">
          <div className="flex items-center gap-2 text-amber-600/50 text-xs">
            <span>✦</span>
            <span className="italic">Choose Your Reading Journey</span>
            <span>✦</span>
          </div>
        </div>
      </div>
      
      {/* Floor shadow */}
      <div className="h-8 bg-gradient-to-b from-black/40 to-transparent -mt-4 blur-xl" />
    </div>
  );
}