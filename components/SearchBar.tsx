'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function SearchBar() {
  const [query, setQuery] = useState('');
  const router = useRouter();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      // For now, we'll just navigate to the search page
      // In the future, this could filter the bookshelf or show suggestions
      router.push(`/search?q=${encodeURIComponent(query.trim())}`);
    }
  };

  return (
    <form onSubmit={handleSearch} className="relative">
      <div className="relative group">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search for a series or book..."
          className="w-full px-6 py-4 pl-14 bg-parchment border-2 border-ink-light/30 rounded-lg shadow-inner text-ink placeholder-ink-light/50 transition-all duration-300 focus:outline-none focus:border-ink-light focus:shadow-md"
          style={{
            backgroundImage: `linear-gradient(to bottom, rgba(244,232,208,0.5), rgba(244,232,208,0.8))`,
          }}
        />
        
        {/* Search icon */}
        <div className="absolute left-5 top-1/2 -translate-y-1/2 text-ink-light/50">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clipRule="evenodd" />
          </svg>
        </div>
        
        {/* Decorative border on focus */}
        <div className="absolute inset-0 border-2 border-gold/0 rounded-lg transition-all duration-300 pointer-events-none group-focus-within:border-gold/30" />
      </div>
      
      {/* Search button */}
      <button
        type="submit"
        className="absolute right-2 top-1/2 -translate-y-1/2 px-6 py-2 bg-ink text-parchment rounded-md shadow-md hover:bg-ink-light transition-all duration-200 hover:shadow-lg active:shadow-inner"
      >
        Search
      </button>
    </form>
  );
}
