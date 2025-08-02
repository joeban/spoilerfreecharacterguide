import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'parchment': '#f4e8d0',
        'parchment-dark': '#e8dbb7',
        'ink': '#2c1810',
        'ink-light': '#4a3426',
        'leather': '#8b4513',
        'leather-dark': '#654321',
        'gold': '#d4af37',
        'gold-light': '#f4e4bc',
      },
      fontFamily: {
        'serif': ['Crimson Text', 'Georgia', 'serif'],
        'display': ['Cinzel', 'Georgia', 'serif'],
      },
      backgroundImage: {
        'parchment-texture': "url('/textures/parchment.jpg')",
        'leather-texture': "url('/textures/leather.jpg')",
      },
      animation: {
        'page-turn': 'pageTurn 0.6s ease-in-out',
        'fade-in': 'fadeIn 0.3s ease-in-out',
      },
      keyframes: {
        pageTurn: {
          '0%': { transform: 'rotateY(0deg)' },
          '100%': { transform: 'rotateY(-180deg)' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
export default config
