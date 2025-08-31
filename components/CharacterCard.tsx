'use client';

import { ProcessedCharacter } from '@/lib/types';
import { useState } from 'react';

interface CharacterCardProps {
  character: ProcessedCharacter;
}

export default function CharacterCard({ character }: CharacterCardProps) {
  const [isExpanded, setIsExpanded] = useState(false);
  // Helper function to capitalize first letter of each word
  const capitalizeWords = (str: string) => {
    return str.split(' ').map(word => 
      word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
    ).join(' ');
  };

  // Format appearances for display (e.g., "1-3, 5, 7-10")
  const formatAppearances = (appearances: number[] | undefined): string => {
    if (!appearances || appearances.length === 0) return '';
    
    const sorted = [...appearances].sort((a, b) => a - b);
    const ranges: string[] = [];
    let start = sorted[0];
    let end = sorted[0];
    
    for (let i = 1; i <= sorted.length; i++) {
      if (i === sorted.length || sorted[i] !== end + 1) {
        if (start === end) {
          ranges.push(start.toString());
        } else if (end === start + 1) {
          ranges.push(`${start}, ${end}`);
        } else {
          ranges.push(`${start}-${end}`);
        }
        if (i < sorted.length) {
          start = sorted[i];
          end = sorted[i];
        }
      } else {
        end = sorted[i];
      }
    }
    
    return ranges.join(', ');
  };

  // Truncate description for abbreviated view with consistent length
  const truncateDescription = (text: string, maxLength: number = 100) => {
    if (text.length <= maxLength) return text;
    const truncated = text.slice(0, maxLength);
    const lastSpaceIndex = truncated.lastIndexOf(' ');
    return truncated.slice(0, lastSpaceIndex > 0 ? lastSpaceIndex : maxLength) + '...';
  };

  // Truncate aliases to fit on one line
  const truncateAliases = (aliases: string[]) => {
    const fullText = `Also known as: ${aliases[0]}`;
    // If the first alias itself is too long (like "Professor Quirinus Quirrell"), truncate it
    if (fullText.length > 50) {
      const truncatedAlias = aliases[0].length > 25 ? aliases[0].slice(0, 25) + '...' : aliases[0];
      return `Also known as: ${truncatedAlias}`;
    }
    return fullText;
  };

  return (
    <div className="relative">
      {/* Individual parchment background for each character */}
      <div 
        className="parchment-panel p-4 sm:p-6 transition-all duration-300 hover:scale-[1.01] cursor-pointer"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        {/* Header section - always visible with consistent height */}
        <div className="flex justify-between items-start mb-3">
          <div className="flex-1">
            <h3 className="text-lg sm:text-xl font-heading font-bold text-parchment-primary leading-tight">
              {character.name}
            </h3>
            {/* Always reserve space for aliases - either show them or empty space */}
            <div className="h-5 mt-1">
              {character.aliases && character.aliases.length > 0 && !isExpanded && (
                <p className="text-xs sm:text-sm text-parchment-secondary italic truncate">
                  {truncateAliases(character.aliases)}
                </p>
              )}
              {character.aliases && character.aliases.length > 0 && isExpanded && (
                <p className="text-sm text-parchment-secondary italic">
                  Also known as: {character.aliases.join(', ')}
                </p>
              )}
            </div>
          </div>
          <div className="flex items-center gap-2 ml-2">
            <span className="text-xs font-medium text-amber-100 bg-gradient-to-br from-amber-700 to-amber-800 px-2 sm:px-3 py-1 sm:py-1.5 rounded-full shadow-sm whitespace-nowrap">
              {character.role}
            </span>
          </div>
        </div>
        
        {/* Description - abbreviated or full with consistent height */}
        <div className={`mb-3 ${!isExpanded ? 'h-12 sm:h-12' : ''}`}>
          <p className="text-sm sm:text-base text-parchment-primary text-readable leading-relaxed">
            {isExpanded ? character.description : truncateDescription(character.description)}
          </p>
        </div>
        
        {/* Expand/Collapse indicator */}
        <div className="flex items-center justify-center mb-3">
          <div className="flex items-center gap-1 text-xs sm:text-sm font-medium text-amber-700 select-none">
            <span>{isExpanded ? 'Click to show less' : 'Click to show more'}</span>
            <svg 
              className={`w-4 h-4 transform transition-transform duration-200 ${isExpanded ? 'rotate-180' : ''}`} 
              fill="none" 
              stroke="currentColor" 
              viewBox="0 0 24 24"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
            </svg>
          </div>
        </div>
        
        {/* Expanded content */}
        {isExpanded && (
          <div className="space-y-4 transition-all duration-200 ease-in-out">
            {/* Relationships section with improved formatting */}
            {character.relationships && Object.keys(character.relationships).length > 0 && (
              <div className="border-t border-stone-300 pt-4">
                <h4 className="text-sm font-heading font-semibold mb-2 text-parchment-primary">Relationships:</h4>
                <div className="text-sm space-y-1.5">
                  {Object.entries(character.relationships).map(([person, relation]) => (
                    <div key={person} className="flex items-start">
                      <span className="text-stone-500 mr-2">•</span>
                      <span className="text-parchment-primary">
                        {capitalizeWords(relation)} - <span className="font-semibold text-parchment-primary">{capitalizeWords(person)}</span>
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}
            
            {/* Footer with chapter info - Enhanced with appearances */}
            <div className="border-t border-stone-300 pt-3 text-xs text-parchment-secondary">
              <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 mb-1">
                <span className="font-medium">First seen: Chapter {character.firstAppearance}</span>
                {character.lastUpdate > character.firstAppearance && (
                  <span className="font-medium">Updated: Chapter {character.lastUpdate}</span>
                )}
              </div>
              {character.allAppearances && character.allAppearances.length > 0 && (
                <div className="mt-2">
                  <span className="text-stone-600">
                    Appears in chapters: {formatAppearances(character.allAppearances)}
                  </span>
                </div>
              )}
            </div>
          </div>
        )}
        
        {/* Compact footer for collapsed state */}
        {!isExpanded && (
          <div className="text-xs text-parchment-secondary">
            <span className="font-medium">First seen: Chapter {character.firstAppearance}</span>
            {character.lastUpdate > character.firstAppearance && (
              <span className="ml-3 font-medium">Updated: Chapter {character.lastUpdate}</span>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
