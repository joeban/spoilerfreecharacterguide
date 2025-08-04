import clsx from 'clsx';

interface BookSpineProps {
  title: string;
  author: string;
  bookCount: number;
  orientation?: 'vertical' | 'horizontal';
}

// Book color patterns for variety
const bookColors = [
  { spine: 'from-amber-900 to-amber-950', cover: 'from-amber-800 to-amber-900', accent: 'border-amber-700' },
  { spine: 'from-red-900 to-red-950', cover: 'from-red-800 to-red-900', accent: 'border-red-700' },
  { spine: 'from-green-900 to-green-950', cover: 'from-green-800 to-green-900', accent: 'border-green-700' },
  { spine: 'from-blue-900 to-blue-950', cover: 'from-blue-800 to-blue-900', accent: 'border-blue-700' },
  { spine: 'from-purple-900 to-purple-950', cover: 'from-purple-800 to-purple-900', accent: 'border-purple-700' },
  { spine: 'from-slate-800 to-slate-900', cover: 'from-slate-700 to-slate-800', accent: 'border-slate-600' },
];

export default function BookSpine({ title, author, bookCount, orientation = 'vertical' }: BookSpineProps) {
  // Use title length to consistently assign colors
  const colorIndex = title.length % bookColors.length;
  const colors = bookColors[colorIndex];
  
  if (orientation === 'horizontal') {
    // Keep horizontal layout for now if needed
    return (
      <div className={clsx(
        'hearthstone-book-horizontal',
        'h-20 w-full px-6 py-3',
        'bg-gradient-to-r',
        colors.cover,
        'border-2',
        colors.accent,
        'rounded-lg',
        'flex items-center justify-between',
        'shadow-lg hover:shadow-xl',
        'transition-all duration-300'
      )}>
        <div>
          <h3 className="text-lg font-display text-amber-100">{title}</h3>
          <p className="text-sm text-amber-200/70">{author}</p>
        </div>
        <div className="flex items-center justify-center w-10 h-10 bg-amber-600/20 rounded-full">
          <span className="text-amber-100 font-bold">{bookCount}</span>
        </div>
      </div>
    );
  }
  
  // 3D vertical book
  return (
    <div className="book-3d-container">
      <div className="book-3d">
        {/* Book spine (left side) */}
        <div className={clsx(
          'book-spine',
          'bg-gradient-to-b',
          colors.spine
        )}>
          {/* Decorative spine details */}
          <div className="spine-decoration">
            {/* Top ornament */}
            <div className="w-full h-4 bg-gradient-to-b from-amber-500/30 to-transparent" />
            
            {/* Title on spine (rotated) */}
            <div className="flex-1 flex items-center justify-center px-1">
              <span className="text-amber-200/60 text-xs writing-mode-vertical whitespace-nowrap overflow-hidden text-ellipsis max-h-full">
                {title}
              </span>
            </div>
            
            {/* Bottom ornament */}
            <div className="w-full h-4 bg-gradient-to-t from-amber-500/30 to-transparent" />
          </div>
        </div>
        
        {/* Book cover (front) */}
        <div className={clsx(
          'book-cover',
          'bg-gradient-to-br',
          colors.cover,
          'border-2',
          colors.accent
        )}>
          {/* Decorative corner flourishes */}
          <div className="absolute top-2 left-2 w-4 h-4 border-l-2 border-t-2 border-amber-500/30 rounded-tl" />
          <div className="absolute top-2 right-2 w-4 h-4 border-r-2 border-t-2 border-amber-500/30 rounded-tr" />
          <div className="absolute bottom-2 left-2 w-4 h-4 border-l-2 border-b-2 border-amber-500/30 rounded-bl" />
          <div className="absolute bottom-2 right-2 w-4 h-4 border-r-2 border-b-2 border-amber-500/30 rounded-br" />
          
          {/* Cover content */}
          <div className="relative z-10 h-full flex flex-col justify-between p-4">
            <div>
              <h3 className="text-base font-display text-amber-100 leading-tight mb-2">{title}</h3>
              <p className="text-xs text-amber-200/70">{author}</p>
            </div>
            
            {/* Book count badge */}
            <div className="self-end">
              <div className="w-10 h-10 bg-gradient-to-br from-amber-600/40 to-amber-700/40 rounded-full flex items-center justify-center border border-amber-500/50">
                <span className="text-amber-100 font-bold text-sm">{bookCount}</span>
              </div>
            </div>
          </div>
          
          {/* Subtle texture overlay */}
          <div className="absolute inset-0 opacity-10"
               style={{
                 backgroundImage: `url("data:image/svg+xml,%3Csvg width='100' height='100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='turbulence' baseFrequency='0.9' numOctaves='4' /%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.5'/%3E%3C/svg%3E")`
               }} />
        </div>
        
        {/* Book top (barely visible) */}
        <div className={clsx(
          'book-top',
          'bg-gradient-to-r',
          colors.spine
        )} />
      </div>
    </div>
  );
}
