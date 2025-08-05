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
- Hanging wooden tavern sign as the main header
- Parchment-style panels for content areas
- 3D book spines with visible thickness
- Wooden shelf textures
- Decorative candle in bottom-left footer
- Amber/gold color scheme throughout

## Key Features

### 1. Homepage (`app/page.tsx`)
- Hanging wooden sign with integrated 3-step process: "📚 Pick your book → 📖 Pick your chapter → ✨ See spoiler-free info"
- Search bar with ornate styling
- Bookshelf display showing all series as 3D books (2 per row on mobile, 4 on desktop)
- Books have realistic 3D perspective with visible spines on the left

### 2. Series Page (`app/[series]/page.tsx`)
- Lists all books in a series using the same 3D BookSpine component
- Amazon affiliate section with 2x2 grid collage of first 4 book covers
- Consistent book styling with homepage

### 3. Book Page (`app/[series]/[book]/page.tsx`)
- Chapter selection grid (consistent spacing with chapter page)
- Amazon affiliate link for specific book
- "No content yet" message if no chapter data exists

### 4. Chapter Page (`app/[series]/[book]/[chapter]/page.tsx`)
- Chapter recap section (collapsible with "Show/Hide Recap" button)
- Character lists divided into "In This Chapter" and "Previously Seen"
- Each character has individual parchment background
- Chapter selector moved to bottom for better UX

## Component Structure

### Core Components
1. **BookSpine** (`components/BookSpine.tsx`)
   - 3D book rendering with spine, cover, and shadow
   - Color assignment based on title length
   - Hover effects and decorative details

2. **CharacterCard** (`components/CharacterCard.tsx`)
   - Individual parchment panels for each character
   - Relationships formatted as "Protected by - Kaladin"
   - Shows name, aliases, role, description, relationships
   - First appearance and last update info

3. **ChapterRecap** (`components/ChapterRecap.tsx`)
   - Collapsible parchment panel
   - Button positioned for easy show/hide without mouse movement
   - Rich amber tones for readability

4. **ChapterSelector** (`components/ChapterSelector.tsx`)
   - Consistent spacing (gap-3) across all pages
   - Flexible layout with max-width constraint

5. **SearchBar** (`components/SearchBar.tsx`)
   - Ornate frame with decorative corners
   - Medieval font styling

## Styling Details

### Key CSS Classes (in `globals.css`)
- `.hanging-sign`: Hover-only animation (not constant)
- `.parchment-panel`: Light parchment background with wooden border
- `.book-3d-container`, `.book-3d`, `.book-spine`, `.book-cover`: 3D book effects
- `.tavern-sign-text`: Golden text with multiple shadows
- `.wooden-shelf`: Gradient wooden texture

### Color Palette
- Background: Dark brown (#1a1108)
- Parchment: #f4e8d0 to #e8dcc4
- Wood: #8b6f47, #654321, #4a3420
- Amber/Gold: #d4af37, various amber shades
- Text on parchment: amber-900 for contrast

## Data Structure
Books are stored in JSON files with:
- Character information revealed progressively by chapter
- Tiered character data (only showing what's known at each point)
- Optional chapter recaps
- Relationships between characters

## Recent Updates
1. Fixed hanging sign to only animate on hover
2. Moved chapter selector below content on chapter pages
3. Made recap section collapsible with better styling
4. Unified book styling across all pages with 3D effect
5. Added individual parchment backgrounds for character cards
6. Reformatted relationships for better readability
7. Created 2x2 book cover collage for series Amazon links
8. Integrated 3-step process into hanging sign
9. Added decorative candle to footer (bottom-left)
10. Improved mobile responsiveness (2 books per shelf)

## User Flow
1. User arrives at homepage → sees bookshelf of series
2. Clicks a series → sees all books in that series
3. Clicks a book → selects their current chapter
4. Views chapter page → sees only spoiler-free character info up to that point

## Important Notes
- Never regenerate existing character data (only add new)
- Maintain spoiler-free integrity at all times
- Amazon affiliate links use tag: `spoilerfree-20`
- Contact email: spoilerfreecharacterguide@gmail.com
- No copyright notice in footer (removed per request)

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
