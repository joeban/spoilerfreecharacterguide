import { getSeries, getBookMeta, loadBookData } from '@/lib/dataLoader';
import { getChaptersWithContent } from '@/lib/spoilerFilter';
import Link from 'next/link';
import { notFound } from 'next/navigation';

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
  
  // Generate array of all chapters
  const allChapters = Array.from({ length: bookMeta.chapters }, (_, i) => i + 1);
  
  // Amazon affiliate link for this specific book
  const amazonSearchUrl = `https://www.amazon.com/s?k=${encodeURIComponent(bookMeta.title + ' ' + series.author)}&tag=spoilerfree-20`;
  
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
        
        {/* Amazon affiliate link */}
        <div className="mt-6">
          <a
            href={amazonSearchUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 px-6 py-3 bg-leather text-parchment rounded-md shadow-md hover:bg-leather-dark transition-all duration-200 hover:shadow-lg"
          >
            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
            </svg>
            Buy This Book on Amazon
          </a>
          <p className="text-xs text-ink-light mt-2 italic">
            As an Amazon Associate, we earn from qualifying purchases
          </p>
        </div>
      </div>
      
      <div className="max-w-6xl mx-auto">
        <h2 className="text-2xl font-display mb-6 text-center">
          Select Your Current Chapter
        </h2>
        <p className="text-center text-ink-light mb-8 max-w-2xl mx-auto">
          Choose the chapter you&apos;ve just finished reading. 
          We&apos;ll show you only the character information available up to that point.
        </p>
        
        <div className="parchment-card p-8">
          <div className="grid grid-cols-5 sm:grid-cols-8 md:grid-cols-10 gap-2">
            {allChapters.map((chapter) => {
              const hasContent = chaptersWithContent.includes(chapter);
              
              return (
                <Link
                  key={chapter}
                  href={`/${params.series}/${params.book}/${chapter}`}
                  className={`
                    chapter-button text-center
                    ${!hasContent ? 'opacity-50' : ''}
                  `}
                  title={!hasContent ? 'No content for this chapter yet' : `View characters up to Chapter ${chapter}`}
                >
                  {chapter}
                </Link>
              );
            })}
          </div>
          
          {chaptersWithContent.length === 0 && (
            <p className="text-center text-ink-light mt-8">
              Character data is being prepared for this book. Check back soon!
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
