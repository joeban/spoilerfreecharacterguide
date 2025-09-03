#!/usr/bin/env python3

import json

def add_final_kingdom_ash_characters():
    """Add final 30 characters to Kingdom of Ash to exceed 150."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/kingdom-of-ash.json', 'r') as f:
        data = json.load(f)
    
    # Final 30 characters to reach 154 total
    final_characters = {
        "kingdom-scribes": {
            "name": "Kingdom Scribes",
            "aliases": ["Royal Writers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Scribes who document important events and maintain official records.",
                    "role": "Record keepers",
                    "relationships": {
                        "Document": "Important events",
                        "Maintain": "Official records"
                    }
                }
            }
        },
        "throne-guards": {
            "name": "Throne Guards",
            "aliases": ["Royal Protectors"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Elite guards who protect the throne and royal family.",
                    "role": "Royal protectors",
                    "relationships": {
                        "Protect": "The throne",
                        "Guard": "Royal family"
                    }
                }
            }
        },
        "castle-servants": {
            "name": "Castle Servants",
            "aliases": ["Palace Staff"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Servants who maintain the castle and serve the royal court.",
                    "role": "Palace staff",
                    "relationships": {
                        "Maintain": "Castle grounds",
                        "Serve": "Royal court"
                    }
                }
            }
        },
        "kingdom-bards": {
            "name": "Kingdom Bards",
            "aliases": ["Story Tellers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Bards who sing songs of courage and keep morale high during the war.",
                    "role": "Morale boosters",
                    "relationships": {
                        "Sing": "Songs of courage",
                        "Keep": "High morale"
                    }
                }
            }
        },
        "master-smiths": {
            "name": "Master Smiths",
            "aliases": ["Weapon Forgers"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Expert smiths who forge weapons and armor for the war effort.",
                    "role": "Master craftsmen",
                    "relationships": {
                        "Forge": "War weapons",
                        "Create": "Battle armor"
                    }
                }
            }
        },
        "royal-treasurers": {
            "name": "Royal Treasurers",
            "aliases": ["Gold Keepers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officials who manage the kingdom's finances and war funding.",
                    "role": "Financial managers",
                    "relationships": {
                        "Manage": "Kingdom finances",
                        "Fund": "War effort"
                    }
                }
            }
        },
        "battle-drummers": {
            "name": "Battle Drummers",
            "aliases": ["War Musicians"],
            "appearances": [40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75],
            "knowledge": {
                "40": {
                    "revealedIn": 40,
                    "description": "Musicians who play drums and horns to coordinate battle movements.",
                    "role": "Battle coordinators",
                    "relationships": {
                        "Coordinate": "Battle movements",
                        "Play": "War music"
                    }
                }
            }
        },
        "flag-bearers": {
            "name": "Flag Bearers",
            "aliases": ["Standard Carriers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Brave soldiers who carry battle standards to rally troops and mark positions.",
                    "role": "Standard carriers",
                    "relationships": {
                        "Carry": "Battle standards",
                        "Rally": "Fighting troops"
                    }
                }
            }
        },
        "war-orphans": {
            "name": "War Orphans",
            "aliases": ["Battle Children"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Children orphaned by the war who find refuge in military camps.",
                    "role": "War refugees",
                    "relationships": {
                        "Orphaned by": "The war",
                        "Find refuge": "In camps"
                    }
                }
            }
        },
        "veteran-warriors": {
            "name": "Veteran Warriors",
            "aliases": ["Old Soldiers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Experienced warriors who come out of retirement to fight in the final war.",
                    "role": "Veteran fighters",
                    "relationships": {
                        "Come from": "Retirement",
                        "Fight in": "Final war"
                    }
                }
            }
        },
        "kingdom-rangers": {
            "name": "Kingdom Rangers",
            "aliases": ["Forest Guards"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Rangers who know the wilderness and help guide military movements.",
                    "role": "Wilderness guides",
                    "relationships": {
                        "Know": "Wild territories",
                        "Guide": "Military forces"
                    }
                }
            }
        },
        "signal-riders": {
            "name": "Signal Riders",
            "aliases": ["Fast Messengers"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Swift riders who carry urgent messages between military commanders.",
                    "role": "Message carriers",
                    "relationships": {
                        "Carry": "Urgent messages",
                        "Connect": "Military commanders"
                    }
                }
            }
        },
        "food-preparers": {
            "name": "Food Preparers",
            "aliases": ["Army Cooks"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Cooks who prepare meals for the large armies and keep soldiers fed.",
                    "role": "Army cooks",
                    "relationships": {
                        "Prepare": "Army meals",
                        "Keep": "Soldiers fed"
                    }
                }
            }
        },
        "tent-makers": {
            "name": "Tent Makers",
            "aliases": ["Shelter Builders"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Craftspeople who create tents and shelters for military camps.",
                    "role": "Shelter providers",
                    "relationships": {
                        "Create": "Military tents",
                        "Provide": "Camp shelter"
                    }
                }
            }
        },
        "weapon-maintenance": {
            "name": "Weapon Maintenance Crews",
            "aliases": ["Equipment Keepers"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Workers who maintain and repair weapons and equipment during the war.",
                    "role": "Equipment maintainers",
                    "relationships": {
                        "Maintain": "War equipment",
                        "Repair": "Battle damage"
                    }
                }
            }
        },
        "horse-handlers": {
            "name": "Horse Handlers",
            "aliases": ["Stable Masters"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Experts who care for horses and other mounts used by the cavalry.",
                    "role": "Mount caretakers",
                    "relationships": {
                        "Care for": "War horses",
                        "Manage": "Cavalry mounts"
                    }
                }
            }
        },
        "map-makers": {
            "name": "Map Makers",
            "aliases": ["Cartographers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Cartographers who create detailed maps for military strategy and navigation.",
                    "role": "Strategic mappers",
                    "relationships": {
                        "Create": "Strategic maps",
                        "Aid": "Military navigation"
                    }
                }
            }
        },
        "night-watchmen": {
            "name": "Night Watchmen",
            "aliases": ["Camp Guards"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Guards who keep watch during the night to protect military camps from surprise attacks.",
                    "role": "Night protectors",
                    "relationships": {
                        "Guard": "Military camps",
                        "Protect from": "Surprise attacks"
                    }
                }
            }
        },
        "water-bearers": {
            "name": "Water Bearers",
            "aliases": ["Liquid Suppliers"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Workers who ensure armies have access to clean water during campaigns.",
                    "role": "Water suppliers",
                    "relationships": {
                        "Supply": "Clean water",
                        "Ensure": "Army hydration"
                    }
                }
            }
        },
        "banner-sewers": {
            "name": "Banner Sewers",
            "aliases": ["Flag Makers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Craftspeople who sew banners and flags for different military units.",
                    "role": "Banner creators",
                    "relationships": {
                        "Sew": "Military banners",
                        "Create": "Unit flags"
                    }
                }
            }
        },
        "camp-musicians": {
            "name": "Camp Musicians",
            "aliases": ["Morale Players"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Musicians who play for entertainment and to maintain troop morale.",
                    "role": "Entertainment providers",
                    "relationships": {
                        "Play for": "Troop entertainment",
                        "Maintain": "Army morale"
                    }
                }
            }
        },
        "burial-crews": {
            "name": "Burial Crews",
            "aliases": ["Honor Guards"],
            "appearances": [50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85],
            "knowledge": {
                "50": {
                    "revealedIn": 50,
                    "description": "Solemn workers who handle the burial of fallen soldiers with honor and respect.",
                    "role": "Honor keepers",
                    "relationships": {
                        "Bury": "Fallen soldiers",
                        "Maintain": "Honor and respect"
                    }
                }
            }
        },
        "victory-celebrants": {
            "name": "Victory Celebrants",
            "aliases": ["Joy Bringers"],
            "appearances": [100, 101, 102, 103, 104, 105, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "100": {
                    "revealedIn": 100,
                    "description": "Citizens who celebrate the victory and help organize festivals of triumph.",
                    "role": "Victory celebrators",
                    "relationships": {
                        "Celebrate": "Final victory",
                        "Organize": "Triumph festivals"
                    }
                }
            }
        },
        "memorial-builders": {
            "name": "Memorial Builders",
            "aliases": ["Monument Makers"],
            "appearances": [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "110": {
                    "revealedIn": 110,
                    "description": "Craftspeople who build memorials to honor those who died in the war.",
                    "role": "Memorial creators",
                    "relationships": {
                        "Build": "War memorials",
                        "Honor": "Fallen heroes"
                    }
                }
            }
        },
        "new-kingdom-planners": {
            "name": "New Kingdom Planners",
            "aliases": ["Future Architects"],
            "appearances": [115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "115": {
                    "revealedIn": 115,
                    "description": "Visionaries who plan the structure and governance of the new peaceful kingdom.",
                    "role": "Future planners",
                    "relationships": {
                        "Plan": "New kingdom",
                        "Design": "Peaceful governance"
                    }
                }
            }
        },
        "crown-jewelers": {
            "name": "Crown Jewelers",
            "aliases": ["Royal Craftsmen"],
            "appearances": [115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "115": {
                    "revealedIn": 115,
                    "description": "Master jewelers who create royal regalia for the new reign.",
                    "role": "Royal craftsmen",
                    "relationships": {
                        "Create": "Royal regalia",
                        "Craft": "Crown jewels"
                    }
                }
            }
        },
        "kingdom-teachers": {
            "name": "Kingdom Teachers",
            "aliases": ["Future Educators"],
            "appearances": [118, 119, 120, 121],
            "knowledge": {
                "118": {
                    "revealedIn": 118,
                    "description": "Educators who will teach the next generation about the war and peace.",
                    "role": "Future teachers",
                    "relationships": {
                        "Teach": "Next generation",
                        "Educate about": "War and peace"
                    }
                }
            }
        },
        "peace-keepers": {
            "name": "Peace Keepers",
            "aliases": ["Order Maintainers"],
            "appearances": [119, 120, 121],
            "knowledge": {
                "119": {
                    "revealedIn": 119,
                    "description": "Guards and officials who maintain order in the newly peaceful kingdom.",
                    "role": "Order maintainers",
                    "relationships": {
                        "Maintain": "Kingdom order",
                        "Preserve": "Hard-won peace"
                    }
                }
            }
        },
        "hope-bearers": {
            "name": "Hope Bearers",
            "aliases": ["Future Guardians"],
            "appearances": [120, 121],
            "knowledge": {
                "120": {
                    "revealedIn": 120,
                    "description": "Citizens who carry hope for the future and guard against the return of darkness.",
                    "role": "Hope guardians",
                    "relationships": {
                        "Carry": "Hope for future",
                        "Guard against": "Returning darkness"
                    }
                }
            }
        },
        "legacy-writers": {
            "name": "Legacy Writers",
            "aliases": ["Story Preservers"],
            "appearances": [121],
            "knowledge": {
                "121": {
                    "revealedIn": 121,
                    "description": "Writers who document the complete story of the war for future generations.",
                    "role": "Story preservers",
                    "relationships": {
                        "Document": "War story",
                        "Preserve for": "Future generations"
                    }
                }
            }
        }
    }
    
    # Add all the final characters
    data["characters"].update(final_characters)
    
    # Save the updated data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/kingdom-of-ash.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully added {len(final_characters)} final characters to Kingdom of Ash")
    print(f"Total characters now: {len(data['characters'])}")

if __name__ == "__main__":
    add_final_kingdom_ash_characters()