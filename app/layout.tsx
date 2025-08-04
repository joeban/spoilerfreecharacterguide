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
                  
                  {/* 3-step explainer instead of subtitle */}
                  <div className="absolute -bottom-12 left-1/2 transform -translate-x-1/2 z-10 w-full max-w-lg px-4">
                    <div className="flex flex-col sm:flex-row items-center justify-center gap-2 text-amber-100 text-sm">
                      <span className="bg-amber-800/80 px-3 py-1 rounded-md shadow-lg whitespace-nowrap border border-amber-700/50">
                        📚 Pick your book
                      </span>
                      <span className="text-amber-400 hidden sm:inline">→</span>
                      <span className="text-amber-400 sm:hidden">↓</span>
                      <span className="bg-amber-800/80 px-3 py-1 rounded-md shadow-lg whitespace-nowrap border border-amber-700/50">
                        📖 Pick your chapter
                      </span>
                      <span className="text-amber-400 hidden sm:inline">→</span>
                      <span className="text-amber-400 sm:hidden">↓</span>
                      <span className="bg-amber-800/80 px-3 py-1 rounded-md shadow-lg whitespace-nowrap border border-amber-700/50">
                        ✨ See spoiler-free info
                      </span>
                    </div>
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
            <div className="wooden-shelf h-20 px-8 flex items-center justify-center relative">
              {/* Candle on the left side of the footer */}
              <div className="absolute left-8 bottom-full mb-1">
                <div className="candle-glow relative">
                  {/* Flame */}
                  <div className="absolute -top-3 left-1/2 transform -translate-x-1/2 w-3 h-5">
                    <div className="absolute inset-0 bg-gradient-to-t from-orange-400 via-yellow-300 to-white 
                                  rounded-full animate-flicker"
                         style={{
                           filter: 'blur(1px)',
                           boxShadow: '0 0 15px rgba(255,191,0,0.8), 0 0 30px rgba(255,140,0,0.6)'
                         }} />
                  </div>
                  
                  {/* Candle body with integrated drips */}
                  <div className="relative">
                    <div className="w-8 h-12 bg-gradient-to-b from-amber-100 to-amber-200 rounded-t-sm relative overflow-visible"
                         style={{
                           boxShadow: 'inset -2px 0 4px rgba(0,0,0,0.2)'
                         }}>
                      {/* Wax drips as part of the candle */}
                      <svg className="absolute inset-0 w-full h-full overflow-visible" style={{ filter: 'drop-shadow(1px 1px 2px rgba(0,0,0,0.3))' }}>
                        {/* Right drip */}
                        <path d="M 32 8 Q 35 8 36 15 T 34 25" 
                              fill="url(#wax-gradient)" 
                              stroke="none" />
                        {/* Left drip */}
                        <path d="M 0 12 Q -3 12 -2 20 T 0 28" 
                              fill="url(#wax-gradient)" 
                              stroke="none" />
                        {/* Small center drip */}
                        <path d="M 20 20 Q 20 20 21 26 T 20 30" 
                              fill="url(#wax-gradient)" 
                              stroke="none" />
                        <defs>
                          <linearGradient id="wax-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" stopColor="#fef3c7" />
                            <stop offset="100%" stopColor="#fde68a" />
                          </linearGradient>
                        </defs>
                      </svg>
                    </div>
                    
                    {/* Candle holder */}
                    <div className="w-10 h-2 bg-gradient-to-b from-amber-800 to-amber-900 
                                  rounded-b-lg -mt-0.5 mx-auto"
                         style={{
                           boxShadow: '0 2px 4px rgba(0,0,0,0.4)'
                         }} />
                  </div>
                  
                  {/* Glow on the shelf */}
                  <div className="absolute -bottom-2 left-1/2 transform -translate-x-1/2 
                                w-20 h-4 bg-gradient-radial from-amber-400/30 to-transparent 
                                rounded-full blur-lg" />
                </div>
              </div>
              
              {/* Footer text */}
              <div className="text-center">
                <p className="text-amber-200/60 text-xs">
                  Navigate your favorite series without fear of spoilers
                </p>
                <p className="text-amber-200/60 text-xs mt-2">
                  Found a mistake? <a href="mailto:spoilerfreecharacterguide@gmail.com" 
                                     className="text-amber-400 hover:text-amber-300 underline transition-colors">
                    Let us know
                  </a>
                </p>
              </div>
            </div>
          </footer>
        </div>
      </body>
    </html>
  )
}
