# Spoiler-Free Character Guide - Context for Claude

## Project Overview
**Website**: spoilerfreecharacterguide.com  
**GitHub**: https://github.com/joeban/spoilerfreecharacterguide/  
**Purpose**: A fantasy/sci-fi book companion website that allows readers to track characters without encountering spoilers. Users select their current chapter and only see character information revealed up to that point.

## Tech Stack
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Deployment**: Vercel
- **Data**: JSON files in `/data` directory

## Design Theme
The website has a **fantasy tavern/library aesthetic** with:
- Dark brown background (#1a1108) with ambient lighting effects
- Hanging wooden tavern sign as the main header with integrated 3-step process
- Parchment-style panels for content areas and better readability
- 3D book spines with visible thickness (spine on left, 30-degree rotation)
- Wooden shelf textures
- Decorative candle in bottom-left footer
- Amber/gold color scheme throughout
- High contrast text: light amber on dark backgrounds, dark amber on parchment

## Key Features

### 1. Homepage (`app/page.tsx`)
- Hanging wooden sign with integrated 3-step process: "📚 Pick your book → 📖 Pick your chapter → ✨ See spoiler-free info"
- Search bar with ornate styling (no tagline text)
- Bookshelf display showing all series as 3D books (2 per row on mobile, 4 on desktop)
- Books have realistic 3D perspective with visible spines on the left
- Decorative candle positioned bottom-left on the footer shelf

### 2. Series Page (`app/[series]/page.tsx`)
- Lists all books in a series using the same 3D BookSpine component
- Amazon affiliate section with 2x2 grid collage of first 4 book covers
- Consistent book styling with homepage
- Improved readability: titles use amber-100 with fire text shadow
- Purchase section wrapped in parchment panel

### 3. Book Page (`app/[series]/[book]/page.tsx`)
- Smart chapter stepper (replaces grid for books with many chapters)
- Two-step navigation: browse with +/- buttons, then click "Go to Chapter X"
- Amazon affiliate link for specific book
- Navigation link wrapped in parchment panel for contrast
- Headers use amber tones for better readability

### 4. Chapter Page (`app/[series]/[book]/[chapter]/page.tsx`)
- Chapter recap section (collapsible with "Show/Hide Recap" button at top center)
- Character lists divided into "In This Chapter" and "Previously Seen"
- Each character has individual parchment background
- Relationships formatted as "Protected by - Kaladin" with bullet points
- Chapter selector (stepper) moved to bottom for better UX

## Component Structure

### Core Components
1. **BookSpine** (`components/BookSpine.tsx`)
   - 3D book rendering with visible spine on left side
   - Spine positioned at `left: -35px` with `rotateY(-90deg)`
   - Shadow on right side for depth
   - Color assignment based on title length
   - Hover effects reduce rotation angle

2. **CharacterCard** (`components/CharacterCard.tsx`)
   - Individual parchment panels for each character
   - Relationships formatted as "Protected by - Kaladin" with capitalization
   - Shows name, aliases, role, description, relationships
   - Amber color scheme on parchment for readability
   - Hover effect scales card slightly

3. **ChapterRecap** (`components/ChapterRecap.tsx`)
   - Collapsible parchment panel
   - Hide button positioned at top center for easy toggle
   - Rich amber tones for readability
   - Darker parchment background when expanded

4. **ChapterSelector** (`components/ChapterSelector.tsx`)
   - Smart stepper design for compact interface
   - Two-step process: select chapter, then navigate
   - +/- buttons for browsing, "Go to Chapter X" button to confirm
   - Direct input with validation
   - Quick jump buttons: First, Middle (20+ chapters), Last
   - Shows current vs selected state

5. **SearchBar** (`components/SearchBar.tsx`)
   - Ornate frame with decorative corners
   - Medieval font styling
   - No tagline text below search

6. **Bookshelf** (`components/Bookshelf.tsx`)
   - Wooden frame with shelf textures
   - 2 books per row on mobile, 4 on desktop
   - No candles between shelves (removed for cleaner look)
   - Uses BookSpine component for consistent 3D books

## Styling Details

### Key CSS Classes (in `globals.css`)
- `.hanging-sign`: Hover-only animation (not constant swaying)
- `.parchment-panel`: Light parchment background (#f4e8d0 to #e8dcc4) with wooden border
- `.book-3d-container`, `.book-3d`, `.book-spine`, `.book-cover`: 3D book effects
- `.tavern-sign-text`: Golden text with multiple shadows
- `.wooden-shelf`: Gradient wooden texture
- `.text-shadow-fire`: Glowing text effect for headers

### Color Palette
- Background: Dark brown (#1a1108)
- Parchment: #f4e8d0 to #e8dcc4
- Wood: #8b6f47, #654321, #4a3420
- Amber/Gold: #d4af37, various amber shades
- Text on dark: amber-100, amber-200 (light ambers)
- Text on parchment: amber-900, amber-800, amber-700 (dark ambers)

### Readability Guidelines
- Always use light amber tones on dark backgrounds
- Always use dark amber tones on parchment backgrounds
- Wrap navigation elements in parchment panels when on dark backgrounds
- Use text-shadow-fire for main headers on dark backgrounds

## Data Structure
Books are stored in JSON files with:
- Character information revealed progressively by chapter
- Tiered character data (only showing what's known at each point)
- Optional chapter recaps
- Relationships between characters (stored as key-value pairs)

## Recent Updates (Latest First)
1. Improved readability across all pages with proper contrast
2. Added smart chapter stepper replacing overwhelming button grids
3. Fixed 3D books to have properly connected spines
4. Made book styling consistent across all pages
5. Integrated 3-step process into hanging sign
6. Reformed character relationships formatting
7. Added individual parchment backgrounds for characters
8. Created 2x2 book cover collage for series Amazon links
9. Fixed hanging sign to only animate on hover
10. Added decorative candle to footer (bottom-left)
11. Improved mobile responsiveness (2 books per shelf)
12. Moved chapter selector below content on chapter pages
13. Made recap section collapsible with better styling

## User Flow
1. User arrives at homepage → sees bookshelf of series
2. Clicks a series → sees all books in that series
3. Clicks a book → uses chapter stepper to select chapter
4. Views chapter page → sees only spoiler-free character info up to that point

## Important Notes
- Never regenerate existing character data (only add new)
- Maintain spoiler-free integrity at all times
- Amazon affiliate links use tag: `spoilerfree-20`
- Contact email: spoilerfreecharacterguide@gmail.com
- No copyright notice in footer
- Footer shows: navigation tagline + contact link for reporting mistakes

## Common Commands
```bash
npm run dev     # Development server
npm run build   # Production build
npm start       # Production server
```

## File Structure
```
/app
  /[series]
    /[book]
      /[chapter]
        page.tsx
      page.tsx
    page.tsx
  layout.tsx
  page.tsx
  globals.css
/components
  BookSpine.tsx
  CharacterCard.tsx
  ChapterRecap.tsx
  ChapterSelector.tsx
  SearchBar.tsx
  Bookshelf.tsx
/lib
  dataLoader.ts
  spoilerFilter.ts
  types.ts
/data
  index.json
  /[series-slug]
    [book-slug].json
```

## Known Issues & Solutions
- Build errors with partial JSX updates: Always provide complete component files
- Text contrast on dark backgrounds: Use amber-100/200 with text shadows
- 3D book disconnection: Spine at `left: -35px`, shadow at `right: -25px`
- Chapter selection overwhelming: Use stepper for 20+ chapter books
