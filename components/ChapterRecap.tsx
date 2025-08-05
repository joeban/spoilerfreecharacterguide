"use client";

import { useState } from "react";

interface ChapterRecapProps {
  recap: string;
  chapter: number;
}

export default function ChapterRecap({ recap, chapter }: ChapterRecapProps) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="parchment-panel p-4 text-amber-900">
      <div className="text-center mb-2">
        <button
          className="text-lg font-semibold underline hover:text-amber-700"
          onClick={() => setExpanded(!expanded)}
        >
          {expanded ? `Hide Recap for Chapter ${chapter}` : `Show Recap for Chapter ${chapter}`}
        </button>
      </div>

      {expanded && (
        <div className="bg-[#e8dcc4] p-4 rounded text-sm leading-relaxed">
          {recap}
        </div>
      )}
    </div>
  );
}
