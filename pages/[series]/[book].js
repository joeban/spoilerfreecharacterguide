// ⚠️ DATA INSTRUCTIONS: Reads character and recap info from the specific book JSON.
import fs from 'fs';
import path from 'path';

export default function BookPage({ bookData }) {
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-2xl font-bold mb-4">{bookData.meta.title}</h1>
      <p className="mb-4 text-gray-600">Select a chapter to see characters.</p>
      <select className="border p-2 rounded mb-4">
        {Array.from({length: bookData.meta.totalChapters}, (_, i) => i + 1).map(ch => (
          <option key={ch}>Chapter {ch}</option>
        ))}
      </select>
      <div className="mt-6">
        <h2 className="text-xl font-semibold">Characters</h2>
        <ul className="list-disc ml-6">
          {Object.keys(bookData.characters).map(name => (
            <li key={name}>{name}</li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export async function getStaticPaths() {
  const indexPath = path.join(process.cwd(), 'data', 'index.json');
  const series = JSON.parse(fs.readFileSync(indexPath, 'utf-8'));
  const paths = [];
  Object.keys(series).forEach(name => {
    series[name].forEach(book => {
      paths.push({ params: { series: name.toLowerCase(), book: String(book.bookNumber) } });
    });
  });
  return { paths, fallback: false };
}

export async function getStaticProps({ params }) {
  const filePath = path.join(process.cwd(), 'data', `${params.series}${params.book}.json`);
  const bookData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  return { props: { bookData } };
}
