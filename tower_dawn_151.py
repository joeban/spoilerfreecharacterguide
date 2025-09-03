#!/usr/bin/env python3

import json

def add_151st_character():
    """Add the 151st character to Tower of Dawn."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/tower-of-dawn.json', 'r') as f:
        data = json.load(f)
    
    # Add the 151st character
    data["characters"]["mountain-guides"] = {
        "name": "Mountain Guides",
        "aliases": ["Peak Pathfinders"],
        "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Experienced guides who know the treacherous mountain paths and help travelers navigate safely.",
                "role": "Mountain pathfinders",
                "relationships": {
                    "Guide": "Mountain travelers",
                    "Know": "Safe mountain paths"
                }
            }
        }
    }
    
    # Save the updated data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/tower-of-dawn.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully added 151st character to Tower of Dawn")
    print(f"Total characters now: {len(data['characters'])}")

if __name__ == "__main__":
    add_151st_character()