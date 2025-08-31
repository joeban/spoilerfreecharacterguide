'use client';

import clsx from 'clsx';
import { useEffect, useState } from 'react';

interface BookSpineProps {
  title: string;
  author: string;
  bookCount: number;
  orientation?: 'vertical' | 'horizontal';
}

// Book color patterns for variety
const bookColors = [
  { spine: 'from-amber-900 to-amber-950', cover: 'from-amber-800 to-amber-900', accent: 'border-amber-700', solid: '#8b4513' },
  { spine: 'from-red-900 to-red-950', cover: 'from-red-800 to-red-900', accent: 'border-red-700', solid: '#991b1b' },
  { spine: 'from-green-900 to-green-950', cover: 'from-green-800 to-green-900', accent: 'border-green-700', solid: '#2d5a2d' },
  { spine: 'from-blue-900 to-blue-950', cover: 'from-blue-800 to-blue-900', accent: 'border-blue-700', solid: '#2c5282' },
  { spine: 'from-purple-900 to-purple-950', cover: 'from-purple-800 to-purple-900', accent: 'border-purple-700', solid: '#553c9a' },
  { spine: 'from-slate-800 to-slate-900', cover: 'from-slate-700 to-slate-800', accent: 'border-slate-600', solid: '#4a4a5a' },
];

export default function BookSpine({ title, author, bookCount, orientation = 'vertical' }: BookSpineProps) {
  // Use title length to consistently assign colors
  const colorIndex = title.length % bookColors.length;
  const colors = bookColors[colorIndex];
  
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
            'bg-gradient-to-b',
            colors.spine
          )}
          style={{
            // Add solid color fallback
            backgroundColor: colors.solid,
            backgroundImage: `linear-gradient(to bottom, ${colors.solid}, ${colors.solid}cc)`
          }}
        >
          {/* Decorative spine details */}
          <div className="spine-decoration">
            {/* Top gold line */}
            <div className="absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-amber-400/50 to-transparent" />
            
            {/* Title on spine (rotated) */}
            <div className="flex-1 flex items-center justify-center px-1 py-4 overflow-hidden">
              <span className="text-amber-200/80 text-xs font-display writing-mode-vertical whitespace-nowrap max-w-full">
                {title.length > 22 ? title.substring(0, 20) + '...' : title}
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
            'bg-gradient-to-br',
            colors.cover,
            'border-r-2 border-t-2 border-b-2',
            colors.accent
          )}
          style={{
            // Add solid color fallback
            backgroundColor: colors.solid,
          }}
        >
          {/* Decorative corner flourishes */}
          <div className="absolute top-2 left-2 w-5 h-5 border-l-2 border-t-2 border-amber-400/20 rounded-tl" />
          <div className="absolute top-2 right-2 w-5 h-5 border-r-2 border-t-2 border-amber-400/20 rounded-tr" />
          <div className="absolute bottom-2 left-2 w-5 h-5 border-l-2 border-b-2 border-amber-400/20 rounded-bl" />
          <div className="absolute bottom-2 right-2 w-5 h-5 border-r-2 border-b-2 border-amber-400/20 rounded-br" />
          
          {/* Cover content */}
          <div className="relative z-10 h-full flex flex-col justify-between p-3">
            <div className="space-y-1">
              <h3 className="text-base font-display font-bold text-amber-100 leading-tight break-normal hyphens-none">
                {title}
              </h3>
              <p className="text-xs text-amber-200/70 italic">{author}</p>
            </div>
            
            {/* Decorative center element */}
            <div className="flex justify-center my-2">
              <div className="w-12 h-px bg-gradient-to-r from-transparent via-amber-400/30 to-transparent" />
            </div>
            
            {/* Book count badge */}
            <div className="self-end">
              <div className="w-12 h-12 bg-gradient-to-br from-amber-500/30 to-amber-600/30 rounded-full flex items-center justify-center border-2 border-amber-400/40 shadow-lg">
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
