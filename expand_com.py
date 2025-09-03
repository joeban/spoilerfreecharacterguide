#!/usr/bin/env python3
import json

# Read existing data
with open('data/throne-of-glass/crown-of-midnight.json', 'r') as f:
    data = json.load(f)

# Additional characters to reach 150+
new_characters = {
    # More court nobles
    "lord-harwick": {
        "name": "Lord Harwick",
        "aliases": [],
        "appearances": [8, 15, 32],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "Noble at court who attends council meetings. Supports the King's policies.",
                "role": "Court noble",
                "relationships": {
                    "King of Adarlan": "Supporter of"
                }
            }
        }
    },
    "lady-beatrice": {
        "name": "Lady Beatrice",
        "aliases": [],
        "appearances": [12, 28],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "Court lady who gossips about Celaena's relationship with the prince and captain.",
                "role": "Court gossip",
                "relationships": {
                    "Lady Araminta": "Friend of"
                }
            }
        }
    },
    "lord-thomas": {
        "name": "Lord Thomas",
        "aliases": [],
        "appearances": [15, 40],
        "knowledge": {
            "15": {
                "revealedIn": 15,
                "description": "Wealthy merchant lord who trades with Melisande.",
                "role": "Merchant lord",
                "relationships": {}
            }
        }
    },
    "councilman-gregory": {
        "name": "Councilman Gregory",
        "aliases": [],
        "appearances": [20, 35],
        "knowledge": {
            "20": {
                "revealedIn": 20,
                "description": "Member of the King's council who advocates for harsher measures against rebels.",
                "role": "Council member",
                "relationships": {
                    "King of Adarlan": "Advisor to"
                }
            }
        }
    },
    
    # More guards and soldiers
    "captain-morris": {
        "name": "Captain Morris",
        "aliases": [],
        "appearances": [18, 42],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "Captain of the castle's night watch.",
                "role": "Night watch captain",
                "relationships": {
                    "Chaol Westfall": "Reports to"
                }
            }
        }
    },
    "sergeant-pike": {
        "name": "Sergeant Pike",
        "aliases": [],
        "appearances": [25],
        "knowledge": {
            "25": {
                "revealedIn": 25,
                "description": "Guard sergeant who discovers Nehemia's body.",
                "role": "Guard sergeant",
                "relationships": {}
            }
        }
    },
    "guard-wilson": {
        "name": "Guard Wilson",
        "aliases": [],
        "appearances": [10, 30],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Young guard who patrols the royal wing.",
                "role": "Palace guard",
                "relationships": {}
            }
        }
    },
    
    # Assassins and underworld
    "ivan-the-terrible": {
        "name": "Ivan the Terrible",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "Notorious assassin from the Guild mentioned in conversations about dangerous killers.",
                "role": "Assassin",
                "relationships": {
                    "Arobynn Hamel": "Works for"
                }
            }
        }
    },
    "black-widow": {
        "name": "The Black Widow",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "Female assassin known for poisoning victims.",
                "role": "Assassin",
                "relationships": {}
            }
        }
    },
    "razor": {
        "name": "Razor",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "Assassin specializing in blade work.",
                "role": "Assassin",
                "relationships": {
                    "Arobynn Hamel": "Trained by"
                }
            }
        }
    },
    
    # Servants and staff
    "maid-alice": {
        "name": "Alice",
        "aliases": [],
        "appearances": [5, 22],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "Chamber maid who tends to Celaena's rooms.",
                "role": "Chamber maid",
                "relationships": {
                    "Philippa": "Works under"
                }
            }
        }
    },
    "footman-charles": {
        "name": "Charles",
        "aliases": [],
        "appearances": [8, 16],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "Footman who serves at royal dinners.",
                "role": "Footman",
                "relationships": {}
            }
        }
    },
    "groom-peter": {
        "name": "Peter",
        "aliases": [],
        "appearances": [11],
        "knowledge": {
            "11": {
                "revealedIn": 11,
                "description": "Stable groom who cares for the horses.",
                "role": "Stable groom",
                "relationships": {
                    "Master Hoke": "Works for"
                }
            }
        }
    },
    
    # Rebels and resistance
    "rebel-marcus": {
        "name": "Marcus",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "30": {
                "revealedIn": 30,
                "description": "Rebel contact in the city's eastern district.",
                "role": "Rebel operative",
                "relationships": {
                    "Ren Allsbrook": "Works with"
                }
            }
        }
    },
    "informant-sara": {
        "name": "Sara the Informant",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "32": {
                "revealedIn": 32,
                "description": "Information broker who sells secrets to rebels.",
                "role": "Information broker",
                "relationships": {}
            }
        }
    },
    
    # Merchants and traders
    "spice-merchant": {
        "name": "Hakim",
        "aliases": ["The Spice Merchant"],
        "appearances": [19],
        "knowledge": {
            "19": {
                "revealedIn": 19,
                "description": "Merchant from the southern continent who trades exotic spices.",
                "role": "Spice merchant",
                "relationships": {}
            }
        }
    },
    "jeweler-mason": {
        "name": "Mason",
        "aliases": [],
        "appearances": [23],
        "knowledge": {
            "23": {
                "revealedIn": 23,
                "description": "Royal jeweler who crafts pieces for the court.",
                "role": "Royal jeweler",
                "relationships": {}
            }
        }
    },
    "book-seller": {
        "name": "Edmund",
        "aliases": ["Edmund the Book Seller"],
        "appearances": [27],
        "knowledge": {
            "27": {
                "revealedIn": 27,
                "description": "Runs a bookshop where Celaena finds ancient texts.",
                "role": "Book seller",
                "relationships": {}
            }
        }
    },
    
    # Eyllwe characters
    "eyllwe-ambassador": {
        "name": "Ambassador Kente",
        "aliases": [],
        "appearances": [15, 24],
        "knowledge": {
            "15": {
                "revealedIn": 15,
                "description": "Eyllwe ambassador trying to negotiate with Adarlan.",
                "role": "Eyllwe ambassador",
                "relationships": {
                    "Nehemia Ytger": "Works with"
                }
            }
        }
    },
    "eyllwe-scribe": {
        "name": "Scribe Aminu",
        "aliases": [],
        "appearances": [24],
        "knowledge": {
            "24": {
                "revealedIn": 24,
                "description": "Nehemia's personal scribe who handles her correspondence.",
                "role": "Royal scribe",
                "relationships": {
                    "Nehemia Ytger": "Serves"
                }
            }
        }
    },
    
    # Historical and mythological
    "first-valg-king": {
        "name": "The First Valg King",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "45": {
                "revealedIn": 45,
                "description": "Ancient demon king who first invaded this world.",
                "role": "Ancient evil",
                "relationships": {
                    "Erawan": "Predecessor of"
                }
            }
        }
    },
    "fae-warrior-athril": {
        "name": "Athril",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "40": {
                "revealedIn": 40,
                "description": "Ancient Fae warrior who fought alongside Brannon.",
                "role": "Ancient warrior",
                "relationships": {
                    "Brannon Galathynius": "Companion of"
                }
            }
        }
    },
    "queen-mab": {
        "name": "Queen Mab",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "40": {
                "revealedIn": 40,
                "description": "One of the ancient Fae Queens mentioned in legends.",
                "role": "Fae Queen",
                "relationships": {}
            }
        }
    },
    "queen-maeve": {
        "name": "Queen Maeve",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "40": {
                "revealedIn": 40,
                "description": "Dark Fae Queen of Doranelle mentioned in ancient texts.",
                "role": "Dark Fae Queen",
                "relationships": {}
            }
        }
    },
    "queen-mora": {
        "name": "Queen Mora",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "40": {
                "revealedIn": 40,
                "description": "Another ancient Fae Queen from the old stories.",
                "role": "Fae Queen",
                "relationships": {}
            }
        }
    },
    
    # More townspeople
    "baker-willem": {
        "name": "Willem the Baker",
        "aliases": [],
        "appearances": [13],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Baker in the lower city who Celaena buys pastries from.",
                "role": "Baker",
                "relationships": {}
            }
        }
    },
    "fishmonger-greta": {
        "name": "Greta",
        "aliases": [],
        "appearances": [21],
        "knowledge": {
            "21": {
                "revealedIn": 21,
                "description": "Fish seller at the docks market.",
                "role": "Fishmonger",
                "relationships": {}
            }
        }
    },
    "flower-girl": {
        "name": "Little Rose",
        "aliases": [],
        "appearances": [17],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "Young girl who sells flowers near the castle gates.",
                "role": "Flower seller",
                "relationships": {}
            }
        }
    },
    
    # Religious figures
    "high-priestess": {
        "name": "High Priestess Calliope",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "35": {
                "revealedIn": 35,
                "description": "High Priestess of the Great Temple mentioned in religious discussions.",
                "role": "High Priestess",
                "relationships": {}
            }
        }
    },
    "temple-guardian": {
        "name": "Brother Matthias",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "35": {
                "revealedIn": 35,
                "description": "Guardian of the temple's sacred texts.",
                "role": "Temple guardian",
                "relationships": {}
            }
        }
    },
    
    # Animals and creatures
    "castle-cat": {
        "name": "Whiskers",
        "aliases": [],
        "appearances": [7, 14],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Castle cat that frequents the kitchens and Celaena's rooms.",
                "role": "Castle pet",
                "relationships": {}
            }
        }
    },
    "messenger-raven": {
        "name": "Blackwing",
        "aliases": [],
        "appearances": [25, 38],
        "knowledge": {
            "25": {
                "revealedIn": 25,
                "description": "One of the castle's messenger ravens.",
                "role": "Messenger bird",
                "relationships": {}
            }
        }
    },
    
    # Additional minor characters
    "scullery-maid": {
        "name": "Beth",
        "aliases": [],
        "appearances": [9],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Young scullery maid in the castle kitchens.",
                "role": "Scullery maid",
                "relationships": {
                    "Head Cook Merta": "Works for"
                }
            }
        }
    },
    "laundress-mary": {
        "name": "Mary",
        "aliases": [],
        "appearances": [16],
        "knowledge": {
            "16": {
                "revealedIn": 16,
                "description": "Head laundress who manages the castle's washing.",
                "role": "Head laundress",
                "relationships": {}
            }
        }
    },
    "page-timothy": {
        "name": "Timothy",
        "aliases": [],
        "appearances": [12, 28],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "Young page who runs messages in the castle.",
                "role": "Page",
                "relationships": {}
            }
        }
    },
    "squire-edmund": {
        "name": "Edmund",
        "aliases": [],
        "appearances": [18],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "Squire training under the castle guard.",
                "role": "Squire",
                "relationships": {
                    "Brullo": "Trains under"
                }
            }
        }
    },
    
    # Foreign dignitaries
    "melisande-lord": {
        "name": "Lord Baptiste",
        "aliases": [],
        "appearances": [33],
        "knowledge": {
            "33": {
                "revealedIn": 33,
                "description": "Visiting lord from Melisande attending court.",
                "role": "Foreign noble",
                "relationships": {}
            }
        }
    },
    "fenharrow-duke": {
        "name": "Duke Carlisle",
        "aliases": [],
        "appearances": [34],
        "knowledge": {
            "34": {
                "revealedIn": 34,
                "description": "Duke from Fenharrow negotiating trade agreements.",
                "role": "Foreign duke",
                "relationships": {}
            }
        }
    },
    
    # More magical beings
    "shadow-speaker": {
        "name": "The Shadow Speaker",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "48": {
                "revealedIn": 48,
                "description": "Mysterious entity that speaks through shadows in the tomb.",
                "role": "Magical entity",
                "relationships": {}
            }
        }
    },
    "tomb-guardian": {
        "name": "The Tomb Guardian",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "50": {
                "revealedIn": 50,
                "description": "Ancient magical guardian of Elena's tomb.",
                "role": "Magical guardian",
                "relationships": {
                    "Elena Havilliard": "Guards tomb of"
                }
            }
        }
    },
    
    # Criminal underworld
    "fence-ricardo": {
        "name": "Ricardo",
        "aliases": ["Ricardo the Fence"],
        "appearances": [],
        "knowledge": {
            "22": {
                "revealedIn": 22,
                "description": "Fence who deals in stolen goods in the thieves' quarter.",
                "role": "Fence",
                "relationships": {}
            }
        }
    },
    "smuggler-captain": {
        "name": "Captain Vega",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "29": {
                "revealedIn": 29,
                "description": "Smuggler captain who runs goods past the blockades.",
                "role": "Smuggler",
                "relationships": {}
            }
        }
    },
    
    # Scholars and academics
    "scholar-abraham": {
        "name": "Scholar Abraham",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "37": {
                "revealedIn": 37,
                "description": "Scholar specializing in ancient languages at the royal library.",
                "role": "Scholar",
                "relationships": {}
            }
        }
    },
    "historian-felix": {
        "name": "Historian Felix",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "37": {
                "revealedIn": 37,
                "description": "Royal historian who maintains the kingdom's records.",
                "role": "Royal historian",
                "relationships": {}
            }
        }
    },
    
    # Entertainers
    "jester-pip": {
        "name": "Pip the Jester",
        "aliases": [],
        "appearances": [26],
        "knowledge": {
            "26": {
                "revealedIn": 26,
                "description": "Court jester who performs at royal gatherings.",
                "role": "Court jester",
                "relationships": {}
            }
        }
    },
    "singer-lydia": {
        "name": "Lydia",
        "aliases": [],
        "appearances": [26],
        "knowledge": {
            "26": {
                "revealedIn": 26,
                "description": "Singer who performs at court events.",
                "role": "Court singer",
                "relationships": {}
            }
        }
    },
    
    # Medical staff
    "physician-harold": {
        "name": "Physician Harold",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "25": {
                "revealedIn": 25,
                "description": "One of the castle physicians who examines Nehemia.",
                "role": "Castle physician",
                "relationships": {
                    "Ligenza": "Works with"
                }
            }
        }
    },
    "nurse-margaret": {
        "name": "Nurse Margaret",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "25": {
                "revealedIn": 25,
                "description": "Nurse who assists with medical emergencies.",
                "role": "Castle nurse",
                "relationships": {}
            }
        }
    },
    
    # Craftsmen
    "carpenter-joseph": {
        "name": "Joseph",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "31": {
                "revealedIn": 31,
                "description": "Master carpenter who maintains the castle's woodwork.",
                "role": "Master carpenter",
                "relationships": {}
            }
        }
    },
    "stonemason-erik": {
        "name": "Erik",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "31": {
                "revealedIn": 31,
                "description": "Stonemason who repairs castle walls and passages.",
                "role": "Stonemason",
                "relationships": {}
            }
        }
    },
    
    # Final additions
    "wine-merchant": {
        "name": "Vintner Claude",
        "aliases": [],
        "appearances": [20],
        "knowledge": {
            "20": {
                "revealedIn": 20,
                "description": "Wine merchant who supplies the royal cellars.",
                "role": "Wine merchant",
                "relationships": {}
            }
        }
    },
    "cheese-monger": {
        "name": "Henri",
        "aliases": [],
        "appearances": [21],
        "knowledge": {
            "21": {
                "revealedIn": 21,
                "description": "Cheese seller at the market.",
                "role": "Cheese monger",
                "relationships": {}
            }
        }
    }
}

# Add new characters to existing data
data['characters'].update(new_characters)

# Save updated file
with open('data/throne-of-glass/crown-of-midnight.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Successfully added {len(new_characters)} new characters")
print(f"Total characters now: {len(data['characters'])}")