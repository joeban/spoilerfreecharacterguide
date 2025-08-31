'use client';

import { useState } from 'react';

interface ChapterRecapProps {
  recap: string;
  chapter: number;
}

export default function ChapterRecap({ recap, chapter }: ChapterRecapProps) {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div className="mb-8">
      {!isExpanded ? (
        // Collapsed state - just the button
        <div className="text-center">
          <button
            onClick={() => setIsExpanded(true)}
            className="inline-flex items-center gap-2 px-6 py-3 
                     bg-gradient-to-b from-amber-700 to-amber-800 
                     border-2 border-amber-600 rounded-lg
                     text-amber-50 font-display text-lg font-medium
                     hover:from-amber-600 hover:to-amber-700
                     transform hover:-translate-y-0.5 transition-all duration-200
                     shadow-lg hover:shadow-xl text-shadow-subtle"
          >
            <span className="text-2xl">📜</span>
            <span>Show Chapter {chapter} Recap</span>
          </button>
        </div>
      ) : (
        // Expanded state - full parchment panel
        <div className="relative">
          {/* Parchment background with darker, richer colors */}
          <div className="relative parchment-panel p-8 md:p-10 shadow-2xl">
            
            {/* Corner decorations */}
            <div className="absolute top-2 left-2 w-8 h-8 border-l-2 border-t-2 border-stone-400 rounded-tl-lg" />
            <div className="absolute top-2 right-2 w-8 h-8 border-r-2 border-t-2 border-stone-400 rounded-tr-lg" />
            <div className="absolute bottom-2 left-2 w-8 h-8 border-l-2 border-b-2 border-stone-400 rounded-bl-lg" />
            <div className="absolute bottom-2 right-2 w-8 h-8 border-r-2 border-b-2 border-stone-400 rounded-br-lg" />

            {/* Hide button at top center */}
            <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 z-20">
              <button
                onClick={() => setIsExpanded(false)}
                className="inline-flex items-center gap-2 px-5 py-2 
                         bg-gradient-to-b from-amber-700 to-amber-800 
                         border-2 border-amber-600 rounded-lg
                         text-amber-50 font-display text-base font-medium
                         hover:from-amber-600 hover:to-amber-700
                         transform hover:-translate-y-0.5 transition-all duration-200
                         shadow-lg hover:shadow-xl text-shadow-subtle"
              >
                <span>Hide Recap</span>
                <span className="text-xl">▲</span>
              </button>
            </div>

            {/* Header with title */}
            <div className="mb-6 relative z-10 text-center pt-8">
              <h3 className="text-2xl font-heading font-bold text-parchment-primary flex items-center justify-center gap-3">
                <span className="text-3xl">📜</span>
                Chapter {chapter} Recap
              </h3>
            </div>

            {/* Recap content */}
            <div className="relative z-10">
              <p className="text-parchment-primary text-readable whitespace-pre-wrap">
                {recap}
              </p>
            </div>

            {/* Subtle inner shadow for depth */}
            <div className="absolute inset-0 rounded-lg pointer-events-none
                          shadow-[inset_0_2px_8px_rgba(139,69,19,0.15)]" />
          </div>
        </div>
      )}
    </div>
  );
}
