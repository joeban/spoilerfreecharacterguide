import { getSeries, getBookMeta, loadBookData } from '@/lib/dataLoader';
import { getCharactersForChapter, getChapterRecap } from '@/lib/spoilerFilter';
import ChapterSelector from '@/components/ChapterSelector';
import ChapterRecap from '@/components/ChapterRecap';
import CharacterList from '@/components/CharacterList';
import Link from 'next/link';
import { notFound } from 'next/navigation';

export default async function ChapterPage({
  params
}: {
  params: { series: string; book: string; chapter: string }
}) {
  const chapterNum = parseInt(params.chapter);
  
  // Validate chapter number
  if (isNaN(chapterNum) || chapterNum < 1) {
    notFound();
  }
  
  const series = await getSeries(params.series);
  const bookMeta = await getBookMeta(params.series, params.book);
  const bookData = await loadBookData(params.series, params.book);
  
  if (!series || !bookMeta || !bookData || chapterNum > bookMeta.chapters) {
    notFound();
  }
  
  // Get characters and recap for this chapter
  const { inThisChapter, previouslySeen } = getCharactersForChapter(bookData, chapterNum);
  const recap = getChapterRecap(bookData, chapterNum);
  
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-8">
        <div className="space-y-2">
          <Link 
            href={`/${params.series}`}
            className="text-ink-light hover:text-ink transition-colors text-sm"
          >
            ← {series.title}
          </Link>
          <span className="text-ink-light mx-2">•</span>
          <Link 
            href={`/${params.series}/${params.book}`}
            className="text-ink-light hover:text-ink transition-colors text-sm"
          >
            {bookMeta.title}
          </Link>
        </div>
        
        <h1 className="text-4xl md:text-5xl font-display mt-4 mb-2 text-shadow-ink">
          Chapter {chapterNum}
        </h1>
        <p className="text-lg text-ink-light">
          Character Guide
        </p>
      </div>
      
      <div className="max-w-6xl mx-auto">
        {/* Chapter selector */}
        <ChapterSelector
          totalChapters={bookMeta.chapters}
          currentChapter={chapterNum}
          seriesSlug={params.series}
          bookSlug={params.book}
        />
        
        {/* Chapter recap (if available) */}
        {recap && <ChapterRecap recap={recap} chapter={chapterNum} />}
        
        {/* Character lists */}
        <CharacterList
          inThisChapter={inThisChapter}
          previouslySeen={previouslySeen}
        />
      </div>
    </div>
  );
}
