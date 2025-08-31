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
    <div className="container mx-auto px-4 py-6">
      <div className="text-center mb-8">
        <div className="space-y-2">
          <Link 
            href={`/${params.series}`}
            className="text-amber-400 hover:text-amber-300 transition-colors text-sm font-medium"
          >
            ← {series.title}
          </Link>
          <span className="text-amber-500/50 mx-2">•</span>
          <Link 
            href={`/${params.series}/${params.book}`}
            className="text-amber-400 hover:text-amber-300 transition-colors text-sm font-medium"
          >
            {bookMeta.title}
          </Link>
        </div>
        
        <h1 className="text-4xl md:text-5xl font-display mt-4 mb-2 text-amber-100 text-shadow-subtle">
          Chapter {chapterNum}
        </h1>
        <p className="text-lg text-amber-200 font-serif">
          Character Guide
        </p>
      </div>
      
      <div className="max-w-6xl mx-auto">
        {/* Chapter recap (if available) */}
        {recap && <ChapterRecap recap={recap} chapter={chapterNum} />}
        
        {/* Character lists */}
        <CharacterList
          inThisChapter={inThisChapter}
          previouslySeen={previouslySeen}
        />
        
        {/* Chapter selector - moved to bottom */}
        <div className="mt-12">
          <ChapterSelector
            totalChapters={bookMeta.chapters}
            currentChapter={chapterNum}
            seriesSlug={params.series}
            bookSlug={params.book}
          />
        </div>
      </div>
    </div>
  );
}
