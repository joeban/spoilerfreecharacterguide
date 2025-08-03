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
      
      {/* Main book block */}
      <div className="book relative w-48 md:w-56 h-72 md:h-80">
        
        {/* Book spine (left side) - continuous with cover */}
        <div className="absolute left-0 top-0 bottom-0 w-8 md:w-10 z-10"
             style={{
               backgroundColor: colors.secondary,
               background: `linear-gradient(90deg, 
                 rgba(0,0,0,0.3) 0%, 
                 ${colors.secondary} 15%, 
                 ${colors.secondary} 85%, 
                 rgba(0,0,0,0.1) 100%)`,
               borderRadius: '4px 0 0 4px',
               boxShadow: 'inset 2px 0 4px rgba(0,0,0,0.2)'
             }}>
          {/* Raised spine bands */}
          <div className="absolute inset-x-1 top-12 h-0.5 bg-black/20" />
          <div className="absolute inset-x-1 top-1/3 h-0.5 bg-black/20" />
          <div className="absolute inset-x-1 bottom-1/3 h-0.5 bg-black/20" />
          <div className="absolute inset-x-1 bottom-12 h-0.5 bg-black/20" />
        </div>
        
        {/* Pages block - top edge (visible from above angle) */}
        <div className="absolute top-0 left-8 md:left-10 right-0 h-3 z-0"
             style={{
               background: 'linear-gradient(to bottom, #fdfcf8 0%, #f4e8d0 100%)',
               borderRadius: '0 4px 0 0',
               boxShadow: 'inset 0 -1px 3px rgba(139,69,19,0.15)',
               transform: 'translateY(-3px)'
             }} />
        
        {/* Pages block - right edge */}
        <div className="absolute top-0 bottom-0 right-0 w-3 z-0"
             style={{
               background: 'linear-gradient(to right, #f4e8d0 0%, #ede0c8 100%)',
               borderRadius: '0 4px 4px 0',
               boxShadow: 'inset -2px 0 4px rgba(139,69,19,0.2)',
               transform: 'translateX(3px)'
             }} />
        
        {/* Book cover (front) - overlaps spine seamlessly */}
        <div className="absolute inset-0 overflow-hidden z-10"
             style={{
               backgroundColor: colors.primary,
               borderRadius: '4px',
               boxShadow: `
                 0 8px 24px rgba(0,0,0,0.25),
                 0 2px 8px rgba(0,0,0,0.15),
                 inset -2px -2px 4px rgba(0,0,0,0.2),
                 inset 1px 1px 2px rgba(255,255,255,0.05)
               `
             }}>
          
          {/* Leather texture gradient */}
          <div className="absolute inset-0"
               style={{
                 background: `
                   radial-gradient(ellipse at 30% 20%, rgba(255,255,255,0.03) 0%, transparent 40%),
                   radial-gradient(ellipse at 70% 80%, rgba(0,0,0,0.15) 0%, transparent 40%),
                   linear-gradient(135deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.05) 100%)
                 `
               }} />
          
          {/* Embossed double border frame */}
          <div className="absolute inset-6 border border-gold/40 rounded-sm"
               style={{
                 boxShadow: `
                   inset 1px 1px 2px rgba(212,175,55,0.3),
                   inset -1px -1px 3px rgba(0,0,0,0.6)
                 `
               }} />
          <div className="absolute inset-8 border border-gold/20 rounded-sm"
               style={{
                 boxShadow: `
                   inset 0.5px 0.5px 1px rgba(212,175,55,0.2),
                   inset -0.5px -0.5px 2px rgba(0,0,0,0.4)
                 `
               }} />
          
          {/* Title and author centered */}
          <div className="absolute inset-0 flex flex-col items-center justify-center p-10 text-center">
            <h3 className="text-xl md:text-2xl font-display font-bold mb-3"
                style={{ 
                  color: '#d4af37',
                  textShadow: `
                    0 2px 4px rgba(0,0,0,0.8),
                    0 0 20px rgba(212,175,55,0.15)
                  `,
                  letterSpacing: '0.08em'
                }}>
              {title}
            </h3>
            
            {/* Decorative separator */}
            <div className="flex items-center gap-3 mb-3">
              <div className="w-12 h-px bg-gradient-to-r from-transparent to-gold/40" />
              <div className="w-1.5 h-1.5 rounded-full bg-gold/40" />
              <div className="w-12 h-px bg-gradient-to-l from-transparent to-gold/40" />
            </div>
            
            <p className="text-sm md:text-base"
               style={{ 
                 color: '#d4af37',
                 textShadow: '0 1px 3px rgba(0,0,0,0.8)',
                 letterSpacing: '0.12em',
                 opacity: 0.85
               }}>
              {author}
            </p>
            
            {/* Book count badge */}
            {bookCount > 1 && (
              <div className="absolute bottom-8 right-8">
                <div className="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm"
                     style={{
                       backgroundColor: colors.primary,
                       color: '#d4af37',
                       boxShadow: `
                         inset 2px 2px 4px rgba(0,0,0,0.6),
                         inset -1px -1px 2px rgba(255,255,255,0.05)
                       `,
                       border: '1px solid rgba(212,175,55,0.2)'
                     }}>
                  {bookCount}
                </div>
              </div>
            )}
          </div>
          
          {/* Subtle corner wear */}
          <div className="absolute top-0 left-0 w-16 h-16 opacity-10"
               style={{
                 background: 'radial-gradient(ellipse at top left, black 0%, transparent 70%)'
               }} />
          <div className="absolute bottom-0 right-0 w-16 h-16 opacity-10"
               style={{
                 background: 'radial-gradient(ellipse at bottom right, black 0%, transparent 70%)'
               }} />
          
          {/* Hover highlight */}
          <div className="absolute inset-0 bg-gradient-to-br from-transparent via-white/3 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none rounded" />
        </div>
        
        {/* Drop shadow */}
        <div className="absolute -bottom-4 left-4 right-4 h-4 bg-black/15 rounded-[50%] blur-xl transform group-hover:scale-105 transition-transform duration-500" />
      </div>
    </div>
  );
}
