import { getSeries, getBookMeta, loadBookData } from '@/lib/dataLoader';
import { getChaptersWithContent } from '@/lib/spoilerFilter';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import ChapterSelector from '@/components/ChapterSelector';
import Breadcrumb from '@/components/Breadcrumb';

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
  
  const breadcrumbItems = [
    { label: 'Home', href: '/' },
    { label: series.title, href: `/${params.series}` },
    { label: bookMeta.title, current: true }
  ];

  return (
    <div className="container mx-auto px-4 py-6">
      <Breadcrumb items={breadcrumbItems} />
      
      <div className="text-center mb-4">
        <h1 className="text-3xl md:text-4xl font-display mb-2 text-amber-50 text-shadow-subtle">
          {bookMeta.title}
        </h1>
        <p className="text-lg text-amber-100 font-serif">
          {bookMeta.chapters} Chapters
        </p>
      </div>
      
      {/* Chapter selector - First */}
      <div className="max-w-6xl mx-auto mb-6">
        <ChapterSelector
          totalChapters={bookMeta.chapters}
          currentChapter={0}  // 0 means no current chapter (book page, not chapter page)
          seriesSlug={params.series}
          bookSlug={params.book}
          chaptersWithContent={chaptersWithContent}
          defaultChapter={1}  // New prop to set default selection to chapter 1
        />
      </div>
      
      {/* Amazon affiliate section - Below chapter selector */}
      <div className="max-w-md mx-auto">
        <div className="parchment-panel p-6">
          <div className="flex flex-col items-center">
            <h3 className="text-lg font-heading font-bold mb-4 text-parchment-primary">Purchase This Book</h3>
            <a
              href={amazonDirectUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="group mb-3"
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
              className="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-b from-amber-700 to-amber-800 text-amber-100 rounded-md shadow-md hover:from-amber-600 hover:to-amber-700 transition-all duration-200 hover:shadow-lg text-sm font-medium"
            >
              <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"/>
              </svg>
              Buy on Amazon
            </a>
            <p className="text-xs text-parchment-secondary italic mt-3 text-center">
              As an Amazon Associate, we earn from qualifying purchases
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
