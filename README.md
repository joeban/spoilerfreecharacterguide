# Spoiler-Free Character Guide

A trusted resource for tracking characters in fantasy and science fiction novels without spoilers. Readers can select their current chapter and see only the character information revealed up to that point.

## Features

- 📚 **Spoiler-Free Design**: Character information is revealed progressively based on your reading progress
- 🎭 **Character Tracking**: Every named character is tracked with tiered information
- 📖 **Chapter Recaps**: Optional chapter summaries (hidden by default)
- 🎨 **Beautiful UI**: Bookshelf design with a leather-and-parchment aesthetic
- 🔒 **Safe Data Structure**: Built to prevent accidental spoilers in the data itself

## Getting Started

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the site.

### Building for Production

```bash
npm run build
npm start
```

## Adding Book Data

### Quick Start

1. Add your series to `data/index.json`
2. Create a folder `data/[series-slug]/`
3. Add book files `data/[series-slug]/[book-slug].json`
4. Follow the schema in `data/DATA_README.md`

### Example Structure

```json
{
  "meta": {
    "title": "The Way of Kings",
    "author": "Brandon Sanderson",
    "chapters": 75
  },
  "characters": {
    "kaladin": {
      "name": "Kaladin",
      "aliases": ["Stormblessed"],
      "tiers": {
        "1": {
          "appearsIn": 1,
          "description": "A young soldier with dark hair",
          "role": "Soldier"
        }
      }
    }
  },
  "recaps": {
    "1": "Kaladin leads his squad in battle..."
  }
}
```

## Important Rules

⚠️ **NEVER regenerate existing character data or recaps**. Only add new information. This ensures consistency for readers.

See `data/DATA_README.md` for detailed documentation on the data structure and rules.

## Tech Stack

- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Vercel** - Deployment

## Contributing

1. Read `data/DATA_README.md` before adding any book data
2. Test thoroughly to ensure no spoilers leak through
3. Follow the existing code style and structure

## License

MIT
