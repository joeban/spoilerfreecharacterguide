import Link from 'next/link';

interface RelatedSeriesProps {
  currentSeries: string;
}

// Series relationships for internal linking (SEO)
const seriesRelationships: Record<string, { title: string; slug: string; reason: string }[]> = {
  'percy-jackson': [
    { title: 'Harry Potter', slug: 'harry-potter', reason: 'Young wizard adventures' },
    { title: 'Wings of Fire', slug: 'wings-of-fire', reason: 'Young heroes with destiny' },
    { title: 'The Hunger Games', slug: 'hunger-games', reason: 'Teen protagonists' }
  ],
  'harry-potter': [
    { title: 'Percy Jackson', slug: 'percy-jackson', reason: 'Magic school adventures' },
    { title: 'Chronicles of Narnia', slug: 'chronicles-of-narnia', reason: 'Classic fantasy' },
    { title: 'Lord of the Rings', slug: 'lord-of-the-rings', reason: 'Epic fantasy quest' }
  ],
  'fourth-wing': [
    { title: 'A Court of Thorns and Roses', slug: 'court-thorns-roses', reason: 'Romantasy with wings' },
    { title: 'Throne of Glass', slug: 'throne-of-glass', reason: 'Sarah J. Maas fans' },
    { title: 'Shadow and Bone', slug: 'shadow-and-bone', reason: 'Magic academy romance' }
  ],
  'court-thorns-roses': [
    { title: 'Fourth Wing', slug: 'fourth-wing', reason: 'Romantasy bestsellers' },
    { title: 'Throne of Glass', slug: 'throne-of-glass', reason: 'Same author' },
    { title: 'Shadow and Bone', slug: 'shadow-and-bone', reason: 'Fantasy romance' }
  ],
  'throne-of-glass': [
    { title: 'A Court of Thorns and Roses', slug: 'court-thorns-roses', reason: 'Same author' },
    { title: 'Fourth Wing', slug: 'fourth-wing', reason: 'Strong female leads' },
    { title: 'The Hunger Games', slug: 'hunger-games', reason: 'Fierce heroines' }
  ],
  'song-ice-fire': [
    { title: 'Lord of the Rings', slug: 'lord-of-the-rings', reason: 'Epic fantasy' },
    { title: 'Wheel of Time', slug: 'wheel-of-time', reason: 'Complex politics' },
    { title: 'The Witcher', slug: 'witcher', reason: 'Dark fantasy' }
  ],
  'wheel-of-time': [
    { title: 'Lord of the Rings', slug: 'lord-of-the-rings', reason: 'Epic quest fantasy' },
    { title: 'A Song of Ice and Fire', slug: 'song-ice-fire', reason: 'Epic scope' },
    { title: 'Stormlight Archive', slug: 'stormlight-archive', reason: 'Brandon Sanderson' }
  ],
  'stormlight-archive': [
    { title: 'Mistborn', slug: 'cosmere', reason: 'Cosmere universe' },
    { title: 'Wheel of Time', slug: 'wheel-of-time', reason: 'Epic fantasy' },
    { title: 'The Kingkiller Chronicle', slug: 'kingkiller-chronicle', reason: 'Magic systems' }
  ],
  'cosmere': [
    { title: 'Stormlight Archive', slug: 'stormlight-archive', reason: 'Cosmere universe' },
    { title: 'The Kingkiller Chronicle', slug: 'kingkiller-chronicle', reason: 'Detailed magic' },
    { title: 'Wheel of Time', slug: 'wheel-of-time', reason: 'Brandon Sanderson' }
  ],
  'lord-of-the-rings': [
    { title: 'Chronicles of Narnia', slug: 'chronicles-of-narnia', reason: 'Classic fantasy' },
    { title: 'Harry Potter', slug: 'harry-potter', reason: 'Fantasy classics' },
    { title: 'A Song of Ice and Fire', slug: 'song-ice-fire', reason: 'Epic worldbuilding' }
  ],
  'hunger-games': [
    { title: 'Percy Jackson', slug: 'percy-jackson', reason: 'Young adult adventures' },
    { title: 'Fourth Wing', slug: 'fourth-wing', reason: 'Life-or-death training' },
    { title: 'Throne of Glass', slug: 'throne-of-glass', reason: 'Strong heroines' }
  ],
  'shadow-and-bone': [
    { title: 'Fourth Wing', slug: 'fourth-wing', reason: 'Magic and romance' },
    { title: 'A Court of Thorns and Roses', slug: 'court-thorns-roses', reason: 'Fantasy romance' },
    { title: 'Throne of Glass', slug: 'throne-of-glass', reason: 'YA fantasy' }
  ],
  'chronicles-of-narnia': [
    { title: 'Lord of the Rings', slug: 'lord-of-the-rings', reason: 'Classic fantasy' },
    { title: 'Harry Potter', slug: 'harry-potter', reason: 'Children\'s fantasy' },
    { title: 'Percy Jackson', slug: 'percy-jackson', reason: 'Young heroes' }
  ],
  'dune': [
    { title: 'Foundation', slug: 'foundation', reason: 'Classic sci-fi epics' },
    { title: 'The Expanse', slug: 'expanse', reason: 'Space politics' },
    { title: 'A Song of Ice and Fire', slug: 'song-ice-fire', reason: 'Political intrigue' }
  ],
  'expanse': [
    { title: 'Dune', slug: 'dune', reason: 'Space opera' },
    { title: 'Foundation', slug: 'foundation', reason: 'Science fiction' },
    { title: 'Stormlight Archive', slug: 'stormlight-archive', reason: 'Epic scope' }
  ],
  'foundation': [
    { title: 'Dune', slug: 'dune', reason: 'Classic sci-fi' },
    { title: 'The Expanse', slug: 'expanse', reason: 'Space civilizations' },
    { title: 'Discworld', slug: 'discworld', reason: 'Social commentary' }
  ],
  'witcher': [
    { title: 'A Song of Ice and Fire', slug: 'song-ice-fire', reason: 'Dark fantasy' },
    { title: 'Lord of the Rings', slug: 'lord-of-the-rings', reason: 'Fantasy quests' },
    { title: 'The Kingkiller Chronicle', slug: 'kingkiller-chronicle', reason: 'Complex protagonists' }
  ],
  'kingkiller-chronicle': [
    { title: 'Stormlight Archive', slug: 'stormlight-archive', reason: 'Magic systems' },
    { title: 'The Witcher', slug: 'witcher', reason: 'Complex heroes' },
    { title: 'Mistborn', slug: 'cosmere', reason: 'Detailed worldbuilding' }
  ],
  'wings-of-fire': [
    { title: 'Percy Jackson', slug: 'percy-jackson', reason: 'Young heroes' },
    { title: 'Harry Potter', slug: 'harry-potter', reason: 'Magical schools' },
    { title: 'Chronicles of Narnia', slug: 'chronicles-of-narnia', reason: 'Fantasy adventures' }
  ],
  'discworld': [
    { title: 'Foundation', slug: 'foundation', reason: 'Social satire' },
    { title: 'The Hitchhiker\'s Guide', slug: 'hitchhikers-guide', reason: 'Humor in genre' },
    { title: 'Lord of the Rings', slug: 'lord-of-the-rings', reason: 'Fantasy worlds' }
  ]
};

export default function RelatedSeries({ currentSeries }: RelatedSeriesProps) {
  const related = seriesRelationships[currentSeries];
  
  if (!related || related.length === 0) {
    return null;
  }

  return (
    <div className="mt-12 p-6 bg-amber-50/10 rounded-lg border border-amber-900/20 backdrop-blur-sm">
      <h2 className="text-xl font-bold text-amber-100 mb-4 font-medieval">
        Readers Also Track Characters In
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {related.map((series) => (
          <Link
            key={series.slug}
            href={`/${series.slug}`}
            className="group p-4 bg-gradient-to-br from-amber-900/30 to-amber-800/20 rounded-lg border border-amber-700/30 hover:border-amber-600/50 transition-all hover:shadow-lg hover:shadow-amber-900/20"
          >
            <h3 className="font-semibold text-amber-100 group-hover:text-amber-50 transition-colors">
              {series.title}
            </h3>
            <p className="text-sm text-amber-200/70 mt-1">
              {series.reason}
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
}