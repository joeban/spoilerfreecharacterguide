# Data Folder Documentation

This folder contains all JSON data for the Spoiler Free Character Guide site.

## 📂 Structure
- **mistborn1.json – mistborn7.json**: Spoiler-free data for all Mistborn books.
- **harrypotter1.json – harrypotter7.json**: Placeholders for Harry Potter books.
- **series.json**: Metadata for Mistborn series.
- **index.json**: Master registry of all series and their JSON files.

## ⚠️ Important Notes
- **DO NOT regenerate JSON** unless absolutely necessary.
- Always reuse and update existing files.
- Every JSON file starts with a "__comment" explaining its purpose.

## ✅ Adding new series
1. Add JSONs following the same naming convention (`seriesname1.json`, etc.).
2. Update `index.json` to include new series & books.
3. Add any needed series metadata (like `series.json` for Mistborn).

