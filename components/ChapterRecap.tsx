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
                     bg-gradient-to-b from-amber-800/80 to-amber-900/80 
                     border-2 border-amber-700/50 rounded-lg
                     text-amber-100 font-display text-lg
                     hover:from-amber-700/80 hover:to-amber-800/80
                     transform hover:-translate-y-0.5 transition-all duration-200
                     shadow-lg hover:shadow-xl"
          >
            <span className="text-2xl">📜</span>
            <span>Show Chapter {chapter} Recap</span>
          </button>
        </div>
      ) : (
        // Expanded state - full parchment panel
        <div className="relative">
          {/* Parchment background with darker, richer colors */}
          <div className="relative bg-gradient-to-br from-amber-100/95 to-amber-50/95 
                          border-4 border-amber-800/50 rounded-lg 
                          shadow-2xl p-6 md:p-8
                          before:absolute before:inset-0 before:rounded-lg
                          before:bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZmlsdGVyIGlkPSJwYXBlciI+CiAgICA8ZmVUdXJidWxlbmNlIHR5cGU9ImZyYWN0YWxOb2lzZSIgYmFzZUZyZXF1ZW5jeT0iMC4wNCIgbnVtT2N0YXZlcz0iNSIgcmVzdWx0PSJub2lzZSIgLz4KICAgIDxmZURpZmZ1c2VMaWdodGluZyBpbj0ibm9pc2UiIGxpZ2h0aW5nLWNvbG9yPSJ3aGl0ZSIgc3VyZmFjZVNjYWxlPSIxIj4KICAgICAgPGZlRGlzdGFudExpZ2h0IGF6aW11dGg9IjQ1IiBlbGV2YXRpb249IjYwIiAvPgogICAgPC9mZURpZmZ1c2VMaWdodGluZz4KICA8L2ZpbHRlcj4KICA8cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWx0ZXI9InVybCgjcGFwZXIpIiBvcGFjaXR5PSIwLjIiIC8+Cjwvc3ZnPg==')]
                          before:opacity-30 before:mix-blend-multiply">
            
            {/* Corner decorations */}
            <div className="absolute top-2 left-2 w-8 h-8 border-l-3 border-t-3 border-amber-700/40 rounded-tl-lg" />
            <div className="absolute top-2 right-2 w-8 h-8 border-r-3 border-t-3 border-amber-700/40 rounded-tr-lg" />
            <div className="absolute bottom-2 left-2 w-8 h-8 border-l-3 border-b-3 border-amber-700/40 rounded-bl-lg" />
            <div className="absolute bottom-2 right-2 w-8 h-8 border-r-3 border-b-3 border-amber-700/40 rounded-br-lg" />

            {/* Header with title and hide button */}
            <div className="flex items-center justify-between mb-4 relative z-10">
              <h3 className="text-2xl font-display text-amber-900 flex items-center gap-2">
                <span className="text-3xl">📜</span>
                Chapter {chapter} Recap
              </h3>
              <button
                onClick={() => setIsExpanded(false)}
                className="text-amber-700 hover:text-amber-900 transition-colors
                         text-sm font-display flex items-center gap-1
                         px-3 py-1 rounded hover:bg-amber-200/50"
              >
                <span>Hide Recap</span>
                <span className="text-lg">▲</span>
              </button>
            </div>

            {/* Recap content */}
            <div className="relative z-10">
              <p className="text-amber-900/90 leading-relaxed text-base md:text-lg 
                           font-serif whitespace-pre-wrap">
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
