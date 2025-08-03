'use client';

interface BookSpineProps {
  title: string;
  author: string;
  bookCount: number;
}

export default function BookSpine({ title, author, bookCount }: BookSpineProps) {
  // Generate consistent colors based on the series
  const colorIndex = title.length % 6;
  const bookColors = [
    { primary: '#5c1a1a', secondary: '#7f1d1d', accent: '#8b2c2c' }, // deep red leather
    { primary: '#1a2f5a', secondary: '#1e3a8a', accent: '#2d4a9c' }, // navy leather
    { primary: '#1a3a1a', secondary: '#14532d', accent: '#2d5a2d' }, // forest green leather
    { primary: '#3a1a5a', secondary: '#581c87', accent: '#6a2c9c' }, // purple leather
    { primary: '#5a3a1a', secondary: '#8b4513', accent: '#a0522d' }, // brown leather
    { primary: '#2a2a4a', secondary: '#312e81', accent: '#3d3a9c' }, // midnight leather
  ];
  
  const colors = bookColors[colorIndex];
  
  return (
    <div className="book-container relative group transition-all duration-500 hover:scale-105 hover:-translate-y-2">
      
      {/* Main book wrapper with visible pages */}
      <div className="book relative">
        
        {/* Pages - Right side (visible edge) */}
        <div className="absolute top-2 bottom-2 -right-3 w-3 bg-gradient-to-r from-gray-100 to-gray-200 rounded-r-sm"
             style={{
               boxShadow: 'inset -1px 0 3px rgba(0,0,0,0.1)',
               background: `
                 repeating-linear-gradient(180deg,
                   #f8f5f0 0px,
                   #f8f5f0 1px,
                   #e8dfd0 1px,
                   #e8dfd0 1.5px
                 ),
                 linear-gradient(to right, #f4e8d0, #ede4d3)
               `
             }}>
        </div>
        
        {/* Pages - Bottom (visible edge) */}
        <div className="absolute left-2 right-2 -bottom-3 h-3 bg-gradient-to-b from-gray-100 to-gray-200 rounded-b-sm"
             style={{
               boxShadow: 'inset 0 -1px 3px rgba(0,0,0,0.1)',
               background: `
                 repeating-linear-gradient(90deg,
                   #f8f5f0 0px,
                   #f8f5f0 1px,
                   #e8dfd0 1px,
                   #e8dfd0 1.5px
                 ),
                 linear-gradient(to bottom, #f4e8d0, #ede4d3)
               `
             }}>
        </div>
        
        {/* Pages - Top (visible edge) */}
        <div className="absolute left-2 right-2 -top-3 h-3 bg-gradient-to-t from-gray-100 to-white rounded-t-sm"
             style={{
               boxShadow: 'inset 0 1px 3px rgba(0,0,0,0.05)',
               background: `
                 repeating-linear-gradient(90deg,
                   #fdfcf8 0px,
                   #fdfcf8 1px,
                   #f4e8d0 1px,
                   #f4e8d0 1.5px
                 ),
                 linear-gradient(to top, #f4e8d0, #fdfcf8)
               `
             }}>
        </div>
        
        {/* Book spine (thick left side) */}
        <div className="absolute -left-6 top-0 bottom-0 w-6 rounded-l-sm"
             style={{
               backgroundColor: colors.secondary,
               background: `
                 linear-gradient(90deg,
                   rgba(0,0,0,0.3) 0%,
                   ${colors.secondary} 10%,
                   ${colors.secondary} 90%,
                   rgba(0,0,0,0.2) 100%
                 )
               `,
               boxShadow: 'inset 0 0 10px rgba(0,0,0,0.4)'
             }}>
          {/* Raised bands on spine */}
          <div className="absolute top-8 left-0 right-0 h-0.5 bg-black/30" />
          <div className="absolute top-1/3 left-0 right-0 h-0.5 bg-black/30" />
          <div className="absolute top-2/3 left-0 right-0 h-0.5 bg-black/30" />
          <div className="absolute bottom-8 left-0 right-0 h-0.5 bg-black/30" />
        </div>
        
        {/* Book cover (front) - leather texture */}
        <div className="relative w-48 md:w-56 h-72 md:h-80 overflow-hidden rounded-r-sm"
             style={{
               backgroundColor: colors.primary,
               boxShadow: `
                 2px 4px 20px rgba(0,0,0,0.3),
                 inset -2px -2px 6px rgba(0,0,0,0.4),
                 inset 1px 1px 3px rgba(255,255,255,0.1)
               `,
               backgroundImage: `
                 repeating-linear-gradient(45deg, 
                   transparent, 
                   transparent 30px, 
                   rgba(0,0,0,0.03) 30px, 
                   rgba(0,0,0,0.03) 60px
                 ),
                 repeating-linear-gradient(-45deg, 
                   transparent, 
                   transparent 30px, 
                   rgba(0,0,0,0.03) 30px, 
                   rgba(0,0,0,0.03) 60px
                 )
               `
             }}>
          
          {/* Leather grain texture overlay */}
          <div className="absolute inset-0 opacity-20"
               style={{
                 backgroundImage: `url("data:image/svg+xml,%3Csvg width='4' height='4' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h1v1H0zM2 2h1v1H2z' fill='%23000000' opacity='0.1'/%3E%3C/svg%3E")`,
                 backgroundSize: '4px 4px'
               }} />
          
          {/* Embossed border - double frame for elegance */}
          <div className="absolute inset-6 border border-gold/30 rounded-sm"
               style={{
                 boxShadow: `
                   inset 1px 1px 3px rgba(212,175,55,0.4),
                   inset -1px -1px 3px rgba(0,0,0,0.6)
                 `
               }} />
          <div className="absolute inset-8 border border-gold/20 rounded-sm"
               style={{
                 boxShadow: `
                   inset 1px 1px 2px rgba(212,175,55,0.2),
                   inset -1px -1px 2px rgba(0,0,0,0.4)
                 `
               }} />
          
          {/* Title and author - embossed effect */}
          <div className="absolute inset-0 flex flex-col items-center justify-center p-10 text-center">
            <h3 className="text-xl md:text-2xl font-display font-bold mb-4"
                style={{ 
                  color: '#d4af37',
                  textShadow: `
                    1px 1px 0 rgba(255,255,255,0.2),
                    -1px -1px 2px rgba(0,0,0,0.8),
                    0 0 10px rgba(212,175,55,0.3)
                  `,
                  letterSpacing: '0.1em'
                }}>
              {title}
            </h3>
            
            {/* Decorative divider - embossed with dots */}
            <div className="flex items-center gap-2 mb-4">
              <div className="w-1 h-1 rounded-full bg-gold/50" />
              <div className="w-16 h-px"
                   style={{
                     background: 'linear-gradient(to right, transparent, #d4af37, transparent)',
                     boxShadow: '0 1px 1px rgba(0,0,0,0.5)'
                   }} />
              <div className="w-1 h-1 rounded-full bg-gold/50" />
            </div>
            
            {/* Author - embossed */}
            <p className="text-sm md:text-base"
               style={{ 
                 color: '#d4af37',
                 textShadow: `
                   1px 1px 0 rgba(255,255,255,0.15),
                   -1px -1px 2px rgba(0,0,0,0.8)
                 `,
                 letterSpacing: '0.15em',
                 opacity: 0.9
               }}>
              {author}
            </p>
            
            {/* Book count badge - embossed into leather */}
            {bookCount > 1 && (
              <div className="absolute bottom-8 right-8">
                <div className="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm"
                     style={{
                       backgroundColor: colors.primary,
                       color: '#d4af37',
                       boxShadow: `
                         inset 2px 2px 4px rgba(0,0,0,0.6),
                         inset -1px -1px 3px rgba(255,255,255,0.1)
                       `,
                       border: '1px solid rgba(212,175,55,0.2)'
                     }}>
                  {bookCount}
                </div>
              </div>
            )}
          </div>
          
          {/* Corner accents - small gold corners */}
          <div className="absolute top-4 left-4 w-4 h-4 border-l-2 border-t-2 border-gold/20" />
          <div className="absolute top-4 right-4 w-4 h-4 border-r-2 border-t-2 border-gold/20" />
          <div className="absolute bottom-4 left-4 w-4 h-4 border-l-2 border-b-2 border-gold/20" />
          <div className="absolute bottom-4 right-4 w-4 h-4 border-r-2 border-b-2 border-gold/20" />
          
          {/* Leather wear effect on edges */}
          <div className="absolute inset-0 rounded-r-sm"
               style={{
                 background: `
                   radial-gradient(ellipse at top left, transparent 70%, rgba(0,0,0,0.1) 100%),
                   radial-gradient(ellipse at bottom right, transparent 70%, rgba(0,0,0,0.1) 100%)
                 `
               }} />
          
          {/* Subtle highlight on hover */}
          <div className="absolute inset-0 bg-gradient-to-br from-white/0 via-white/5 to-white/0 opacity-0 group-hover:opacity-100 transition-opacity duration-700 rounded-r-sm" />
        </div>
        
        {/* Book shadow */}
        <div className="absolute -bottom-4 -left-2 right-2 h-6 bg-black/20 rounded-[50%] blur-xl transform group-hover:scale-110 transition-transform duration-500" />
      </div>
    </div>
  );
}
