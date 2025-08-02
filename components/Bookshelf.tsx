import Link from 'next/link';
import { Series } from '@/lib/types';
import BookSpine from './BookSpine';

interface BookshelfProps {
  series: Array<{ slug: string; series: Series }>;
}

export default function Bookshelf({ series }: BookshelfProps) {
  return (
    <div className="bookshelf-container">
      <div className="flex justify-center">
        <div className="inline-block leather-texture p-8 rounded-lg shadow-2xl">
          <div className="flex gap-4 items-end">
            {series.map(({ slug, series: seriesData }) => (
              <Link key={slug} href={`/${slug}`}>
                <BookSpine
                  title={seriesData.title}
                  author={seriesData.author}
                  bookCount={Object.keys(seriesData.books).length}
                />
              </Link>
            ))}
          </div>
          
          {/* Bookshelf bottom */}
          <div className="h-4 bg-gradient-to-b from-leather-dark to-leather mt-2 rounded-b-sm shadow-inner" />
        </div>
      </div>
    </div>
  );
}
