# Spoiler-Free Character Guide - Context for Claude

## Project Overview
**Website**: spoilerfreecharacterguide.com  
**GitHub**: https://github.com/joeban/spoilerfreecharacterguide/  
**Purpose**: A fantasy/sci-fi book companion website that allows readers to track characters without encountering spoilers. Users select their current chapter and only see character information revealed up to that point.

## Content Strategy
**Priority System**: Series are prioritized for data completion based on estimated search traffic potential:
1. **Tier 1 (Highest Traffic)**: Popular ongoing series with active readership
   - Fourth Wing / Iron Flame (recent bestsellers, high search volume)
   - Throne of Glass (Sarah J. Maas - massive fanbase)
   - A Court of Thorns and Roses (Sarah J. Maas - extremely popular)
   - Hunger Games (evergreen popularity, new content releases)
2. **Tier 2 (Strong Traffic)**: Established series with consistent readership
   - Percy Jackson (Rick Riordan - continuous new readers)
   - Shadow and Bone / Grishaverse (Netflix adaptation boost)
   - Mistborn / Cosmere (Brandon Sanderson - dedicated fanbase)
   - Wheel of Time (Amazon Prime series)
3. **Tier 3 (Steady Traffic)**: Classic series with stable search volume
   - Harry Potter (already complete - evergreen traffic)
   - Lord of the Rings (already complete - classic status)
   - Dune (already complete - movie adaptations)
   - Chronicles of Narnia (timeless classic)
4. **Tier 4 (Niche Traffic)**: Specialized audiences
   - Stormlight Archive (complex, dedicated readers)
   - The Expanse (sci-fi audience)
   - Discworld (specific fanbase)
   - Foundation (classic sci-fi)

**Implementation Order**: Complete series in order of traffic potential, focusing on:
- Series with recent adaptations or new releases
- Series with active online communities
- Series commonly read by book clubs
- Series with complex character rosters that benefit most from our guide

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
- Chapter selector at both top and bottom for easy navigation
- Chapter recap section (collapsible with "Show/Hide Recap" button at top center)
- Character lists divided into "In This Chapter" and "Previously Seen"
- Each character has individual parchment background
- Character cards show:
  - Whether character appears in current chapter
  - Full appearance history (e.g., "Appears in chapters: 1-3, 5, 7-10")
  - Relationships formatted as "Protected by - Kaladin" with bullet points
- Amazon purchase section below character lists with book cover and affiliate link
- "As an Amazon Associate, we earn from qualifying purchases" disclaimer

## Data Structure (v2.0 - UPDATED)

### Overview
The data structure now separates **character appearances** (which chapters they're in) from **character knowledge** (what we learn about them). This provides accurate "In This Chapter" listings.

### Character Structure
```typescript
interface Character {
  name: string;
  aliases?: string[];
  appearances: number[];  // All chapters where character actually appears
  knowledge: Record<string, CharacterKnowledge>;  // Information revealed by chapter
}

interface CharacterKnowledge {
  revealedIn: number;  // Chapter where this info is revealed
  description: string;
  role: string;
  relationships?: Record<string, string>;
}
```

### Migration Status
- **Schema Version 1.0**: Legacy format using `tiers` with `appearsIn`
- **Schema Version 2.0**: New format with `appearances` array and `knowledge` object
- The site supports both formats for backward compatibility
- Migration helper available in `lib/migrationHelper.ts`

### Example Book Data (v2.0)
```json
{
  "meta": {
    "title": "The Philosopher's Stone",
    "author": "J.K. Rowling",
    "chapters": 17,
    "schemaVersion": "2.0"
  },
  "characters": {
    "harry-potter": {
      "name": "Harry Potter",
      "aliases": ["The Boy Who Lived"],
      "appearances": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
      "knowledge": {
        "1": {
          "revealedIn": 1,
          "description": "A baby with a lightning bolt scar...",
          "role": "Orphaned infant",
          "relationships": {...}
        },
        "2": {
          "revealedIn": 2,
          "description": "Lives under the stairs, has green eyes...",
          "role": "The Dursleys' nephew",
          "relationships": {...}
        }
      }
    }
  },
  "recaps": {...}
}
```

## Component Structure

### Core Components
1. **BookSpine** (`components/BookSpine.tsx`)
   - 3D book rendering with visible spine on left side
   - Color assignment based on title length
   - Hover effects reduce rotation angle

2. **CharacterCard** (`components/CharacterCard.tsx`)
   - Shows if character appears in current chapter
   - Displays full appearance history (formatted as ranges)
   - Individual parchment panels for each character
   - Relationships formatted with proper capitalization

3. **ChapterRecap** (`components/ChapterRecap.tsx`)
   - Collapsible parchment panel
   - Hide button positioned at top center

4. **ChapterSelector** (`components/ChapterSelector.tsx`)
   - Smart stepper design for compact interface
   - Two-step process: select chapter, then navigate

5. **SearchBar** (`components/SearchBar.tsx`)
   - Ornate frame with decorative corners
   - Medieval font styling

6. **Bookshelf** (`components/Bookshelf.tsx`)
   - Wooden frame with shelf textures
   - Responsive layout: 2 books (mobile), 3 books (tablet), 4 books (desktop), 5 books (large screens)

7. **CharacterList** (`components/CharacterList.tsx`)
   - Organizes characters into "In This Chapter" and "Previously Seen" sections
   - Handles character filtering and display logic

## Updated Type System

### Key Types (lib/types.ts)
- `Character` - New structure with `appearances` array
- `LegacyCharacter` - Old structure for backward compatibility
- `CharacterKnowledge` - Renamed from `CharacterTier`
- `ProcessedCharacter` - Enhanced with appearance tracking
- Helper functions: `isNewCharacterFormat()`, `isLegacyCharacterFormat()`

### Spoiler Filter (lib/spoilerFilter.ts)
- Handles both new and legacy formats seamlessly
- `getCharactersForChapter()` now accurately shows who appears in each chapter
- `characterAppearsInChapter()` checks the appearances array
- `getCharacterKnowledge()` returns the latest knowledge available at current chapter

### Migration Helper (lib/migrationHelper.ts)
- `migrateLegacyCharacter()` - Converts old format to new
- `migrateBookData()` - Migrates entire book file
- `generateMigrationReport()` - Shows what needs manual correction

## Data Entry Guidelines

### Chapter Recaps (MANDATORY)
- **EVERY SINGLE CHAPTER must have a recap** - no exceptions
- Each recap should be 2-4 sentences summarizing key plot points without spoilers
- Recaps are stored in the `recaps` object with chapter numbers as keys
- Example: `"1": "Harry Potter receives his Hogwarts letter..."`
- Missing recaps will break the user experience

### Character Coverage (MANDATORY) 
- **EVERY NAMED CHARACTER must have an entry** - no exceptions
- This includes major characters, minor characters, and even briefly mentioned characters
- Characters with single mentions should still have entries documenting their role
- Missing character entries reduce the guide's completeness and usefulness
- When in doubt, include the character rather than omit them

### Adding New Characters
1. List ALL chapters where the character appears in `appearances`
2. Add `knowledge` entries only when significant new information is revealed
3. Each knowledge entry's `revealedIn` should also be in `appearances`
4. Include ALL named characters, regardless of importance or screen time

### Character Appearances vs Knowledge
- **Appearances**: Every chapter where the character is present
- **Knowledge**: Only chapters where we learn something new
- Example: Harry appears in chapters 1-17, but knowledge updates might only be in chapters 1, 2, 4, 7, etc.

### Quality Checks
- **CRITICAL**: Verify ALL chapters (1 through meta.chapters) have recaps
- **CRITICAL**: Verify ALL named characters are included, no matter how minor
- Verify `appearances` array is complete and accurate
- Ensure `revealedIn` values are subset of `appearances`
- Check that descriptions are spoiler-free for their chapter
- Relationships should reflect what's known at that point
- Review text for any unnamed references that could become character entries

## Recent Updates (Latest First)
1. **MAJOR: Separated character appearances from knowledge updates** (v2.0)
2. Added character appearance tracking on cards
3. Improved "In This Chapter" accuracy
4. Added backward compatibility for legacy data
5. Created migration helpers for data conversion
6. Enhanced CharacterCard to show appearance ranges
7. Updated type system with proper type guards
8. Improved readability across all pages with proper contrast
9. Added smart chapter stepper replacing overwhelming button grids
10. Fixed 3D books to have properly connected spines

## Development Workflow

### Terminal-Based Development with Claude Code
All development is done through the terminal using Claude Code:
- **Development server**: `npm run dev` runs on http://localhost:3000
- **Git workflow**: Make changes → test locally → `git add` → `git commit` → `git push`
- **Testing**: Always verify changes at localhost:3000 before committing
- **Deployment**: Automatic via Vercel on push to main branch

### Common Commands
```bash
# Development
npm run dev     # Start dev server at http://localhost:3000
npm run build   # Production build
npm start       # Production server

# Git workflow
git status                          # Check what's changed
git add .                          # Stage all changes
git add data/series/book.json     # Stage specific file
git commit -m "feat: description"  # Commit with descriptive message
git push                           # Push to GitHub → triggers Vercel deploy

# Verification commands
python3 -c "import json; data = json.load(open('data/series/book.json')); print(f'Characters: {len(data[\"characters\"])}')"  # Count characters
python3 -c "import json; json.load(open('data/series/book.json')); print('✅ Valid JSON')"  # Validate JSON
```

### Best Practices for Large Character Data Projects

#### 1. Use Task Tool for Large Expansions
For adding 50+ characters, use the Task tool with general-purpose agent:
```
Phase 1: Main characters (20-30 chars)
Phase 2: Supporting characters by faction (30-40 chars)
Phase 3: Minor characters by location (20-30 chars)
Phase 4: Historical/referenced characters (10-20 chars)
```

#### 2. Systematic Expansion Process
```bash
# 1. Check current state
python3 -c "import json; ..."

# 2. Use Task tool for expansion
# 3. Verify new count
python3 -c "import json; ..."

# 4. Commit with descriptive message
git add data/series/book.json
git commit -m "feat: expand Book Name characters (22→307)"
git push
```

#### 3. Series-Wide Strategy
- Complete one book fully before moving to next
- Use TodoWrite tool to track progress across books
- Verify JSON validity after each major addition
- Commit after each book completion

#### 4. Commit Message Format
```
feat: expand [Book] characters ([old count]→[new count])

Expanded character coverage:
- Phase 1: [description] ([count] characters)
- Phase 2: [description] ([count] characters)
...

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
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
  /search
    page.tsx
  layout.tsx
  page.tsx
  globals.css
/components
  BookSpine.tsx
  Bookshelf.tsx
  CharacterCard.tsx
  CharacterList.tsx
  ChapterRecap.tsx
  ChapterSelector.tsx
  SearchBar.tsx
/lib
  dataLoader.ts
  spoilerFilter.ts
  types.ts
  migrationHelper.ts
/data
  index.json
  /[series-slug]
    [book-slug].json  # Can be v1.0 or v2.0 format
```

## Migration Process

### For Existing Books (v1.0 → v2.0)
1. Run migration helper to convert structure
2. Review auto-generated `appearances` arrays
3. Manually add missing chapter appearances
4. Verify all `revealedIn` values are accurate
5. Update `schemaVersion` to "2.0"

### For New Books
1. Start with v2.0 structure
2. List all character appearances upfront
3. Add knowledge entries as you document each chapter
4. Set `schemaVersion` to "2.0"

## Known Issues & Solutions
- **Inaccurate "In This Chapter"**: Update to v2.0 format with complete `appearances` arrays
- **Legacy data compatibility**: Site handles both formats, but v2.0 is more accurate
- **Missing character appearances**: Review each chapter to ensure all present characters are listed

## Important Notes
- Never regenerate existing character data (only add new)
- Maintain spoiler-free integrity at all times
- `appearances` must be complete for accurate chapter displays
- `knowledge` entries should be cumulative but spoiler-free
- Amazon affiliate links use tag: `spoilerfree-20`
- Contact email: spoilerfreecharacterguide@gmail.com

## Data Completion Status

### Coverage Levels
- **🟢 Comprehensive**: Every named character included (100+ characters typical)
- **🟡 Standard**: Main and supporting characters (50-100 characters)
- **🟠 Basic**: Main characters only (20-50 characters)
- **🔴 Minimal**: Key characters only (<20 characters)

### Fully Complete Series (with coverage level)
- ✅ **Harry Potter** (7 books)
  - 🟡 Philosopher's Stone: 55 characters, all recaps, v2.0
  - 🟡 Chamber of Secrets: 76 characters, all recaps, v2.0
  - 🟡 Prisoner of Azkaban: 53 characters, all recaps, v2.0
  - 🟡 Goblet of Fire: 71 characters, all recaps, v2.0
  - 🟢 Order of Phoenix: 105 characters, all recaps, v2.0
  - 🟠 Half-Blood Prince: 48 characters, all recaps, v2.0
  - 🟡 Deathly Hallows: 75 characters, all recaps, v2.0

- ✅ **Percy Jackson** (5 books)
  - 🟡 Lightning Thief: 63 characters, all recaps, v2.0
  - 🟡 Sea of Monsters: 63 characters, all recaps, v2.0
  - 🟡 Titan's Curse: 67 characters, all recaps, v2.0
  - 🟡 Battle of Labyrinth: 64 characters, all recaps, v2.0
  - 🟡 Last Olympian: 61 characters, all recaps, v2.0

- ✅ **Lord of the Rings/Hobbit** (4 books)
  - 🟡 The Hobbit: 50+ characters, all recaps, v2.0
  - 🟡 Fellowship: 80+ characters, all recaps, v2.0
  - 🟡 Two Towers: 70+ characters, all recaps, v2.0
  - 🟡 Return of King: 75+ characters, all recaps, v2.0

- ✅ **Dune** (6 books)
  - 🟡 Dune: 90+ characters, all recaps, v2.0
  - 🟡 Dune Messiah: 50+ characters, all recaps, v2.0
  - 🟡 Children of Dune: 60+ characters, all recaps, v2.0
  - 🟡 God Emperor: 40+ characters, all recaps, v2.0
  - 🟡 Heretics: 50+ characters, all recaps, v2.0
  - 🟡 Chapterhouse: 55+ characters, all recaps, v2.0

- ✅ **A Song of Ice and Fire** (5 books)
  - 🟢 Game of Thrones: 303 characters, all recaps, v2.0
  - 🟡 Clash of Kings: 80+ characters, all recaps, v2.0
  - 🟡 Storm of Swords: 90+ characters, all recaps, v2.0
  - 🟡 Feast for Crows: 70+ characters, all recaps, v2.0
  - 🟡 Dance with Dragons: 85+ characters, all recaps, v2.0

- ✅ **The Witcher** (8 books)
  - 🟡 Last Wish: 45+ characters, all recaps, v2.0
  - 🟡 Sword of Destiny: 50+ characters, all recaps, v2.0
  - 🟡 Blood of Elves: 55+ characters, all recaps, v2.0
  - 🟡 Time of Contempt: 60+ characters, all recaps, v2.0
  - 🟡 Baptism of Fire: 65+ characters, all recaps, v2.0
  - 🟡 Tower of Swallows: 70+ characters, all recaps, v2.0
  - 🟡 Lady of the Lake: 80+ characters, all recaps, v2.0
  - 🟡 Season of Storms: 45+ characters, all recaps, v2.0

- ✅ **Fourth Wing** (2 books)
  - 🟡 Fourth Wing: 85+ characters, all recaps, v2.0
  - 🟡 Iron Flame: 95+ characters, all recaps, v2.0

- ✅ **Wheel of Time** (5 of 14 books)
  - 🟡 Eye of the World: 90+ characters, all recaps, v2.0
  - 🟡 Great Hunt: 85+ characters, all recaps, v2.0
  - 🟡 Dragon Reborn: 80+ characters, all recaps, v2.0
  - 🟡 Shadow Rising: 95+ characters, all recaps, v2.0
  - 🟡 Fires of Heaven: 90+ characters, all recaps, v2.0

### Partially Complete Series
- ⚠️ **Stormlight Archive** (1 of 4 books)
  - 🟠 Way of Kings: 30+ characters, all recaps, v2.0

### Not Started (Configured but no data)
- ❌ **Mistborn/Cosmere** (0 of 7 books)
- ❌ **Throne of Glass** (0 of 8 books)
- ❌ **A Court of Thorns and Roses** (0 of 5 books)
- ❌ **Hunger Games** (0 of 4 books)
- ❌ **Shadow and Bone/Grishaverse** (0 of 5 books)
- ❌ **Chronicles of Narnia** (0 of 7 books)
- ❌ **The Expanse** (0 of 9 books)
- ❌ **Foundation** (0 of 5 books)
- ❌ **Kingkiller Chronicle** (0 of 2 books)
- ❌ **Wings of Fire** (0 of 5 books)
- ❌ **Discworld** (0 of 8 books configured)

### Books Needing Character Expansion
Priority books that need upgrading to Comprehensive (🟢) coverage:
1. **Harry Potter** series - Books 1-4, 6-7 need 50-200 more characters each for true comprehensive coverage
2. **A Song of Ice and Fire** (books 2-5) - Need 200+ more characters each to match GoT's coverage
3. **Percy Jackson** series - Each book needs 50+ additional minor characters
4. **Lord of the Rings** trilogy - Missing many minor characters from each book
5. **Wheel of Time** (books 1-5) - Each needs 100+ additional characters

### Next Priority for NEW Series (Based on Traffic Strategy)
1. **Throne of Glass** - Sarah J. Maas series, massive fanbase
2. **A Court of Thorns and Roses** - Sarah J. Maas, extremely popular
3. **Hunger Games** - Evergreen popularity, new prequel
4. **Shadow and Bone/Grishaverse** - Netflix adaptation boost

## Project Statistics (as of latest update)
- **Total Series Configured**: 20 series
- **Fully Complete Series**: 8 series
- **Total Books with Data**: 30+ books
- **Total Characters**: 2,000+ unique characters across all series
- **All complete books have**: Full chapter recaps, comprehensive character coverage, v2.0 schema
- **Development Environment**: Claude Code terminal-based workflow
- **Testing**: http://localhost:3000
- **Production**: https://spoilerfreecharacterguide.com (auto-deployed via Vercel)
- **Analytics**: Vercel Analytics + Speed Insights enabled
