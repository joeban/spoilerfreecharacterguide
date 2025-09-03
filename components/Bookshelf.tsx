import Link from 'next/link';
import { Series } from '@/lib/types';
import BookSpine from './BookSpine';

interface BookshelfProps {
  series: Array<{ slug: string; series: Series }>;
}

export default function Bookshelf({ series }: BookshelfProps) {
  // Group books dynamically based on responsive breakpoints
  // We'll create separate groups for each breakpoint
  const groupBooksForBreakpoint = (booksPerRow: number) => {
    const rows = [];
    for (let i = 0; i < series.length; i += booksPerRow) {
      rows.push(series.slice(i, i + booksPerRow));
    }
    return rows;
  };

  // Create groups for each breakpoint
  const mobileRows = groupBooksForBreakpoint(2);     // < 640px
  const tabletRows = groupBooksForBreakpoint(3);     // 640px - 900px  
  const desktopRows = groupBooksForBreakpoint(4);    // 900px - 1200px
  const largeRows = groupBooksForBreakpoint(5);      // > 1200px

  return (
    <div className="bookshelf-container max-w-7xl mx-auto px-4">
      {/* Main bookcase frame - refined styling */}
      <div className="relative rounded-xl overflow-hidden"
           style={{
             background: 'linear-gradient(180deg, #4a3420 0%, #3a2818 50%, #2a1f15 100%)',
             boxShadow: `
               inset 0 2px 8px rgba(255,255,255,0.05),
               inset 0 -2px 8px rgba(0,0,0,0.4),
               0 8px 32px rgba(0,0,0,0.6),
               0 2px 8px rgba(0,0,0,0.4)
             `
           }}>
        
        {/* Enhanced bookcase sides with wood grain */}
        <div className="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/40 to-transparent rounded-l-xl z-10" />
        <div className="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/40 to-transparent rounded-r-xl z-10" />
        
        {/* Refined decorative top trim */}
        <div className="h-6 rounded-t-xl relative" style={{
          background: 'linear-gradient(to bottom, #6b5537 0%, #4a3420 50%, transparent 100%)',
          boxShadow: 'inset 0 2px 4px rgba(255,255,255,0.08)'
        }} />
        
        <div className="p-8 pb-10">
          {/* Mobile Layout (2 books per row) - visible < 640px */}
          <div className="sm:hidden space-y-6">
            {mobileRows.map((row, rowIndex) => (
              <div key={`mobile-${rowIndex}`}>
                <div className="grid grid-cols-2 gap-6 mb-4 justify-items-center">
                  {row.map(({ slug, series: seriesData }) => (
                    <Link key={slug} href={`/${slug}`} className="block flex justify-center">
                      <BookSpine
                        title={seriesData.title}
                        author={seriesData.author}
                        bookCount={Object.keys(seriesData.books).length}
                        orientation="vertical"
                      />
                    </Link>
                  ))}
                  {row.length === 1 && <div />}
                </div>
                <div className="h-5 rounded relative overflow-hidden" style={{
                  background: 'linear-gradient(180deg, #5a4530 0%, #4a3525 50%, #3a2818 100%)',
                  boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.4), 0 1px 2px rgba(255,255,255,0.05)'
                }}>
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-700/20 to-transparent" />
                </div>
              </div>
            ))}
          </div>
          
          {/* Tablet Layout (3 books per row) - visible 640px to 900px */}
          <div className="hidden sm:block tablet-max:block desktop:hidden space-y-6">
            {tabletRows.map((row, rowIndex) => (
              <div key={`tablet-${rowIndex}`}>
                <div className="grid grid-cols-3 gap-6 mb-4 justify-items-center">
                  {row.map(({ slug, series: seriesData }) => (
                    <Link key={slug} href={`/${slug}`} className="block flex justify-center">
                      <BookSpine
                        title={seriesData.title}
                        author={seriesData.author}
                        bookCount={Object.keys(seriesData.books).length}
                        orientation="vertical"
                      />
                    </Link>
                  ))}
                  {/* Fill empty spaces */}
                  {Array.from({ length: 3 - row.length }).map((_, i) => (
                    <div key={`empty-${i}`} />
                  ))}
                </div>
                <div className="h-5 rounded relative overflow-hidden" style={{
                  background: 'linear-gradient(180deg, #5a4530 0%, #4a3525 50%, #3a2818 100%)',
                  boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.4), 0 1px 2px rgba(255,255,255,0.05)'
                }}>
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-700/20 to-transparent" />
                </div>
              </div>
            ))}
          </div>
          
          {/* Desktop Layout (4 books per row) - visible 900px to 1200px */}
          <div className="hidden desktop:block xl:hidden space-y-6">
            {desktopRows.map((row, rowIndex) => (
              <div key={`desktop-${rowIndex}`}>
                <div className="grid grid-cols-4 gap-6 mb-4 justify-items-center">
                  {row.map(({ slug, series: seriesData }) => (
                    <Link key={slug} href={`/${slug}`} className="block flex justify-center">
                      <BookSpine
                        title={seriesData.title}
                        author={seriesData.author}
                        bookCount={Object.keys(seriesData.books).length}
                        orientation="vertical"
                      />
                    </Link>
                  ))}
                  {Array.from({ length: 4 - row.length }).map((_, i) => (
                    <div key={`empty-${i}`} />
                  ))}
                </div>
                <div className="h-5 rounded relative overflow-hidden" style={{
                  background: 'linear-gradient(180deg, #5a4530 0%, #4a3525 50%, #3a2818 100%)',
                  boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.4), 0 1px 2px rgba(255,255,255,0.05)'
                }}>
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-700/20 to-transparent" />
                </div>
              </div>
            ))}
          </div>
          
          {/* Large Desktop Layout (5 books per row) - visible > 1200px */}
          <div className="hidden xl:block space-y-6">
            {largeRows.map((row, rowIndex) => (
              <div key={`large-${rowIndex}`}>
                <div className="grid grid-cols-5 gap-4 mb-4 justify-items-center">
                  {row.map(({ slug, series: seriesData }) => (
                    <Link key={slug} href={`/${slug}`} className="block flex justify-center">
                      <BookSpine
                        title={seriesData.title}
                        author={seriesData.author}
                        bookCount={Object.keys(seriesData.books).length}
                        orientation="vertical"
                      />
                    </Link>
                  ))}
                  {Array.from({ length: 5 - row.length }).map((_, i) => (
                    <div key={`empty-${i}`} />
                  ))}
                </div>
                <div className="h-5 rounded relative overflow-hidden" style={{
                  background: 'linear-gradient(180deg, #5a4530 0%, #4a3525 50%, #3a2818 100%)',
                  boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.4), 0 1px 2px rgba(255,255,255,0.05)'
                }}>
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-700/20 to-transparent" />
                </div>
              </div>
            ))}
          </div>
        </div>
        
        {/* Enhanced bottom decorative base */}
        <div className="h-14 relative rounded-b-xl flex items-end justify-center pb-3" style={{
          background: 'linear-gradient(to top, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.3) 50%, transparent 100%)'
        }}>
          <div className="flex items-center gap-3 text-amber-500/60 text-sm font-medium">
            <span className="text-amber-400/40">◆</span>
            <span className="tracking-wide">A Collection of Epic Tales</span>
            <span className="text-amber-400/40">◆</span>
          </div>
        </div>
      </div>
      
      {/* Enhanced floor shadow for depth */}
      <div className="h-12 bg-gradient-to-b from-black/50 via-black/20 to-transparent -mt-6 blur-2xl" />
    </div>
  );
}
