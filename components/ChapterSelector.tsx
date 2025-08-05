"use client";

import { useRouter } from "next/navigation";
import { useState, useEffect } from "react";

interface ChapterSelectorProps {
  series: string;
  book: string;
  totalChapters: number;
}

export default function ChapterSelector({ series, book, totalChapters }: ChapterSelectorProps) {
  const router = useRouter();

  // No chapter has been selected yet — user is on the book page
  const [currentChapter, setCurrentChapter] = useState<number | null>(null);
  const [selectedChapter, setSelectedChapter] = useState<number>(1);

  // Smart quick jump button values
  const middleChapter = Math.floor(totalChapters / 2);

  const handleGoClick = () => {
    setCurrentChapter(selectedChapter);
    router.push(`/${series}/${book}/${selectedChapter}`);
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = parseInt(e.target.value);
    if (!isNaN(value) && value >= 1 && value <= totalChapters) {
      setSelectedChapter(value);
    }
  };

  const disableGoButton = selectedChapter === currentChapter && currentChapter !== null;

  return (
    <div className="parchment-panel p-4 text-center">
      <h2 className="text-xl font-bold text-amber-900 mb-2">Choose Your Chapter</h2>

      <div className="flex justify-center items-center gap-4 mb-4">
        <button
          className="px-3 py-1 bg-amber-200 hover:bg-amber-300 rounded"
          onClick={() => setSelectedChapter((prev) => Math.max(1, prev - 1))}
        >
          −
        </button>

        <input
          type="number"
          className="w-20 text-center px-2 py-1 border border-amber-400 rounded"
          value={selectedChapter}
          min={1}
          max={totalChapters}
          onChange={handleInputChange}
        />

        <button
          className="px-3 py-1 bg-amber-200 hover:bg-amber-300 rounded"
          onClick={() => setSelectedChapter((prev) => Math.min(totalChapters, prev + 1))}
        >
          +
        </button>
      </div>

      <div className="flex justify-center gap-2 mb-2">
        <button onClick={() => setSelectedChapter(1)} className="text-sm underline text-amber-700 hover:text-amber-900">First</button>
        {totalChapters >= 20 && (
          <button onClick={() => setSelectedChapter(middleChapter)} className="text-sm underline text-amber-700 hover:text-amber-900">Middle</button>
        )}
        <button onClick={() => setSelectedChapter(totalChapters)} className="text-sm underline text-amber-700 hover:text-amber-900">Last</button>
      </div>

      <button
        className={`px-4 py-2 mt-2 font-semibold rounded ${
          disableGoButton
            ? "bg-gray-300 text-gray-500 cursor-not-allowed"
            : "bg-amber-500 hover:bg-amber-600 text-white"
        }`}
        onClick={handleGoClick}
        disabled={disableGoButton}
      >
        Go to Chapter {selectedChapter}
      </button>

      <div className="mt-2 text-sm text-amber-800">
        {currentChapter === null
          ? "No chapter selected yet"
          : selectedChapter === currentChapter
          ? `Currently on Chapter ${currentChapter}`
          : `Ready to go to Chapter ${selectedChapter}`}
      </div>
    </div>
  );
}
