# Spoiler-Free Character Guide

A beautiful, interactive website for navigating fantasy book series without spoilers. Features chapter-by-chapter character tracking and spoiler-safe descriptions.

## 🚀 Quick Start

1. Upload all files to your GitHub repository
2. Enable GitHub Pages or deploy to Vercel
3. Your site will be live immediately!

## 📁 File Structure

```
/
├── index.html          # Main website file
├── data/              # Book series data files
│   ├── mistborn.json
│   ├── harry-potter.json
│   └── [other-series].json
└── README.md          # This file
```

## 📚 Current Series

- **Mistborn Trilogy** (Complete)
  - The Final Empire (38 chapters, 17 characters)
  - The Well of Ascension (Coming soon)
  - The Hero of Ages (Coming soon)

- **Harry Potter** (Sample)
  - Philosopher's Stone (17 chapters, 3 characters)

## ✨ Features

- **Spoiler-Safe**: Characters only appear after they're introduced
- **Chapter-Dependent Descriptions**: Character info updates based on reader progress
- **Beautiful Design**: Bookshelf aesthetic with hover animations
- **Mobile Responsive**: Works perfectly on all devices
- **Easy Navigation**: Breadcrumb navigation and intuitive interface

## 🔧 Adding New Series

### 1. Create JSON File

Create a new file in the `data/` folder following this structure:

```json
{
  "title": "Series Name",
  "books": {
    "book-id": {
      "title": "Book Title",
      "chapters": 25,
      "characters": {
        "character-id": {
          "name": "Character Name",
          "appearsInChapters": [1,2,3,5,8,10],
          "descriptions": {
            "1": "First appearance description (spoiler-free for chapter 1)",
            "5": "Updated description for chapter 5 (includes developments up to ch 5)",
            "10": "Later description (includes all developments up to chapter 10)"
          }
        }
      },
      "chapterSummaries": {
        "1": "Brief, spoiler-free summary of chapter 1",
        "2": "Brief, spoiler-free summary of chapter 2"
      }
    }
  }
}
```

### 2. Update Configuration

In `index.html`, add your series to the `seriesConfig` object:

```javascript
'your-series-id': {
    title: 'Your Series Name',
    file: 'data/your-series.json',
    cssClass: 'your-series-id'
}
```

### 3. Add CSS Styling

Add a CSS class for your book series color:

```css
.book.your-series-id { 
    background: linear-gradient(45deg, #color1, #color2); 
}
```

## 📝 Writing Guidelines

### Character Descriptions
- **First sentence**: Character background and context
- **Second sentence**: Current story arc and developments
- **Spoiler-safe**: Only include info revealed by that chapter
- **1-2 sentences**: Keep descriptions concise

### Chapter Summaries
- **1-2 sentences**: Brief recap of main events
- **Spoiler-free**: Safe for readers at that exact chapter
- **Focus on plot**: Mention key developments without revealing outcomes

## 🎨 Design Philosophy

- **Text-forward**: Content is king, design supports readability
- **Bookshelf aesthetic**: Warm, literary feel with rich browns and golds
- **Interactive elements**: Subtle animations that enhance experience
- **Accessibility**: High contrast, semantic markup, keyboard navigation

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Add new series**: Create JSON files for popular fantasy series
2. **Expand existing series**: Add more books to current series
3. **Improve descriptions**: Enhance character descriptions and chapter summaries
4. **Fix issues**: Report bugs or suggest improvements

### Contributing Guidelines

- Keep descriptions spoiler-free and chapter-appropriate
- Follow the established JSON structure
- Test your additions before submitting
- Include all named characters, even minor ones
- Write descriptions that help readers who haven't read in a while

## 🛠️ Technical Details

- **Pure HTML/CSS/JavaScript**: No build process required
- **Client-side JSON loading**: Fast, cacheable data files
- **GitHub Pages compatible**: Deploy anywhere static sites work
- **Mobile responsive**: Works on all screen sizes
- **Modern browser support**: Uses ES6+ features

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🌟 Roadmap

- [ ] Complete Mistborn trilogy data
- [ ] Add more Harry Potter books
- [ ] Include popular series: Wheel of Time, Stormlight Archive, LOTR
- [ ] Search functionality
- [ ] Bookmark system
- [ ] Reading progress tracking
- [ ] Community contributions system

---

**Happy reading! 📖✨**
