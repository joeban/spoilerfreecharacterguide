import { getAllSeries } from '@/lib/dataLoader';
import Bookshelf from '@/components/Bookshelf';
import SearchBar from '@/components/SearchBar';

export default async function HomePage() {
  const allSeries = await getAllSeries();

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Search Section */}
      <div className="max-w-3xl mx-auto mb-12">
        <div className="parchment-panel p-6">
          <SearchBar />
        </div>
      </div>

      {/* Bookshelf */}
      {allSeries.length > 0 ? (
        <Bookshelf series={allSeries} />
      ) : (
        <div className="text-center py-16">
          <div className="parchment-panel max-w-md mx-auto p-8">
            <h3 className="text-2xl font-display mb-4 text-amber-900">Library Coming Soon</h3>
            <p className="text-amber-800">
              We&apos;re preparing our collection of spoiler-free guides. 
              Check back soon for your favorite series!
            </p>
          </div>
        </div>
      )}

      {/* Whimsical Candle at Bottom */}
      <div className="relative mt-16 mb-8">
        <div className="flex justify-center">
          <div className="relative">
            {/* Candle */}
            <div className="candle-glow relative">
              {/* Flame */}
              <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 w-3 h-6 
                            bg-gradient-to-t from-orange-400 via-yellow-300 to-white 
                            rounded-full animate-pulse"
                   style={{
                     filter: 'blur(1px)',
                     boxShadow: '0 0 20px rgba(255,191,0,0.8), 0 0 40px rgba(255,140,0,0.6)'
                   }} />
              
              {/* Candle body */}
              <div className="w-8 h-16 bg-gradient-to-b from-amber-100 to-amber-200 rounded-t-sm"
                   style={{
                     boxShadow: 'inset -2px 0 4px rgba(0,0,0,0.2)'
                   }} />
              
              {/* Wax drips */}
              <div className="absolute top-2 -right-1 w-2 h-8 bg-amber-100 rounded-full"
                   style={{
                     transform: 'rotate(15deg)',
                     filter: 'drop-shadow(1px 1px 2px rgba(0,0,0,0.3))'
                   }} />
              <div className="absolute top-6 -left-1.5 w-2.5 h-6 bg-amber-100 rounded-full"
                   style={{
                     transform: 'rotate(-20deg)',
                     filter: 'drop-shadow(1px 1px 2px rgba(0,0,0,0.3))'
                   }} />
              <div className="absolute top-10 right-0 w-1.5 h-5 bg-amber-100 rounded-full"
                   style={{
                     transform: 'rotate(10deg)',
                     filter: 'drop-shadow(1px 1px 2px rgba(0,0,0,0.3))'
                   }} />
              
              {/* Candle holder */}
              <div className="w-12 h-3 bg-gradient-to-b from-amber-800 to-amber-900 
                            rounded-b-lg -mt-0.5"
                   style={{
                     boxShadow: '0 2px 4px rgba(0,0,0,0.4)'
                   }} />
              
              {/* Melted wax pool */}
              <div className="absolute -bottom-1 left-1/2 transform -translate-x-1/2 
                            w-16 h-2 bg-amber-100/50 rounded-full blur-sm" />
            </div>
            
            {/* Ambient glow on "floor" */}
            <div className="absolute -bottom-4 left-1/2 transform -translate-x-1/2 
                          w-32 h-8 bg-gradient-radial from-amber-400/20 to-transparent 
                          rounded-full blur-xl" />
          </div>
        </div>
      </div>
    </div>
  );
}
