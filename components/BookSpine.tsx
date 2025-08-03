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
  const thickness = 40; // Book thickness in pixels
  
  return (
    <div className="book-container relative group transition-all duration-500 hover:scale-105 hover:-translate-y-2">
      
      {/* Book wrapper with 3D perspective */}
      <div className="book relative" 
           style={{ 
             width: '200px',
             height: '280px',
             transformStyle: 'preserve-3d',
             transform: 'perspective(1000px) rotateY(-20deg)'
           }}>
        
        {/* Front cover */}
        <div className="absolute inset-0"
             style={{
               width: '200px',
               height: '280px',
               backgroundColor: colors.primary,
               borderRadius: '0 3px 3px 0',
               transformOrigin: 'left center',
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
          <div className="absolute inset-6 border border-gold/40 rounded-sm"
               style={{
                 boxShadow: `
                   inset 1px 1px 2px rgba(212,175,55,0.3),
                   inset -1px -1px 3px rgba(0,0,0,0.6)
                 `
               }} />
          
          {/* Title and author */}
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
        
        {/* Spine */}
        <div className="absolute top-0 bottom-0"
             style={{
               left: 0,
               width: `${thickness}px`,
               backgroundColor: colors.secondary,
               transform: `translateX(-${thickness}px) rotateY(-90deg)`,
               transformOrigin: 'right center',
               background: `linear-gradient(to right,
                 rgba(0,0,0,0.3) 0%,
                 ${colors.secondary} 10%,
                 ${colors.secondary} 90%,
                 rgba(0,0,0,0.1) 100%
               )`
             }}>
          {/* Raised bands */}
          <div className="absolute inset-x-2 top-1/4 h-0.5 bg-black/30 rounded-full" />
          <div className="absolute inset-x-2 top-2/4 h-0.5 bg-black/30 rounded-full" />
          <div className="absolute inset-x-2 top-3/4 h-0.5 bg-black/30 rounded-full" />
        </div>
        
        {/* Top edge (pages) */}
        <div className="absolute left-0 right-0"
             style={{
               top: 0,
               height: `${thickness}px`,
               backgroundColor: '#f5e6d3',
               transform: `translateY(-${thickness}px) rotateX(90deg)`,
               transformOrigin: 'bottom center',
               background: `linear-gradient(to bottom,
                 #fdfcf8 0%,
                 #f5e6d3 60%,
                 #e8dcc4 100%
               )`,
               boxShadow: 'inset 0 -2px 4px rgba(139,69,19,0.1)'
             }}>
          {/* Page texture */}
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
        
        {/* Back cover */}
        <div className="absolute top-0 bottom-0"
             style={{
               left: 0,
               width: '200px',
               height: '280px',
               backgroundColor: colors.primary,
               transform: `translateZ(-${thickness}px)`,
               filter: 'brightness(0.85)',
               borderRadius: '0 3px 3px 0'
             }} />
        
        {/* Right edge */}
        <div className="absolute top-0 bottom-0"
             style={{
               right: 0,
               width: `${thickness}px`,
               backgroundColor: colors.primary,
               transform: `translateX(${thickness/2}px) translateZ(-${thickness/2}px) rotateY(90deg)`,
               transformOrigin: 'center center',
               filter: 'brightness(0.8)'
             }} />
        
        {/* Bottom edge */}
        <div className="absolute left-0 right-0"
             style={{
               bottom: 0,
               height: `${thickness}px`,
               backgroundColor: colors.primary,
               transform: `translateY(${thickness/2}px) translateZ(-${thickness/2}px) rotateX(-90deg)`,
               transformOrigin: 'center center',
               filter: 'brightness(0.7)'
             }} />
        
        {/* Cast shadow */}
        <div className="absolute"
             style={{
               bottom: '-20px',
               left: '10px',
               right: '-10px',
               height: '20px',
               background: 'radial-gradient(ellipse at center, rgba(0,0,0,0.3) 0%, transparent 70%)',
               filter: 'blur(15px)',
               transform: 'rotateY(20deg)'
             }} />
      </div>
    </div>
  );
}
