// ⚠️ DATA SOURCE INFO (UPDATED)
// JSON files now use a dictionary-based format.
// - Characters are keyed by name (characters['Vin'])
// - Each character has tiered descriptions in tiers['1-5'] etc.
// - Chapter recaps are in recaps['1']
// See DATA_README.md for examples of the structure.

// ⚠️ DATA SOURCE INFO (UPDATED)
// All character and recap data is stored in /data/*.json.
// - Do NOT regenerate these JSON files unless absolutely necessary.
// - Update existing JSONs to add or edit content.
// - The /data/index.json file lists all series and books.
// - See DATA_README.md in /data for documentation.

export default function About() {
  return (
    <div className="min-h-screen bg-stone-50 p-6 text-center">
      <h1 className="text-3xl font-bold text-gray-800 mb-4">About Spoiler Free Character Guide</h1>
      <p className="max-w-2xl mx-auto text-gray-700">
        We love fantasy and sci-fi, and built this site so readers can explore characters without fear of spoilers.
        Our guides are carefully written to reveal only what you’ve read so far, preserving the joy of discovery in every story.
      </p>
    </div>
  );
}