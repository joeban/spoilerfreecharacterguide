import { 
  Character, 
  LegacyCharacter, 
  CharacterKnowledge, 
  ProcessedCharacter, 
  BookData,
  isNewCharacterFormat,
  isLegacyCharacterFormat 
} from './types';

// Get the appropriate knowledge/tier of information for a character based on current chapter
export function getCharacterKnowledge(
  character: Character | LegacyCharacter, 
  currentChapter: number
): CharacterKnowledge | null {
  
  if (isNewCharacterFormat(character)) {
    // New format: use knowledge
    const relevantKnowledge = Object.entries(character.knowledge)
      .filter(([_, knowledge]) => knowledge.revealedIn <= currentChapter)
      .sort(([a], [b]) => Number(b) - Number(a));
    
    return relevantKnowledge[0]?.[1] || null;
  } else {
    // Legacy format: use tiers
    const relevantTiers = Object.entries(character.tiers)
      .filter(([_, tier]) => tier.appearsIn <= currentChapter)
      .sort(([a], [b]) => Number(b) - Number(a));
    
    if (relevantTiers[0]) {
      const tier = relevantTiers[0][1];
      // Convert legacy tier to new knowledge format
      return {
        revealedIn: tier.appearsIn,
        description: tier.description,
        role: tier.role,
        relationships: tier.relationships
      };
    }
    return null;
  }
}

// Check if a character appears in a specific chapter
export function characterAppearsInChapter(
  character: Character | LegacyCharacter,
  chapter: number
): boolean {
  if (isNewCharacterFormat(character)) {
    return character.appearances.includes(chapter);
  } else {
    // For legacy format, we can only guess based on tiers
    // Character "appears" if they have been introduced by this chapter
    const hasBeenIntroduced = Object.values(character.tiers)
      .some(tier => tier.appearsIn <= chapter);
    return hasBeenIntroduced;
  }
}

// Process a character for display, filtering to appropriate knowledge level
export function processCharacter(
  id: string,
  character: Character | LegacyCharacter,
  currentChapter: number
): ProcessedCharacter | null {
  const knowledge = getCharacterKnowledge(character, currentChapter);
  if (!knowledge) return null;
  
  // Get all appearances up to current chapter
  let allAppearances: number[] = [];
  let appearsInThisChapter = false;
  
  if (isNewCharacterFormat(character)) {
    allAppearances = character.appearances.filter(ch => ch <= currentChapter);
    appearsInThisChapter = character.appearances.includes(currentChapter);
  } else {
    // For legacy format, we don't have accurate appearance data
    const introChapter = Math.min(...Object.values(character.tiers).map(t => t.appearsIn));
    if (introChapter <= currentChapter) {
      // We can only say they appeared when introduced
      allAppearances = [introChapter];
      appearsInThisChapter = introChapter === currentChapter;
    }
  }
  
  // Find when character was first introduced and last updated
  let firstAppearance: number;
  let lastUpdate: number;
  
  if (isNewCharacterFormat(character)) {
    firstAppearance = Math.min(...allAppearances);
    const updates = Object.values(character.knowledge)
      .map(k => k.revealedIn)
      .filter(ch => ch <= currentChapter);
    lastUpdate = Math.max(...updates);
  } else {
    const appearances = Object.values(character.tiers)
      .map(t => t.appearsIn)
      .filter(ch => ch <= currentChapter);
    firstAppearance = Math.min(...appearances);
    lastUpdate = Math.max(...appearances);
  }
  
  return {
    id,
    name: character.name,
    aliases: character.aliases,
    description: knowledge.description,
    role: knowledge.role,
    relationships: knowledge.relationships,
    firstAppearance,
    lastUpdate,
    appearsInThisChapter,
    allAppearances
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
    
    // For new format, use the appearances array
    // For legacy format, check if this is an update chapter
    if (isNewCharacterFormat(character)) {
      if (character.appearances.includes(currentChapter)) {
        inThisChapter.push(processed);
      } else if (character.appearances.some(ch => ch < currentChapter)) {
        previouslySeen.push(processed);
      }
    } else {
      // Legacy behavior: character appears in chapter if they have a tier for it
      const appearsInThisChapter = Object.values(character.tiers).some(
        tier => tier.appearsIn === currentChapter
      );
      
      if (appearsInThisChapter) {
        inThisChapter.push(processed);
      } else {
        const hasAppearedBefore = Object.values(character.tiers).some(
          tier => tier.appearsIn < currentChapter
        );
        if (hasAppearedBefore) {
          previouslySeen.push(processed);
        }
      }
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
  
  // Find all chapters where characters appear or have updates
  Object.values(bookData.characters).forEach(character => {
    if (isNewCharacterFormat(character)) {
      // Add all appearance chapters
      character.appearances.forEach(ch => chaptersWithCharacters.add(ch));
    } else {
      // Legacy: add all tier chapters
      Object.values(character.tiers).forEach(tier => {
        chaptersWithCharacters.add(tier.appearsIn);
      });
    }
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
