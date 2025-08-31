import { ProcessedCharacter } from '@/lib/types';
import CharacterCard from './CharacterCard';

interface CharacterListProps {
  inThisChapter: ProcessedCharacter[];
  previouslySeen: ProcessedCharacter[];
}

export default function CharacterList({ inThisChapter, previouslySeen }: CharacterListProps) {
  return (
    <div className="space-y-8">
      {/* Characters in this chapter */}
      {inThisChapter.length > 0 && (
        <section>
          <h2 className="text-2xl font-display mb-4 text-center flex items-center justify-center gap-4">
            <span className="h-px bg-amber-600/50 dark:bg-amber-400/50 flex-1 max-w-[100px]"></span>
            <span>In This Chapter</span>
            <span className="h-px bg-amber-600/50 dark:bg-amber-400/50 flex-1 max-w-[100px]"></span>
          </h2>
          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {inThisChapter.map((character) => (
              <CharacterCard key={character.id} character={character} />
            ))}
          </div>
        </section>
      )}
      
      {/* Previously seen characters */}
      {previouslySeen.length > 0 && (
        <section>
          <h2 className="text-2xl font-display mb-4 text-center flex items-center justify-center gap-4">
            <span className="h-px bg-amber-600/50 dark:bg-amber-400/50 flex-1 max-w-[100px]"></span>
            <span>Previously Seen</span>
            <span className="h-px bg-amber-600/50 dark:bg-amber-400/50 flex-1 max-w-[100px]"></span>
          </h2>
          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {previouslySeen.map((character) => (
              <CharacterCard key={character.id} character={character} />
            ))}
          </div>
        </section>
      )}
      
      {/* No characters message */}
      {inThisChapter.length === 0 && previouslySeen.length === 0 && (
        <div className="text-center py-12">
          <div className="parchment-card max-w-md mx-auto p-8">
            <p className="text-amber-600 dark:text-amber-300">
              No character information available for this chapter yet.
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
