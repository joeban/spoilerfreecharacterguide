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
              color={book.color}
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
