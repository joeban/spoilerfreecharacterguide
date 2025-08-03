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
    { primary: '#4a1a1a', secondary: '#5c2424', accent: '#d4af37' }, // burgundy
    { primary: '#1a3344', secondary: '#244454', accent: '#d4af37' }, // navy
    { primary: '#1a3a2a', secondary: '#2a5a3a', accent: '#d4af37' }, // forest
    { primary: '#3a1a4a', secondary: '#4a2a5a', accent: '#d4af37' }, // purple
    { primary: '#4a3a1a', secondary: '#5a4a2a', accent: '#d4af37' }, // brown
    { primary: '#2a2a3a', secondary: '#3a3a4a', accent: '#d4af37' }, // charcoal
  ];
  
  const colors = bookColors[colorIndex];
  
  return (
    <div className="book-container relative group transition-all duration-500 hover:scale-105 hover:-translate-y-2">
      
      {/* Book wrapper */}
      <div className="book relative" style={{ perspective: '600px' }}>
        
        {/* Main book block */}
        <div className="relative w-48 md:w-56 h-72 md:h-80"
             style={{
               transform: 'rotateY(-15deg)',
               transformStyle: 'preserve-3d'
             }}>
          
          {/* Book cover (front face) */}
          <div className="absolute inset-0"
               style={{
                 backgroundColor: colors.primary,
                 borderRadius: '0 3px 3px 0',
                 boxShadow: `
                   4px 6px 20px rgba(0,0,0,0.3),
                   inset -2px -2px 6px rgba(0,0,0,0.3),
                   inset 1px 1px 3px rgba(255,255,255,0.05)
                 `
               }}>
            
            {/* Subtle leather texture */}
            <div className="absolute inset-0 opacity-20"
                 style={{
                   background: `
                     repeating-linear-gradient(45deg, 
                       transparent, 
                       transparent 40px, 
                       rgba(0,0,0,0.03) 40px, 
                       rgba(0,0,0,0.03) 80px
                     )
                   `
                 }} />
            
            {/* Gold border frame */}
            <div className="absolute inset-6 border border-gold/30 rounded-sm"
                 style={{
                   boxShadow: `
                     inset 1px 1px 2px rgba(212,175,55,0.3),
                     inset -1px -1px 3px rgba(0,0,0,0.6)
                   `
                 }} />
            
            {/* Title and content */}
            <div className="absolute inset-0 flex flex-col items-center justify-center p-10 text-center">
              <h3 className="text-xl md:text-2xl font-display font-bold mb-3"
                  style={{ 
                    color: colors.accent,
                    textShadow: `
                      0 1px 3px rgba(0,0,0,0.8),
                      0 0 20px rgba(212,175,55,0.15)
                    `,
                    letterSpacing: '0.08em'
                  }}>
                {title}
              </h3>
              
              <div className="w-16 h-px bg-gold/40 mb-3" />
              
              <p className="text-sm md:text-base"
                 style={{ 
                   color: colors.accent,
                   textShadow: '0 1px 2px rgba(0,0,0,0.8)',
                   letterSpacing: '0.1em',
                   opacity: 0.85
                 }}>
                {author}
              </p>
              
              {bookCount > 1 && (
                <div className="absolute bottom-8 right-8">
                  <div className="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm"
                       style={{
                         backgroundColor: colors.primary,
                         color: colors.accent,
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
          </div>
          
          {/* Spine (left side) - visible due to rotation */}
          <div className="absolute left-0 top-0 bottom-0 w-8"
               style={{
                 backgroundColor: colors.secondary,
                 transform: 'translateX(-8px) rotateY(90deg)',
                 transformOrigin: 'right center',
                 background: `linear-gradient(to right,
                   rgba(0,0,0,0.3) 0%,
                   ${colors.secondary} 20%,
                   ${colors.secondary} 80%,
                   rgba(0,0,0,0.1) 100%
                 )`,
                 boxShadow: 'inset 0 0 10px rgba(0,0,0,0.3)'
               }}>
            {/* Spine bands */}
            <div className="absolute inset-x-1 top-1/4 h-px bg-black/30" />
            <div className="absolute inset-x-1 top-2/4 h-px bg-black/30" />
            <div className="absolute inset-x-1 top-3/4 h-px bg-black/30" />
          </div>
          
          {/* Top pages edge */}
          <div className="absolute top-0 left-0 right-0 h-6"
               style={{
                 backgroundColor: '#f5e6d3',
                 transform: 'translateY(-6px) rotateX(90deg)',
                 transformOrigin: 'bottom center',
                 background: `
                   linear-gradient(to bottom,
                     #fdfcf8 0%,
                     #f5e6d3 50%,
                     #ede0c8 100%
                   )
                 `,
                 boxShadow: 'inset 0 -1px 3px rgba(139,69,19,0.15)'
               }}>
            {/* Page texture lines */}
            <div className="absolute inset-0"
                 style={{
                   background: `repeating-linear-gradient(90deg,
                     transparent 0px,
                     rgba(139,69,19,0.05) 1px,
                     transparent 2px
                   )`
                 }} />
          </div>
          
          {/* Right side (back edge) */}
          <div className="absolute right-0 top-0 bottom-0 w-3"
               style={{
                 backgroundColor: colors.primary,
                 transform: 'translateX(3px) rotateY(90deg)',
                 transformOrigin: 'left center',
                 filter: 'brightness(0.85)',
                 boxShadow: 'inset -2px 0 4px rgba(0,0,0,0.3)'
               }} />
          
          {/* Bottom edge */}
          <div className="absolute bottom-0 left-0 right-0 h-3"
               style={{
                 backgroundColor: colors.primary,
                 transform: 'translateY(3px) rotateX(90deg)',
                 transformOrigin: 'top center',
                 filter: 'brightness(0.7)',
                 boxShadow: 'inset 0 -2px 4px rgba(0,0,0,0.4)'
               }} />
        </div>
        
        {/* Shadow */}
        <div className="absolute -bottom-4 left-4 right-0 h-6 bg-black/20 rounded-[50%] blur-xl" />
      </div>
    </div>
  );
}
