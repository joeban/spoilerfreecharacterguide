import { getSeries, getBookMeta, loadBookData } from '@/lib/dataLoader';
import { getCharactersForChapter, getChapterRecap } from '@/lib/spoilerFilter';
import ChapterSelector from '@/components/ChapterSelector';
import ChapterRecap from '@/components/ChapterRecap';
import CharacterList from '@/components/CharacterList';
import Breadcrumb from '@/components/Breadcrumb';
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
  
  const breadcrumbItems = [
    { label: 'Home', href: '/' },
    { label: series.title, href: `/${params.series}` },
    { label: bookMeta.title, href: `/${params.series}/${params.book}` },
    { label: `Chapter ${chapterNum}`, current: true }
  ];

  return (
    <div className="container mx-auto px-4 py-6">
      <Breadcrumb items={breadcrumbItems} />
      
      <div className="text-center mb-8">
        <h1 className="text-4xl md:text-5xl font-display mt-4 mb-2 text-amber-100 text-shadow-subtle">
          Chapter {chapterNum}
        </h1>
      </div>
      
      <div className="max-w-6xl mx-auto">
        {/* Chapter selector at top */}
        <div className="mb-8">
          <ChapterSelector
            totalChapters={bookMeta.chapters}
            currentChapter={chapterNum}
            seriesSlug={params.series}
            bookSlug={params.book}
          />
        </div>
        
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
