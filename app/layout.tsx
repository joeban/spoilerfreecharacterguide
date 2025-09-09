import type { Metadata } from 'next'
import Link from 'next/link'
import './globals.css'
import { Analytics } from '@vercel/analytics/react'
import { SpeedInsights } from '@vercel/speed-insights/next'

export const metadata: Metadata = {
  metadataBase: new URL('https://spoilerfreecharacterguide.com'),
  title: {
    default: 'Spoiler-Free Character Guide - Track Book Characters Without Spoilers',
    template: '%s | Spoiler-Free Character Guide',
    absolute: 'Spoiler-Free Character Guide - Track Book Characters Without Spoilers'
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
  },
  icons: {
    icon: '/icon.png',
    shortcut: '/favicon.ico',
    apple: '/apple-icon.png',
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
                  <div className="absolute -top-8 left-8 w-1 h-8 rounded-full sign-chain" />
                  <div className="absolute -top-8 right-8 w-1 h-8 rounded-full sign-chain" />
                  
                  {/* Wooden sign board */}
                  <div className="px-12 py-6 rounded-lg shadow-2xl relative sign-board">
                    {/* Wood grain texture overlay */}
                    <div className="absolute inset-0 opacity-20 sign-texture" />
                    
                    {/* Metal corner bolts */}
                    <div className="absolute top-3 left-3 w-5 h-5 rounded-full sign-nail" />
                    <div className="absolute top-3 right-3 w-5 h-5 rounded-full sign-nail" />
                    <div className="absolute bottom-3 left-3 w-5 h-5 rounded-full sign-nail" />
                    <div className="absolute bottom-3 right-3 w-5 h-5 rounded-full sign-nail" />
                    
                    {/* Logo-style title */}
                    <div className="text-center relative">
                      <div className="relative inline-block">
                        <h1 className="font-display tavern-sign-text">
                          <span className="block text-5xl md:text-6xl lg:text-7xl font-black" style={{ letterSpacing: '0.01em', marginBottom: '0.35rem' }}>SPOILER-FREE</span>
                          <span className="block text-3xl md:text-4xl lg:text-5xl font-bold tracking-wider">CHARACTER GUIDE</span>
                        </h1>
                      </div>
                    </div>
                    
                    {/* Bold claim tagline - refined typography */}
                    <div className="mt-4 text-center">
                      <p className="text-base md:text-lg font-semibold tracking-wide text-amber-200" style={{ textShadow: '1px 1px 2px rgba(0,0,0,0.6)' }}>
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
          <footer className="relative z-20 mt-auto">
            <div className="wooden-shelf h-16 px-8 flex items-center justify-center">
              {/* Footer text */}
              <div className="text-center">
                <p className="text-amber-200/60 text-xs">
                  Navigate your favorite series without fear of spoilers
                </p>
                <p className="text-amber-200/60 text-xs mt-1">
                  Found a mistake? <a href="mailto:spoilerfreecharacterguide@gmail.com" 
                                     className="text-amber-400 hover:text-amber-300 underline transition-colors relative z-30">
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
