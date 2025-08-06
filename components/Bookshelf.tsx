import Link from 'next/link';
import { Series } from '@/lib/types';
import BookSpine from './BookSpine';

interface BookshelfProps {
  series: Array<{ slug: string; series: Series }>;
}

export default function Bookshelf({ series }: BookshelfProps) {
  // Group books for mobile (2 per row) and desktop (4 per row)
  const mobileRows = [];
  const desktopRows = [];
  
  // Create mobile rows (2 books per row)
  for (let i = 0; i < series.length; i += 2) {
    mobileRows.push(series.slice(i, i + 2));
  }
  
  // Create desktop rows (4 books per row)
  for (let i = 0; i < series.length; i += 4) {
    desktopRows.push(series.slice(i, i + 4));
  }
  
  return (
    <div className="bookshelf-container max-w-6xl mx-auto px-4">
      {/* Main bookcase frame */}
      <div className="relative"
           style={{
             background: 'linear-gradient(180deg, #3a2a1a 0%, #2a1a0a 100%)',
             borderRadius: '1rem',
             boxShadow: `
               inset 0 0 50px rgba(0,0,0,0.5),
               0 10px 40px rgba(0,0,0,0.8)
             `
           }}>
        
        {/* Bookcase sides */}
        <div className="absolute left-0 top-0 bottom-0 w-8 bg-gradient-to-r from-black/30 to-transparent rounded-l-lg" />
        <div className="absolute right-0 top-0 bottom-0 w-8 bg-gradient-to-l from-black/30 to-transparent rounded-r-lg" />
        
        {/* Decorative top trim */}
        <div className="h-4 bg-gradient-to-b from-amber-800/20 to-transparent rounded-t-lg" />
        
        <div className="p-6">
          {/* Mobile Layout - visible only on small screens */}
          <div className="md:hidden space-y-6">
            {mobileRows.map((row, rowIndex) => (
              <div key={`mobile-row-${rowIndex}`}>
                {/* Books row - 2 columns on mobile */}
                <div className="grid grid-cols-2 gap-3 mb-2">
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
                  {/* Add empty space if odd number in last row */}
                  {row.length === 1 && <div />}
                </div>
                
                {/* Wooden shelf under books */}
                <div className="wooden-shelf h-4 rounded-md relative overflow-hidden">
                  <div className="absolute inset-0 bg-gradient-to-b from-amber-900/20 to-transparent" />
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-600/30 to-transparent" />
                </div>
              </div>
            ))}
          </div>
          
          {/* Desktop Layout - visible only on medium+ screens */}
          <div className="hidden md:block space-y-8">
            {desktopRows.map((row, rowIndex) => (
              <div key={`desktop-row-${rowIndex}`}>
                {/* Books row - 4 columns on desktop */}
                <div className="flex flex-wrap justify-center gap-4 mb-2">
                  {row.map(({ slug, series: seriesData }) => (
                    <Link key={slug} href={`/${slug}`} className="block">
                      <BookSpine
                        title={seriesData.title}
                        author={seriesData.author}
                        bookCount={Object.keys(seriesData.books).length}
                        orientation="vertical"
                      />
                    </Link>
                  ))}
                </div>
                
                {/* Wooden shelf under books */}
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
            <span className="italic">A Collection of Epic Tales</span>
            <span>✦</span>
          </div>
        </div>
      </div>
      
      {/* Floor shadow */}
      <div className="h-8 bg-gradient-to-b from-black/40 to-transparent -mt-4 blur-xl" />
    </div>
  );
}
