'use client';

interface BookSpineProps {
  title: string;
  author: string;
  bookCount: number;
  orientation?: 'vertical' | 'horizontal';
}

export default function BookSpine({ title, author, bookCount, orientation = 'vertical' }: BookSpineProps) {
  // Generate consistent colors based on the series
  const colorIndex = title.length % 8;
  const bookColorClasses = [
    'book-burgundy',
    'book-navy', 
    'book-forest',
    'book-purple',
    'book-brown',
    'book-charcoal',
    'book-crimson',
    'book-teal'
  ];
  
  const colorClass = bookColorClasses[colorIndex];
  
  if (orientation === 'horizontal') {
    return (
      <div className={`hearthstone-book ${colorClass} relative h-16 md:h-20 flex items-center px-6 cursor-pointer group`}>
        {/* Book spine decoration */}
        <div className="absolute left-2 top-2 bottom-2 w-1 bg-gradient-to-b from-amber-400/20 to-amber-600/20 rounded-full" />
        <div className="absolute right-2 top-2 bottom-2 w-1 bg-gradient-to-b from-amber-400/20 to-amber-600/20 rounded-full" />
        
        {/* Horizontal bands */}
        <div className="absolute inset-x-4 top-1/3 h-0.5 bg-gradient-to-r from-transparent via-amber-500/20 to-transparent" />
        <div className="absolute inset-x-4 bottom-1/3 h-0.5 bg-gradient-to-r from-transparent via-amber-500/20 to-transparent" />
        
        {/* Content */}
        <div className="flex items-center justify-between w-full">
          <div className="flex items-center gap-4">
            <h3 className="text-lg md:text-xl font-bold text-amber-100"
                style={{ 
                  fontFamily: 'MedievalSharp, serif',
                  textShadow: '2px 2px 4px rgba(0,0,0,0.8)'
                }}>
              {title}
            </h3>
            <span className="text-amber-200/70 text-sm hidden md:inline">by {author}</span>
          </div>
          
          {bookCount > 1 && (
            <div className="bg-amber-700/50 border border-amber-500/50 rounded-full w-8 h-8 flex items-center justify-center">
              <span className="text-amber-100 font-bold text-sm">{bookCount}</span>
            </div>
          )}
        </div>
      </div>
    );
  }
  
  // Vertical orientation (default)
  return (
    <div className={`hearthstone-book ${colorClass} relative w-44 md:w-52 h-64 md:h-72 p-4 flex flex-col items-center justify-center cursor-pointer group`}>
      {/* Book spine decorations */}
      <div className="absolute top-4 left-4 right-4 h-0.5 bg-gradient-to-r from-transparent via-amber-500/30 to-transparent" />
      <div className="absolute bottom-4 left-4 right-4 h-0.5 bg-gradient-to-r from-transparent via-amber-500/30 to-transparent" />
      
      {/* Corner ornaments */}
      <div className="absolute top-3 left-3 w-4 h-4 border-l-2 border-t-2 border-amber-500/30 rounded-tl" />
      <div className="absolute top-3 right-3 w-4 h-4 border-r-2 border-t-2 border-amber-500/30 rounded-tr" />
      <div className="absolute bottom-3 left-3 w-4 h-4 border-l-2 border-b-2 border-amber-500/30 rounded-bl" />
      <div className="absolute bottom-3 right-3 w-4 h-4 border-r-2 border-b-2 border-amber-500/30 rounded-br" />
      
      {/* Central gem/seal */}
      <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-24 h-24 rounded-full bg-gradient-to-br from-amber-600/10 to-amber-800/10 blur-xl" />
      
      {/* Title */}
      <h3 className="text-xl md:text-2xl font-bold text-amber-100 text-center mb-3 relative z-10"
          style={{ 
            fontFamily: 'MedievalSharp, serif',
            textShadow: '2px 2px 4px rgba(0,0,0,0.8), 0 0 20px rgba(255,191,0,0.3)'
          }}>
        {title}
      </h3>
      
      {/* Decorative divider */}
      <div className="w-16 h-0.5 bg-gradient-to-r from-transparent via-amber-500/50 to-transparent mb-3" />
      
      {/* Author */}
      <p className="text-amber-200/80 text-sm text-center relative z-10"
         style={{ 
           textShadow: '1px 1px 2px rgba(0,0,0,0.8)'
         }}>
        {author}
      </p>
      
      {/* Book count badge */}
      {bookCount > 1 && (
        <div className="absolute bottom-4 right-4 bg-amber-700/50 border border-amber-500/50 rounded-full w-10 h-10 flex items-center justify-center">
          <span className="text-amber-100 font-bold">{bookCount}</span>
        </div>
      )}
      
      {/* Magical hover glow is handled by CSS */}
    </div>
  );
}
