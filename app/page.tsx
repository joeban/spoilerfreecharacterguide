import { getAllSeries } from '@/lib/dataLoader';
import Bookshelf from '@/components/Bookshelf';
import SearchBar from '@/components/SearchBar';
import StructuredData from '@/components/StructuredData';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Track Book Characters Without Spoilers - Fantasy & Sci-Fi Series',
  description: 'The ultimate spoiler-free character guide for fantasy and sci-fi books. Track characters chapter by chapter in Harry Potter, Percy Jackson, Lord of the Rings, Dune, and more popular series.',
  keywords: ['spoiler-free character guide', 'book character tracker', 'fantasy book guide', 'sci-fi book guide', 'Harry Potter characters', 'Percy Jackson characters', 'LOTR characters', 'no spoilers reading'],
  alternates: {
    canonical: 'https://spoilerfreecharacterguide.com'
  },
  openGraph: {
    title: 'Spoiler-Free Character Guide - Track Characters Without Spoilers',
    description: 'The ultimate spoiler-free character guide for fantasy and sci-fi books. Choose your chapter and see only what you need to know.',
    url: 'https://spoilerfreecharacterguide.com',
    type: 'website'
  }
};

export default async function HomePage() {
  const allSeries = await getAllSeries();

  return (
    <>
      <StructuredData 
        type="website"
        data={{
          description: 'The ultimate spoiler-free character guide for fantasy and sci-fi books. Track characters chapter by chapter without spoilers.'
        }}
      />
      <div className="container mx-auto px-4 py-8">
      {/* Search Section */}
      <div className="max-w-3xl mx-auto mb-12">
        <div className="wood-fine rounded-lg p-6">
          <SearchBar />
        </div>
      </div>

      {/* Bookshelf */}
      {allSeries.length > 0 ? (
        <Bookshelf series={allSeries} />
      ) : (
        <div className="text-center py-16">
          <div className="parchment-panel max-w-md mx-auto p-8">
            <h3 className="text-2xl font-heading font-bold mb-4 text-parchment-primary">Library Coming Soon</h3>
            <p className="text-parchment-primary text-readable">
              We&apos;re preparing our collection of spoiler-free guides. 
              Check back soon for your favorite series!
            </p>
          </div>
        </div>
      )}
    </div>
    </>
  );
}
