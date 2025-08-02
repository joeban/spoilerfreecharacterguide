import { ProcessedCharacter } from '@/lib/types';

interface CharacterCardProps {
  character: ProcessedCharacter;
}

export default function CharacterCard({ character }: CharacterCardProps) {
  return (
    <div className="parchment-card p-4 hover:shadow-lg transition-shadow duration-300">
      <div className="flex justify-between items-start mb-2">
        <div>
          <h3 className="text-xl font-display font-semibold">
            {character.name}
          </h3>
          {character.aliases && character.aliases.length > 0 && (
            <p className="text-sm text-ink-light italic">
              Also known as: {character.aliases.join(', ')}
            </p>
          )}
        </div>
        <span className="text-sm text-ink-light bg-parchment-dark px-2 py-1 rounded">
          {character.role}
        </span>
      </div>
      
      <p className="text-ink mb-3">
        {character.description}
      </p>
      
      {character.relationships && Object.keys(character.relationships).length > 0 && (
        <div className="border-t border-ink-light/30 pt-3">
          <h4 className="text-sm font-semibold mb-1 text-ink-light">Relationships:</h4>
          <div className="text-sm space-y-1">
            {Object.entries(character.relationships).map(([person, relation]) => (
              <div key={person}>
                <span className="font-medium">{person}</span>
                <span className="text-ink-light"> — {relation}</span>
              </div>
            ))}
          </div>
        </div>
      )}
      
      <div className="mt-3 text-xs text-ink-light">
        First seen: Chapter {character.firstAppearance}
        {character.lastUpdate > character.firstAppearance && (
          <span> • Updated: Chapter {character.lastUpdate}</span>
        )}
      </div>
    </div>
  );
}
