import { Registry, BookData, Series, BookMeta } from './types';
import path from 'path';
import { promises as fs } from 'fs';

// Get the absolute path to the data directory
function getDataPath(...paths: string[]): string {
  return path.join(process.cwd(), 'data', ...paths);
}

// Load the main registry of all series and books
export async function loadRegistry(): Promise<Registry> {
  try {
    const data = await fs.readFile(getDataPath('index.json'), 'utf-8');
    return JSON.parse(data);
  } catch (error) {
    console.error('Error loading registry:', error);
    // Return empty registry if file doesn't exist yet
    return { series: {} };
  }
}

// Get a specific series
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

// Load full book data including characters and recaps
export async function loadBookData(seriesSlug: string, bookSlug: string): Promise<BookData | null> {
  try {
    const data = await fs.readFile(
      getDataPath(seriesSlug, `${bookSlug}.json`),
      'utf-8'
    );
    return JSON.parse(data);
  } catch (error) {
    console.error(`Error loading book data for ${seriesSlug}/${bookSlug}:`, error);
    return null;
  }
}

// Get all series (for the homepage)
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
