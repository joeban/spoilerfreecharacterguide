# Data Structure Documentation

## ⚠️ CRITICAL RULES - READ BEFORE MODIFYING ANY DATA

### 🚫 NEVER REGENERATE RULE
Once character data or chapter recaps are created, they must NEVER be regenerated or overwritten. This ensures consistency for readers who may have already used the guide.

### ✅ ONLY APPEND/EXTEND
- You can ADD new character tiers (for later chapters)
- You can ADD new characters
- You can ADD new chapter recaps
- You CANNOT modify existing descriptions, recaps, or tier information

## Directory Structure

```
data/
├── index.json              # Registry of all series and books
├── DATA_README.md          # This file
└── [series-slug]/          # One folder per series
    └── [book-slug].json    # One file per book
```

## File Formats

### index.json
```json
{
  "series": {
    "series-slug": {
      "title": "Series Title",
      "author": "Author Name",
      "books": {
        "book-slug": {
          "title": "Book Title",
          "chapters": 50,
          "published": "2023"
        }
      }
    }
  }
}
```

### Book Data File ([book-slug].json)
```json
{
  "meta": {
    "title": "Book Title",
    "author": "Author Name",
    "chapters": 50,
    "createdAt": "2024-01-01T00:00:00Z",
    "schemaVersion": "1.0"
  },
  "characters": {
    "character-id": {
      "name": "Character Name",
      "aliases": ["Nickname1", "Title"],
      "tiers": {
        "1": {
          "appearsIn": 1,
          "description": "Initial description when first introduced",
          "role": "Initial Role"
        },
        "5": {
          "appearsIn": 5,
          "description": "Updated description with new info from chapters 2-5",
          "role": "Updated Role",
          "relationships": {
            "Other Character": "Relationship type"
          }
        }
      }
    }
  },
  "recaps": {
    "1": "What happens in chapter 1...",
    "2": "What happens in chapter 2..."
  }
}
```

## Guidelines for Adding Data

### Character IDs
- Use lowercase, hyphenated names: `kaladin-stormblessed`, `shallan-davar`
- Keep IDs consistent across books in a series

### Character Tiers
- Each tier represents information available at a specific chapter
- Tier numbers should match significant character development points
- Descriptions should be cumulative but spoiler-free
- Later tiers can expand on earlier info but shouldn't contradict it

### Writing Descriptions
- Write as if explaining to someone who just finished that chapter
- Include only information that has been explicitly revealed
- Avoid hints about future events
- Keep descriptions concise but informative

### Chapter Recaps
- Maximum 2-3 sentences per chapter
- Focus on major plot points without spoiling future events
- Written from the perspective of someone who just read that chapter

## Adding a New Series

1. Create a new folder: `data/[series-slug]/`
2. Add the series to `data/index.json`
3. Create book files: `data/[series-slug]/[book-slug].json`
4. Follow the schema exactly - TypeScript will validate the structure

## Common Mistakes to Avoid

1. **Don't use arrays for characters** - Always use objects with IDs
2. **Don't skip tier numbers** - They should be sequential within reason
3. **Don't reference future events** - Even subtle hints are spoilers
4. **Don't modify existing data** - Only add new tiers or characters
5. **Don't forget aliases** - Important for characters with multiple names

## Schema Versioning

Current version: 1.0

If the schema needs to change in the future:
1. Increment the version in new files
2. Maintain backwards compatibility
3. Document migration steps here
