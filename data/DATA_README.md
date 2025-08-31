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

#### Schema Version 2.0 (Current Format)
```json
{
  "meta": {
    "title": "Book Title",
    "author": "Author Name",
    "chapters": 50,
    "createdAt": "2024-01-01T00:00:00Z",
    "schemaVersion": "2.0"
  },
  "characters": {
    "character-id": {
      "name": "Character Name",
      "aliases": ["Nickname1", "Title"],
      "appearances": [1, 3, 5, 7, 8, 12, 15],
      "knowledge": {
        "1": {
          "revealedIn": 1,
          "description": "Initial description when first introduced",
          "role": "Initial Role",
          "relationships": {
            "Other Character": "Relationship type"
          }
        },
        "5": {
          "revealedIn": 5,
          "description": "Updated description with new info revealed in chapter 5",
          "role": "Updated Role",
          "relationships": {
            "Other Character": "Updated relationship",
            "New Character": "New relationship type"
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

#### Schema Version 1.0 (Legacy Format - Still Supported)
```json
{
  "meta": {
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
        }
      }
    }
  }
}
```

## Guidelines for Adding Data

### Character IDs
- Use lowercase, hyphenated names: `kaladin-stormblessed`, `shallan-davar`
- Keep IDs consistent across books in a series

### Schema Version 2.0 Format (Recommended for New Data)

#### Character Appearances vs Knowledge
- **Appearances Array**: List ALL chapters where the character physically appears or is mentioned
- **Knowledge Object**: Only add entries when significant NEW information is revealed about the character
- Example: A character might appear in chapters 1-10, but only have knowledge entries for chapters 1, 3, and 7

#### Character Knowledge Entries
- Each knowledge entry represents information available at a specific chapter
- Key `revealedIn` should match when that info is first revealed
- Descriptions should be cumulative but spoiler-free  
- Later entries can expand on earlier info but shouldn't contradict it
- Include `relationships` that are known at that point in the story

### Legacy Schema Version 1.0 Format

#### Character Tiers (Legacy)
- Each tier represents information available at a specific chapter
- `appearsIn` field indicates when character appears (single chapter)
- Tier numbers should match significant character development points
- Still supported for backward compatibility

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

### For Schema Version 2.0
1. **Don't use arrays for characters** - Always use objects with IDs
2. **Don't forget the appearances array** - List ALL chapters where character appears
3. **Don't add knowledge entries for every appearance** - Only when new info is revealed
4. **Don't reference future events** - Even subtle hints are spoilers
5. **Don't modify existing data** - Only add new knowledge entries or characters
6. **Don't forget aliases** - Important for characters with multiple names
7. **Ensure revealedIn values are in appearances** - Knowledge entries should correspond to actual appearances

### For Legacy Schema Version 1.0
1. **Don't skip tier numbers** - They should be sequential within reason
2. **Don't modify existing tiers** - Only add new tiers

## Schema Versioning

**Current version: 2.0** (Recommended for all new data)
**Legacy version: 1.0** (Still supported for existing data)

### Version History:
- **2.0**: Introduced `appearances` arrays and `knowledge` objects for better character tracking
- **1.0**: Original format with `tiers` and `appearsIn` fields

### Migration Guidelines:
- New series should use version 2.0
- Existing version 1.0 data remains supported
- Both versions work seamlessly with the website
- Version 2.0 provides more accurate "In This Chapter" listings
