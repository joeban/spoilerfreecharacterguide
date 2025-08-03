import { getAllSeries } from '@/lib/dataLoader';
import Bookshelf from '@/components/Bookshelf';
import SearchBar from '@/components/SearchBar';

export default async function HomePage() {
  const allSeries = await getAllSeries();

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-2xl mx-auto mb-12">
        <SearchBar />
      </div>

      {allSeries.length > 0 ? (
        <Bookshelf series={allSeries} />
      ) : (
        <div className="text-center py-16">
          <div className="parchment-card max-w-md mx-auto p-8">
            <h3 className="text-2xl font-display mb-4">Library Coming Soon</h3>
            <p className="text-ink-light">
              We&apos;re preparing our collection of spoiler-free guides. 
              Check back soon for your favorite series!
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
