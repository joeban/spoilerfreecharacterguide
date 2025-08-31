import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      screens: {
        'tablet-max': {'min': '640px', 'max': '899px'},
        'desktop': '900px',
      },
      colors: {
        'parchment': '#f4e8d0',
        'parchment-dark': '#e8dcc4',
        'ink': '#2c1810',
        'ink-light': '#4a3426',
        'leather': '#8b4513',
        'leather-dark': '#654321',
        'gold': '#d4af37',
        'gold-light': '#f4e4bc',
        'wood-light': '#8b6f47',
        'wood': '#654321',
        'wood-dark': '#4a3420',
        'candle': '#ffbf00',
        'hearth': '#ff8c00',
      },
      fontFamily: {
        'serif': ['Crimson Text', 'Merriweather', 'Georgia', 'serif'],
        'display': ['Cinzel', 'MedievalSharp', 'serif'],
        'fantasy': ['MedievalSharp', 'serif'],
        'body': ['Merriweather', 'Georgia', 'serif'],
        'heading': ['Crimson Text', 'Georgia', 'serif'],
      },
      animation: {
        'gentle-swing': 'gentle-swing 4s ease-in-out infinite',
        'flicker': 'flicker 3s ease-in-out infinite',
        'magical-glow': 'magical-glow 2s ease-in-out infinite',
      },
      backgroundImage: {
        'wood-texture': "url('/textures/wood.jpg')",
        'parchment-texture': "url('/textures/parchment.jpg')",
      },
    },
  },
  plugins: [],
}
export default config
