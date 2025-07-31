import BookButton from '../components/BookButton';

export default function Home() {
  const series = [
    { name: 'Mistborn', slug: 'mistborn', color: '#6b2c2c' },
    { name: 'Harry Potter', slug: 'sorcerers-stone', color: '#1e3a8a' }
  ];

  return (
    <div className="min-h-screen bg-stone-50 p-6">
      <header className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800">Spoiler Free Character Guide</h1>
        <p className="text-lg text-gray-600">Your safe guide to epic stories</p>
      </header>

      <main className="max-w-5xl mx-auto">
        <h2 className="text-2xl font-semibold text-gray-800 mb-6 text-center">Choose a series to get started!</h2>
        <div className="flex flex-wrap gap-6 justify-center">
          {series.map((s) => (
            <BookButton key={s.slug} seriesName={s.name} slug={s.slug} color={s.color} />
          ))}
        </div>
      </main>
    </div>
  );
}
