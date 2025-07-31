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



## 📜 Rules for Building This Site

These rules guide how content is created and maintained for the Spoiler Free Character Guide.

### 1️⃣ Spoiler Safety
- **Never reveal future plot points early.** 
- Only include information a reader would know **up to the chapter they’re on.**

### 2️⃣ Tiered Character Descriptions
- Characters have **tiered descriptions** that evolve as the reader progresses.
- Each tier adds context **without spoiling future developments.**
- Always **retain the core identity** of the character in every tier (e.g., “Vin is a street urchin…” stays true in later tiers).

### 3️⃣ Consistent Core Facts
- Details like **titles, family ties, affiliations** must remain present across tiers unless revealing them would spoil the plot.

### 4️⃣ Every Named Character
- **Every named character** in the book must be included — no matter how minor.

### 5️⃣ Chapter-Specific Recaps
- Recaps must be **short** and **spoiler-free.**
- Tone: factual but light enough to “remind” a reader, not summarize the whole plot.

### 6️⃣ Amazon Affiliate Links
- Include affiliate links for each book’s page (using `profitfirstre-20` store ID).
- Links should be **helpful and subtle**, never intrusive.

### 7️⃣ UI Guidelines
- When a chapter is selected:
  - First show **characters present in that chapter.**
  - Then list **all previously introduced characters** for context.
- Keep the site **minimalist, text-based, responsive** — book readers first.

### 8️⃣ Data Maintenance
- ⚠️ **Never regenerate JSONs** unless absolutely necessary. 
- Always **update existing files** with new characters, recaps, or corrections.
- Use `index.json` to register new series and maintain order.

