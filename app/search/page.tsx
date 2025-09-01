import { getAllSeries } from '@/lib/dataLoader';
import Link from 'next/link';
import BookSpine from '@/components/BookSpine';

interface SearchResult {
  type: 'series' | 'book';
  seriesSlug: string;
  seriesTitle: string;
  seriesAuthor: string;
  bookSlug?: string;
  bookTitle?: string;
  bookCount: number;
  relevanceScore: number;
}

async function searchContent(query: string): Promise<SearchResult[]> {
  const allSeries = await getAllSeries();
  const results: SearchResult[] = [];
  const searchTerms = query.toLowerCase().trim().split(/\s+/);
  
  allSeries.forEach(({ slug: seriesSlug, series }) => {
    // Check series title and author
    const seriesText = `${series.title} ${series.author}`.toLowerCase();
    
    // Calculate relevance score for series
    let seriesScore = 0;
    searchTerms.forEach(term => {
      if (series.title.toLowerCase().includes(term)) seriesScore += 3;
      if (series.author.toLowerCase().includes(term)) seriesScore += 2;
    });
    
    // Add series result if matches
    if (seriesScore > 0) {
      results.push({
        type: 'series',
        seriesSlug,
        seriesTitle: series.title,
        seriesAuthor: series.author,
        bookCount: Object.keys(series.books).length,
        relevanceScore: seriesScore
      });
    }
    
    // Check individual books
    Object.entries(series.books).forEach(([bookSlug, book]) => {
      let bookScore = 0;
      searchTerms.forEach(term => {
        if (book.title.toLowerCase().includes(term)) bookScore += 3;
        if (series.author.toLowerCase().includes(term)) bookScore += 1;
        if (series.title.toLowerCase().includes(term)) bookScore += 1;
      });
      
      if (bookScore > 0) {
        results.push({
          type: 'book',
          seriesSlug,
          seriesTitle: series.title,
          seriesAuthor: series.author,
          bookSlug,
          bookTitle: book.title,
          bookCount: 1,
          relevanceScore: bookScore
        });
      }
    });
  });
  
  // Sort by relevance score (highest first)
  results.sort((a, b) => b.relevanceScore - a.relevanceScore);
  
  // Remove duplicate series entries if individual books from that series are already shown
  const uniqueResults: SearchResult[] = [];
  const seenSeries = new Set<string>();
  
  // First pass: add all books
  results.forEach(result => {
    if (result.type === 'book') {
      uniqueResults.push(result);
      seenSeries.add(result.seriesSlug);
    }
  });
  
  // Second pass: add series that don't have individual book results
  results.forEach(result => {
    if (result.type === 'series' && !seenSeries.has(result.seriesSlug)) {
      uniqueResults.push(result);
    }
  });
  
  return uniqueResults;
}

export default async function SearchPage({
  searchParams
}: {
  searchParams: Promise<{ q?: string }>
}) {
  const resolvedSearchParams = await searchParams;
  const query = resolvedSearchParams.q || '';
  
  if (!query.trim()) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="text-center">
          <h1 className="text-4xl font-display mb-4 text-amber-100 text-shadow-fire">
            Search the Library
          </h1>
          <div className="parchment-panel max-w-md mx-auto p-8 mt-8">
            <p className="text-amber-800">
              Enter a series title, book title, or author name to search our collection.
            </p>
          </div>
        </div>
      </div>
    );
  }
  
  const results = await searchContent(query);
  
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-display mb-2 text-amber-100 text-shadow-fire">
          Search Results
        </h1>
        <p className="text-amber-200">
          for "{query}"
        </p>
      </div>
      
      {results.length === 0 ? (
        <div className="max-w-2xl mx-auto">
          <div className="parchment-panel p-8 text-center">
            <h2 className="text-2xl font-display mb-4 text-amber-900">
              No Results Found
            </h2>
            <p className="text-amber-800 mb-4">
              We couldn't find any series, books, or authors matching "{query}".
            </p>
            <p className="text-amber-700 text-sm mb-6">
              Try searching for:
            </p>
            <ul className="text-amber-700 text-sm space-y-1 mb-6">
              <li>• Series names (e.g., "Harry Potter", "Stormlight")</li>
              <li>• Book titles (e.g., "Fellowship", "Dune")</li>
              <li>• Author names (e.g., "Sanderson", "Tolkien")</li>
            </ul>
            <Link
              href="/"
              className="inline-block px-6 py-2 bg-gradient-to-b from-amber-700 to-amber-800 
                       text-amber-100 rounded-md shadow-md hover:from-amber-600 
                       hover:to-amber-700 transition-all duration-200"
            >
              Browse All Series
            </Link>
          </div>
        </div>
      ) : (
        <div className="max-w-6xl mx-auto">
          <div className="parchment-panel p-6 mb-4">
            <p className="text-amber-800 text-center">
              Found {results.length} {results.length === 1 ? 'result' : 'results'}
            </p>
          </div>
          
          <div className="space-y-6">
            {results.map((result, index) => (
              <div key={`${result.seriesSlug}-${result.bookSlug || 'series'}-${index}`} 
                   className="parchment-panel p-6 hover:shadow-xl transition-shadow duration-300">
                <div className="flex flex-col md:flex-row gap-6 items-center">
                  {/* Book spine preview */}
                  <div className="flex-shrink-0">
                    <Link
                      href={result.type === 'book' 
                        ? `/${result.seriesSlug}/${result.bookSlug}`
                        : `/${result.seriesSlug}`}
                    >
                      <BookSpine
                        title={result.type === 'book' ? result.bookTitle! : result.seriesTitle}
                        author={result.seriesAuthor}
                        bookCount={result.bookCount}
                        orientation="vertical"
                      />
                    </Link>
                  </div>
                  
                  {/* Result details */}
                  <div className="flex-1 text-center md:text-left">
                    <div className="mb-2">
                      {result.type === 'book' ? (
                        <>
                          <Link
                            href={`/${result.seriesSlug}/${result.bookSlug}`}
                            className="text-2xl font-display text-amber-900 hover:text-amber-700 transition-colors"
                          >
                            {result.bookTitle}
                          </Link>
                          <p className="text-sm text-amber-700 mt-1">
                            Book from{' '}
                            <Link
                              href={`/${result.seriesSlug}`}
                              className="underline hover:text-amber-600"
                            >
                              {result.seriesTitle}
                            </Link>
                          </p>
                        </>
                      ) : (
                        <Link
                          href={`/${result.seriesSlug}`}
                          className="text-2xl font-display text-amber-900 hover:text-amber-700 transition-colors"
                        >
                          {result.seriesTitle} Series
                        </Link>
                      )}
                    </div>
                    
                    <p className="text-amber-800 mb-3">
                      by {result.seriesAuthor}
                    </p>
                    
                    {result.type === 'series' && (
                      <p className="text-sm text-amber-700">
                        {result.bookCount} book{result.bookCount !== 1 ? 's' : ''} in series
                      </p>
                    )}
                    
                    <Link
                      href={result.type === 'book' 
                        ? `/${result.seriesSlug}/${result.bookSlug}`
                        : `/${result.seriesSlug}`}
                      className="inline-block mt-4 px-4 py-2 bg-gradient-to-b from-amber-700 to-amber-800 
                               text-amber-100 rounded-md shadow-md hover:from-amber-600 
                               hover:to-amber-700 transition-all duration-200 text-sm"
                    >
                      {result.type === 'book' ? 'View Book' : 'View Series'}
                    </Link>
                  </div>
                </div>
              </div>
            ))}
          </div>
          
          {/* Help text about character search */}
          <div className="mt-12 text-center">
            <div className="parchment-panel max-w-2xl mx-auto p-6">
              <p className="text-amber-700 text-sm italic">
                Looking for a specific character? To maintain our spoiler-free promise, 
                please select your book and chapter first, then browse characters safely.
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
