# DATA FOLDER DOCUMENTATION

All book, character, and recap data for the Spoiler Free Character Guide is stored here.

## 📂 Structure
- **index.json** – Registry of all series and their books.
- **[series][number].json** – One JSON per book (e.g., mistborn1.json).
- **DATA_README.md** – This file.

## 📜 Rules
- Do **NOT** regenerate JSON files once created. Only edit to add/update characters or recaps.
- Every **named character** must be included in the correct JSON file.
- Descriptions must always be spoiler-free for chapters not yet read.

## 📦 Book JSON Format

```json
{
  "meta": {
    "title": "Mistborn: The Final Empire",
    "bookNumber": 1,
    "totalChapters": 38,
    "affiliateLink": "https://amazon.com/...",
    "series": "Mistborn"
  },
  "characters": {
    "Vin": {
      "firstAppearance": 1,
      "featuredIn": [1, 2, 3],
      "tiers": {
        "1-5": "Vin is a wary street urchin surviving in Luthadel.",
        "6-10": "Vin begins to trust Kelsier and the crew."
      }
    }
  },
  "recaps": {
    "1": "Vin struggles to survive in the streets of Luthadel.",
    "2": "Vin meets Kelsier, who begins to draw her into a daring plan."
  }
}
```

