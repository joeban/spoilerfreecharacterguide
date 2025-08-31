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
        
        {/* Book cover and Amazon link */}
        <div className="mb-8">
          <div className="parchment-panel max-w-2xl mx-auto p-6">
            <div className="flex flex-col sm:flex-row items-center sm:items-start gap-6">
              <a
                href={amazonDirectUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="group flex-shrink-0"
              >
                <div className="relative overflow-hidden rounded-lg shadow-lg transition-all duration-300 group-hover:shadow-xl group-hover:scale-105">
                  {coverImageUrl ? (
                    <img 
                      src={coverImageUrl}
                      alt={`${bookMeta.title} cover`}
                      className="w-32 h-auto"
                      loading="lazy"
                    />
                  ) : (
                    <div className="w-32 h-48 bg-gradient-to-br from-leather to-leather-dark flex flex-col items-center justify-center p-3">
                      <span className="text-parchment text-center">
                        <div className="font-display text-sm mb-2">{bookMeta.title}</div>
                        <div className="text-xs opacity-80">{series.author}</div>
                      </span>
                    </div>
                  )}
                  <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300 flex items-center justify-center">
                    <span className="text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-black/70 px-3 py-2 rounded text-xs">
                      View on Amazon
                    </span>
                  </div>
                </div>
              </a>
              <div className="flex-1 text-center sm:text-left">
                <h3 className="text-lg font-heading font-bold mb-2 text-parchment-primary">{bookMeta.title}</h3>
                <p className="text-sm text-parchment-secondary mb-3">by {series.author}</p>
                <a
                  href={amazonDirectUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-block px-4 py-2 bg-amber-700 hover:bg-amber-600 text-amber-50 rounded transition-colors duration-200 text-sm font-medium"
                >
                  Purchase on Amazon
                </a>
              </div>
            </div>
          </div>
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
