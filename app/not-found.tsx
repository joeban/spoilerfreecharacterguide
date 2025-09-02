import Link from 'next/link';
import { getAllSeries } from '@/lib/dataLoader';
import BookSpine from '@/components/BookSpine';

export default async function NotFound() {
  const allSeries = await getAllSeries();
  const popularSeries = allSeries.slice(0, 8); // Show first 8 series

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h1 className="text-5xl font-display mb-4 text-amber-100 text-shadow-fire">
          Page Not Found
        </h1>
        <p className="text-xl text-amber-200 mb-8">
          The page you're looking for seems to have vanished into the Shadow Fold...
        </p>
      </div>

      <div className="parchment-panel max-w-2xl mx-auto p-8 mb-12">
        <h2 className="text-2xl font-display mb-4 text-parchment-primary text-center">
          Were you looking for one of these?
        </h2>
        
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
          {popularSeries.map(({ slug, series }) => (
            <Link
              key={slug}
              href={`/${slug}`}
              className="text-center hover:scale-105 transition-transform"
            >
              <BookSpine
                title={series.title}
                author={series.author}
                bookCount={Object.keys(series.books).length}
                orientation="vertical"
              />
            </Link>
          ))}
        </div>

        <div className="text-center space-y-4">
          <Link
            href="/"
            className="inline-block px-6 py-2 bg-gradient-to-b from-amber-700 to-amber-800 
                     text-amber-100 rounded-md shadow-md hover:from-amber-600 
                     hover:to-amber-700 transition-all duration-200"
          >
            Browse All Series
          </Link>
          
          <p className="text-sm text-parchment-secondary">
            Or try searching for your favorite book or character
          </p>
        </div>
      </div>

      <div className="text-center">
        <p className="text-amber-200/60 text-sm">
          If you believe this is an error, please{' '}
          <a
            href="mailto:spoilerfreecharacterguide@gmail.com"
            className="text-amber-400 hover:text-amber-300 underline"
          >
            let us know
          </a>
        </p>
      </div>
    </div>
  );
}