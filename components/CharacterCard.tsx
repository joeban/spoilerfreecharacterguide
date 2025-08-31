import { ProcessedCharacter } from '@/lib/types';

interface CharacterCardProps {
  character: ProcessedCharacter;
}

export default function CharacterCard({ character }: CharacterCardProps) {
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

  return (
    <div className="relative">
      {/* Individual parchment background for each character */}
      <div className="parchment-panel p-6 transition-all duration-300 hover:scale-[1.01]">
        {/* Header section */}
        <div className="flex justify-between items-start mb-3">
          <div className="flex-1">
            <h3 className="text-xl font-heading font-bold text-parchment-primary">
              {character.name}
            </h3>
            {character.aliases && character.aliases.length > 0 && (
              <p className="text-sm text-parchment-secondary italic mt-1">
                Also known as: {character.aliases.join(', ')}
              </p>
            )}
          </div>
          <span className="text-xs font-medium text-amber-100 bg-gradient-to-br from-amber-700 to-amber-800 px-3 py-1.5 rounded-full shadow-sm ml-2">
            {character.role}
          </span>
        </div>
        
        {/* Description with better contrast */}
        <div className="mb-4">
          <p className="text-parchment-primary text-readable">
            {character.description}
          </p>
        </div>
        
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
        <div className="mt-4 pt-3 border-t border-stone-300 text-xs text-parchment-secondary">
          <div className="flex items-center justify-between mb-1">
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
    </div>
  );
}
