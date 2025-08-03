import Link from 'next/link';
import { Series } from '@/lib/types';
import BookSpine from './BookSpine';

interface BookshelfProps {
  series: Array<{ slug: string; series: Series }>;
}

export default function Bookshelf({ series }: BookshelfProps) {
  return (
    <div className="bookshelf-container max-w-7xl mx-auto">
      {/* Bookshelf Back Panel */}
      <div className="relative bg-amber-900 p-12 rounded-lg shadow-2xl" 
           style={{
             background: 'linear-gradient(180deg, #654321 0%, #8b4513 100%)',
             boxShadow: 'inset 0 4px 8px rgba(0,0,0,0.5), 0 16px 32px rgba(0,0,0,0.3)'
           }}>
        
        {/* Wood grain effect */}
        <div className="absolute inset-0 opacity-20 rounded-lg"
             style={{
               backgroundImage: `repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(0,0,0,0.1) 2px, rgba(0,0,0,0.1) 4px),
                                repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px)`
             }} />
        
        {/* Back panel decorative nails/studs */}
        <div className="absolute top-4 left-4 w-3 h-3 rounded-full bg-gold shadow-inner" />
        <div className="absolute top-4 right-4 w-3 h-3 rounded-full bg-gold shadow-inner" />
        <div className="absolute bottom-4 left-4 w-3 h-3 rounded-full bg-gold shadow-inner" />
        <div className="absolute bottom-4 right-4 w-3 h-3 rounded-full bg-gold shadow-inner" />
        
        {/* Books Container */}
        <div className="relative grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 md:gap-8 justify-items-center">
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
        <div className="absolute bottom-0 left-0 right-0 h-6 bg-amber-950 rounded-b-lg"
             style={{
               background: 'linear-gradient(to bottom, #654321, #3e2723)',
               boxShadow: 'inset 0 3px 6px rgba(0,0,0,0.5), 0 -2px 4px rgba(0,0,0,0.3)'
             }} />
      </div>
      
      {/* Bookshelf shadow on floor */}
      <div className="h-6 bg-black bg-opacity-15 rounded-full blur-2xl -mt-3 mx-8" />
    </div>
  );
}
