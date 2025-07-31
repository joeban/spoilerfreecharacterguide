import Link from 'next/link';
import seriesData from '../../data/series.json';

export default function SeriesPage({ series, books }) {
  return (
    <div className="min-h-screen bg-stone-50 p-6">
      <header className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-800">{series} Series</h1>
        <p className="text-gray-600">Choose a book from this series</p>
      </header>
      <main className="max-w-xl mx-auto bg-white rounded-lg shadow-md p-6">
        <ul className="space-y-3">
          {books.map((book) => (
            <li key={book.slug}>
              <Link
                href={`/book/${book.slug}`}
                className="block p-4 rounded-lg border border-gray-200 hover:bg-gray-100 transition text-lg font-medium"
              >
                {`Book ${book.number}: ${book.title}`}
              </Link>
            </li>
          ))}
        </ul>
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
