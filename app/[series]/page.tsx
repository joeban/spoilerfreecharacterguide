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
  
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h1 className="text-4xl md:text-5xl font-display mb-4 text-shadow-ink">
          {series.title}
        </h1>
        <p className="text-xl text-ink-light">
          by {series.author}
        </p>
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
    </div>
  );
}
