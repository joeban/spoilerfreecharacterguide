import { getAllSeries } from '@/lib/dataLoader';
import Bookshelf from '@/components/Bookshelf';
import SearchBar from '@/components/SearchBar';

export default async function HomePage() {
  const allSeries = await getAllSeries();

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Search Section */}
      <div className="max-w-3xl mx-auto mb-12">
        <div className="bg-gradient-to-br from-amber-900/40 to-amber-800/30 border-2 border-amber-700/50 rounded-lg p-6 shadow-lg">
          <SearchBar />
        </div>
      </div>

      {/* Bookshelf */}
      {allSeries.length > 0 ? (
        <Bookshelf series={allSeries} />
      ) : (
        <div className="text-center py-16">
          <div className="parchment-panel max-w-md mx-auto p-8">
            <h3 className="text-2xl font-heading font-bold mb-4 text-parchment-primary">Library Coming Soon</h3>
            <p className="text-parchment-primary text-readable">
              We&apos;re preparing our collection of spoiler-free guides. 
              Check back soon for your favorite series!
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
