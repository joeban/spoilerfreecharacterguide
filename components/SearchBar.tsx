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
      <div className="flex gap-3">
        {/* Enhanced search input */}
        <div className="flex-1 relative group">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
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
  );
}
