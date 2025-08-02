import { getAllSeries } from '@/lib/dataLoader';
import Bookshelf from '@/components/Bookshelf';

export default async function HomePage() {
  const allSeries = await getAllSeries();

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h2 className="text-4xl md:text-5xl font-display mb-4 text-shadow-ink">
          Choose Your Adventure
        </h2>
        <p className="text-lg text-ink-light max-w-2xl mx-auto">
          Select a series below to begin exploring characters chapter by chapter. 
          Our guides reveal only what you&apos;ve read, keeping future surprises intact.
        </p>
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
