import { Registry, BookData, Series, BookMeta } from './types';
import path from 'path';
import { promises as fs } from 'fs';

// Cache for frequently accessed data
const dataCache = new Map<string, any>();
const CACHE_TTL = 1000 * 60 * 5; // 5 minutes cache
const cacheTimestamps = new Map<string, number>();

// Get the absolute path to the data directory
function getDataPath(...paths: string[]): string {
  return path.join(process.cwd(), 'data', ...paths);
}

// Helper to check cache validity
function isCacheValid(key: string): boolean {
  const timestamp = cacheTimestamps.get(key);
  if (!timestamp) return false;
  return Date.now() - timestamp < CACHE_TTL;
}

// Helper to set cache
function setCache<T>(key: string, data: T): T {
  dataCache.set(key, data);
  cacheTimestamps.set(key, Date.now());
  return data;
}

// Helper to get from cache
function getCache<T>(key: string): T | null {
  if (!isCacheValid(key)) {
    dataCache.delete(key);
    cacheTimestamps.delete(key);
    return null;
  }
  return dataCache.get(key) || null;
}

// Load the main registry with caching
export async function loadRegistry(): Promise<Registry> {
  const cacheKey = 'registry';
  const cached = getCache<Registry>(cacheKey);
  if (cached) return cached;

  try {
    const data = await fs.readFile(getDataPath('index.json'), 'utf-8');
    return setCache(cacheKey, JSON.parse(data));
  } catch (error) {
    console.error('Error loading registry:', error);
    return { series: {} };
  }
}

// Get a specific series with caching
export async function getSeries(seriesSlug: string): Promise<Series | null> {
  const registry = await loadRegistry();
  return registry.series[seriesSlug] || null;
}

// Get a specific book's metadata
export async function getBookMeta(seriesSlug: string, bookSlug: string): Promise<BookMeta | null> {
  const series = await getSeries(seriesSlug);
  if (!series) return null;
  return series.books[bookSlug] || null;
}

// Load minimal book data (just metadata and chapter count)
export async function loadBookMetadata(seriesSlug: string, bookSlug: string): Promise<{ meta: any; chapterCount: number } | null> {
  const cacheKey = `book-meta-${seriesSlug}-${bookSlug}`;
  const cached = getCache<{ meta: any; chapterCount: number }>(cacheKey);
  if (cached) return cached;

  try {
    const data = await fs.readFile(
      getDataPath(seriesSlug, `${bookSlug}.json`),
      'utf-8'
    );
    const bookData = JSON.parse(data);
    const result = {
      meta: bookData.meta,
      chapterCount: bookData.meta.chapters || 0
    };
    return setCache(cacheKey, result);
  } catch (error) {
    console.error(`Error loading book metadata for ${seriesSlug}/${bookSlug}:`, error);
    return null;
  }
}

// Load full book data with caching
export async function loadBookData(seriesSlug: string, bookSlug: string): Promise<BookData | null> {
  const cacheKey = `book-${seriesSlug}-${bookSlug}`;
  const cached = getCache<BookData>(cacheKey);
  if (cached) return cached;

  try {
    const data = await fs.readFile(
      getDataPath(seriesSlug, `${bookSlug}.json`),
      'utf-8'
    );
    return setCache(cacheKey, JSON.parse(data));
  } catch (error) {
    console.error(`Error loading book data for ${seriesSlug}/${bookSlug}:`, error);
    return null;
  }
}

// Load only chapter-specific data (optimized for chapter pages)
export async function loadChapterData(
  seriesSlug: string,
  bookSlug: string,
  chapterNumber: number
): Promise<{ characters: any; recap: string | null; meta: any } | null> {
  const cacheKey = `chapter-${seriesSlug}-${bookSlug}-${chapterNumber}`;
  const cached = getCache<any>(cacheKey);
  if (cached) return cached;

  const bookData = await loadBookData(seriesSlug, bookSlug);
  if (!bookData) return null;

  // Filter only the characters and recap needed for this chapter
  const chapterKey = chapterNumber.toString();
  const recap = bookData.recaps?.[chapterKey] || null;
  
  // Only include characters that appear up to this chapter
  const relevantCharacters: any = {};
  for (const [charId, character] of Object.entries(bookData.characters)) {
    // Check if character has appeared by this chapter
    const hasAppeared = (character as any).appearances?.some((ch: number) => ch <= chapterNumber) ||
                       (character as any).tiers?.some((tier: any) => tier.appearsIn <= chapterNumber);
    
    if (hasAppeared) {
      relevantCharacters[charId] = character;
    }
  }

  const result = {
    characters: relevantCharacters,
    recap,
    meta: bookData.meta
  };

  return setCache(cacheKey, result);
}

// Get all series with basic info only (optimized for homepage)
export async function getAllSeriesOptimized(): Promise<Array<{ slug: string; title: string; bookCount: number }>> {
  const cacheKey = 'all-series-optimized';
  const cached = getCache<Array<{ slug: string; title: string; bookCount: number }>>(cacheKey);
  if (cached) return cached;

  const registry = await loadRegistry();
  const result = Object.entries(registry.series).map(([slug, series]) => ({
    slug,
    title: series.title,
    bookCount: Object.keys(series.books).length
  }));
  
  return setCache(cacheKey, result);
}

// Get all series (full data)
export async function getAllSeries(): Promise<Array<{ slug: string; series: Series }>> {
  const registry = await loadRegistry();
  return Object.entries(registry.series).map(([slug, series]) => ({
    slug,
    series,
  }));
}

// Get all books in a series
export async function getBooksInSeries(seriesSlug: string): Promise<Array<{ slug: string; book: BookMeta }> | null> {
  const series = await getSeries(seriesSlug);
  if (!series) return null;
  
  return Object.entries(series.books).map(([slug, book]) => ({
    slug,
    book,
  }));
}

// Preload critical data for performance
export async function preloadCriticalData() {
  // Preload registry on app start
  await loadRegistry();
}

// Clear cache (useful for development)
export function clearCache() {
  dataCache.clear();
  cacheTimestamps.clear();
}