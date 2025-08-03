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
      <body className="min-h-screen">
        <div className="relative min-h-screen">
          {/* Ambient lighting effects */}
          <div className="fixed inset-0 pointer-events-none">
            <div className="absolute top-0 left-1/4 w-96 h-96 bg-orange-600/10 rounded-full blur-3xl animate-pulse" />
            <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-amber-600/10 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '2s' }} />
          </div>
          
          {/* Hanging Tavern Sign Header */}
          <header className="relative z-20">
            <div className="flex justify-center pt-8 pb-4">
              <Link href="/" className="block">
                <div className="hanging-sign relative">
                  {/* Sign chains */}
                  <div className="absolute -top-8 left-8 w-1 h-8 bg-gradient-to-b from-amber-700 to-amber-900 rounded-full" />
                  <div className="absolute -top-8 right-8 w-1 h-8 bg-gradient-to-b from-amber-700 to-amber-900 rounded-full" />
                  
                  {/* Wooden sign board */}
                  <div className="relative bg-gradient-to-b from-amber-800 to-amber-900 px-12 py-6 rounded-lg shadow-2xl"
                       style={{
                         backgroundImage: `
                           linear-gradient(180deg, #8b6f47 0%, #654321 50%, #4a3420 100%),
                           url("data:image/svg+xml,%3Csvg width='100' height='100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='wood'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.02 0.1' result='noise' /%3E%3C/filter%3E%3Crect width='100' height='100' filter='url(%23wood)' opacity='0.4'/%3E%3C/svg%3E")
                         `,
                         border: '4px solid #3a1c0f',
                         boxShadow: `
                           inset 0 2px 4px rgba(255,255,255,0.1),
                           inset 0 -2px 4px rgba(0,0,0,0.5),
                           0 8px 16px rgba(0,0,0,0.8)
                         `
                       }}>
                    {/* Decorative corners */}
                    <div className="absolute top-2 left-2 w-6 h-6 border-l-2 border-t-2 border-amber-600/50 rounded-tl" />
                    <div className="absolute top-2 right-2 w-6 h-6 border-r-2 border-t-2 border-amber-600/50 rounded-tr" />
                    <div className="absolute bottom-2 left-2 w-6 h-6 border-l-2 border-b-2 border-amber-600/50 rounded-bl" />
                    <div className="absolute bottom-2 right-2 w-6 h-6 border-r-2 border-b-2 border-amber-600/50 rounded-br" />
                    
                    <h1 className="text-3xl md:text-4xl font-display tavern-sign-text text-center whitespace-nowrap">
                      Spoiler-Free
                    </h1>
                    <h1 className="text-3xl md:text-4xl font-display tavern-sign-text text-center whitespace-nowrap -mt-2">
                      Character Guide
                    </h1>
                  </div>
                  
                  {/* Subtitle plaque */}
                  <div className="absolute -bottom-6 left-1/2 transform -translate-x-1/2 bg-gradient-to-b from-amber-700 to-amber-800 px-4 py-1 rounded-md shadow-lg border border-amber-900 z-10">
                    <p className="text-xs text-amber-100 whitespace-nowrap">
                      Your trusted guide for tracking characters without spoilers
                    </p>
                  </div>
                </div>
              </Link>
            </div>
          </header>
          
          {/* Main content */}
          <main className="relative z-10 pb-20">
            {children}
          </main>
          
          {/* Footer */}
          <footer className="relative z-10 mt-auto">
            <div className="wooden-shelf h-20 px-8 flex items-center justify-center">
              <div className="text-center">
                <p className="text-amber-200/80 text-sm">© 2024 Spoiler-Free Character Guide</p>
                <p className="text-amber-200/60 text-xs mt-1">
                  Navigate your favorite series without fear of spoilers
                </p>
              </div>
            </div>
          </footer>
        </div>
      </body>
    </html>
  )
}
