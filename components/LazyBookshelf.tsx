'use client';

import { useEffect, useState, useRef, useCallback } from 'react';
import BookSpine from './BookSpine';
import Link from 'next/link';

interface SeriesData {
  slug: string;
  series: {
    title: string;
    author?: string;
    books: Record<string, { title: string; chapters?: number; asin?: string }>;
  };
}

interface LazyBookshelfProps {
  initialSeries: SeriesData[];
}

export default function LazyBookshelf({ initialSeries }: LazyBookshelfProps) {
  const [visibleSeries, setVisibleSeries] = useState<SeriesData[]>([]);
  const [loadedCount, setLoadedCount] = useState(0);
  const observerRef = useRef<IntersectionObserver | null>(null);
  const loadMoreRef = useRef<HTMLDivElement>(null);
  
  // Initial batch size and increment
  const INITIAL_LOAD = 8;
  const LOAD_INCREMENT = 4;

  // Load more series
  const loadMore = useCallback(() => {
    const nextCount = Math.min(loadedCount + LOAD_INCREMENT, initialSeries.length);
    setVisibleSeries(initialSeries.slice(0, nextCount));
    setLoadedCount(nextCount);
  }, [loadedCount, initialSeries]);

  // Setup intersection observer for infinite scrolling
  useEffect(() => {
    if (observerRef.current) observerRef.current.disconnect();

    observerRef.current = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && loadedCount < initialSeries.length) {
          loadMore();
        }
      },
      { threshold: 0.1, rootMargin: '100px' }
    );

    if (loadMoreRef.current) {
      observerRef.current.observe(loadMoreRef.current);
    }

    return () => {
      if (observerRef.current) observerRef.current.disconnect();
    };
  }, [loadedCount, initialSeries.length, loadMore]);

  // Initial load
  useEffect(() => {
    const initial = Math.min(INITIAL_LOAD, initialSeries.length);
    setVisibleSeries(initialSeries.slice(0, initial));
    setLoadedCount(initial);
  }, [initialSeries]);

  // Get responsive grid columns
  const getResponsiveColumns = () => {
    if (typeof window === 'undefined') return 4;
    const width = window.innerWidth;
    if (width < 640) return 2;  // mobile
    if (width < 768) return 3;  // tablet
    if (width < 1024) return 4; // desktop
    return 5; // large screens
  };

  const [columns, setColumns] = useState(4);

  useEffect(() => {
    const handleResize = () => setColumns(getResponsiveColumns());
    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return (
    <div className="bookshelf-container">
      <div className="bookshelf">
        <div className="wooden-frame">
          <div className="frame-top"></div>
          <div className="frame-content">
            <div className={`grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-6 p-4`}>
              {visibleSeries.map(({ slug, series }) => (
                <Link 
                  key={slug} 
                  href={`/${slug}`} 
                  className="block hover:scale-105 transition-transform duration-200"
                  prefetch={false}
                >
                  <BookSpine
                    title={series.title}
                    author={series.author || 'Unknown Author'}
                    bookCount={Object.keys(series.books).length}
                  />
                </Link>
              ))}
            </div>
            
            {/* Invisible trigger for loading more */}
            {loadedCount < initialSeries.length && (
              <div ref={loadMoreRef} className="h-20 flex items-center justify-center">
                <div className="text-amber-100/50 text-sm">Loading more series...</div>
              </div>
            )}
          </div>
          <div className="shelf-bottom"></div>
        </div>
      </div>
    </div>
  );
}