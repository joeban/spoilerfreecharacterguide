import { notFound } from "next/navigation";
import { getChapterData, getBookMeta } from "@/lib/dataLoader";
import ChapterRecap from "@/components/ChapterRecap";
import CharacterCard from "@/components/CharacterCard";
import ChapterSelector from "@/components/ChapterSelector";

interface PageProps {
  params: {
    series: string;
    book: string;
    chapter: string;
  };
}

export default async function ChapterPage({ params }: PageProps) {
  const { series, book, chapter } = params;
  const chapterNum = parseInt(chapter);

  const bookMeta = await getBookMeta(series, book);
  const chapterData = await getChapterData(series, book, chapterNum);

  if (!chapterData || !bookMeta) {
    notFound();
  }

  return (
    <main className="min-h-screen bg-[#1a1108] text-amber-100 p-4">
      <div className="max-w-4xl mx-auto space-y-6">
        <h1 className="text-3xl tavern-sign-text">Chapter {chapterNum}</h1>

        <ChapterRecap recap={chapterData.recap} />

        <section>
          <h2 className="text-2xl font-bold mb-2">In This Chapter</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {chapterData.characters.map((char: any) => (
              <CharacterCard key={char.name} character={char} />
            ))}
          </div>
        </section>

        <section>
          <h2 className="text-2xl font-bold mb-2">Previously Seen</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {chapterData.previousCharacters.map((char: any) => (
              <CharacterCard key={char.name} character={char} />
            ))}
          </div>
        </section>

        <ChapterSelector
          totalChapters={bookMeta.chapters}
          series={series}
          book={book}
        />
      </div>
    </main>
  );
}
