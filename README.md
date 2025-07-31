# Chapter Companion - Spoiler-Free Character Guide

A web application that provides spoiler-free character guides for fiction novels, helping readers keep track of characters without revealing future plot points.

## Features

- **Bookshelf Navigation**: Visual bookshelf interface for browsing series and books
- **Chapter-by-Chapter Progress**: Select your current chapter to see only relevant information
- **Spoiler-Free Summaries**: Chapter summaries hidden behind toggles to avoid accidental spoilers
- **Character Tracking**: Shows characters introduced in current chapter and all previous characters
- **Dynamic Character Descriptions**: Character backgrounds and story arcs update based on reading progress

## Project Structure

```
chapter-companion/
├── index.html          # Main website file
├── data/              # JSON data files
│   ├── series.json    # List of all book series
│   ├── mistborn/      # Mistborn series data
│   │   ├── book1.json # The Final Empire
│   │   ├── book2.json # The Well of Ascension
│   │   └── book3.json # The Hero of Ages
│   ├── harry-potter/  # Harry Potter series data
│   │   ├── book1.json
│   │   └── ...
│   └── ...           # Other series folders
└── README.md         # This file
```

## JSON Data Structure

### series.json
Contains the master list of all book series:
```json
{
  "series": [
    {
      "id": "mistborn",
      "title": "Mistborn",
      "author": "Brandon Sanderson",
      "books": ["The Final Empire", "The Well of Ascension", "The Hero of Ages"]
    }
  ]
}
```

### Individual Book JSON (e.g., book1.json)
Contains chapter-by-chapter character information:
```json
{
  "title": "The Final Empire",
  "author": "Brandon Sanderson",
  "totalChapters": 38,
  "chapters": [
    {
      "number": 1,
      "title": "The Survivor of Hathsin",
      "summary": "Brief spoiler-free chapter summary",
      "charactersIntroduced": ["Kelsier", "Dockson"],
      "characters": {
        "
