'use client';

import { useState, useEffect, useRef } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';

// Import the index data for search
import indexData from '@/data/index.json';

interface SearchResult {
  type: 'series' | 'book';
  seriesSlug: string;
  seriesTitle: string;
  bookSlug?: string;
  bookTitle?: string;
  url: string;
}

export default function SearchBar() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [showDropdown, setShowDropdown] = useState(false);
  const [selectedIndex, setSelectedIndex] = useState(-1);
  const router = useRouter();
  const dropdownRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setShowDropdown(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Search function
  const performSearch = (searchQuery: string) => {
    if (!searchQuery.trim()) {
      setResults([]);
      setShowDropdown(false);
      return;
    }

    const searchResults: SearchResult[] = [];
    const lowerQuery = searchQuery.toLowerCase();

    // Search through series and books
    Object.entries(indexData.series).forEach(([seriesSlug, series]) => {
      const seriesMatches = series.title.toLowerCase().includes(lowerQuery) || 
                           series.author.toLowerCase().includes(lowerQuery);
      
      // Check if series title matches
      if (seriesMatches) {
        searchResults.push({
          type: 'series',
          seriesSlug,
          seriesTitle: series.title,
          url: `/${seriesSlug}`
        });
        
        // If series matches, also add all its books in order
        Object.entries(series.books).forEach(([bookSlug, book]) => {
          searchResults.push({
            type: 'book',
            seriesSlug,
            seriesTitle: series.title,
            bookSlug,
            bookTitle: book.title,
            url: `/${seriesSlug}/${bookSlug}`
          });
        });
      } else {
        // If series doesn't match, still check individual book titles
        Object.entries(series.books).forEach(([bookSlug, book]) => {
          if (book.title.toLowerCase().includes(lowerQuery)) {
            searchResults.push({
              type: 'book',
              seriesSlug,
              seriesTitle: series.title,
              bookSlug,
              bookTitle: book.title,
              url: `/${seriesSlug}/${bookSlug}`
            });
          }
        });
      }
    });

    // Remove duplicates (in case a book matches both via series and title)
    const uniqueResults = searchResults.filter((result, index, self) =>
      index === self.findIndex((r) => r.url === result.url)
    );

    // Sort by relevance and limit
    const sortedResults = uniqueResults.sort((a, b) => {
      const aTitle = a.type === 'series' ? a.seriesTitle : a.bookTitle!;
      const bTitle = b.type === 'series' ? b.seriesTitle : b.bookTitle!;
      const aSeriesTitle = a.seriesTitle;
      const bSeriesTitle = b.seriesTitle;
      
      // First priority: exact matches at the start
      const aExact = aTitle.toLowerCase().startsWith(lowerQuery);
      const bExact = bTitle.toLowerCase().startsWith(lowerQuery);
      
      if (aExact && !bExact) return -1;
      if (!aExact && bExact) return 1;
      
      // Second priority: if same series, put series link first, then books in order
      if (aSeriesTitle === bSeriesTitle) {
        if (a.type === 'series' && b.type === 'book') return -1;
        if (a.type === 'book' && b.type === 'series') return 1;
        // Both are books from same series - maintain their original order
        return 0;
      }
      
      // Third priority: series matches before other matches
      const aSeriesMatches = aSeriesTitle.toLowerCase().includes(lowerQuery);
      const bSeriesMatches = bSeriesTitle.toLowerCase().includes(lowerQuery);
      
      if (aSeriesMatches && !bSeriesMatches) return -1;
      if (!aSeriesMatches && bSeriesMatches) return 1;
      
      // Finally, alphabetical by title
      return aTitle.localeCompare(bTitle);
    }).slice(0, 15); // Increased limit to show more results

    setResults(sortedResults);
    setShowDropdown(sortedResults.length > 0);
    setSelectedIndex(-1);
  };

  // Handle input change
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newQuery = e.target.value;
    setQuery(newQuery);
    performSearch(newQuery);
  };

  // Handle keyboard navigation
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (!showDropdown || results.length === 0) return;

    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        setSelectedIndex(prev => (prev < results.length - 1 ? prev + 1 : 0));
        break;
      case 'ArrowUp':
        e.preventDefault();
        setSelectedIndex(prev => (prev > 0 ? prev - 1 : results.length - 1));
        break;
      case 'Enter':
        e.preventDefault();
        if (selectedIndex >= 0 && selectedIndex < results.length) {
          router.push(results[selectedIndex].url);
          setShowDropdown(false);
          setQuery('');
        } else if (query.trim()) {
          // If no selection, go to search page
          router.push(`/search?q=${encodeURIComponent(query.trim())}`);
          setShowDropdown(false);
        }
        break;
      case 'Escape':
        setShowDropdown(false);
        setSelectedIndex(-1);
        break;
    }
  };

  // Handle form submit
  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      router.push(`/search?q=${encodeURIComponent(query.trim())}`);
      setShowDropdown(false);
    }
  };

  return (
    <div className="relative" ref={dropdownRef}>
      <form onSubmit={handleSearch}>
        <div className="flex gap-3">
          {/* Enhanced search input */}
          <div className="flex-1 relative group">
            <input
              ref={inputRef}
              type="text"
              value={query}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown}
              onFocus={() => query && performSearch(query)}
              placeholder="Search for a series or book..."
              className="w-full px-6 py-4 bg-gradient-to-br from-amber-50 to-amber-100/90 border-2 border-amber-800/30 rounded-lg placeholder-amber-900/50 text-amber-950 font-medium text-lg focus:outline-none focus:ring-2 focus:ring-amber-600/40 focus:border-amber-600 transition-all duration-200 shadow-inner"
              style={{
                boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.05)'
              }}
            />
            
            {/* Subtle decorative accents */}
            <div className="absolute top-0 left-0 w-4 h-4 border-l-2 border-t-2 border-amber-600/20 rounded-tl-sm pointer-events-none" />
            <div className="absolute top-0 right-0 w-4 h-4 border-r-2 border-t-2 border-amber-600/20 rounded-tr-sm pointer-events-none" />
            <div className="absolute bottom-0 left-0 w-4 h-4 border-l-2 border-b-2 border-amber-600/20 rounded-bl-sm pointer-events-none" />
            <div className="absolute bottom-0 right-0 w-4 h-4 border-r-2 border-b-2 border-amber-600/20 rounded-br-sm pointer-events-none" />
          </div>
          
          {/* Enhanced search button */}
          <button
            type="submit"
            className="px-8 py-4 bg-gradient-to-b from-amber-600 to-amber-700 hover:from-amber-500 hover:to-amber-600 border-2 border-amber-800/40 rounded-lg text-amber-50 font-display font-bold text-lg tracking-wide shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 active:translate-y-0 transition-all duration-150"
            style={{
              textShadow: '1px 1px 2px rgba(0,0,0,0.4)'
            }}
          >
            SEARCH
          </button>
        </div>
      </form>

      {/* Dropdown results */}
      {showDropdown && results.length > 0 && (
        <div className="absolute top-full left-0 right-0 mt-2 bg-gradient-to-br from-amber-50 to-amber-100 border-2 border-amber-800/30 rounded-lg shadow-xl z-50 max-h-96 overflow-y-auto">
          <div className="py-2">
            {results.map((result, index) => (
              <Link
                key={`${result.type}-${result.seriesSlug}-${result.bookSlug || ''}`}
                href={result.url}
                onClick={() => {
                  setQuery('');
                  setShowDropdown(false);
                }}
                className={`block px-4 py-3 hover:bg-amber-200/50 transition-colors ${
                  index === selectedIndex ? 'bg-amber-200/70' : ''
                }`}
              >
                <div className="flex items-center gap-3">
                  {/* Icon */}
                  <span className="text-amber-700 text-lg">
                    {result.type === 'series' ? '📚' : '📖'}
                  </span>
                  
                  {/* Content */}
                  <div className="flex-1">
                    <div className="font-semibold text-amber-950">
                      {result.type === 'series' ? result.seriesTitle : result.bookTitle}
                    </div>
                    {result.type === 'book' && (
                      <div className="text-sm text-amber-800/70">
                        from {result.seriesTitle}
                      </div>
                    )}
                  </div>
                  
                  {/* Type label */}
                  <span className="text-xs font-medium px-2 py-1 bg-amber-700/20 text-amber-800 rounded">
                    {result.type === 'series' ? 'Series' : 'Book'}
                  </span>
                </div>
              </Link>
            ))}
          </div>
          
          {/* Search all results link */}
          <div className="border-t border-amber-800/20 px-4 py-3 bg-amber-100/50">
            <button
              onClick={() => {
                router.push(`/search?q=${encodeURIComponent(query.trim())}`);
                setShowDropdown(false);
                setQuery('');
              }}
              className="text-sm text-amber-800 hover:text-amber-900 font-medium"
            >
              View all results for "{query}" →
            </button>
          </div>
        </div>
      )}
    </div>
  );
}