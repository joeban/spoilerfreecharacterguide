// Core type definitions for the Spoiler-Free Character Guide

export interface Series {
  title: string;
  author: string;
  books: Record<string, BookMeta>;
}

export interface BookMeta {
  title: string;
  chapters: number;
  published: string;
  asin?: string;
}

export interface Registry {
  series: Record<string, Series>;
}

// NEW: Renamed from CharacterTier to CharacterKnowledge
export interface CharacterKnowledge {
  revealedIn: number;  // Renamed from appearsIn
  description: string;
  role: string;
  relationships?: Record<string, string>;
}

// UPDATED: Character structure with appearances array
export interface Character {
  name: string;
  aliases?: string[];
  appearances: number[];  // NEW: Array of chapter numbers where character appears
  knowledge: Record<string, CharacterKnowledge>;  // Renamed from tiers
}

// For backwards compatibility during migration
export interface LegacyCharacter {
  name: string;
  aliases?: string[];
  tiers: Record<string, {
    appearsIn: number;
    description: string;
    role: string;
    relationships?: Record<string, string>;
  }>;
}

export interface BookData {
  meta: {
    title: string;
    author: string;
    chapters: number;
    createdAt?: string;
    schemaVersion?: string;  // Made optional for compatibility
  };
  characters: Record<string, Character | LegacyCharacter>;
  recaps: Record<string, string>;
}

// Helper type guard to check if character uses new structure
export function isNewCharacterFormat(char: Character | LegacyCharacter): char is Character {
  return 'appearances' in char && 'knowledge' in char;
}

// Helper type guard to check if character uses legacy structure  
export function isLegacyCharacterFormat(char: Character | LegacyCharacter): char is LegacyCharacter {
  return 'tiers' in char;
}

export interface ProcessedCharacter {
  id: string;
  name: string;
  aliases?: string[];
  description: string;
  role: string;
  relationships?: Record<string, string>;
  firstAppearance: number;
  lastUpdate: number;
  appearsInThisChapter?: boolean;  // NEW: For better UI display
  allAppearances?: number[];  // NEW: All chapters where character appears
}
