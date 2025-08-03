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
    <div className="book-container relative group transition-all duration-500 hover:scale-105 hover:-translate-y-2"
         style={{ perspective: '800px' }}>
      
      {/* Main book with 3D rotation */}
      <div className="book relative w-48 md:w-56 h-72 md:h-80"
           style={{ 
             transformStyle: 'preserve-3d',
             transform: 'rotateY(25deg)'
           }}>
        
        {/* Book spine - visible from angle */}
        <div className="absolute left-0 top-0 bottom-0 w-12 md:w-16 origin-left"
             style={{
               backgroundColor: colors.secondary,
               transform: 'rotateY(90deg) translateZ(0px)',
               background: `linear-gradient(90deg, 
                 rgba(0,0,0,0.4) 0%, 
                 ${colors.secondary} 10%, 
                 ${colors.secondary} 90%, 
                 rgba(0,0,0,0.2) 100%)`,
               boxShadow: 'inset 0 0 20px rgba(0,0,0,0.3)'
             }}>
          {/* Raised bands on spine */}
          <div className="absolute inset-x-2 top-12 h-1 rounded-full"
               style={{ 
                 background: 'linear-gradient(90deg, transparent, rgba(0,0,0,0.3), transparent)',
                 boxShadow: '0 1px 0 rgba(255,255,255,0.1)'
               }} />
          <div className="absolute inset-x-2 top-1/3 h-1 rounded-full"
               style={{ 
                 background: 'linear-gradient(90deg, transparent, rgba(0,0,0,0.3), transparent)',
                 boxShadow: '0 1px 0 rgba(255,255,255,0.1)'
               }} />
          <div className="absolute inset-x-2 bottom-1/3 h-1 rounded-full"
               style={{ 
                 background: 'linear-gradient(90deg, transparent, rgba(0,0,0,0.3), transparent)',
                 boxShadow: '0 1px 0 rgba(255,255,255,0.1)'
               }} />
          <div className="absolute inset-x-2 bottom-12 h-1 rounded-full"
               style={{ 
                 background: 'linear-gradient(90deg, transparent, rgba(0,0,0,0.3), transparent)',
                 boxShadow: '0 1px 0 rgba(255,255,255,0.1)'
               }} />
          
          {/* Spine text (optional - rotated) */}
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="transform -rotate-90 text-xs opacity-50 text-gold whitespace-nowrap">
              {title}
            </div>
          </div>
        </div>
        
        {/* Pages - top edge (thick block of pages) */}
        <div className="absolute top-0 left-0 right-0 h-12 md:h-16 origin-top"
             style={{
               backgroundColor: '#f4e8d0',
               transform: 'rotateX(-90deg) translateZ(0px)',
               background: `
                 repeating-linear-gradient(0deg,
                   #fdfcf8 0px,
                   #fdfcf8 0.5px,
                   #ede0c8 0.5px,
                   #ede0c8 1px
                 ),
                 linear-gradient(to bottom, #fdfcf8 0%, #f4e8d0 100%)
               `,
               boxShadow: 'inset 0 2px 4px rgba(139,69,19,0.2)'
             }}>
          {/* Page texture for realism */}
          <div className="absolute inset-0 opacity-40"
               style={{
                 background: 'repeating-linear-gradient(90deg, transparent 0px, rgba(139,69,19,0.05) 1px, transparent 2px)'
               }} />
        </div>
        
        {/* Pages - fore-edge (right side) - NOT visible from this angle */}
        
        {/* Book back cover - visible at an angle */}
        <div className="absolute top-0 bottom-0 right-0 w-12 md:w-16 origin-right"
             style={{
               backgroundColor: colors.primary,
               transform: 'rotateY(90deg) translateZ(0px)',
               filter: 'brightness(0.9)',
               boxShadow: 'inset 0 0 10px rgba(0,0,0,0.4)'
             }} />
        
        {/* Book cover (front) */}
        <div className="absolute inset-0 origin-center"
             style={{
               backgroundColor: colors.primary,
               transform: 'translateZ(0px)',
               borderRadius: '4px 0 0 4px',
               boxShadow: `
                 -4px 8px 24px rgba(0,0,0,0.3),
                 inset 2px -2px 6px rgba(0,0,0,0.3),
                 inset -2px 2px 4px rgba(255,255,255,0.05)
               `
             }}>
          
          {/* Leather texture with grain */}
          <div className="absolute inset-0 opacity-20"
               style={{
                 backgroundImage: `
                   repeating-linear-gradient(45deg, 
                     transparent, 
                     transparent 30px, 
                     rgba(0,0,0,0.05) 30px, 
                     rgba(0,0,0,0.05) 60px
                   ),
                   repeating-linear-gradient(-45deg, 
                     transparent, 
                     transparent 30px, 
                     rgba(0,0,0,0.05) 30px, 
                     rgba(0,0,0,0.05) 60px
                   )
                 `,
                 borderRadius: '0 4px 4px 0'
               }} />
          
          {/* Embossed border */}
          <div className="absolute inset-6 border border-gold/40 rounded-sm"
               style={{
                 boxShadow: `
                   inset 2px 2px 4px rgba(212,175,55,0.3),
                   inset -2px -2px 4px rgba(0,0,0,0.6),
                   0 0 8px rgba(212,175,55,0.1)
                 `
               }} />
          
          {/* Title and author */}
          <div className="absolute inset-0 flex flex-col items-center justify-center p-10 text-center">
            <h3 className="text-xl md:text-2xl font-display font-bold mb-4"
                style={{ 
                  color: '#d4af37',
                  textShadow: `
                    0 2px 4px rgba(0,0,0,0.9),
                    0 0 20px rgba(212,175,55,0.2),
                    inset 0 -1px 0 rgba(0,0,0,0.5)
                  `,
                  letterSpacing: '0.08em'
                }}>
              {title}
            </h3>
            
            {/* Ornate divider */}
            <div className="flex items-center gap-2 mb-4">
              <div className="w-8 h-px bg-gradient-to-r from-transparent to-gold/50" />
              <div className="w-2 h-2 rounded-full bg-gold/40 shadow-sm" />
              <div className="w-8 h-px bg-gradient-to-l from-transparent to-gold/50" />
            </div>
            
            <p className="text-sm md:text-base"
               style={{ 
                 color: '#d4af37',
                 textShadow: '0 1px 3px rgba(0,0,0,0.9)',
                 letterSpacing: '0.12em',
                 opacity: 0.85
               }}>
              {author}
            </p>
            
            {/* Book count */}
            {bookCount > 1 && (
              <div className="absolute bottom-8 right-8">
                <div className="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm"
                     style={{
                       backgroundColor: colors.primary,
                       color: '#d4af37',
                       boxShadow: `
                         inset 2px 2px 4px rgba(0,0,0,0.7),
                         inset -1px -1px 2px rgba(255,255,255,0.05)
                       `,
                       border: '1px solid rgba(212,175,55,0.25)'
                     }}>
                  {bookCount}
                </div>
              </div>
            )}
          </div>
          
          {/* Wear and aging on corners */}
          <div className="absolute top-0 left-0 w-20 h-20 opacity-20"
               style={{
                 background: 'radial-gradient(ellipse at top left, rgba(0,0,0,0.3) 0%, transparent 60%)',
                 borderRadius: '4px 0 0 0'
               }} />
          <div className="absolute bottom-0 left-0 w-20 h-20 opacity-20"
               style={{
                 background: 'radial-gradient(ellipse at bottom left, rgba(0,0,0,0.3) 0%, transparent 60%)',
                 borderRadius: '0 0 0 4px'
               }} />
          
          {/* Hover shine */}
          <div className="absolute inset-0 bg-gradient-to-br from-transparent via-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none rounded-l" />
        </div>
        
        {/* Book back cover - barely visible for depth */}
        <div className="absolute inset-0"
             style={{
               backgroundColor: colors.primary,
               transform: 'translateZ(-16px)',
               filter: 'brightness(0.8)',
               boxShadow: '0 0 20px rgba(0,0,0,0.5)'
             }} />
        
        {/* Shadow */}
        <div className="absolute -bottom-6 left-0 right-4 h-6 bg-black/25 rounded-[40%] blur-2xl"
             style={{
               transform: 'rotateY(-25deg) translateZ(-20px)',
               transformOrigin: 'right center'
             }} />
      </div>
    </div>
  );
}
