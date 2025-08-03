'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function SearchBar() {
  const [query, setQuery] = useState('');
  const router = useRouter();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      router.push(`/search?q=${encodeURIComponent(query.trim())}`);
    }
  };

  return (
    <form onSubmit={handleSearch} className="relative">
      <div className="flex gap-2">
        {/* Search input with ornate frame */}
        <div className="flex-1 relative">
          <div className="absolute inset-0 bg-gradient-to-r from-amber-700 via-amber-600 to-amber-700 rounded-lg blur-sm opacity-50" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search for a series or book..."
            className="relative w-full px-6 py-4 search-parchment placeholder-amber-700/50 focus:outline-none focus:ring-2 focus:ring-amber-500/50 rounded-lg"
            style={{
              fontFamily: 'MedievalSharp, serif',
              letterSpacing: '0.02em'
            }}
          />
          
          {/* Ornamental corners */}
          <div className="absolute top-1 left-1 w-3 h-3 border-l-2 border-t-2 border-amber-700/30 rounded-tl pointer-events-none" />
          <div className="absolute top-1 right-1 w-3 h-3 border-r-2 border-t-2 border-amber-700/30 rounded-tr pointer-events-none" />
          <div className="absolute bottom-1 left-1 w-3 h-3 border-l-2 border-b-2 border-amber-700/30 rounded-bl pointer-events-none" />
          <div className="absolute bottom-1 right-1 w-3 h-3 border-r-2 border-b-2 border-amber-700/30 rounded-br pointer-events-none" />
        </div>
        
        {/* Search button */}
        <button
          type="submit"
          className="search-button px-6 py-3 font-bold hover:scale-105 active:scale-95 transition-transform"
          style={{
            fontFamily: 'MedievalSharp, serif'
          }}
        >
          Search
        </button>
      </div>
      
      {/* Decorative subtitle */}
      <p className="text-center text-amber-800/70 text-sm mt-2 italic">
        Discover characters from your favorite tales...
      </p>
    </form>
  );
}
