# Data Schema Documentation

## Overview
This document defines the JSON structure for all data files in the Chapter Companion project.

## File Naming Conventions

- Series data: `data/books/[series-id]/series-info.json`
- Book data: `data/books/[series-id]/book-NNN.json` (NNN = 001, 002, etc.)
- Master list: `data/series.json`

## Schema Definitions

### 1. Master Series List (`series.json`)

```json
{
  "version": "1.0.0",
  "lastUpdated": "2024-01-01",
  "series": [
    {
      "id": "mistborn",
      "title": "Mistborn",
      "author": "Brandon Sanderson",
      "bookCount": 3,
      "status": "complete"
    }
  ]
}
```

**Field Descriptions:**
- `version`: Schema version for migration tracking
- `lastUpdated`: ISO date of last modification
- `series`: Array of series objects
- `id`: URL-safe identifier (lowercase, hyphens)
- `title`: Display title
- `author`: Primary author name
- `bookCount`: Number of books available
- `status`: "complete" | "ongoing" | "incomplete"

### 2. Series Information (`series-info.json`)

```json
{
  "version": "1.0.0",
  "id": "mistborn",
  "title": "Mistborn",
  "author": "Brandon Sanderson",
  "description": "Brief series description",
  "books": [
    {
      "number": 1,
      "title": "The Final Empire",
      "filename": "book-001.json",
      "chapterCount": 38,
      "status": "complete"
    }
  ],
  "metadata": {
    "genre": ["fantasy", "epic fantasy"],
    "firstPublished": 2006,
    "setting": "The Final Empire"
  }
}
```

### 3. Book Data (`book-NNN.json`)

```json
{
  "version": "1.0.0",
  "bookNumber": 1,
  "title": "The Final Empire",
  "author": "Brandon Sanderson",
  "totalChapters": 38,
  "lastUpdated": "2024-01-01",
  "chapters": [
    {
      "number": 1,
      "title": "The Survivor of Hathsin",
      "summary": "Brief spoiler-free summary (max 100 chars)",
      "setting": "Luthadel",
      "timeframe": "evening",
      "charactersIntroduced": ["Kelsier", "Dockson"],
      "charactersPresent": ["Kelsier", "Dockson"],
      "characters": {
        "Kelsier": {
          "background": "Role and context (max 150 chars)",
          "arc": "Story up to this chapter (max 150 chars)",
          "status": "active"
        }
      }
    }
  ]
}
```

**Field Descriptions:**

**Chapter Object:**
- `number`: Chapter number (integer)
- `title`: Chapter title
- `summary`: Spoiler-free summary (≤100 characters)
- `setting`: Primary location
- `timeframe`: When chapter occurs
- `charactersIntroduced`: Array of new character names
- `charactersPresent`: All characters in chapter
- `characters`: Character information object

**Character Object:**
- `background`: Who they are, their role (≤150 chars)
- `arc`: Their story up to this chapter (≤150 chars)
- `status`: "active" | "mentioned" | "deceased"

## Validation Rules

1. **Character Consistency**:
   - Character names must be consistent across chapters
   - Once introduced, characters must have entries in subsequent chapters where present

2. **Progressive Information**:
   - Character arcs can only reference events up to current chapter
   - No future spoilers in any field

3. **Size Limits**:
   - Summary: 100 characters max
   - Background: 150 characters max
   - Arc: 150 characters max
   - Book file: 500 lines max

4. **Required Fields**:
   - All fields shown are required unless marked optional
   - Empty arrays are valid (e.g., no characters introduced)

## Adding New Content

### Adding a Series
1. Add entry to `data/series.json`
2. Create folder `data/books/[series-id]/`
3. Create `series-info.json` in folder
4. Validate against schema

### Adding a Book
1. Create `book-NNN.json` with next number
2. Update `series-info.json` with book entry
3. Update `bookCount` in `series.json`
4. Validate all files

## Data Validation

Run validation before committing:
```bash
npm run validate-data
```

This checks:
- JSON syntax validity
- Schema compliance
- Character consistency
- Size limits
- Required fields

## Migration Strategy

When schema changes:
1. Update version in schema files
2. Create migration script in `scripts/migrations/`
3. Update this documentation
4. Run migration on all data files
5. Validate migrated data
