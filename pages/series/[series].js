import MiniBookButton from '../../components/MiniBookButton';
import seriesData from '../../data/series.json';

export default function SeriesPage({ seriesDisplayName, books }) {
  return (
    <div className="min-h-screen bg-stone-50 p-6">
      <header className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-800">{seriesDisplayName} Series</h1>
        <p className="text-gray-600">Choose a book from this series</p>
      </header>
      <main className="max-w-5xl mx-auto">
        <div className="flex flex-wrap gap-6 justify-center">
          {books.map((book) => (
            <MiniBookButton
              key={book.slug}
              bookTitle={book.title}
              slug={book.slug}
              color={getSeriesColor(seriesDisplayName)}
              number={book.number}
            />
          ))}
        </div>
      </main>
    </div>
  );
}

export async function getStaticPaths() {
  return {
    paths: Object.keys(seriesData).map((series) => ({ params: { series } })),
    fallback: false
  };
}

export async function getStaticProps({ params }) {
  const seriesInfo = seriesData[params.series];
  const books = seriesInfo.books || [];
  return { props: { seriesDisplayName: seriesInfo.displayName, books } };
}

// Helper to map series to colors (same palette as homepage)
function getSeriesColor(seriesName) {
  const palette = {
    'Mistborn': '#6B2C2C',
    'Harry Potter': '#1E3A8A',
    'Stormlight Archive': '#2E4057',
    'Wheel of Time': '#264D3B',
    'Lord of the Rings': '#3E4E32',
    'Dune': '#7A4A21'
  };
  return palette[seriesName] || '#6B2C2C';
}
