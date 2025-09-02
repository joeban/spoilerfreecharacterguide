import { getSeries, getBookMeta, loadBookData } from '@/lib/dataLoader';
import { getCharactersForChapter, getChapterRecap } from '@/lib/spoilerFilter';
import ChapterSelector from '@/components/ChapterSelector';
import ChapterRecap from '@/components/ChapterRecap';
import CharacterList from '@/components/CharacterList';
import Breadcrumb from '@/components/Breadcrumb';
import StructuredData from '@/components/StructuredData';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';

export async function generateMetadata({
  params
}: {
  params: Promise<{ series: string; book: string; chapter: string }>
}): Promise<Metadata> {
  const resolvedParams = await params;
  const chapterNum = parseInt(resolvedParams.chapter);
  const series = await getSeries(resolvedParams.series);
  const bookMeta = await getBookMeta(resolvedParams.series, resolvedParams.book);
  const bookData = await loadBookData(resolvedParams.series, resolvedParams.book);
  
  if (!series || !bookMeta || !bookData || isNaN(chapterNum)) {
    return {
      title: 'Chapter Not Found'
    };
  }

  const { inThisChapter, previouslySeen } = getCharactersForChapter(bookData, chapterNum);
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
  
  // Validate chapter number
  if (isNaN(chapterNum) || chapterNum < 1) {
    notFound();
  }
  
  const series = await getSeries(resolvedParams.series);
  const bookMeta = await getBookMeta(resolvedParams.series, resolvedParams.book);
  const bookData = await loadBookData(resolvedParams.series, resolvedParams.book);
  
  if (!series || !bookMeta || !bookData || chapterNum > bookMeta.chapters) {
    notFound();
  }
  
  // Get characters and recap for this chapter
  const { inThisChapter, previouslySeen } = getCharactersForChapter(bookData, chapterNum);
  const recap = getChapterRecap(bookData, chapterNum);
  
  // Amazon affiliate link for this specific book
  const amazonSearchUrl = `https://www.amazon.com/s?k=${encodeURIComponent(bookMeta.title + ' ' + series.author)}&tag=spoilerfree-20`;
  
  // Amazon direct link if we have ASIN
  const amazonDirectUrl = bookMeta.asin 
    ? `https://www.amazon.com/dp/${bookMeta.asin}?tag=spoilerfree-20`
    : amazonSearchUrl;
    
  // Amazon image URL
  const coverImageUrl = bookMeta.asin 
    ? `https://images-na.ssl-images-amazon.com/images/P/${bookMeta.asin}.01._SX300_.jpg`
    : null;
  
  const breadcrumbItems = [
    { label: 'Home', href: '/' },
    { label: series.title, href: `/${resolvedParams.series}` },
    { label: bookMeta.title, href: `/${resolvedParams.series}/${resolvedParams.book}` },
    { label: `Chapter ${chapterNum}`, current: true }
  ];

  return (
    <>
      <StructuredData 
        type="chapter"
        data={{
          title: `${bookMeta.title} - Chapter ${chapterNum}`,
          description: recap || `Chapter ${chapterNum} of ${bookMeta.title} by ${series.author}. Track ${inThisChapter.length + previouslySeen.length} characters without spoilers.`,
          url: `https://spoilerfreecharacterguide.com/${resolvedParams.series}/${resolvedParams.book}/${chapterNum}`,
          breadcrumbs: [
            { name: 'Home', url: 'https://spoilerfreecharacterguide.com' },
            { name: series.title, url: `https://spoilerfreecharacterguide.com/${resolvedParams.series}` },
            { name: bookMeta.title, url: `https://spoilerfreecharacterguide.com/${resolvedParams.series}/${resolvedParams.book}` },
            { name: `Chapter ${chapterNum}`, url: `https://spoilerfreecharacterguide.com/${resolvedParams.series}/${resolvedParams.book}/${chapterNum}` }
          ]
        }}
      />
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
            seriesSlug={resolvedParams.series}
            bookSlug={resolvedParams.book}
          />
        </div>
        
        {/* Chapter recap (if available) */}
        {recap && <ChapterRecap recap={recap} chapter={chapterNum} />}
        
        {/* Character lists */}
        <CharacterList
          inThisChapter={inThisChapter}
          previouslySeen={previouslySeen}
        />
        
        {/* Amazon affiliate section - matching book page format */}
        <div className="pt-12">
          <div className="parchment-panel max-w-2xl mx-auto p-8">
            <div className="flex flex-col items-center">
              <h3 className="text-xl font-heading font-bold mb-6 text-parchment-primary">Purchase This Book</h3>
              <a
                href={amazonDirectUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="group"
              >
                <div className="relative overflow-hidden rounded-lg shadow-lg transition-all duration-300 group-hover:shadow-xl group-hover:scale-105">
                  {coverImageUrl ? (
                    <img 
                      src={coverImageUrl}
                      alt={`${bookMeta.title} by ${series.author} - Book Cover - Spoiler-Free Character Guide`}
                      className="w-36 h-auto"
                      loading="lazy"
                    />
                  ) : (
                    <div className="w-36 h-54 bg-gradient-to-br from-leather to-leather-dark flex flex-col items-center justify-center p-3">
                      <span className="text-parchment text-center">
                        <div className="font-display text-base mb-2">{bookMeta.title}</div>
                        <div className="text-xs opacity-80">{series.author}</div>
                      </span>
                    </div>
                  )}
                  <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300 flex items-center justify-center">
                    <span className="text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-black/70 px-3 py-2 rounded text-sm">
                      View on Amazon
                    </span>
                  </div>
                </div>
              </a>
              <a
                href={amazonDirectUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 mt-4 px-5 py-2.5 bg-gradient-to-b from-amber-700 to-amber-800 text-amber-100 rounded-md shadow-md hover:from-amber-600 hover:to-amber-700 transition-all duration-200 hover:shadow-lg text-sm font-medium"
              >
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                </svg>
                Buy This Book on Amazon
              </a>
            </div>
            
            {/* Amazon affiliate disclosure */}
            <div className="mt-6 text-center">
              <p className="text-xs text-parchment-secondary italic">
                As an Amazon Associate, we earn from qualifying purchases
              </p>
            </div>
          </div>
        </div>
        
        {/* Chapter selector at bottom */}
        <div className="mt-12">
          <ChapterSelector
            totalChapters={bookMeta.chapters}
            currentChapter={chapterNum}
            seriesSlug={resolvedParams.series}
            bookSlug={resolvedParams.book}
          />
        </div>
      </div>
    </div>
    </>
  );
}
