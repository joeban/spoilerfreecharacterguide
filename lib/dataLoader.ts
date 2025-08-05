import fs from "fs/promises";
import path from "path";
import { notFound } from "next/navigation";

// Load the full book file (includes metadata, chapters, etc.)
export async function getBookMeta(series: string, book: string) {
  try {
    const filePath = path.join(process.cwd(), "data", series, `${book}.json`);
    const fileContents = await fs.readFile(filePath, "utf8");
    const bookData = JSON.parse(fileContents);
    return bookData;
  } catch (error) {
    console.error("Error loading book metadata:", error);
    notFound();
  }
}

// Load just one chapter's data from a book file
export async function getChapterData(series: string, book: string, chapterNum: number) {
  try {
    const filePath = path.join(process.cwd(), "data", series, `${book}.json`);
    const fileContents = await fs.readFile(filePath, "utf8");
    const bookData = JSON.parse(fileContents);

    const chapterData = bookData.chapters?.[chapterNum - 1];
    if (!chapterData) {
      notFound();
    }

    return chapterData;
  } catch (error) {
    console.error("Error loading chapter data:", error);
    notFound();
  }
}
