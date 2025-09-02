import type { Metadata } from 'next'
import Link from 'next/link'
import './globals.css'
import { Analytics } from '@vercel/analytics/react'
import { SpeedInsights } from '@vercel/speed-insights/next'

export const metadata: Metadata = {
  metadataBase: new URL('https://spoilerfreecharacterguide.com'),
  title: {
    default: 'Spoiler-Free Character Guide - Track Book Characters Without Spoilers',
    template: '%s | Spoiler-Free Character Guide'
  },
  description: 'Track characters in fantasy & sci-fi books without spoilers. Choose your chapter and see only what you need to know. Covers Harry Potter, Percy Jackson, LOTR, Dune & more.',
  keywords: ['spoiler-free', 'character guide', 'book characters', 'fantasy books', 'sci-fi books', 'reading companion', 'no spoilers', 'chapter by chapter'],
  authors: [{ name: 'Spoiler-Free Character Guide' }],
  creator: 'Spoiler-Free Character Guide',
  publisher: 'Spoiler-Free Character Guide',
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://spoilerfreecharacterguide.com',
    siteName: 'Spoiler-Free Character Guide',
    title: 'Spoiler-Free Character Guide - Track Book Characters Without Spoilers',
    description: 'Track characters in fantasy & sci-fi books without spoilers. Choose your chapter and see only what you need to know.',
    images: [
      {
        url: '/og-image.jpg',
        width: 1200,
        height: 630,
        alt: 'Spoiler-Free Character Guide'
      }
    ]
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Spoiler-Free Character Guide',
    description: 'Track characters in fantasy & sci-fi books without spoilers',
    images: ['/og-image.jpg']
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  verification: {
    google: 'google-site-verification-code',
  },
  alternates: {
    canonical: 'https://spoilerfreecharacterguide.com'
  }
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="min-h-screen" suppressHydrationWarning>
        <div className="relative min-h-screen">
          {/* Ambient lighting effects */}
          <div className="fixed inset-0 pointer-events-none">
            <div className="absolute top-0 left-1/4 w-96 h-96 bg-orange-600/10 rounded-full blur-3xl animate-pulse" />
            <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-amber-600/10 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '2s' }} />
          </div>
          
          {/* Hanging Tavern Sign Header */}
          <header className="relative z-20">
            <div className="flex justify-center pt-8 pb-2">
              <Link href="/" className="block">
                <div className="hanging-sign relative">
                  {/* Sign chains */}
                  <div className="absolute -top-8 left-8 w-1 h-8 rounded-full" style={{background: `linear-gradient(to bottom, #8b6f47, #654321)`}} />
                  <div className="absolute -top-8 right-8 w-1 h-8 rounded-full" style={{background: `linear-gradient(to bottom, #8b6f47, #654321)`}} />
                  
                  {/* Wooden sign board */}
                  <div className="px-12 py-6 rounded-lg shadow-2xl relative"
                       style={{
                         background: `linear-gradient(180deg, 
                           #8b6f47 0%, 
                           #a0845c 15%, 
                           #6b5537 40%, 
                           #5a4530 60%, 
                           #4a3525 85%, 
                           #3a2818 100%)`,
                         boxShadow: `
                           inset 0 2px 4px rgba(255,255,255,0.1),
                           inset 0 -2px 8px rgba(0,0,0,0.4),
                           inset 2px 0 8px rgba(0,0,0,0.3),
                           inset -2px 0 8px rgba(0,0,0,0.3),
                           0 8px 32px rgba(0,0,0,0.8),
                           0 4px 16px rgba(0,0,0,0.6)`,
                         border: '2px solid',
                         borderColor: '#2a1f15',
                         position: 'relative',
                         overflow: 'hidden'
                       }}>
                    {/* Wood grain texture overlay */}
                    <div className="absolute inset-0 opacity-20" 
                         style={{
                           backgroundImage: `repeating-linear-gradient(
                             90deg,
                             transparent,
                             transparent 2px,
                             rgba(0,0,0,0.1) 2px,
                             rgba(0,0,0,0.1) 4px
                           ), repeating-linear-gradient(
                             180deg,
                             transparent,
                             transparent 10px,
                             rgba(0,0,0,0.05) 10px,
                             rgba(0,0,0,0.05) 11px
                           )`,
                           mixBlendMode: 'multiply'
                         }} />
                    
                    {/* Metal corner bolts */}
                    <div className="absolute top-3 left-3 w-5 h-5 rounded-full" 
                         style={{
                           background: 'radial-gradient(circle at 30% 30%, #6b5d4f 0%, #4a3f32 40%, #2d2520 100%)',
                           boxShadow: 'inset -2px -2px 4px rgba(0,0,0,0.8), 0 2px 4px rgba(0,0,0,0.5)',
                           border: '1px solid #1a1511'
                         }} />
                    <div className="absolute top-3 right-3 w-5 h-5 rounded-full" 
                         style={{
                           background: 'radial-gradient(circle at 30% 30%, #6b5d4f 0%, #4a3f32 40%, #2d2520 100%)',
                           boxShadow: 'inset -2px -2px 4px rgba(0,0,0,0.8), 0 2px 4px rgba(0,0,0,0.5)',
                           border: '1px solid #1a1511'
                         }} />
                    <div className="absolute bottom-3 left-3 w-5 h-5 rounded-full" 
                         style={{
                           background: 'radial-gradient(circle at 30% 30%, #6b5d4f 0%, #4a3f32 40%, #2d2520 100%)',
                           boxShadow: 'inset -2px -2px 4px rgba(0,0,0,0.8), 0 2px 4px rgba(0,0,0,0.5)',
                           border: '1px solid #1a1511'
                         }} />
                    <div className="absolute bottom-3 right-3 w-5 h-5 rounded-full" 
                         style={{
                           background: 'radial-gradient(circle at 30% 30%, #6b5d4f 0%, #4a3f32 40%, #2d2520 100%)',
                           boxShadow: 'inset -2px -2px 4px rgba(0,0,0,0.8), 0 2px 4px rgba(0,0,0,0.5)',
                           border: '1px solid #1a1511'
                         }} />
                    
                    {/* Logo-style title with medieval flourishes */}
                    <div className="text-center relative">
                      <div className="relative inline-block">
                        {/* Ornamental brackets around the title */}
                        <div className="absolute -left-8 top-1/2 -translate-y-1/2 text-amber-600/70 text-2xl font-display">⟬</div>
                        <div className="absolute -right-8 top-1/2 -translate-y-1/2 text-amber-600/70 text-2xl font-display">⟭</div>
                        
                        <h1 className="text-4xl md:text-5xl font-display tavern-sign-text tracking-wide">
                          <span className="block text-5xl md:text-6xl font-black" style={{ letterSpacing: '0.02em', textShadow: '2px 2px 4px rgba(0,0,0,0.8), 0 0 20px rgba(212,175,55,0.3)' }}>SPOILER-FREE</span>
                          <span className="block text-3xl md:text-4xl font-black mt-1 tracking-widest" style={{ textShadow: '2px 2px 4px rgba(0,0,0,0.8), 0 0 20px rgba(212,175,55,0.3)' }}>CHARACTER GUIDE</span>
                        </h1>
                      </div>
                    </div>
                    
                    {/* Bold claim tagline */}
                    <div className="mt-6 text-center text-amber-100">
                      <p className="text-lg md:text-xl font-bold tracking-wide">
                        Every Named Character. Every Book. Zero Spoilers.
                      </p>
                    </div>
                  </div>
                  
                </div>
              </Link>
            </div>
          </header>
          
          {/* Main content */}
          <main className="relative z-10 pb-12">
            {children}
          </main>
          
          {/* Footer */}
          <footer className="relative z-10 mt-auto">
            <div className="wooden-shelf h-16 px-8 flex items-center justify-center">
              {/* Footer text */}
              <div className="text-center">
                <p className="text-amber-200/60 text-xs">
                  Navigate your favorite series without fear of spoilers
                </p>
                <p className="text-amber-200/60 text-xs mt-1">
                  Found a mistake? <a href="mailto:spoilerfreecharacterguide@gmail.com" 
                                     className="text-amber-400 hover:text-amber-300 underline transition-colors">
                    Let us know
                  </a>
                </p>
              </div>
            </div>
          </footer>
        </div>
        <Analytics />
        <SpeedInsights />
      </body>
    </html>
  )
}
