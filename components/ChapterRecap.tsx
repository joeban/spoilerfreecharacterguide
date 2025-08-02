'use client';

import { useState } from 'react';

interface ChapterRecapProps {
  recap: string;
  chapter: number;
}

export default function ChapterRecap({ recap, chapter }: ChapterRecapProps) {
  const [isVisible, setIsVisible] = useState(false);
  
  return (
    <div className="parchment-card p-4 mb-6">
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-display">
          Chapter {chapter} Recap
        </h3>
        <button
          onClick={() => setIsVisible(!isVisible)}
          className="text-sm px-3 py-1 border border-ink-light rounded-sm hover:bg-ink hover:text-parchment transition-colors duration-200"
        >
          {isVisible ? 'Hide' : 'Show'} Recap
        </button>
      </div>
      
      {isVisible && (
        <div className="mt-4 pt-4 border-t border-ink-light/30 animate-fade-in">
          <p className="text-ink leading-relaxed">
            {recap}
          </p>
        </div>
      )}
    </div>
  );
}
