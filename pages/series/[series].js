import MiniBookButton from '../../components/MiniBookButton';
import seriesData from '../../data/series.json';

export default function SeriesPage({ series, books }) {
  return (
    <div className="min-h-screen bg-stone-50 p-6">
      <header className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-800">{series} Series</h1>
        <p className="text-gray-600">Choose a book from this series</p>
      </header>
      <main className="max-w-5xl mx-auto">
        <div className="flex flex-wrap gap-6 justify-center">
          {books.map((book) => (
            <MiniBookButton
              key={book.slug}
              bookTitle={book.title}
              slug={book.slug}
              color={getSeriesColor(series)}
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
  const books = seriesData[params.series] || [];
  return { props: { series: params.series.replace('-', ' '), books } };
}

// Helper to map series to colors (same palette as homepage)
function getSeriesColor(series) {
  const palette = {
    'mistborn': '#6B2C2C',
    'harry-potter': '#1E3A8A',
    'stormlight-archive': '#2E4057',
    'wheel-of-time': '#264D3B',
    'lord-of-the-rings': '#3E4E32',
    'dune': '#7A4A21'
  };
  return palette[series] || '#6B2C2C';
}
