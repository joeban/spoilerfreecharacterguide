import Link from 'next/link';
import { Series } from '@/lib/types';
import BookSpine from './BookSpine';

interface BookshelfProps {
  series: Array<{ slug: string; series: Series }>;
}

export default function Bookshelf({ series }: BookshelfProps) {
  // Organize books: 4 vertical + 1 horizontal per shelf unit
  const shelfUnits = [];
  for (let i = 0; i < series.length; i += 5) {
    shelfUnits.push({
      vertical: series.slice(i, i + 4),
      horizontal: series[i + 4]
    });
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
        
        <div className="p-6 space-y-8">
          {shelfUnits.map((unit, unitIndex) => (
            <div key={unitIndex} className="space-y-4">
              {/* Vertical books shelf */}
              {unit.vertical.length > 0 && (
                <div>
                  <div className="flex flex-wrap justify-center gap-3 md:gap-4 mb-2">
                    {unit.vertical.map(({ slug, series: seriesData }) => (
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
                  
                  {/* Wooden shelf under vertical books */}
                  <div className="wooden-shelf h-4 rounded-md relative overflow-hidden">
                    <div className="absolute inset-0 bg-gradient-to-b from-amber-900/20 to-transparent" />
                    {/* Shelf edge highlight */}
                    <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-600/30 to-transparent" />
                  </div>
                </div>
              )}
              
              {/* Horizontal book shelf */}
              {unit.horizontal && (
                <div>
                  <Link href={`/${unit.horizontal.slug}`} className="block">
                    <BookSpine
                      title={unit.horizontal.series.title}
                      author={unit.horizontal.series.author}
                      bookCount={Object.keys(unit.horizontal.series.books).length}
                      orientation="horizontal"
                    />
                  </Link>
                  
                  {/* Wooden shelf under horizontal book */}
                  <div className="wooden-shelf h-4 rounded-md relative overflow-hidden mt-2">
                    <div className="absolute inset-0 bg-gradient-to-b from-amber-900/20 to-transparent" />
                    <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-amber-600/30 to-transparent" />
                  </div>
                </div>
              )}
              
              {/* Decorative elements between shelf units */}
              {unitIndex < shelfUnits.length - 1 && (
                <div className="flex justify-center items-center py-4">
                  <div className="flex items-center gap-4">
                    <div className="w-20 h-0.5 bg-gradient-to-r from-transparent to-amber-700/30" />
                    <div className="candle-glow relative">
                      <div className="w-4 h-8 bg-gradient-to-b from-amber-100 to-amber-600 rounded-t-full"
                           style={{
                             boxShadow: '0 0 20px rgba(255,191,0,0.6)'
                           }} />
                      <div className="w-6 h-2 bg-amber-800 rounded-b-lg -mt-0.5" />
                    </div>
                    <div className="w-20 h-0.5 bg-gradient-to-l from-transparent to-amber-700/30" />
                  </div>
                </div>
              )}
            </div>
          ))}
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
