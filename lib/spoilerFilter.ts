import { Character, CharacterTier, ProcessedCharacter, BookData } from './types';

// Get the appropriate tier of information for a character based on current chapter
export function getCharacterTier(character: Character, currentChapter: number): CharacterTier | null {
  // Get all tiers that have appeared by this chapter
  const relevantTiers = Object.entries(character.tiers)
    .filter(([_, tier]) => tier.appearsIn <= currentChapter)
    .sort(([a], [b]) => Number(b) - Number(a)); // Sort by tier number descending
  
  // Return the highest tier that has appeared
  return relevantTiers[0]?.[1] || null;
}

// Process a character for display, filtering to appropriate tier
export function processCharacter(
  id: string,
  character: Character,
  currentChapter: number
): ProcessedCharacter | null {
  const tier = getCharacterTier(character, currentChapter);
  if (!tier) return null;
  
  // Find first appearance and last update
  const appearances = Object.values(character.tiers)
    .map(t => t.appearsIn)
    .filter(chapter => chapter <= currentChapter);
  
  return {
    id,
    name: character.name,
    aliases: character.aliases,
    description: tier.description,
    role: tier.role,
    relationships: tier.relationships,
    firstAppearance: Math.min(...appearances),
    lastUpdate: Math.max(...appearances),
  };
}

// Get all characters visible at a specific chapter
export function getCharactersForChapter(
  bookData: BookData,
  currentChapter: number
): {
  inThisChapter: ProcessedCharacter[];
  previouslySeen: ProcessedCharacter[];
} {
  const inThisChapter: ProcessedCharacter[] = [];
  const previouslySeen: ProcessedCharacter[] = [];
  
  Object.entries(bookData.characters).forEach(([id, character]) => {
    const processed = processCharacter(id, character, currentChapter);
    if (!processed) return;
    
    // Check if this character has a tier that appears in this specific chapter
    const appearsInThisChapter = Object.values(character.tiers).some(
      tier => tier.appearsIn === currentChapter
    );
    
    if (appearsInThisChapter) {
      inThisChapter.push(processed);
    } else {
      previouslySeen.push(processed);
    }
  });
  
  // Sort by name for consistent display
  inThisChapter.sort((a, b) => a.name.localeCompare(b.name));
  previouslySeen.sort((a, b) => a.name.localeCompare(b.name));
  
  return { inThisChapter, previouslySeen };
}

// Get chapter recap if it exists
export function getChapterRecap(bookData: BookData, chapter: number): string | null {
  return bookData.recaps[chapter.toString()] || null;
}

// Get list of chapters that have content (characters or recaps)
export function getChaptersWithContent(bookData: BookData): number[] {
  const chaptersWithCharacters = new Set<number>();
  const chaptersWithRecaps = new Set<number>();
  
  // Find all chapters where characters appear
  Object.values(bookData.characters).forEach(character => {
    Object.values(character.tiers).forEach(tier => {
      chaptersWithCharacters.add(tier.appearsIn);
    });
  });
  
  // Find all chapters with recaps
  Object.keys(bookData.recaps).forEach(chapter => {
    chaptersWithRecaps.add(parseInt(chapter));
  });
  
  // Combine and sort
  const allChapters = Array.from(new Set([
    ...Array.from(chaptersWithCharacters),
    ...Array.from(chaptersWithRecaps)
  ]));
  return allChapters.sort((a, b) => a - b);
}
