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
         style={{ 
           perspective: '1000px',
           transformStyle: 'preserve-3d'
         }}>
      
      {/* Main book wrapper */}
      <div className="book relative"
           style={{ 
             transformStyle: 'preserve-3d',
             transform: 'rotateY(-5deg)'
           }}>
        
        {/* Back cover (slightly visible for depth) */}
        <div className="absolute inset-0 w-48 md:w-56 h-72 md:h-80"
             style={{
               backgroundColor: colors.primary,
               transform: 'translateZ(-40px)',
               boxShadow: '0 0 20px rgba(0,0,0,0.4)',
             }} />
        
        {/* Pages block - right side */}
        <div className="absolute right-0 top-1 bottom-1 w-10"
             style={{
               backgroundColor: '#f4e8d0',
               transform: 'rotateY(90deg) translateZ(20px)',
               transformOrigin: 'right',
               boxShadow: 'inset -2px 0 6px rgba(139,69,19,0.2)',
             }}>
          {/* Page texture */}
          <div className="h-full w-full"
               style={{
                 backgroundImage: `
                   repeating-linear-gradient(0deg, 
                     rgba(139,69,19,0.05) 0px, 
                     rgba(139,69,19,0.05) 1px, 
                     transparent 1px, 
                     transparent 2px
                   )
                 `
               }} />
        </div>
        
        {/* Pages block - top */}
        <div className="absolute top-0 left-1 right-1 h-10"
             style={{
               backgroundColor: '#f4e8d0',
               transform: 'rotateX(90deg) translateZ(20px)',
               transformOrigin: 'top',
               boxShadow: 'inset 0 -2px 6px rgba(139,69,19,0.2)',
             }}>
          {/* Page lines */}
          <div className="h-full w-full"
               style={{
                 backgroundImage: `
                   repeating-linear-gradient(90deg, 
                     rgba(139,69,19,0.05) 0px, 
                     rgba(139,69,19,0.05) 1px, 
                     transparent 1px, 
                     transparent 2px
                   ),
                   linear-gradient(to bottom, 
                     transparent, 
                     rgba(139,69,19,0.1)
                   )
                 `
               }} />
        </div>
        
        {/* Pages block - bottom */}
        <div className="absolute bottom-0 left-1 right-1 h-10"
             style={{
               backgroundColor: '#ede4d3',
               transform: 'rotateX(-90deg) translateZ(20px)',
               transformOrigin: 'bottom',
               boxShadow: 'inset 0 2px 6px rgba(139,69,19,0.2)',
             }}>
          <div className="h-full w-full"
               style={{
                 backgroundImage: `
                   repeating-linear-gradient(90deg, 
                     rgba(139,69,19,0.05) 0px, 
                     rgba(139,69,19,0.05) 1px, 
                     transparent 1px, 
                     transparent 2px
                   )
                 `
               }} />
        </div>
        
        {/* Book spine (left side) */}
        <div className="absolute left-0 top-0 bottom-0 w-10"
             style={{
               backgroundColor: colors.secondary,
               transform: 'rotateY(-90deg) translateZ(20px)',
               transformOrigin: 'left',
               boxShadow: 'inset 2px 0 4px rgba(0,0,0,0.3)',
               backgroundImage: `
                 linear-gradient(to right, 
                   rgba(0,0,0,0.2), 
                   transparent 20%, 
                   transparent 80%, 
                   rgba(0,0,0,0.2)
                 )
               `
             }}>
          {/* Raised bands on spine */}
          <div className="absolute top-8 left-0 right-0 h-1 bg-black/20" />
          <div className="absolute top-16 left-0 right-0 h-1 bg-black/20" />
          <div className="absolute bottom-16 left-0 right-0 h-1 bg-black/20" />
          <div className="absolute bottom-8 left-0 right-0 h-1 bg-black/20" />
        </div>
        
        {/* Book cover (front) - leather texture */}
        <div className="relative w-48 md:w-56 h-72 md:h-80 overflow-hidden"
             style={{
               backgroundColor: colors.primary,
               boxShadow: `
                 0 10px 40px rgba(0,0,0,0.4),
                 inset -2px -2px 6px rgba(0,0,0,0.3),
                 inset 1px 1px 3px rgba(255,255,255,0.1)
               `,
               transform: 'translateZ(0)',
               backgroundImage: `
                 repeating-linear-gradient(45deg, 
                   transparent, 
                   transparent 20px, 
                   rgba(0,0,0,0.02) 20px, 
                   rgba(0,0,0,0.02) 40px
                 ),
                 repeating-linear-gradient(-45deg, 
                   transparent, 
                   transparent 20px, 
                   rgba(0,0,0,0.02) 20px, 
                   rgba(0,0,0,0.02) 40px
                 )
               `
             }}>
          
          {/* Leather grain texture */}
          <div className="absolute inset-0 opacity-30"
               style={{
                 backgroundImage: `url("data:image/svg+xml,%3Csvg width='100' height='100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence baseFrequency='0.9' numOctaves='4' /%3E%3C/filter%3E%3Crect width='100' height='100' filter='url(%23noise)' opacity='0.4'/%3E%3C/svg%3E")`,
                 mixBlendMode: 'multiply'
               }} />
          
          {/* Embossed border */}
          <div className="absolute inset-6 border border-gold/40 rounded-sm"
               style={{
                 boxShadow: `
                   inset 1px 1px 2px rgba(212,175,55,0.3),
                   inset -1px -1px 2px rgba(0,0,0,0.5)
                 `
               }} />
          
          {/* Title and author - embossed effect */}
          <div className="absolute inset-0 flex flex-col items-center justify-center p-10 text-center">
            <h3 className="text-xl md:text-2xl font-display font-bold mb-4"
                style={{ 
                  color: '#d4af37',
                  textShadow: `
                    0 1px 0 rgba(255,255,255,0.2),
                    0 -1px 2px rgba(0,0,0,0.8),
                    0 2px 4px rgba(0,0,0,0.5)
                  `,
                  letterSpacing: '0.1em'
                }}>
              {title}
            </h3>
            
            {/* Decorative divider - embossed */}
            <div className="w-20 h-px mb-4"
                 style={{
                   background: 'linear-gradient(to right, transparent, #d4af37, transparent)',
                   boxShadow: '0 1px 1px rgba(0,0,0,0.5)'
                 }} />
            
            {/* Author - embossed */}
            <p className="text-sm md:text-base"
               style={{ 
                 color: '#d4af37',
                 textShadow: `
                   0 1px 0 rgba(255,255,255,0.2),
                   0 -1px 2px rgba(0,0,0,0.8)
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
                         inset 2px 2px 4px rgba(0,0,0,0.5),
                         inset -1px -1px 2px rgba(255,255,255,0.1)
                       `,
                       border: '1px solid rgba(212,175,55,0.3)'
                     }}>
                  {bookCount}
                </div>
              </div>
            )}
          </div>
          
          {/* Leather highlight on hover */}
          <div className="absolute inset-0 bg-gradient-to-br from-white/5 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700" />
        </div>
        
        {/* Book shadow */}
        <div className="absolute -bottom-4 left-2 right-2 h-8 bg-black/30 rounded-[50%] blur-2xl transform group-hover:scale-110 transition-transform duration-500" />
      </div>
    </div>
  );
}
