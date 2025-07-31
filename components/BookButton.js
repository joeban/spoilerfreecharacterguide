import Link from 'next/link';
import { motion } from 'framer-motion';

export default function BookButton({ seriesName, slug, color }) {
  return (
    <motion.div whileHover={{ scale: 1.05, rotate: -1 }} whileTap={{ scale: 0.97 }}>
      <Link href={`/book/${slug}`}>
        <div
          className="h-40 w-16 sm:h-56 sm:w-20 md:h-64 md:w-24 rounded-md shadow-md border-l-4 flex items-center justify-center cursor-pointer transition"
          style={{
            backgroundColor: color,
            borderColor: '#d4af37',
            backgroundImage: "url('/textures/leather.png')",
            backgroundSize: 'cover',
            backgroundBlendMode: 'multiply'
          }}
        >
          <span className="transform -rotate-90 text-white font-serif tracking-wide text-sm sm:text-base">
            {seriesName}
          </span>
        </div>
      </Link>
    </motion.div>
  );
}
