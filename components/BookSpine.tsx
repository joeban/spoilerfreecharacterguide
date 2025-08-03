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
    { primary: '#4a1a1a', secondary: '#6b2424', pages: '#f5e6d3' }, // burgundy leather
    { primary: '#1a2844', secondary: '#243454', pages: '#f5e6d3' }, // navy leather
    { primary: '#1a3a2a', secondary: '#245434', pages: '#f5e6d3' }, // forest leather
    { primary: '#3a1a4a', secondary: '#542474', pages: '#f5e6d3' }, // purple leather
    { primary: '#4a3a1a', secondary: '#6b5424', pages: '#f5e6d3' }, // brown leather
    { primary: '#2a2a3a', secondary: '#3a3a4a', pages: '#f5e6d3' }, // charcoal leather
  ];
  
  const colors = bookColors[colorIndex];
  
  return (
    <div className="book-container relative group transition-all duration-500 hover:scale-105 hover:-translate-y-2">
      
      {/* Main book block with subtle 3D rotation */}
      <div className="book relative"
           style={{ 
             width: '200px',
             height: '280px',
             transform: 'rotateY(-8deg) rotateX(2deg)',
             transformStyle: 'preserve-3d'
           }}>
        
        {/* Spine - just barely visible on left */}
        <div className="absolute -left-3 top-0 bottom-0 w-3"
             style={{
               background: `linear-gradient(to right, 
                 ${colors.secondary} 0%, 
                 ${colors.primary} 100%)`,
               boxShadow: '-2px 0 4px rgba(0,0,0,0.4)',
               borderRadius: '2px 0 0 2px'
             }}>
          {/* Subtle raised bands */}
          <div className="absolute inset-x-0 top-1/4 h-px bg-black/20" />
          <div className="absolute inset-x-0 top-2/4 h-px bg-black/20" />
          <div className="absolute inset-x-0 top-3/4 h-px bg-black/20" />
        </div>
        
        {/* Pages block - top (prominent for thickness) */}
        <div className="absolute -top-8 left-0 right-0 h-8"
             style={{
               background: `linear-gradient(to bottom,
                 #fdfaf5 0%,
                 ${colors.pages} 50%,
                 #e8dcc8 100%)`,
               boxShadow: 'inset 0 -2px 4px rgba(0,0,0,0.1)',
               borderRadius: '0 2px 0 0'
             }}>
          {/* Page edge texture */}
          <div className="absolute inset-0"
               style={{
                 background: `repeating-linear-gradient(90deg,
                   transparent 0px,
                   transparent 0.5px,
                   rgba(139,69,19,0.08) 0.5px,
                   rgba(139,69,19,0.08) 1px
                 )`
               }} />
        </div>
        
        {/* Main cover */}
        <div className="relative w-full h-full overflow-hidden"
             style={{
               backgroundColor: colors.primary,
               borderRadius: '0 4px 4px 0',
               boxShadow: `
                 0 6px 20px rgba(0,0,0,0.3),
                 inset 0 0 60px rgba(0,0,0,0.1),
                 inset 2px 2px 4px rgba(255,255,255,0.02)
               `
             }}>
          
          {/* Leather texture */}
          <div className="absolute inset-0 opacity-30"
               style={{
                 backgroundImage: `url("data:image/svg+xml,%3Csvg width='4' height='4' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h2v2H0zm2 2h2v2H2z' fill='%23000000' opacity='0.05'/%3E%3C/svg%3E")`,
                 backgroundSize: '4px 4px'
               }} />
          
          {/* Gold embossed border - single elegant frame */}
          <div className="absolute inset-6 border-2 border-gold/30"
               style={{
                 boxShadow: `
                   inset 1px 1px 3px rgba(212,175,55,0.4),
                   inset -1px -1px 3px rgba(0,0,0,0.6),
                   0 0 10px rgba(212,175,55,0.05)
                 `,
                 borderRadius: '2px'
               }} />
          
          {/* Corner ornaments */}
          <div className="absolute top-5 left-5 w-8 h-8 border-l-2 border-t-2 border-gold/20" />
          <div className="absolute top-5 right-5 w-8 h-8 border-r-2 border-t-2 border-gold/20" />
          <div className="absolute bottom-5 left-5 w-8 h-8 border-l-2 border-b-2 border-gold/20" />
          <div className="absolute bottom-5 right-5 w-8 h-8 border-r-2 border-b-2 border-gold/20" />
          
          {/* Title and author */}
          <div className="absolute inset-0 flex flex-col items-center justify-center p-12 text-center">
            <h3 className="text-2xl font-display font-semibold mb-4 tracking-wide"
                style={{ 
                  color: '#d4af37',
                  textShadow: `
                    1px 1px 0 rgba(0,0,0,0.8),
                    0 0 30px rgba(212,175,55,0.2),
                    0 2px 4px rgba(0,0,0,0.6)
                  `,
                  letterSpacing: '0.05em',
                  fontWeight: '600'
                }}>
              {title}
            </h3>
            
            {/* Simple line ornament */}
            <div className="w-20 h-0.5 mb-4"
                 style={{
                   background: 'linear-gradient(to right, transparent, #d4af37, transparent)',
                   boxShadow: '0 1px 2px rgba(0,0,0,0.5)'
                 }} />
            
            <p className="text-base tracking-wider"
               style={{ 
                 color: '#d4af37',
                 textShadow: '1px 1px 2px rgba(0,0,0,0.8)',
                 letterSpacing: '0.1em',
                 opacity: 0.9,
                 fontWeight: '400'
               }}>
              {author}
            </p>
            
            {/* Book count - subtle bottom corner */}
            {bookCount > 1 && (
              <div className="absolute bottom-10 right-10">
                <div className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold"
                     style={{
                       backgroundColor: colors.primary,
                       color: '#d4af37',
                       boxShadow: `
                         inset 1px 1px 3px rgba(0,0,0,0.6),
                         inset -1px -1px 2px rgba(255,255,255,0.02)
                       `,
                       border: '1px solid rgba(212,175,55,0.2)'
                     }}>
                  {bookCount}
                </div>
              </div>
            )}
          </div>
          
          {/* Subtle aging/wear */}
          <div className="absolute inset-0"
               style={{
                 background: `
                   radial-gradient(ellipse at 20% 30%, transparent 40%, rgba(0,0,0,0.05) 100%),
                   radial-gradient(ellipse at 80% 70%, transparent 40%, rgba(0,0,0,0.05) 100%)
                 `,
                 borderRadius: '0 4px 4px 0'
               }} />
          
          {/* Hover glow */}
          <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-700"
               style={{
                 background: 'radial-gradient(ellipse at center, rgba(212,175,55,0.05) 0%, transparent 60%)',
                 borderRadius: '0 4px 4px 0'
               }} />
        </div>
        
        {/* Right edge - subtle depth */}
        <div className="absolute top-0 bottom-0 -right-2 w-2"
             style={{
               background: `linear-gradient(to left, 
                 rgba(0,0,0,0.3) 0%, 
                 ${colors.primary} 100%)`,
               filter: 'brightness(0.8)'
             }} />
        
        {/* Bottom edge - subtle */}
        <div className="absolute left-0 right-0 -bottom-2 h-2"
             style={{
               background: colors.primary,
               filter: 'brightness(0.7)',
               boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.4)'
             }} />
        
        {/* Cast shadow */}
        <div className="absolute -bottom-4 left-2 right-2 h-6 bg-black/20 blur-2xl"
             style={{
               borderRadius: '50%',
               transform: 'rotateY(8deg)'
             }} />
      </div>
    </div>
  );
}
