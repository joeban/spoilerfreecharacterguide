import Link from 'next/link';
import { Series } from '@/lib/types';
import BookSpine from './BookSpine';

interface BookshelfProps {
  series: Array<{ slug: string; series: Series }>;
}

export default function Bookshelf({ series }: BookshelfProps) {
  // Organize books into shelves (4 books per shelf)
  const booksPerShelf = 4;
  const shelves = [];
  
  for (let i = 0; i < series.length; i += booksPerShelf) {
    shelves.push(series.slice(i, i + booksPerShelf));
  }
  
  return (
    <div className="bookshelf-container max-w-7xl mx-auto">
      {/* Bookshelf Frame */}
      <div className="relative bg-amber-900 rounded-lg shadow-2xl" 
           style={{
             background: 'linear-gradient(180deg, #654321 0%, #8b4513 100%)',
             boxShadow: `
               inset 0 4px 8px rgba(0,0,0,0.5),
               0 16px 32px rgba(0,0,0,0.3),
               0 24px 48px rgba(0,0,0,0.2)
             `,
             padding: '20px 20px 0 20px'
           }}>
        
        {/* Wood grain texture */}
        <div className="absolute inset-0 opacity-20 rounded-lg pointer-events-none"
             style={{
               backgroundImage: `
                 repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(0,0,0,0.1) 2px, rgba(0,0,0,0.1) 4px),
                 repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px)
               `
             }} />
        
        {/* Top decorative edge */}
        <div className="absolute top-0 left-0 right-0 h-4 bg-gradient-to-b from-black/30 to-transparent" />
        
        {/* Side panels */}
        <div className="absolute left-0 top-0 bottom-0 w-4 bg-gradient-to-r from-black/20 to-transparent" />
        <div className="absolute right-0 top-0 bottom-0 w-4 bg-gradient-to-l from-black/20 to-transparent" />
        
        {/* Individual Shelves */}
        {shelves.map((shelfBooks, shelfIndex) => (
          <div key={shelfIndex} className="shelf-section mb-0">
            {/* Books on this shelf */}
            <div className="relative z-10 flex justify-center items-end gap-6 md:gap-8 pb-4"
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
            
            {/* Shelf platform */}
            <div className="relative">
              {/* Shelf top surface */}
              <div className="h-8 relative z-20"
                   style={{
                     background: `linear-gradient(to bottom, 
                       #8b6f47 0%, 
                       #654321 40%,
                       #543621 100%
                     )`,
                     boxShadow: `
                       inset 0 2px 4px rgba(255,255,255,0.1),
                       inset 0 -2px 8px rgba(0,0,0,0.4),
                       0 4px 8px rgba(0,0,0,0.3)
                     `,
                     borderRadius: '2px'
                   }}>
                {/* Wood texture on shelf */}
                <div className="absolute inset-0 opacity-30"
                     style={{
                       background: `repeating-linear-gradient(90deg,
                         transparent 0px,
                         rgba(0,0,0,0.1) 2px,
                         transparent 4px
                       )`
                     }} />
              </div>
              
              {/* Shelf front edge */}
              <div className="h-3 -mt-1 relative z-10"
                   style={{
                     background: 'linear-gradient(to bottom, #543621 0%, #3e2723 100%)',
                     boxShadow: '0 2px 4px rgba(0,0,0,0.4)',
                     borderRadius: '0 0 4px 4px'
                   }} />
              
              {/* Shelf brackets (decorative) */}
              {shelfIndex < shelves.length - 1 && (
                <>
                  <div className="absolute -bottom-6 left-12 w-8 h-6"
                       style={{
                         background: '#3e2723',
                         clipPath: 'polygon(0 0, 100% 0, 80% 100%, 20% 100%)',
                         boxShadow: '0 2px 4px rgba(0,0,0,0.3)'
                       }} />
                  <div className="absolute -bottom-6 right-12 w-8 h-6"
                       style={{
                         background: '#3e2723',
                         clipPath: 'polygon(0 0, 100% 0, 80% 100%, 20% 100%)',
                         boxShadow: '0 2px 4px rgba(0,0,0,0.3)'
                       }} />
                </>
              )}
            </div>
            
            {/* Gap between shelves */}
            {shelfIndex < shelves.length - 1 && (
              <div className="h-16" />
            )}
          </div>
        ))}
        
        {/* Bottom base of bookshelf */}
        <div className="relative mt-8">
          <div className="h-12 bg-amber-950 rounded-b-lg"
               style={{
                 background: 'linear-gradient(to bottom, #3e2723 0%, #2e1a17 100%)',
                 boxShadow: `
                   inset 0 4px 8px rgba(0,0,0,0.5),
                   0 4px 8px rgba(0,0,0,0.3)
                 `
               }}>
            {/* Base decoration */}
            <div className="absolute inset-x-8 top-1/2 -translate-y-1/2 h-4 bg-black/20 rounded-sm" />
          </div>
        </div>
        
        {/* Corner decorations */}
        <div className="absolute top-4 left-4 w-6 h-6 rounded-full bg-gold/30 shadow-inner"
             style={{
               boxShadow: 'inset 0 1px 3px rgba(0,0,0,0.5), 0 1px 2px rgba(212,175,55,0.3)'
             }} />
        <div className="absolute top-4 right-4 w-6 h-6 rounded-full bg-gold/30 shadow-inner"
             style={{
               boxShadow: 'inset 0 1px 3px rgba(0,0,0,0.5), 0 1px 2px rgba(212,175,55,0.3)'
             }} />
      </div>
      
      {/* Floor shadow */}
      <div className="h-8 bg-gradient-to-b from-black/20 to-transparent -mt-4 mx-8 blur-xl" />
    </div>
  );
}
