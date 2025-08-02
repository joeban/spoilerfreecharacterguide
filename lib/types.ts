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
}

export interface Registry {
  series: Record<string, Series>;
}

export interface CharacterTier {
  appearsIn: number;
  description: string;
  role: string;
  relationships?: Record<string, string>;
}

export interface Character {
  name: string;
  aliases?: string[];
  tiers: Record<string, CharacterTier>;
}

export interface BookData {
  meta: {
    title: string;
    author: string;
    chapters: number;
  };
  characters: Record<string, Character>;
  recaps: Record<string, string>;
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
}
