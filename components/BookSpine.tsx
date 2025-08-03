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
      
      {/* Main book wrapper */}
      <div className="book relative" style={{ perspective: '600px' }}>
        
        {/* Book spine (left side) */}
        <div className="absolute -left-4 top-0 bottom-0 w-4 rounded-l"
             style={{
               backgroundColor: colors.secondary,
               background: `linear-gradient(90deg, 
                 rgba(0,0,0,0.3) 0%, 
                 ${colors.secondary} 20%, 
                 ${colors.secondary} 80%, 
                 rgba(0,0,0,0.1) 100%)`,
               boxShadow: '-2px 0 4px rgba(0,0,0,0.3)'
             }}>
          {/* Spine bands */}
          <div className="absolute inset-x-0 top-1/4 h-px bg-black/20" />
          <div className="absolute inset-x-0 top-1/2 h-px bg-black/20" />
          <div className="absolute inset-x-0 bottom-1/4 h-px bg-black/20" />
        </div>
        
        {/* Pages block - right side */}
        <div className="absolute -right-2 top-1 bottom-1 w-2 bg-parchment rounded-r"
             style={{
               background: 'linear-gradient(to right, #f4e8d0 0%, #ede0c8 100%)',
               boxShadow: 'inset -1px 0 2px rgba(139,69,19,0.2)'
             }} />
        
        {/* Pages block - top */}
        <div className="absolute -top-2 left-0 right-0 h-2 bg-parchment"
             style={{
               background: 'linear-gradient(to bottom, #fdfcf8 0%, #f4e8d0 100%)',
               boxShadow: 'inset 0 -1px 2px rgba(139,69,19,0.1)'
             }} />
        
        {/* Pages block - bottom */}
        <div className="absolute -bottom-2 left-0 right-0 h-2 bg-parchment rounded-b"
             style={{
               background: 'linear-gradient(to top, #e8dcc4 0%, #f4e8d0 100%)',
               boxShadow: 'inset 0 1px 2px rgba(139,69,19,0.2)'
             }} />
        
        {/* Book cover (front) */}
        <div className="relative w-48 md:w-56 h-72 md:h-80 overflow-hidden rounded-r"
             style={{
               backgroundColor: colors.primary,
               transform: 'rotateY(-2deg)',
               transformOrigin: 'left center',
               boxShadow: `
                 4px 4px 12px rgba(0,0,0,0.3),
                 inset -1px -1px 2px rgba(0,0,0,0.2),
                 inset 1px 1px 2px rgba(255,255,255,0.05)
               `
             }}>
          
          {/* Subtle leather texture */}
          <div className="absolute inset-0"
               style={{
                 backgroundImage: `
                   radial-gradient(ellipse at top left, rgba(255,255,255,0.05) 0%, transparent 50%),
                   radial-gradient(ellipse at bottom right, rgba(0,0,0,0.1) 0%, transparent 50%)
                 `,
                 mixBlendMode: 'overlay'
               }} />
          
          {/* Embossed border frame */}
          <div className="absolute inset-6 border border-gold/40 rounded-sm"
               style={{
                 boxShadow: `
                   inset 1px 1px 2px rgba(212,175,55,0.3),
                   inset -1px -1px 2px rgba(0,0,0,0.5),
                   0 0 4px rgba(212,175,55,0.1)
                 `
               }} />
          
          {/* Title and author */}
          <div className="absolute inset-0 flex flex-col items-center justify-center p-10 text-center">
            <h3 className="text-xl md:text-2xl font-display font-bold mb-3"
                style={{ 
                  color: '#d4af37',
                  textShadow: `
                    0 1px 2px rgba(0,0,0,0.8),
                    0 0 12px rgba(212,175,55,0.2)
                  `,
                  letterSpacing: '0.08em'
                }}>
              {title}
            </h3>
            
            {/* Simple decorative line */}
            <div className="w-16 h-px bg-gold/50 mb-3 shadow-sm" />
            
            <p className="text-sm md:text-base"
               style={{ 
                 color: '#d4af37',
                 textShadow: '0 1px 2px rgba(0,0,0,0.8)',
                 letterSpacing: '0.12em',
                 opacity: 0.85
               }}>
              {author}
            </p>
            
            {/* Book count */}
            {bookCount > 1 && (
              <div className="absolute bottom-6 right-6">
                <div className="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm"
                     style={{
                       backgroundColor: colors.primary,
                       color: '#d4af37',
                       boxShadow: `
                         inset 1px 1px 3px rgba(0,0,0,0.5),
                         inset -1px -1px 2px rgba(255,255,255,0.05)
                       `,
                       border: '1px solid rgba(212,175,55,0.25)'
                     }}>
                  {bookCount}
                </div>
              </div>
            )}
          </div>
          
          {/* Hover shine effect */}
          <div className="absolute inset-0 bg-gradient-to-br from-transparent via-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none" />
        </div>
        
        {/* Shadow */}
        <div className="absolute -bottom-3 left-2 right-2 h-4 bg-black/20 rounded-[50%] blur-lg transform group-hover:scale-110 transition-transform duration-500" />
      </div>
    </div>
  );
}
