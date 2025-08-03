import Link from 'next/link';
import { Series } from '@/lib/types';
import BookSpine from './BookSpine';

interface BookshelfProps {
  series: Array<{ slug: string; series: Series }>;
}

export default function Bookshelf({ series }: BookshelfProps) {
  // Organize books into shelves (5 books per shelf for 20 total = 4 shelves)
  const booksPerShelf = 5;
  const shelves = [];
  
  for (let i = 0; i < series.length; i += booksPerShelf) {
    shelves.push(series.slice(i, i + booksPerShelf));
  }
  
  return (
    <div className="bookshelf-container max-w-6xl mx-auto px-4">
      {/* Main Bookshelf Structure */}
      <div className="relative" 
           style={{
             background: '#4a2c17',
             borderRadius: '8px 8px 0 0',
             boxShadow: '0 20px 50px rgba(0,0,0,0.4)'
           }}>
        
        {/* Back panel of bookshelf */}
        <div className="absolute inset-0 rounded-t-lg"
             style={{
               background: `
                 linear-gradient(180deg, #5a3621 0%, #4a2c17 50%, #3a1c0f 100%),
                 radial-gradient(ellipse at top, rgba(0,0,0,0) 0%, rgba(0,0,0,0.2) 100%)
               `,
               boxShadow: 'inset 0 0 50px rgba(0,0,0,0.3)'
             }}>
          {/* Wood grain pattern */}
          <div className="absolute inset-0 opacity-30"
               style={{
                 backgroundImage: `url("data:image/svg+xml,%3Csvg width='100' height='100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='wood'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.02 0.1' result='noise' numOctaves='4' /%3E%3CfeColorMatrix in='noise' type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='100' height='100' filter='url(%23wood)' opacity='0.4'/%3E%3C/svg%3E")`,
                 backgroundSize: '200px 200px'
               }} />
        </div>
        
        {/* Side panels - thick wooden sides */}
        <div className="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/30 to-transparent z-20" />
        <div className="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/30 to-transparent z-20" />
        
        {/* Shelves */}
        <div className="relative z-10 px-12 pt-8">
          {shelves.map((shelfBooks, shelfIndex) => (
            <div key={shelfIndex}>
              {/* Books area */}
              <div className="flex justify-center items-end gap-4 md:gap-6 pb-2"
                   style={{ minHeight: '320px' }}>
                {shelfBooks.map(({ slug, series: seriesData }) => (
                  <Link key={slug} href={`/${slug}`} className="block">
                    <BookSpine
                      title={seriesData.title}
                      author={seriesData.author}
                      bookCount={Object.keys(seriesData.books).length}
                    />
                  </Link>
                ))}
              </div>
              
              {/* Solid wooden shelf */}
              <div className="relative h-12 -mx-12"
                   style={{
                     background: `
                       linear-gradient(to bottom, 
                         #6b4423 0%, 
                         #5a3621 30%,
                         #4a2c17 60%,
                         #3a1c0f 100%
                       )
                     `,
                     boxShadow: `
                       inset 0 2px 4px rgba(255,255,255,0.1),
                       inset 0 -4px 8px rgba(0,0,0,0.4),
                       0 4px 8px rgba(0,0,0,0.5)
                     `
                   }}>
                {/* Top edge highlight */}
                <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-b from-white/10 to-transparent" />
                
                {/* Wood texture */}
                <div className="absolute inset-0 opacity-20"
                     style={{
                       background: `repeating-linear-gradient(90deg,
                         transparent 0px,
                         rgba(0,0,0,0.1) 3px,
                         transparent 6px,
                         rgba(0,0,0,0.05) 9px,
                         transparent 12px
                       )`
                     }} />
                
                {/* Front edge detail */}
                <div className="absolute bottom-0 left-0 right-0 h-2 bg-black/20" />
              </div>
              
              {/* Space between shelves */}
              {shelfIndex < shelves.length - 1 && <div className="h-12" />}
            </div>
          ))}
        </div>
        
        {/* Heavy base */}
        <div className="relative h-20 -mt-4"
             style={{
               background: `
                 linear-gradient(to bottom,
                   #3a1c0f 0%,
                   #2a1309 50%,
                   #1a0a05 100%
                 )
               `,
               boxShadow: 'inset 0 4px 8px rgba(0,0,0,0.6)'
             }}>
          {/* Base molding detail */}
          <div className="absolute top-4 left-0 right-0 h-2"
               style={{
                 background: 'linear-gradient(to bottom, #4a2c17 0%, #3a1c0f 100%)',
                 boxShadow: '0 2px 4px rgba(0,0,0,0.4)'
               }} />
        </div>
      </div>
      
      {/* Floor shadow */}
      <div className="h-6 bg-black/30 -mt-1 rounded-b-lg blur-xl" 
           style={{
             transform: 'scaleX(1.1)',
             filter: 'blur(20px)'
           }} />
    </div>
  );
}
