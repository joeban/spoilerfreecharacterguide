import { getSeries, getBookMeta } from '@/lib/dataLoader';
import { loadChapterData } from '@/lib/optimizedDataLoader';
import { getCharactersForChapter, getChapterRecap } from '@/lib/spoilerFilter';
import dynamic from 'next/dynamic';
import ChapterSelector from '@/components/ChapterSelector';
import ChapterRecap from '@/components/ChapterRecap';
import Breadcrumb from '@/components/Breadcrumb';
import StructuredData from '@/components/StructuredData';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';

// Lazy load the character list for better performance
const CharacterList = dynamic(() => import('@/components/CharacterList'), {
  loading: () => (
    <div className="text-amber-100/50 animate-pulse">Loading characters...</div>
  ),
  ssr: true
});

export async function generateMetadata({
  params
}: {
  params: Promise<{ series: string; book: string; chapter: string }>
}): Promise<Metadata> {
  const resolvedParams = await params;
  const chapterNum = parseInt(resolvedParams.chapter);
  const series = await getSeries(resolvedParams.series);
  const bookMeta = await getBookMeta(resolvedParams.series, resolvedParams.book);
  
  if (!series || !bookMeta || isNaN(chapterNum)) {
    return {
      title: 'Chapter Not Found'
    };
  }
  
  // Use optimized chapter data loading for metadata
  const chapterData = await loadChapterData(resolvedParams.series, resolvedParams.book, chapterNum);
  if (!chapterData) {
    return {
      title: 'Chapter Not Found'
    };
  }

  const bookData = {
    meta: chapterData.meta,
    characters: chapterData.characters,
    recaps: { [chapterNum]: chapterData.recap }
  };
  
  const { inThisChapter, previouslySeen } = getCharactersForChapter(bookData as any, chapterNum);
  const totalCharacters = inThisChapter.length + previouslySeen.length;
  
  return {
    title: `${bookMeta.title} Chapter ${chapterNum} Characters - Spoiler-Free Guide`,
    description: `Characters in ${bookMeta.title} Chapter ${chapterNum} without spoilers. See ${inThisChapter.length} characters appearing in this chapter plus ${previouslySeen.length} previously introduced. Safe reading guide.`,
    keywords: [`${bookMeta.title} chapter ${chapterNum}`, `chapter ${chapterNum} characters`, `${series.title} spoiler-free`, 'no spoilers chapter guide', `${series.author}`],
    alternates: {
      canonical: `https://spoilerfreecharacterguide.com/${resolvedParams.series}/${resolvedParams.book}/${chapterNum}`
    },
    openGraph: {
      title: `Chapter ${chapterNum} - ${bookMeta.title} Character Guide`,
      description: `Track ${totalCharacters} characters in Chapter ${chapterNum} of ${bookMeta.title} without any spoilers.`,
      url: `https://spoilerfreecharacterguide.com/${resolvedParams.series}/${resolvedParams.book}/${chapterNum}`,
      type: 'article'
    }
  };
}

export default async function ChapterPage({
  params
}: {
  params: Promise<{ series: string; book: string; chapter: string }>
}) {
  const resolvedParams = await params;
  const chapterNum = parseInt(resolvedParams.chapter);
  
  if (isNaN(chapterNum) || chapterNum < 1) {
    notFound();
  }

  const series = await getSeries(resolvedParams.series);
  const bookMeta = await getBookMeta(resolvedParams.series, resolvedParams.book);
  
  if (!series || !bookMeta) {
    notFound();
  }

  // Use optimized chapter-specific data loading
  const chapterData = await loadChapterData(resolvedParams.series, resolvedParams.book, chapterNum);
  
  if (!chapterData || chapterNum > chapterData.meta.chapters) {
    notFound();
  }

  // Construct minimal bookData object for compatibility
  const bookData = {
    meta: chapterData.meta,
    characters: chapterData.characters,
    recaps: { [chapterNum]: chapterData.recap }
  };

  const recap = chapterData.recap;
  const { inThisChapter, previouslySeen } = getCharactersForChapter(bookData as any, chapterNum);

  // Breadcrumb data for component
  const breadcrumbItems = [
    { label: series.title, href: `/${resolvedParams.series}` },
    { label: bookMeta.title, href: `/${resolvedParams.series}/${resolvedParams.book}` },
    { label: `Chapter ${chapterNum}`, current: true }
  ];
  
  // Breadcrumb data for StructuredData (different format)
  const breadcrumbs = [
    { name: series.title, url: `/${resolvedParams.series}` },
    { name: bookMeta.title, url: `/${resolvedParams.series}/${resolvedParams.book}` },
    { name: `Chapter ${chapterNum}`, url: `/${resolvedParams.series}/${resolvedParams.book}/${chapterNum}` }
  ];

  return (
    <>
      <StructuredData 
        type="chapter"
        data={{
          title: `${bookMeta.title} - Chapter ${chapterNum}`,
          description: `Character guide for Chapter ${chapterNum} of ${bookMeta.title}`,
          author: series.author,
          seriesName: series.title,
          url: `https://spoilerfreecharacterguide.com/${resolvedParams.series}/${resolvedParams.book}/${chapterNum}`,
          breadcrumbs
        }}
      />
      
      <div className="container mx-auto px-4 py-8">
        <Breadcrumb items={breadcrumbItems} />
        
        <div className="max-w-6xl mx-auto">
          <header className="mb-8 text-center">
            <h1 className="text-4xl font-heading mb-2 text-amber-100 fire-text-shadow">
              {bookMeta.title}
            </h1>
            <h2 className="text-2xl font-medieval text-amber-200">
              Chapter {chapterNum} of {chapterData.meta.chapters}
            </h2>
          </header>

          {/* Top Chapter Selector */}
          <div className="mb-8">
            <ChapterSelector
              currentChapter={chapterNum}
              totalChapters={chapterData.meta.chapters}
              seriesSlug={resolvedParams.series}
              bookSlug={resolvedParams.book}
            />
          </div>

          {/* Chapter Recap */}
          {recap && (
            <div className="mb-8">
              <ChapterRecap recap={recap} chapter={chapterNum} />
            </div>
          )}

          {/* Character Lists with lazy loading */}
          <CharacterList 
            inThisChapter={inThisChapter} 
            previouslySeen={previouslySeen}
          />

          {/* Amazon Link */}
          {bookMeta.asin && (
            <div className="mt-8 mb-8">
              <div className="parchment-panel p-6 text-center">
                <h3 className="text-xl font-heading mb-4 text-parchment-primary">Purchase This Book</h3>
                <a 
                  href={`https://www.amazon.com/dp/${bookMeta.asin}?tag=spoilerfree-20`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-block bg-amber-600 hover:bg-amber-700 text-white px-6 py-3 rounded-lg font-medieval transition-colors"
                >
                  Buy {bookMeta.title} on Amazon
                </a>
                <p className="mt-4 text-xs text-parchment-secondary italic">
                  As an Amazon Associate, we earn from qualifying purchases
                </p>
              </div>
            </div>
          )}

          {/* Bottom Chapter Selector */}
          <div className="mt-8 mb-4">
            <ChapterSelector
              currentChapter={chapterNum}
              totalChapters={chapterData.meta.chapters}
              seriesSlug={resolvedParams.series}
              bookSlug={resolvedParams.book}
            />
          </div>

          {/* Back to Book Link */}
          <div className="mt-8 text-center">
            <Link 
              href={`/${resolvedParams.series}/${resolvedParams.book}`}
              className="text-amber-300 hover:text-amber-100 transition-colors font-medieval"
            >
              ← Back to {bookMeta.title} Chapters
            </Link>
          </div>
        </div>
      </div>
    </>
  );
}