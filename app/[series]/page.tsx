import { getSeries, getBooksInSeries } from '@/lib/dataLoader';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import SeriesBookshelf from '@/components/SeriesBookshelf';
import Breadcrumb from '@/components/Breadcrumb';

export default async function SeriesPage({
  params
}: {
  params: { series: string }
}) {
  const series = await getSeries(params.series);
  const books = await getBooksInSeries(params.series);
  
  if (!series || !books) {
    notFound();
  }
  
  // Amazon affiliate link for the series
  const amazonSearchUrl = `https://www.amazon.com/s?k=${encodeURIComponent(series.title + ' ' + series.author + ' box set')}&tag=spoilerfree-20`;
  
  // Get first 4 books' ASINs for cover collage - filter out nulls to ensure string[]
  const coverImages: string[] = books
    .slice(0, 4)
    .map(({ book }) => 
      book.asin ? `https://images-na.ssl-images-amazon.com/images/P/${book.asin}.01._SX300_.jpg` : null
    )
    .filter((url): url is string => url !== null);
  
  const breadcrumbItems = [
    { label: 'Home', href: '/' },
    { label: series.title, current: true }
  ];

  return (
    <div className="container mx-auto px-4 py-12">
      <Breadcrumb items={breadcrumbItems} />
      
      <div className="text-center mb-12">
        <h1 className="text-4xl md:text-5xl font-display mb-4 text-amber-50 text-shadow-subtle">
          {series.title}
        </h1>
        <p className="text-xl text-amber-100 font-serif">
          by {series.author}
        </p>
      </div>
      
      {/* Books display - Using SeriesBookshelf component for consistency */}
      <div className="mb-16">
        <SeriesBookshelf books={books} seriesSlug={params.series} />
      </div>
      
      {/* Amazon affiliate section - AFTER books */}
      <div className="pt-12">
        <div className="parchment-panel max-w-2xl mx-auto p-8">
          <div className="flex flex-col items-center">
            <h3 className="text-xl font-heading font-bold mb-6 text-parchment-primary">Purchase This Series</h3>
            <a
              href={amazonSearchUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="group"
            >
              <div className="relative overflow-hidden rounded-lg shadow-lg transition-all duration-300 group-hover:shadow-xl group-hover:scale-105">
                {coverImages.length > 0 ? (
                  <div className="w-40 h-60 grid grid-cols-2 gap-0.5 bg-black/20 p-0.5">
                    {/* Show up to 4 covers in a 2x2 grid */}
                    {coverImages.slice(0, 4).map((coverUrl, index) => (
                      <div key={index} className="relative overflow-hidden">
                        <img 
                          src={coverUrl}
                          alt={`${series.title} book ${index + 1} cover`}
                          className="w-full h-full object-cover"
                          loading="lazy"
                        />
                      </div>
                    ))}
                    {/* Fill empty spots if less than 4 books */}
                    {[...Array(Math.max(0, 4 - coverImages.length))].map((_, index) => (
                      <div 
                        key={`empty-${index}`} 
                        className="bg-gradient-to-br from-amber-800 to-amber-900"
                      />
                    ))}
                  </div>
                ) : (
                  <div className="w-40 h-60 bg-gradient-to-br from-leather to-leather-dark flex items-center justify-center">
                    <span className="text-parchment-dark text-sm text-center px-4">
                      {series.title}<br />Collection
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
              href={amazonSearchUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 mt-4 px-5 py-2.5 bg-gradient-to-b from-amber-700 to-amber-800 text-amber-100 rounded-md shadow-md hover:from-amber-600 hover:to-amber-700 transition-all duration-200 hover:shadow-lg text-sm font-medium"
            >
              <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
              </svg>
              Buy Complete Series on Amazon
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
    </div>
  );
}
