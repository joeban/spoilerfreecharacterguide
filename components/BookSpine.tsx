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
    'bg-red-800',
    'bg-blue-800',
    'bg-green-800',
    'bg-purple-800',
    'bg-yellow-700',
    'bg-indigo-800',
  ];
  
  return (
    <div className="book-spine group">
      <div className={`relative h-64 w-16 ${spineColors[colorIndex]} rounded-sm shadow-lg overflow-hidden`}>
        {/* Spine decoration */}
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-black/20 to-transparent" />
        
        {/* Gold foil stripes */}
        <div className="absolute top-4 left-0 right-0 h-px bg-gradient-to-r from-transparent via-gold to-transparent" />
        <div className="absolute bottom-4 left-0 right-0 h-px bg-gradient-to-r from-transparent via-gold to-transparent" />
        
        {/* Title and author (rotated) */}
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="transform -rotate-90 whitespace-nowrap text-parchment">
            <div className="text-xs font-display tracking-wider mb-2">
              {title}
            </div>
            <div className="text-[10px] opacity-80">
              {author}
            </div>
          </div>
        </div>
        
        {/* Book count badge */}
        {bookCount > 1 && (
          <div className="absolute bottom-2 left-1/2 transform -translate-x-1/2">
            <div className="bg-gold text-ink text-[10px] rounded-full w-5 h-5 flex items-center justify-center font-bold">
              {bookCount}
            </div>
          </div>
        )}
        
        {/* Hover effect */}
        <div className="absolute inset-0 bg-gradient-to-t from-transparent to-white/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
      </div>
    </div>
  );
}
