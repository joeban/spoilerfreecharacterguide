export default function Footer() {
  return (
    <footer className="bg-stone-100 border-t border-stone-300 mt-12 py-6 text-center text-xs text-stone-600">
      <div className="max-w-4xl mx-auto px-4">
        <p className="mb-2">As an Amazon Associate, we earn from qualifying purchases.</p>
        <p className="mb-2">All book titles, covers, and related marks are the property of their respective owners.</p>
        <p className="mb-2">
          <a href="/about" className="underline hover:text-stone-800">About</a> |{" "}
          <a href="mailto:spoilerfreecharacterguide@gmail.com" className="underline hover:text-stone-800">Contact</a>
        </p>
        <p>© {new Date().getFullYear()} Spoiler Free Character Guide. All rights reserved.</p>
      </div>
    </footer>
  );
}
