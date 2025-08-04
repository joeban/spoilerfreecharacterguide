'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
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
  const pathname = usePathname();
  
  // Generate array of chapter numbers
  const chapters = Array.from({ length: totalChapters }, (_, i) => i + 1);
  
  return (
    <div className="mb-8">
      <h3 className="text-lg font-display mb-4 text-center">Select Chapter</h3>
      <div className="flex flex-wrap gap-3 justify-center max-w-4xl mx-auto">
        {chapters.map((chapter) => {
          const hasContent = !chaptersWithContent || chaptersWithContent.includes(chapter);
          const isActive = chapter === currentChapter;
          
          return (
            <Link
              key={chapter}
              href={`/${seriesSlug}/${bookSlug}/${chapter}`}
              className={clsx(
                'chapter-button',
                isActive && 'active',
                !hasContent && 'opacity-50 cursor-not-allowed'
              )}
              title={!hasContent ? 'No content for this chapter yet' : `Go to Chapter ${chapter}`}
            >
              {chapter}
            </Link>
          );
        })}
      </div>
    </div>
  );
}
