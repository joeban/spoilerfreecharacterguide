import { getSeries, getBookMeta, loadBookData } from '@/lib/dataLoader';
import { getChaptersWithContent } from '@/lib/spoilerFilter';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import ChapterSelector from '@/components/ChapterSelector';

export default async function BookPage({
  params
}: {
  params: { series: string; book: string }
}) {
  const series = await getSeries(params.series);
  const bookMeta = await getBookMeta(params.series, params.book);
  const bookData = await loadBookData(params.series, params.book);
  
  if (!series || !bookMeta) {
    notFound();
  }
  
  // Get chapters that have content
  const chaptersWithContent = bookData ? getChaptersWithContent(bookData) : [];
  
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
  
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <Link 
          href={`/${params.series}`}
          className="text-ink-light hover:text-ink transition-colors text-sm"
        >
          ← Back to {series.title}
        </Link>
        <h1 className="text-4xl md:text-5xl font-display mt-4 mb-2 text-shadow-ink">
          {bookMeta.title}
        </h1>
        <p className="text-lg text-ink-light">
          {bookMeta.chapters} Chapters
        </p>
      </div>
      
      {/* Chapter selection - Using ChapterSelector stepper */}
      <div className="max-w-6xl mx-auto mb-16">
        <ChapterSelector
          totalChapters={bookMeta.chapters}
          currentChapter={1}
          seriesSlug={params.series}
          bookSlug={params.book}
          chaptersWithContent={chaptersWithContent}
        />
      </div>
      
      {/* Amazon affiliate section - AFTER chapter selection */}
      <div className="pt-12 border-t border-ink-light/20">
        <div className="flex flex-col items-center">
          <h3 className="text-xl font-display mb-6 text-ink-light">Purchase This Book</h3>
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
                  alt={`${bookMeta.title} cover`}
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
            className="inline-flex items-center gap-2 mt-4 px-5 py-2.5 bg-leather text-parchment rounded-md shadow-md hover:bg-leather-dark transition-all duration-200 hover:shadow-lg text-sm"
          >
            <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
            </svg>
            Buy This Book on Amazon
          </a>
        </div>
      </div>
      
      {/* Amazon affiliate disclosure */}
      <div className="mt-8 text-center">
        <p className="text-xs text-ink-light italic">
          As an Amazon Associate, we earn from qualifying purchases
        </p>
      </div>
    </div>
  );
}
