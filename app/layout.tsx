import type { Metadata } from 'next'
import Link from 'next/link'
import './globals.css'

export const metadata: Metadata = {
  title: 'Spoiler-Free Character Guide',
  description: 'A trusted resource for tracking characters in fantasy and science fiction novels without spoilers',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-parchment">
        <div className="relative min-h-screen">
          {/* Parchment texture overlay */}
          <div className="fixed inset-0 opacity-20 pointer-events-none"
               style={{
                 backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400' viewBox='0 0 400 400'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' /%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.4'/%3E%3C/svg%3E")`,
                 backgroundRepeat: 'repeat',
               }}
          />
          
          {/* Header */}
          <header className="relative z-10 bg-leather-dark text-parchment shadow-lg">
            <div className="container mx-auto px-4 py-6">
              <Link href="/" className="block group">
                <h1 className="text-3xl md:text-4xl font-display text-center gold-foil transition-all duration-300 group-hover:scale-105">
                  Spoiler-Free Character Guide
                </h1>
                <p className="text-center mt-2 text-parchment-dark text-sm group-hover:text-parchment transition-colors duration-300">
                  Your trusted companion for fantasy & science fiction journeys
                </p>
              </Link>
            </div>
          </header>
          
          {/* Main content */}
          <main className="relative z-10">
            {children}
          </main>
          
          {/* Footer */}
          <footer className="relative z-10 bg-ink-light text-parchment-dark mt-16 py-8">
            <div className="container mx-auto px-4 text-center text-sm">
              <p>© 2024 Spoiler-Free Character Guide</p>
              <p className="mt-2">
                Navigate your favorite series without fear of spoilers
              </p>
            </div>
          </footer>
        </div>
      </body>
    </html>
  )
}
