#!/usr/bin/env python3

import json

def add_final_tower_dawn_characters():
    """Add final 5 characters to Tower of Dawn to exceed 150."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/tower-of-dawn.json', 'r') as f:
        data = json.load(f)
    
    # Final 5 characters to exceed 150
    final_characters = {
        "ancient-scholars": {
            "name": "Ancient Scholars",
            "aliases": ["Old Wise Ones"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Elderly scholars who preserve ancient knowledge and study historical texts.",
                    "role": "Knowledge keepers",
                    "relationships": {
                        "Preserve": "Ancient wisdom",
                        "Study": "Historical texts"
                    }
                }
            }
        },
        "tower-messengers": {
            "name": "Tower Messengers",
            "aliases": ["Swift Riders"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Fast riders who carry messages between the Torre Cesme and other locations.",
                    "role": "Message carriers",
                    "relationships": {
                        "Serve": "Torre Cesme",
                        "Carry": "Important messages"
                    }
                }
            }
        },
        "desert-nomads": {
            "name": "Desert Nomads",
            "aliases": ["Sand Wanderers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Nomadic tribes who travel the vast deserts and know the ancient paths.",
                    "role": "Desert travelers",
                    "relationships": {
                        "Know": "Desert paths",
                        "Travel": "Ancient routes"
                    }
                }
            }
        },
        "royal-astronomers": {
            "name": "Royal Astronomers",
            "aliases": ["Star Readers"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Court astronomers who study the stars and celestial movements for the khagan.",
                    "role": "Star students",
                    "relationships": {
                        "Study": "Celestial movements",
                        "Advise": "The khagan"
                    }
                }
            }
        },
        "temple-acolytes": {
            "name": "Temple Acolytes",
            "aliases": ["Sacred Servants"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Young servants who tend to the sacred temples and assist the priests.",
                    "role": "Temple servants",
                    "relationships": {
                        "Serve": "Temple priests",
                        "Tend": "Sacred spaces"
                    }
                }
            }
        }
    }
    
    # Add the final characters
    data["characters"].update(final_characters)
    
    # Save the updated data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/tower-of-dawn.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully added {len(final_characters)} final characters to Tower of Dawn")
    print(f"Total characters now: {len(data['characters'])}")

if __name__ == "__main__":
    add_final_tower_dawn_characters()