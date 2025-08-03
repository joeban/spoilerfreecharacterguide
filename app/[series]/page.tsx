import { getSeries, getBooksInSeries } from '@/lib/dataLoader';
import Link from 'next/link';
import { notFound } from 'next/navigation';

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
  
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h1 className="text-4xl md:text-5xl font-display mb-4 text-shadow-ink">
          {series.title}
        </h1>
        <p className="text-xl text-ink-light">
          by {series.author}
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
            Buy Complete Series on Amazon
          </a>
        </div>
      </div>
      
      <div className="max-w-4xl mx-auto">
        <h2 className="text-2xl font-display mb-6 text-center">
          Select a Book
        </h2>
        
        <div className="grid gap-6 md:grid-cols-2">
          {books.map(({ slug, book }) => (
            <Link
              key={slug}
              href={`/${params.series}/${slug}`}
              className="block group"
            >
              <div className="parchment-card p-6 h-full hover:shadow-xl transition-all duration-300 group-hover:scale-[1.02]">
                <h3 className="text-2xl font-display mb-2 group-hover:text-leather transition-colors">
                  {book.title}
                </h3>
                <div className="text-sm text-ink-light space-y-1">
                  <p>Published: {book.published}</p>
                  <p>{book.chapters} chapters</p>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
      
      {/* Amazon affiliate disclosure */}
      <div className="mt-16 text-center">
        <p className="text-xs text-ink-light italic">
          As an Amazon Associate, we earn from qualifying purchases
        </p>
      </div>
    </div>
  );
}
