// ⚠️ DATA INSTRUCTIONS: Uses /data/index.json to list books in a series.
import fs from 'fs';
import path from 'path';

export default function SeriesPage({ seriesName, books }) {
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-2xl font-bold mb-4">{seriesName}</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {books.map(book => (
          <a key={book.bookNumber} href={`/${seriesName.toLowerCase()}/${book.bookNumber}`} className="p-6 rounded-lg border bg-white hover:shadow">
            <h2 className="text-xl font-semibold">{book.title}</h2>
            <p className="text-sm text-gray-500">Book {book.bookNumber}</p>
          </a>
        ))}
      </div>
    </div>
  )
}

export async function getStaticPaths() {
  const filePath = path.join(process.cwd(), 'data', 'index.json');
  const series = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const paths = Object.keys(series).map(name => ({ params: { series: name.toLowerCase() } }));
  return { paths, fallback: false };
}

export async function getStaticProps({ params }) {
  const filePath = path.join(process.cwd(), 'data', 'index.json');
  const series = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const seriesName = Object.keys(series).find(name => name.toLowerCase() === params.series);
  return { props: { seriesName, books: series[seriesName] } };
}
