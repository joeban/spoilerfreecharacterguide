'use client';

interface BookSpineProps {
  title: string;
  author: string;
  bookCount: number;
}

export default function BookSpine({ title, author, bookCount }: BookSpineProps) {
  // Generate a consistent color based on the title
  const colorIndex = title.length % 6;
  const spineColors = [
    '#991b1b', // red-800
    '#1e3a8a', // blue-800
    '#14532d', // green-800
    '#581c87', // purple-800
    '#a16207', // yellow-700
    '#312e81', // indigo-800
  ];
  
  const spineColor = spineColors[colorIndex];
  
  return (
    <div className="book-spine group relative h-48 md:h-64 w-12 md:w-16 transition-all duration-300"
         style={{
           backgroundColor: spineColor,
           transform: 'rotateY(-20deg)',
           transformStyle: 'preserve-3d',
           boxShadow: '-2px 0 4px rgba(0,0,0,0.4), -4px 0 8px rgba(0,0,0,0.2), inset 1px 0 1px rgba(255,255,255,0.2)',
         }}
         onMouseEnter={(e) => {
           e.currentTarget.style.transform = 'rotateY(-10deg) translateZ(10px)';
         }}
         onMouseLeave={(e) => {
           e.currentTarget.style.transform = 'rotateY(-20deg)';
         }}>
      
      {/* Spine decoration - gradient overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-transparent via-black/20 to-transparent rounded-sm" />
      
      {/* Gold foil stripes at top and bottom */}
      <div className="absolute top-4 left-0 right-0 h-px"
           style={{
             background: 'linear-gradient(to right, transparent, #d4af37, transparent)'
           }} />
      <div className="absolute bottom-4 left-0 right-0 h-px"
           style={{
             background: 'linear-gradient(to right, transparent, #d4af37, transparent)'
           }} />
      
      {/* Title and author (rotated) */}
      <div className="absolute inset-0 flex items-center justify-center">
        <div className="transform -rotate-90 whitespace-nowrap text-center"
             style={{ color: '#f4e8d0' }}>
          <div className="text-xs md:text-sm font-bold tracking-wider mb-1"
               style={{ fontFamily: 'Cinzel, serif' }}>
            {title}
          </div>
          <div className="text-[10px] md:text-xs opacity-80">
            {author}
          </div>
        </div>
      </div>
      
      {/* Book count badge */}
      {bookCount > 1 && (
        <div className="absolute bottom-2 left-1/2 transform -translate-x-1/2">
          <div className="text-xs rounded-full w-5 h-5 flex items-center justify-center font-bold"
               style={{
                 backgroundColor: '#d4af37',
                 color: '#2c1810'
               }}>
            {bookCount}
          </div>
        </div>
      )}
      
      {/* Hover shine effect */}
      <div className="absolute inset-0 bg-gradient-to-t from-transparent to-white/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-sm" />
    </div>
  );
}
