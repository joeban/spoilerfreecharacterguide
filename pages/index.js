// ⚠️ DATA INSTRUCTIONS: All book, character, and recap data lives in /data.
// DO NOT regenerate JSON. Only update existing files. See DATA_README.md.

import fs from 'fs';
import path from 'path';

export default function Home({ series }) {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-8">
      <h1 className="text-3xl font-bold mb-6">📚 Spoiler Free Character Guide</h1>
      <p className="mb-4 text-gray-600">Choose a series to get started.</p>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {Object.keys(series)
          .filter(name => !name.startsWith('_') && !name.toLowerCase().includes('comment'))
          .map(name => (
          <a key={name} href={`/${name.toLowerCase()}`} className="p-6 rounded-lg border bg-white hover:shadow">
            <h2 className="text-xl font-semibold">{name}</h2>
            <p className="text-sm text-gray-500">{series[name].length} book(s)</p>
          </a>
        ))}
      </div>
    </div>
  )
}

export async function getStaticProps() {
  const filePath = path.join(process.cwd(), 'data', 'index.json');
  const series = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  return { props: { series } };
}
