import Link from 'next/link';
import { motion } from 'framer-motion';

export default function MiniBookButton({ bookTitle, slug, color, number }) {
  const spineColor = shadeColor(color, -30);

  return (
    <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.97 }}>
      <Link href={`/book/${slug}`}>
        <div
          className="relative h-40 w-28 sm:h-48 sm:w-32 md:h-52 md:w-36 cursor-pointer overflow-hidden shadow-md hover:shadow-xl transition-shadow duration-300 rounded-lg"
          style={{
            backgroundColor: color,
            backgroundImage: "url('/textures/leather.png')",
            backgroundSize: 'contain',
            backgroundBlendMode: 'multiply',
            boxShadow: 'inset 0 1px 4px rgba(255,255,255,0.3), inset 0 -1px 4px rgba(0,0,0,0.3)'
          }}
        >
          {/* spine */}
          <div className="absolute top-0 left-0 h-full w-6 rounded-l-lg"
            style={{
              backgroundColor: spineColor,
              backgroundImage: "url('/textures/leather.png')",
              backgroundSize: 'contain',
              backgroundBlendMode: 'multiply',
              boxShadow: 'inset -5px 0px 6px rgba(0,0,0,0.4)'
            }}
          ></div>

          {/* page edge right */}
          <div className="absolute top-0 right-0 h-full w-2 rounded-r-lg"
            style={{
              backgroundColor: '#f8f4e6',
              backgroundImage: "repeating-linear-gradient(to bottom, #f8f4e6, #f8f4e6 2px, #eae4d6 2px, #eae4d6 4px)"
            }}
          ></div>

          {/* page edge top */}
          <div className="absolute top-0 left-0 w-full h-2 rounded-t-lg"
            style={{
              backgroundColor: '#f8f4e6',
              backgroundImage: "repeating-linear-gradient(to right, #f8f4e6, #f8f4e6 2px, #eae4d6 2px, #eae4d6 4px)",
              borderBottom: '1px solid rgba(0,0,0,0.1)'
            }}
          ></div>

          {/* gold frame */}
          <div className="absolute inset-0 border-2 rounded-lg pointer-events-none gold-frame"></div>

          {/* book title */}
          <div className="absolute inset-0 flex items-center justify-center text-center px-3">
            <span className="text-sm sm:text-base font-bold text-white drop-shadow-md">{bookTitle}</span>
          </div>

          {/* book number badge */}
          <div className="absolute top-1 left-1 bg-yellow-700 text-white text-xs px-2 py-1 rounded shadow">
            Book {number}
          </div>
        </div>
      </Link>
    </motion.div>
  );
}

function shadeColor(color, percent) {
  let R = parseInt(color.substring(1,3),16);
  let G = parseInt(color.substring(3,5),16);
  let B = parseInt(color.substring(5,7),16);

  R = parseInt(R * (100 + percent) / 100);
  G = parseInt(G * (100 + percent) / 100);
  B = parseInt(B * (100 + percent) / 100);

  R = (R<255)?R:255;
  G = (G<255)?G:255;
  B = (B<255)?B:255;

  const RR = ((R.toString(16).length==1)?"0"+R.toString(16):R.toString(16));
  const GG = ((G.toString(16).length==1)?"0"+G.toString(16):G.toString(16));
  const BB = ((B.toString(16).length==1)?"0"+B.toString(16):B.toString(16));

  return "#"+RR+GG+BB;
}
