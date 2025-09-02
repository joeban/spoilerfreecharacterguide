import { MetadataRoute } from 'next';
import { getAllSeries } from '@/lib/dataLoader';

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const baseUrl = 'https://spoilerfreecharacterguide.com';
  const allSeries = await getAllSeries();
  
  // Start with static pages
  const sitemap: MetadataRoute.Sitemap = [
    {
      url: baseUrl,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 1.0,
    },
    {
      url: `${baseUrl}/search`,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.8,
    },
  ];
  
  // Add all series pages
  for (const { slug: seriesSlug, series } of allSeries) {
    sitemap.push({
      url: `${baseUrl}/${seriesSlug}`,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.9,
    });
    
    // Add all book pages for this series
    for (const bookSlug of Object.keys(series.books)) {
      const bookMeta = series.books[bookSlug];
      
      sitemap.push({
        url: `${baseUrl}/${seriesSlug}/${bookSlug}`,
        lastModified: new Date(),
        changeFrequency: 'weekly',
        priority: 0.8,
      });
      
      // Add all chapter pages for this book
      for (let chapter = 1; chapter <= bookMeta.chapters; chapter++) {
        sitemap.push({
          url: `${baseUrl}/${seriesSlug}/${bookSlug}/${chapter}`,
          lastModified: new Date(),
          changeFrequency: 'monthly',
          priority: 0.7,
        });
      }
    }
  }
  
  return sitemap;
}