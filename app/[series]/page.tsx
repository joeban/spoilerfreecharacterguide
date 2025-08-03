import { getSeries, getBooksInSeries } from '@/lib/dataLoader';
import Link from 'next/link';
import { notFound } from 'next/navigation';

export default async function SeriesPage({
  params
}: {
  params: { series: string }
}) {
  const series = await getSeries(params.series);
  const books = await getBooksInSeries(params.series);
  
  if (!series || !books) {
    notFound();
  }
  
  // Amazon affiliate link for the series
  const amazonSearchUrl = `https://www.amazon.com/s?k=${encodeURIComponent(series.title + ' ' + series.author + ' box set')}&tag=spoilerfree-20`;
  
  // Get first book's ASIN for cover image (as representative of series)
  const firstBook = books[0]?.book;
  const coverImageUrl = firstBook?.asin 
    ? `https://images-na.ssl-images-amazon.com/images/P/${firstBook.asin}.01._SX300_.jpg`
    : null;
  
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h1 className="text-4xl md:text-5xl font-display mb-4 text-shadow-ink">
          {series.title}
        </h1>
        <p className="text-xl text-ink-light">
          by {series.author}
        </p>
        
        {/* Amazon affiliate link with cover image */}
        <div className="mt-8 flex flex-col items-center">
          <a
            href={amazonSearchUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="group"
          >
            <div className="relative overflow-hidden rounded-lg shadow-lg transition-all duration-300 group-hover:shadow-xl group-hover:scale-105">
              {coverImageUrl ? (
                <img 
                  src={coverImageUrl}
                  alt={`${series.title} series cover`}
                  className="w-48 h-auto"
                  loading="lazy"
                />
              ) : (
                <div className="w-48 h-72 bg-gradient-to-br from-leather to-leather-dark flex items-center justify-center">
                  <span className="text-parchment-dark text-sm text-center px-4">
                    {series.title}<br />Collection
                  </span>
                </div>
              )}
              {/* Overlay on hover */}
              <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300 flex items-center justify-center">
                <span className="text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-black/70 px-4 py-2 rounded">
                  View on Amazon
                </span>
              </div>
            </div>
          </a>
          <a
            href={amazonSearchUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 mt-4 px-6 py-3 bg-leather text-parchment rounded-md shadow-md hover:bg-leather-dark transition-all duration-200 hover:shadow-lg"
          >
            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
            </svg>
            Buy Complete Series on Amazon
          </a>
        </div>
      </div>
      
      <div className="max-w-6xl mx-auto">
        <div className="flex flex-wrap justify-center gap-8">
          {books.map(({ slug, book }, index) => {
            // Generate unique colors for each book
            const bookColors = [
              { primary: '#4a1a1a', secondary: '#5c2424' }, // burgundy
              { primary: '#1a3344', secondary: '#244454' }, // navy
              { primary: '#1a3a2a', secondary: '#2a5a3a' }, // forest
              { primary: '#3a1a4a', secondary: '#4a2a5a' }, // purple
              { primary: '#4a3a1a', secondary: '#5a4a2a' }, // brown
              { primary: '#2a2a3a', secondary: '#3a3a4a' }, // charcoal
              { primary: '#3a4a4a', secondary: '#4a5a5a' }, // slate
              { primary: '#4a2a2a', secondary: '#5a3a3a' }, // crimson
            ];
            const colors = bookColors[index % bookColors.length];
            
            return (
              <Link
                key={slug}
                href={`/${params.series}/${slug}`}
                className="block group"
              >
                <div className="book-container relative transition-all duration-500 hover:scale-105 hover:-translate-y-2">
                  <div className="book relative" 
                       style={{ 
                         width: '180px',
                         height: '240px',
                         transformStyle: 'preserve-3d',
                         transform: 'perspective(1200px) rotateY(30deg) rotateX(8deg)'
                       }}>
                    
                    {/* Front cover */}
                    <div className="absolute inset-0"
                         style={{
                           backgroundColor: colors.primary,
                           borderRadius: '0 3px 3px 0',
                           boxShadow: `
                             2px 4px 12px rgba(0,0,0,0.3),
                             inset -2px -2px 4px rgba(0,0,0,0.2),
                             inset 1px 1px 2px rgba(255,255,255,0.05)
                           `
                         }}>
                      
                      {/* Leather texture */}
                      <div className="absolute inset-0 opacity-10"
                           style={{
                             background: `repeating-linear-gradient(
                               45deg,
                               transparent,
                               transparent 40px,
                               rgba(0,0,0,0.05) 40px,
                               rgba(0,0,0,0.05) 80px
                             )`,
                             borderRadius: '0 3px 3px 0'
                           }} />
                      
                      {/* Gold border */}
                      <div className="absolute inset-5 border border-gold/30 rounded-sm"
                           style={{
                             boxShadow: `
                               inset 1px 1px 2px rgba(212,175,55,0.3),
                               inset -1px -1px 3px rgba(0,0,0,0.6)
                             `
                           }} />
                      
                      {/* Title */}
                      <div className="absolute inset-0 flex flex-col items-center justify-center p-6 text-center">
                        <h3 className="text-base font-display font-bold"
                            style={{ 
                              color: '#d4af37',
                              textShadow: `
                                0 1px 3px rgba(0,0,0,0.8),
                                0 0 20px rgba(212,175,55,0.15)
                              `,
                              letterSpacing: '0.05em'
                            }}>
                          {book.title}
                        </h3>
                        
                        <div className="w-12 h-px bg-gold/40 my-2" />
                        
                        <p className="text-xs"
                           style={{ 
                             color: '#d4af37',
                             textShadow: '0 1px 2px rgba(0,0,0,0.8)',
                             opacity: 0.8
                           }}>
                          {book.published}
                        </p>
                        
                        <p className="text-xs mt-1"
                           style={{ 
                             color: '#d4af37',
                             textShadow: '0 1px 2px rgba(0,0,0,0.8)',
                             opacity: 0.7
                           }}>
                          {book.chapters} chapters
                        </p>
                      </div>
                    </div>
                    
                    {/* Spine */}
                    <div className="absolute top-0 bottom-0"
                         style={{
                           left: 0,
                           width: '30px',
                           backgroundColor: colors.secondary,
                           transform: 'translateX(-30px) rotateY(-90deg)',
                           transformOrigin: 'right center',
                           background: `linear-gradient(to right,
                             rgba(0,0,0,0.3) 0%,
                             ${colors.secondary} 10%,
                             ${colors.secondary} 90%,
                             rgba(0,0,0,0.1) 100%
                           )`
                         }}>
                      <div className="absolute inset-x-1 top-1/3 h-0.5 bg-black/30 rounded-full" />
                      <div className="absolute inset-x-1 top-2/3 h-0.5 bg-black/30 rounded-full" />
                    </div>
                    
                    {/* Top pages */}
                    <div className="absolute left-0 right-0"
                         style={{
                           top: 0,
                           height: '30px',
                           backgroundColor: '#f5e6d3',
                           transform: 'translateY(-30px) rotateX(90deg)',
                           transformOrigin: 'bottom center',
                           background: `linear-gradient(to bottom,
                             #fdfcf8 0%,
                             #f5e6d3 60%,
                             #e8dcc4 100%
                           )`,
                           boxShadow: 'inset 0 -2px 4px rgba(139,69,19,0.1)'
                         }}>
                      <div className="absolute inset-0"
                           style={{
                             background: `repeating-linear-gradient(
                               90deg,
                               transparent 0px,
                               rgba(139,69,19,0.06) 0.5px,
                               transparent 1px
                             )`
                           }} />
                    </div>
                    
                    {/* Shadow */}
                    <div className="absolute"
                         style={{
                           bottom: '-15px',
                           left: '-20px',
                           right: '20px',
                           height: '20px',
                           background: 'radial-gradient(ellipse at center, rgba(0,0,0,0.25) 0%, transparent 60%)',
                           filter: 'blur(12px)',
                           transform: 'rotateY(-30deg) scaleY(0.5)'
                         }} />
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      </div>
      
      {/* Amazon affiliate disclosure */}
      <div className="mt-16 text-center">
        <p className="text-xs text-ink-light italic">
          As an Amazon Associate, we earn from qualifying purchases
        </p>
      </div>
    </div>
  );
}
