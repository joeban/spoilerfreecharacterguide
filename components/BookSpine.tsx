'use client';

import clsx from 'clsx';
import { useEffect, useState } from 'react';

interface BookSpineProps {
  title: string;
  author: string;
  bookCount: number;
  orientation?: 'vertical' | 'horizontal';
}

// Expanded professional book color palette
const bookColors = [
  'book-burgundy',
  'book-navy', 
  'book-forest',
  'book-purple',
  'book-brown',
  'book-charcoal',
  'book-crimson',
  'book-teal',
  'book-indigo',
  'book-amber',
  'book-emerald',
  'book-slate',
  'book-olive',
  'book-maroon',
  'book-bronze'
];

// Map specific series to thematic colors (matching actual titles from index.json)
const seriesColorMap: Record<string, string> = {
  'Harry Potter': 'book-burgundy',
  'A Song of Ice and Fire': 'book-charcoal',
  'Lord of the Rings / The Hobbit': 'book-forest',
  'Dune': 'book-amber',
  'The Wheel of Time': 'book-navy',
  'Mistborn (Cosmere)': 'book-slate',
  'The Stormlight Archive': 'book-indigo',
  'The Witcher': 'book-maroon',
  'A Court of Thorns and Roses': 'book-purple',
  'Fourth Wing': 'book-crimson',
  'Throne of Glass': 'book-teal',
  'Shadow and Bone': 'book-bronze',
  'The Hunger Games': 'book-olive',
  'Percy Jackson and the Olympians': 'book-emerald',
  'The Expanse': 'book-charcoal',
  'Wings of Fire': 'book-amber',
  'The Kingkiller Chronicle': 'book-brown',
  'Chronicles of Narnia': 'book-purple',
  'Foundation': 'book-slate',
  'Discworld': 'book-olive'
};

export default function BookSpine({ title, author, bookCount, orientation = 'vertical' }: BookSpineProps) {
  // First check if series has a specific color mapping
  let bookColorClass = seriesColorMap[title];
  
  // If no specific mapping, use a hash function for consistent but varied colors
  if (!bookColorClass) {
    // Better hash function to avoid clustering
    let hash = 0;
    for (let i = 0; i < title.length; i++) {
      hash = ((hash << 5) - hash) + title.charCodeAt(i);
      hash = hash & hash; // Convert to 32bit integer
    }
    const colorIndex = Math.abs(hash) % bookColors.length;
    bookColorClass = bookColors[colorIndex];
  }
  
  // Force re-render on mount to fix back navigation issues
  const [mounted, setMounted] = useState(false);
  
  useEffect(() => {
    setMounted(true);
    // Force a repaint after a short delay
    const timer = setTimeout(() => {
      const books = document.querySelectorAll('.book-3d');
      books.forEach(book => {
        // Force repaint by temporarily changing transform
        const element = book as HTMLElement;
        const currentTransform = element.style.transform;
        element.style.transform = 'rotateY(30.1deg)';
        // eslint-disable-next-line no-unused-expressions
        element.offsetHeight; // Force reflow
        element.style.transform = currentTransform || '';
      });
    }, 10);
    
    return () => clearTimeout(timer);
  }, []);
  
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
        'transition-all duration-300',
        'force-repaint'
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
      <div className={clsx('book-3d', mounted && 'book-mounted')}>
        {/* Book spine (left side) */}
        <div 
          className={clsx(
            'book-spine',
            bookColorClass
          )}
        >
          {/* Decorative spine details */}
          <div className="spine-decoration">
            {/* Top gold line */}
            <div className="absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-amber-400/50 to-transparent" />
            
            {/* Title on spine (rotated) */}
            <div className="flex-1 flex items-center justify-center px-1 py-4 overflow-hidden">
              <span className="text-amber-200/90 text-xs font-display writing-mode-vertical whitespace-nowrap max-w-full">
                {title.length > 20 ? title.substring(0, 18) + '...' : title}
              </span>
            </div>
            
            {/* Bottom gold line */}
            <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-amber-400/50 to-transparent" />
            
            {/* Publisher mark */}
            <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 w-6 h-6 rounded-full bg-amber-500/20 flex items-center justify-center">
              <div className="w-3 h-3 rounded-full bg-amber-400/30" />
            </div>
          </div>
        </div>
        
        {/* Book cover (front) */}
        <div 
          className={clsx(
            'book-cover',
            bookColorClass
          )}
        >
          {/* Decorative corner flourishes */}
          <div className="absolute top-2 left-2 w-5 h-5 border-l-2 border-t-2 border-amber-400/20 rounded-tl" />
          <div className="absolute top-2 right-2 w-5 h-5 border-r-2 border-t-2 border-amber-400/20 rounded-tr" />
          <div className="absolute bottom-2 left-2 w-5 h-5 border-l-2 border-b-2 border-amber-400/20 rounded-bl" />
          <div className="absolute bottom-2 right-2 w-5 h-5 border-r-2 border-b-2 border-amber-400/20 rounded-br" />
          
          {/* Cover content */}
          <div className="relative z-10 h-full flex flex-col justify-between p-3">
            <div className="space-y-1">
              <h3 className="text-base font-display font-bold text-amber-100 leading-tight break-normal hyphens-none drop-shadow-md">
                {title}
              </h3>
              <p className="text-xs text-amber-200/80 font-medium">{author}</p>
            </div>
            
            {/* Decorative center element */}
            <div className="flex justify-center my-2">
              <div className="w-12 h-px bg-gradient-to-r from-transparent via-amber-400/30 to-transparent" />
            </div>
            
            {/* Book count badge - refined */}
            <div className="self-end">
              <div className="w-12 h-12 bg-gradient-to-br from-amber-600/20 to-amber-700/30 rounded-full flex items-center justify-center border border-amber-500/30 shadow-inner">
                <span className="text-amber-100 font-bold text-lg">{bookCount}</span>
              </div>
            </div>
          </div>
          
          {/* Subtle leather texture overlay */}
          <div className="absolute inset-0 opacity-5 rounded-r-lg"
               style={{
                 backgroundImage: `url("data:image/svg+xml,%3Csvg width='100' height='100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='roughPaper'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.02' numOctaves='5' result='noise' /%3E%3CfeColorMatrix in='noise' values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23roughPaper)' /%3E%3C/svg%3E")`
               }} />
        </div>
        
        {/* Book top edge (pages) */}
        <div className={clsx(
          'book-top',
          'bg-gradient-to-r',
          'from-amber-50 to-amber-100'
        )} />
      </div>
    </div>
  );
}
