import Link from 'next/link';
import { Series } from '@/lib/types';
import BookSpine from './BookSpine';

interface BookshelfProps {
  series: Array<{ slug: string; series: Series }>;
}

export default function Bookshelf({ series }: BookshelfProps) {
  return (
    <div className="bookshelf-container max-w-6xl mx-auto">
      {/* Bookshelf Back Panel */}
      <div className="relative bg-amber-900 p-8 rounded-lg shadow-2xl" 
           style={{
             background: 'linear-gradient(180deg, #654321 0%, #8b4513 100%)',
             boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.5), 0 8px 16px rgba(0,0,0,0.3)'
           }}>
        
        {/* Wood grain effect */}
        <div className="absolute inset-0 opacity-20 rounded-lg"
             style={{
               backgroundImage: `repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(0,0,0,0.1) 2px, rgba(0,0,0,0.1) 4px),
                                repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px)`
             }} />
        
        {/* Books Container */}
        <div className="relative flex gap-2 md:gap-4 items-end justify-center perspective-1000">
          {series.map(({ slug, series: seriesData }) => (
            <Link key={slug} href={`/${slug}`} className="block">
              <BookSpine
                title={seriesData.title}
                author={seriesData.author}
                bookCount={Object.keys(seriesData.books).length}
              />
            </Link>
          ))}
        </div>
        
        {/* Bookshelf bottom ledge */}
        <div className="absolute bottom-0 left-0 right-0 h-4 bg-amber-950 rounded-b-lg"
             style={{
               background: 'linear-gradient(to bottom, #654321, #3e2723)',
               boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.5)'
             }} />
      </div>
      
      {/* Bookshelf shadow */}
      <div className="h-4 bg-black bg-opacity-20 rounded-full blur-xl -mt-2" />
    </div>
  );
}
