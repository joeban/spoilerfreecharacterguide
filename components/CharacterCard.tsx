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

  return (
    <div className="relative">
      {/* Individual parchment background for each character */}
      <div className="parchment-panel p-5 hover:shadow-xl transition-all duration-300 hover:transform hover:scale-[1.02]">
        {/* Header section */}
        <div className="flex justify-between items-start mb-3">
          <div className="flex-1">
            <h3 className="text-xl font-display font-bold text-amber-900">
              {character.name}
            </h3>
            {character.aliases && character.aliases.length > 0 && (
              <p className="text-sm text-amber-700 italic mt-1">
                Also known as: {character.aliases.join(', ')}
              </p>
            )}
          </div>
          <span className="text-xs text-amber-100 bg-gradient-to-br from-amber-700 to-amber-800 px-3 py-1 rounded-full shadow-sm ml-2">
            {character.role}
          </span>
        </div>
        
        {/* Description with better contrast */}
        <div className="mb-4">
          <p className="text-amber-900/90 leading-relaxed">
            {character.description}
          </p>
        </div>
        
        {/* Relationships section with improved formatting */}
        {character.relationships && Object.keys(character.relationships).length > 0 && (
          <div className="border-t border-amber-700/30 pt-3">
            <h4 className="text-sm font-semibold mb-2 text-amber-800">Relationships:</h4>
            <div className="text-sm space-y-1.5">
              {Object.entries(character.relationships).map(([person, relation]) => (
                <div key={person} className="flex items-start">
                  <span className="text-amber-900/80 mr-2">•</span>
                  <span className="text-amber-900/90">
                    {capitalizeWords(relation)} - <span className="font-medium text-amber-900">{capitalizeWords(person)}</span>
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}
        
        {/* Footer with chapter info */}
        <div className="mt-4 pt-3 border-t border-amber-700/20 text-xs text-amber-700/80 flex items-center justify-between">
          <span>First seen: Chapter {character.firstAppearance}</span>
          {character.lastUpdate > character.firstAppearance && (
            <span>Updated: Chapter {character.lastUpdate}</span>
          )}
        </div>
      </div>
    </div>
  );
}
