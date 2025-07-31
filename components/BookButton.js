import Link from 'next/link';
import { motion } from 'framer-motion';

export default function BookButton({ seriesName, slug, color }) {
  const fontMap = {
    'Mistborn': 'Cinzel, serif',
    'Harry Potter': 'EB Garamond, serif'
  };
  const fontFamily = fontMap[seriesName] || 'Merriweather, serif';

  const spineColor = shadeColor(color, -30);

  return (
    <motion.div whileHover={{ scale: 1.05, rotate: -1 }} whileTap={{ scale: 0.97 }}>
      <Link href={`/${slug}`}>
        <div
          className="relative h-48 w-32 sm:h-56 sm:w-40 md:h-64 md:w-48 cursor-pointer rounded-md overflow-hidden shadow-xl hover:shadow-2xl transition-shadow duration-300"
          style={{
            backgroundColor: color,
            backgroundImage: "url('/textures/leather.png')",
            backgroundSize: 'contain',
              backgroundBlendMode: 'multiply',
            backgroundBlendMode: 'multiply',
            fontFamily
          }}
        >
          {/* thicker, curved spine */}
          <div className="absolute top-0 left-0 h-full w-8"
            style={{
              backgroundColor: spineColor,
              backgroundImage: "url('/textures/leather.png')",
              backgroundSize: 'contain',
              backgroundBlendMode: 'multiply',
            backgroundBlendMode: 'multiply',
              boxShadow: 'inset -6px 0px 8px rgba(0,0,0,0.4)'
            }}
          ></div>

          {/* page edge right side */}
          <div className="absolute top-0 right-0 h-full w-3"
            style={{
              backgroundColor: '#f8f4e6',
              backgroundImage: "repeating-linear-gradient(to bottom, #f8f4e6, #f8f4e6 2px, #eae4d6 2px, #eae4d6 4px)"
            }}
          ></div>

          {/* page edge top */}
          <div className="absolute top-0 left-0 w-full h-3"
            style={{
              backgroundColor: '#f8f4e6',
              backgroundImage: "repeating-linear-gradient(to right, #f8f4e6, #f8f4e6 2px, #eae4d6 2px, #eae4d6 4px)",
              borderBottom: '1px solid rgba(0,0,0,0.1)'
            }}
          ></div>

          {/* gold frame (around book cover edges only) */}
          <div className="absolute inset-0 border-2 rounded-md pointer-events-none gold-frame"></div>

          {/* series title */}
          <div className="absolute inset-0 flex items-center justify-center text-center px-4">
            <span className="text-xl sm:text-2xl font-bold text-white drop-shadow-md">{seriesName}</span>
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
