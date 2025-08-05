'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import clsx from 'clsx';

interface ChapterSelectorProps {
  totalChapters: number;
  currentChapter: number;
  seriesSlug: string;
  bookSlug: string;
  chaptersWithContent?: number[];
}

export default function ChapterSelector({
  totalChapters,
  currentChapter,
  seriesSlug,
  bookSlug,
  chaptersWithContent
}: ChapterSelectorProps) {
  const router = useRouter();
  const [inputValue, setInputValue] = useState(currentChapter.toString());
  const [isInvalid, setIsInvalid] = useState(false);

  // Reset input when currentChapter changes (e.g., navigation)
  useEffect(() => {
    setInputValue(currentChapter.toString());
  }, [currentChapter]);

  const navigateToChapter = (chapter: number) => {
    if (chapter >= 1 && chapter <= totalChapters) {
      router.push(`/${seriesSlug}/${bookSlug}/${chapter}`);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    
    // Allow empty input for typing
    if (value === '') {
      setInputValue('');
      setIsInvalid(false);
      return;
    }

    // Only allow numbers
    if (!/^\d+$/.test(value)) return;

    const num = parseInt(value);
    setInputValue(value);

    // Validate range
    if (num < 1 || num > totalChapters) {
      setIsInvalid(true);
    } else {
      setIsInvalid(false);
    }
  };

  const handleInputBlur = () => {
    if (inputValue === '') {
      setInputValue(currentChapter.toString());
      setIsInvalid(false);
      return;
    }

    const num = parseInt(inputValue);
    if (num >= 1 && num <= totalChapters && num !== currentChapter) {
      navigateToChapter(num);
    } else if (num < 1 || num > totalChapters) {
      setInputValue(currentChapter.toString());
      setIsInvalid(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.currentTarget.blur();
    }
  };

  const handleDecrement = () => {
    if (currentChapter > 1) {
      navigateToChapter(currentChapter - 1);
    }
  };

  const handleIncrement = () => {
    if (currentChapter < totalChapters) {
      navigateToChapter(currentChapter + 1);
    }
  };

  const hasContent = (chapter: number) => {
    return !chaptersWithContent || chaptersWithContent.includes(chapter);
  };

  return (
    <div className="flex flex-col items-center space-y-4">
      <h3 className="text-lg font-display text-center">Select Chapter</h3>
      
      <div className="parchment-panel px-6 py-4">
        <div className="flex items-center gap-3">
          {/* Decrement button */}
          <button
            onClick={handleDecrement}
            disabled={currentChapter <= 1}
            className={clsx(
              'w-10 h-10 rounded-full flex items-center justify-center transition-all',
              'bg-gradient-to-b from-amber-700 to-amber-800 border border-amber-900',
              'hover:from-amber-600 hover:to-amber-700 hover:shadow-lg',
              'active:scale-95',
              currentChapter <= 1 && 'opacity-50 cursor-not-allowed hover:from-amber-700 hover:to-amber-800'
            )}
            title="Previous chapter"
          >
            <span className="text-amber-100 text-xl font-bold">−</span>
          </button>

          {/* Chapter input */}
          <div className="relative">
            <input
              type="text"
              value={inputValue}
              onChange={handleInputChange}
              onBlur={handleInputBlur}
              onKeyDown={handleKeyDown}
              className={clsx(
                'w-20 h-12 text-center text-lg font-display',
                'bg-amber-50 border-2 rounded-md',
                'focus:outline-none focus:ring-2 focus:ring-amber-500',
                'transition-all',
                isInvalid 
                  ? 'border-red-600 text-red-700' 
                  : 'border-amber-700 text-amber-900'
              )}
              style={{ appearance: 'textfield' }}
            />
            <div className="text-xs text-amber-700 text-center mt-1">
              of {totalChapters}
            </div>
          </div>

          {/* Increment button */}
          <button
            onClick={handleIncrement}
            disabled={currentChapter >= totalChapters}
            className={clsx(
              'w-10 h-10 rounded-full flex items-center justify-center transition-all',
              'bg-gradient-to-b from-amber-700 to-amber-800 border border-amber-900',
              'hover:from-amber-600 hover:to-amber-700 hover:shadow-lg',
              'active:scale-95',
              currentChapter >= totalChapters && 'opacity-50 cursor-not-allowed hover:from-amber-700 hover:to-amber-800'
            )}
            title="Next chapter"
          >
            <span className="text-amber-100 text-xl font-bold">+</span>
          </button>
        </div>

        {/* Content availability indicator */}
        {!hasContent(currentChapter) && (
          <p className="text-xs text-amber-700 text-center mt-3 italic">
            No content available for this chapter yet
          </p>
        )}
      </div>

      {/* Quick jump shortcuts for common chapters */}
      <div className="flex gap-2 text-xs">
        <button
          onClick={() => navigateToChapter(1)}
          className={clsx(
            'px-3 py-1 rounded-full transition-all',
            currentChapter === 1
              ? 'bg-amber-700 text-amber-100'
              : 'bg-amber-200 text-amber-800 hover:bg-amber-300'
          )}
        >
          First
        </button>
        {totalChapters > 20 && (
          <>
            <button
              onClick={() => navigateToChapter(Math.floor(totalChapters / 2))}
              className={clsx(
                'px-3 py-1 rounded-full transition-all',
                currentChapter === Math.floor(totalChapters / 2)
                  ? 'bg-amber-700 text-amber-100'
                  : 'bg-amber-200 text-amber-800 hover:bg-amber-300'
              )}
            >
              Middle
            </button>
          </>
        )}
        <button
          onClick={() => navigateToChapter(totalChapters)}
          className={clsx(
            'px-3 py-1 rounded-full transition-all',
            currentChapter === totalChapters
              ? 'bg-amber-700 text-amber-100'
              : 'bg-amber-200 text-amber-800 hover:bg-amber-300'
          )}
        >
          Last
        </button>
      </div>
    </div>
  );
}
