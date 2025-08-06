// Migration helper to convert legacy character format to new format
import { Character, LegacyCharacter, BookData, isLegacyCharacterFormat } from './types';

// Convert a single legacy character to new format
export function migrateLegacyCharacter(legacyChar: LegacyCharacter): Character {
  // Extract all chapters where we have tier information
  const tierChapters = Object.values(legacyChar.tiers)
    .map(tier => tier.appearsIn)
    .sort((a, b) => a - b);
  
  // For now, we'll assume the character appears in their tier chapters
  // This will need to be manually corrected with accurate appearance data
  const appearances = [...tierChapters];
  
  // Convert tiers to knowledge
  const knowledge: Character['knowledge'] = {};
  Object.entries(legacyChar.tiers).forEach(([tierKey, tier]) => {
    knowledge[tierKey] = {
      revealedIn: tier.appearsIn,
      description: tier.description,
      role: tier.role,
      relationships: tier.relationships
    };
  });
  
  return {
    name: legacyChar.name,
    aliases: legacyChar.aliases,
    appearances,
    knowledge
  };
}

// Migrate an entire book's data
export function migrateBookData(bookData: BookData): BookData {
  const migratedCharacters: BookData['characters'] = {};
  
  Object.entries(bookData.characters).forEach(([id, character]) => {
    if (isLegacyCharacterFormat(character)) {
      migratedCharacters[id] = migrateLegacyCharacter(character);
    } else {
      // Already in new format
      migratedCharacters[id] = character;
    }
  });
  
  return {
    ...bookData,
    meta: {
      ...bookData.meta,
      schemaVersion: '2.0'
    },
    characters: migratedCharacters
  };
}

// Helper to generate a migration report showing what needs manual correction
export function generateMigrationReport(bookData: BookData): string {
  const report: string[] = [];
  report.push(`Migration Report for "${bookData.meta.title}"`);
  report.push('=' .repeat(50));
  report.push('');
  
  Object.entries(bookData.characters).forEach(([id, character]) => {
    if (isLegacyCharacterFormat(character)) {
      const migrated = migrateLegacyCharacter(character);
      report.push(`Character: ${character.name} (${id})`);
      report.push(`  Auto-detected appearances: [${migrated.appearances.join(', ')}]`);
      report.push(`  ⚠️  NEEDS REVIEW: These are only chapters with tier updates.`);
      report.push(`      Please add all chapters where character actually appears.`);
      report.push('');
    }
  });
  
  report.push('Migration Instructions:');
  report.push('1. Review each character\'s appearances array');
  report.push('2. Add missing chapter numbers where character appears');
  report.push('3. Verify knowledge entries have correct revealedIn values');
  report.push('4. Update schemaVersion to "2.0" when complete');
  
  return report.join('\n');
}

// Function to create a properly structured character with full appearance data
export function createCharacter(
  name: string,
  options: {
    aliases?: string[];
    appearances: number[];
    initialKnowledge: {
      chapter: number;
      description: string;
      role: string;
      relationships?: Record<string, string>;
    };
  }
): Character {
  return {
    name,
    aliases: options.aliases || [],
    appearances: options.appearances,
    knowledge: {
      "1": {
        revealedIn: options.initialKnowledge.chapter,
        description: options.initialKnowledge.description,
        role: options.initialKnowledge.role,
        relationships: options.initialKnowledge.relationships
      }
    }
  };
}
