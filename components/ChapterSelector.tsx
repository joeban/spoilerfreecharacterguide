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
  const [selectedChapter, setSelectedChapter] = useState(currentChapter);
  const [inputValue, setInputValue] = useState(currentChapter.toString());
  const [isInvalid, setIsInvalid] = useState(false);

  // Update selected chapter when currentChapter changes (e.g., navigation)
  useEffect(() => {
    setSelectedChapter(currentChapter);
    setInputValue(currentChapter.toString());
  }, [currentChapter]);

  const navigateToChapter = (chapter: number) => {
    if (chapter >= 1 && chapter <= totalChapters && chapter !== currentChapter) {
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

    // Validate range and update selected chapter
    if (num >= 1 && num <= totalChapters) {
      setSelectedChapter(num);
      setIsInvalid(false);
    } else {
      setIsInvalid(true);
    }
  };

  const handleInputBlur = () => {
    if (inputValue === '' || isInvalid) {
      setInputValue(selectedChapter.toString());
      setIsInvalid(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !isInvalid && selectedChapter !== currentChapter) {
      navigateToChapter(selectedChapter);
    }
  };

  const handleDecrement = () => {
    if (selectedChapter > 1) {
      const newChapter = selectedChapter - 1;
      setSelectedChapter(newChapter);
      setInputValue(newChapter.toString());
      setIsInvalid(false);
    }
  };

  const handleIncrement = () => {
    if (selectedChapter < totalChapters) {
      const newChapter = selectedChapter + 1;
      setSelectedChapter(newChapter);
      setInputValue(newChapter.toString());
      setIsInvalid(false);
    }
  };

  const handleGo = () => {
    if (selectedChapter !== currentChapter && !isInvalid) {
      navigateToChapter(selectedChapter);
    }
  };

  const hasContent = (chapter: number) => {
    return !chaptersWithContent || chaptersWithContent.includes(chapter);
  };

  const showGoButton = selectedChapter !== currentChapter && !isInvalid;

  return (
    <div className="flex flex-col items-center space-y-4">
      <h3 className="text-lg font-display text-center">
        {currentChapter === selectedChapter ? 'Current Chapter' : 'Select Chapter'}
      </h3>
      
      <div className="parchment-panel px-6 py-4">
        <div className="flex items-center gap-3">
          {/* Decrement button */}
          <button
            onClick={handleDecrement}
            disabled={selectedChapter <= 1}
            className={clsx(
              'w-10 h-10 rounded-full flex items-center justify-center transition-all',
              'bg-gradient-to-b from-amber-700 to-amber-800 border border-amber-900',
              'hover:from-amber-600 hover:to-amber-700 hover:shadow-lg',
              'active:scale-95',
              selectedChapter <= 1 && 'opacity-50 cursor-not-allowed hover:from-amber-700 hover:to-amber-800'
            )}
            title="Previous chapter"
            aria-label="Previous chapter"
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
                  : selectedChapter === currentChapter
                  ? 'border-amber-700 text-amber-900'
                  : 'border-amber-600 text-amber-800 bg-amber-100'
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
            disabled={selectedChapter >= totalChapters}
            className={clsx(
              'w-10 h-10 rounded-full flex items-center justify-center transition-all',
              'bg-gradient-to-b from-amber-700 to-amber-800 border border-amber-900',
              'hover:from-amber-600 hover:to-amber-700 hover:shadow-lg',
              'active:scale-95',
              selectedChapter >= totalChapters && 'opacity-50 cursor-not-allowed hover:from-amber-700 hover:to-amber-800'
            )}
            title="Next chapter"
            aria-label="Next chapter"
          >
            <span className="text-amber-100 text-xl font-bold">+</span>
          </button>
        </div>

        {/* Go button - appears when chapter is different from current */}
        {showGoButton && (
          <div className="mt-4 text-center">
            <button
              onClick={handleGo}
              className="px-6 py-2 bg-gradient-to-b from-amber-600 to-amber-700 
                       text-amber-100 font-display rounded-md
                       hover:from-amber-500 hover:to-amber-600 
                       active:scale-95 transition-all shadow-md hover:shadow-lg"
            >
              Go to Chapter {selectedChapter}
            </button>
          </div>
        )}

        {/* Content availability indicator */}
        {!hasContent(selectedChapter) && (
          <p className="text-xs text-amber-700 text-center mt-3 italic">
            {selectedChapter === currentChapter 
              ? 'No content available for this chapter yet'
              : `Chapter ${selectedChapter} has no content yet`
            }
          </p>
        )}
      </div>

      {/* Quick jump shortcuts */}
      <div className="flex gap-2 text-xs">
        <button
          onClick={() => {
            setSelectedChapter(1);
            setInputValue('1');
            setIsInvalid(false);
          }}
          className={clsx(
            'px-3 py-1 rounded-full transition-all',
            selectedChapter === 1
              ? 'bg-amber-700 text-amber-100'
              : 'bg-amber-200 text-amber-800 hover:bg-amber-300'
          )}
        >
          First
        </button>
        {totalChapters > 20 && (
          <button
            onClick={() => {
              const middle = Math.floor(totalChapters / 2);
              setSelectedChapter(middle);
              setInputValue(middle.toString());
              setIsInvalid(false);
            }}
            className={clsx(
              'px-3 py-1 rounded-full transition-all',
              selectedChapter === Math.floor(totalChapters / 2)
                ? 'bg-amber-700 text-amber-100'
                : 'bg-amber-200 text-amber-800 hover:bg-amber-300'
            )}
          >
            Middle
          </button>
        )}
        <button
          onClick={() => {
            setSelectedChapter(totalChapters);
            setInputValue(totalChapters.toString());
            setIsInvalid(false);
          }}
          className={clsx(
            'px-3 py-1 rounded-full transition-all',
            selectedChapter === totalChapters
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
