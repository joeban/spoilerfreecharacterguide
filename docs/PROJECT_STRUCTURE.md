# Chapter Companion - AI-Optimized Project Structure

## Core Design Principles

1. **Chunk-Based Architecture**: Every file should be small enough for an AI to process in a single context
2. **Self-Documenting**: Each file contains its own documentation header
3. **Progressive Enhancement**: Start with core functionality, add features incrementally
4. **Version Control Friendly**: Small, atomic changes that are easy to track
5. **Fail-Safe Design**: Graceful degradation if any component fails

## Directory Structure

```
chapter-companion/
├── docs/                      # Documentation
│   ├── PROJECT_STRUCTURE.md   # This file
│   ├── DEVELOPMENT_LOG.md     # Track all changes
│   ├── DATA_SCHEMA.md         # JSON structure documentation
│   └── CONTRIBUTING.md        # How to add content
│
├── src/                       # Source code
│   ├── index.html            # Main HTML (minimal, just structure)
│   ├── css/
│   │   ├── base.css         # Reset and base styles
│   │   ├── layout.css       # Layout and grid
│   │   ├── components.css   # Reusable components
│   │   ├── bookshelf.css    # Bookshelf specific styles
│   │   └── theme.css        # Colors and theming
│   │
│   ├── js/
│   │   ├── config.js        # Configuration and constants
│   │   ├── state.js         # State management
│   │   ├── data-loader.js   # Data fetching logic
│   │   ├── views/
│   │   │   ├── series-view.js    # Series selection
│   │   │   ├── book-view.js      # Book selection
│   │   │   └── chapter-view.js   # Chapter/character display
│   │   ├── components/
│   │   │   ├── book-spine.js     # Book spine component
│   │   │   ├── character-card.js # Character card component
│   │   │   └── spoiler-toggle.js # Spoiler component
│   │   └── app.js           # Main application entry
│   │
│   └── templates/            # HTML templates for components
│       ├── book-spine.html
│       ├── character-card.html
│       └── chapter-selector.html
│
├── data/                     # Content data
│   ├── README.md            # Data structure guide
│   ├── series.json          # Master series list
│   ├── schema/              # JSON schemas for validation
│   │   ├── series.schema.json
│   │   └── book.schema.json
│   └── books/               # Book data organized by series
│       ├── mistborn/
│       │   ├── series-info.json
│       │   ├── book-001.json
│       │   ├── book-002.json
│       │   └── book-003.json
│       └── [series-id]/
│           └── book-NNN.json
│
├── scripts/                  # Development scripts
│   ├── validate-data.js     # Validate JSON against schemas
│   ├── create-book.js       # Helper to create new book files
│   └── backup-data.sh       # Backup data files
│
├── tests/                    # Test files
│   ├── data-integrity.test.js
│   └── navigation.test.js
│
├── backups/                  # Automatic backups
│   └── YYYY-MM-DD/          # Daily backup folders
│
├── .github/                  # GitHub specific
│   ├── workflows/
│   │   └── validate.yml     # Auto-validate on push
│   └── ISSUE_TEMPLATE/
│       ├── add-book.md
│       └── bug-report.md
│
├── package.json             # Dependencies and scripts
├── .gitignore              # Git ignore rules
└── README.md               # User-facing documentation
```

## File Size Guidelines

- **HTML files**: < 100 lines
- **CSS files**: < 200 lines per file
- **JS modules**: < 150 lines per file
- **JSON data files**: < 500 lines per book
- **Documentation**: < 300 lines per file

## Development Phases

### Phase 1: Core Structure (Current)
1. Set up directory structure
2. Create base HTML/CSS
3. Implement series selection
4. Add basic data loading

### Phase 2: Book Navigation
1. Book selection view
2. Data validation system
3. Error handling

### Phase 3: Chapter Features
1. Chapter selection
2. Character display
3. Spoiler protection

### Phase 4: Enhancement
1. Search functionality
2. Progress tracking
3. User preferences

## Module Boundaries

Each module should:
1. Have a single responsibility
2. Export a clear API
3. Include JSDoc comments
4. Handle its own errors
5. Be testable in isolation

## Data Management Strategy

1. **Versioning**: Each data file includes version number
2. **Validation**: JSON schemas ensure data integrity
3. **Backup**: Automatic daily backups of data/
4. **Migration**: Scripts to update data structure

## Documentation Standards

Each file must include:
```javascript
/**
 * @file filename.js
 * @description Brief description of file purpose
 * @module ModuleName
 * @requires Dependencies
 * @exports What this file exports
 * @version 1.0.0
 * @lastModified 2024-01-01
 */
```

## Git Workflow

1. **Commit Messages**: 
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation
   - `data:` Content updates
   - `refactor:` Code improvement

2. **Branch Strategy**:
   - `main` - Production ready
   - `develop` - Integration branch
   - `feature/` - New features
   - `content/` - Content updates

## AI Collaboration Guidelines

1. **Context Limits**: Keep files small enough for single AI context
2. **Clear Boundaries**: Each module has defined inputs/outputs
3. **Documentation First**: Update docs before changing code
4. **Incremental Changes**: Small, testable changes
5. **Explicit Dependencies**: Clear module dependencies

## Next Steps

1. Create directory structure
2. Implement Phase 1 core files
3. Set up data validation
4. Create first book dataset
5. Test and iterate
