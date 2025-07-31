import Footer from '../components/Footer';
import BookButton from '../components/BookButton';

export default function Home() {
  // Color palette for series
  const series = [
    { name: 'Mistborn', slug: 'series/mistborn', color: '#6B2C2C' }, // deep burgundy
    { name: 'Harry Potter', slug: 'series/harry-potter', color: '#1E3A8A' }, // deep navy
    { name: 'Stormlight Archive', slug: 'series/stormlight-archive', color: '#2E4057' }, // slate blue
    { name: 'Wheel of Time', slug: 'series/wheel-of-time', color: '#264D3B' }, // dark green
    { name: 'Lord of the Rings', slug: 'series/lord-of-the-rings', color: '#3E4E32' }, // deep forest
    { name: 'Dune', slug: 'series/dune', color: '#7A4A21' } // ochre
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
      <Footer />
      </main>
    </div>
  );
}
