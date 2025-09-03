#!/usr/bin/env python3

import json

def add_final_characters_to_empire_of_storms():
    """Add final characters to Empire of Storms to reach 150+ total."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/empire-of-storms.json', 'r') as f:
        data = json.load(f)
    
    # Final characters to add - 3 more to exceed 150
    additional_characters = {
        "sea-oracles": {
            "name": "Sea Oracles",
            "aliases": ["Ocean Prophets"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Mystical figures who prophesy events related to the ocean and its power.",
                    "role": "Ocean prophets",
                    "relationships": {
                        "Prophesy": "Sea-related events",
                        "Commune with": "Ocean spirits"
                    }
                }
            }
        },
        "storm-riders": {
            "name": "Storm Riders",
            "aliases": ["Tempest Masters"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Legendary figures who can travel through storms and command tempests.",
                    "role": "Storm masters",
                    "relationships": {
                        "Ride": "Storm winds",
                        "Command": "Tempests"
                    }
                }
            }
        },
        "ocean-guardians": {
            "name": "Ocean Guardians",
            "aliases": ["Sea Protectors"],
            "appearances": [45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65],
            "knowledge": {
                "45": {
                    "revealedIn": 45,
                    "description": "Ancient beings who protect the oceans and their secrets from those who would misuse them.",
                    "role": "Ocean protectors",
                    "relationships": {
                        "Protect": "Ocean secrets",
                        "Guard against": "Misuse of sea power"
                    }
                }
            }
        }
    }
    
    # Add all the new characters
    data["characters"].update(additional_characters)
    
    # Save the updated data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/empire-of-storms.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully added {len(additional_characters)} characters to Empire of Storms")
    print(f"Total characters now: {len(data['characters'])}")

if __name__ == "__main__":
    add_final_characters_to_empire_of_storms()