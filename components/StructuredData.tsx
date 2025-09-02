import Script from 'next/script';

interface BreadcrumbItem {
  name: string;
  url: string;
}

interface StructuredDataProps {
  type: 'series' | 'book' | 'chapter' | 'website';
  data: {
    title?: string;
    author?: string;
    description?: string;
    url?: string;
    bookCount?: number;
    chapters?: number;
    characterCount?: number;
    breadcrumbs?: BreadcrumbItem[];
    isbn?: string;
    bookFormat?: string;
    inLanguage?: string;
    genre?: string[];
    seriesName?: string;
    position?: number;
  };
}

export default function StructuredData({ type, data }: StructuredDataProps) {
  const generateSchema = () => {
    const baseUrl = 'https://spoilerfreecharacterguide.com';
    
    switch (type) {
      case 'website':
        return {
          '@context': 'https://schema.org',
          '@type': 'WebSite',
          name: 'Spoiler-Free Character Guide',
          description: data.description || 'Track characters in fantasy and sci-fi books without spoilers',
          url: baseUrl,
          potentialAction: {
            '@type': 'SearchAction',
            target: {
              '@type': 'EntryPoint',
              urlTemplate: `${baseUrl}/search?q={search_term_string}`
            },
            'query-input': 'required name=search_term_string'
          }
        };
        
      case 'series':
        return {
          '@context': 'https://schema.org',
          '@type': 'BookSeries',
          name: data.title,
          author: {
            '@type': 'Person',
            name: data.author
          },
          description: data.description,
          url: data.url,
          numberOfItems: data.bookCount,
          genre: data.genre || ['Fantasy', 'Science Fiction']
        };
        
      case 'book':
        const bookSchema: any = {
          '@context': 'https://schema.org',
          '@type': 'Book',
          name: data.title,
          author: {
            '@type': 'Person',
            name: data.author
          },
          description: data.description,
          url: data.url,
          bookFormat: 'https://schema.org/Paperback',
          inLanguage: 'en',
          genre: data.genre || ['Fantasy', 'Science Fiction']
        };
        
        if (data.isbn) {
          bookSchema.isbn = data.isbn;
        }
        
        if (data.seriesName) {
          bookSchema.isPartOf = {
            '@type': 'BookSeries',
            name: data.seriesName,
            position: data.position
          };
        }
        
        return bookSchema;
        
      case 'chapter':
        return {
          '@context': 'https://schema.org',
          '@type': 'Article',
          headline: data.title,
          description: data.description,
          url: data.url,
          author: {
            '@type': 'Organization',
            name: 'Spoiler-Free Character Guide'
          },
          publisher: {
            '@type': 'Organization',
            name: 'Spoiler-Free Character Guide',
            url: baseUrl
          },
          mainEntityOfPage: {
            '@type': 'WebPage',
            '@id': data.url
          }
        };
        
      default:
        return null;
    }
  };
  
  // Generate breadcrumb schema if provided
  const breadcrumbSchema = data.breadcrumbs ? {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: data.breadcrumbs.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      item: item.url
    }))
  } : null;
  
  const mainSchema = generateSchema();
  
  if (!mainSchema) return null;
  
  return (
    <>
      <Script
        id="structured-data"
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(mainSchema)
        }}
      />
      {breadcrumbSchema && (
        <Script
          id="breadcrumb-data"
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(breadcrumbSchema)
          }}
        />
      )}
    </>
  );
}