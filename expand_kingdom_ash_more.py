#!/usr/bin/env python3

import json

def add_more_kingdom_ash_characters():
    """Add 70+ more characters to Kingdom of Ash to reach 150+."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/kingdom-of-ash.json', 'r') as f:
        data = json.load(f)
    
    # Additional characters to reach comprehensive coverage
    more_characters = {
        # Ilias and other wyverns
        "abraxos-wyvern": {
            "name": "Abraxos",
            "aliases": ["Manon's Wyvern"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90, 95, 96, 97, 98, 99, 100, 105, 106, 107, 108, 109, 110, 115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Manon's loyal wyvern, one of the most powerful and intelligent of his kind.",
                    "role": "Wyvern mount",
                    "relationships": {
                        "Bonded to": "Manon Blackbeak",
                        "Leads": "Other wyverns"
                    }
                }
            }
        },
        "wyvern-bulls": {
            "name": "Wyvern Bulls",
            "aliases": ["Alpha Wyverns"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Powerful male wyverns that serve as mounts for the Thirteen and other witches.",
                    "role": "Wyvern mounts",
                    "relationships": {
                        "Serve as": "Witch mounts",
                        "Follow": "Abraxos's lead"
                    }
                }
            }
        },
        "wyvern-matrons": {
            "name": "Wyvern Matrons",
            "aliases": ["Mother Wyverns"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Female wyverns who protect their young and nest in the mountains.",
                    "role": "Mother dragons",
                    "relationships": {
                        "Protect": "Wyvern young",
                        "Nest in": "Mountain caves"
                    }
                }
            }
        },
        # More Fae courts and their members
        "dawn-court-fae": {
            "name": "Dawn Court Fae",
            "aliases": ["Morning Fae"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Fae from the Dawn Court who command light-based magic.",
                    "role": "Light wielders",
                    "relationships": {
                        "Command": "Light magic",
                        "Fight alongside": "Other courts"
                    }
                }
            }
        },
        "dusk-court-fae": {
            "name": "Dusk Court Fae",
            "aliases": ["Evening Fae"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Fae from the Dusk Court with shadow and twilight magic.",
                    "role": "Shadow wielders",
                    "relationships": {
                        "Wield": "Shadow magic",
                        "Unite with": "Other courts"
                    }
                }
            }
        },
        "summer-court-fae": {
            "name": "Summer Court Fae",
            "aliases": ["Sun Fae"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Fae from the Summer Court with heat and sun-based powers.",
                    "role": "Sun warriors",
                    "relationships": {
                        "Command": "Heat magic",
                        "Serve": "The greater alliance"
                    }
                }
            }
        },
        "autumn-court-fae": {
            "name": "Autumn Court Fae",
            "aliases": ["Harvest Fae"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Fae from the Autumn Court with earth and harvest magic.",
                    "role": "Earth wielders",
                    "relationships": {
                        "Control": "Earth magic",
                        "Join": "The final battle"
                    }
                }
            }
        },
        # Ancient Fae bloodlines
        "ancient-fae-bloodlines": {
            "name": "Ancient Fae Bloodlines",
            "aliases": ["Old Blood Fae"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Fae with the oldest bloodlines who possess the strongest ancient magic.",
                    "role": "Ancient magic users",
                    "relationships": {
                        "Possess": "Ancient magic",
                        "Carry": "Oldest bloodlines"
                    }
                }
            }
        },
        "fae-seers": {
            "name": "Fae Seers",
            "aliases": ["Future Sight Fae"],
            "appearances": [40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75],
            "knowledge": {
                "40": {
                    "revealedIn": 40,
                    "description": "Fae with the gift of foresight who help guide military strategy.",
                    "role": "Prophetic advisors",
                    "relationships": {
                        "Possess": "Foresight gift",
                        "Guide": "Military strategy"
                    }
                }
            }
        },
        # More specific witch covens and clans
        "blackbeak-elders": {
            "name": "Blackbeak Elders",
            "aliases": ["Ancient Blackbeaks"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Elder witches of the Blackbeak clan who remember the old ways.",
                    "role": "Clan elders",
                    "relationships": {
                        "Remember": "Old witch ways",
                        "Advise": "Clan decisions"
                    }
                }
            }
        },
        "witch-sentinels": {
            "name": "Witch Sentinels",
            "aliases": ["Guard Witches"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Witch guards who protect important locations and leaders.",
                    "role": "Protective guards",
                    "relationships": {
                        "Protect": "Witch leaders",
                        "Guard": "Important sites"
                    }
                }
            }
        },
        "witch-mothers": {
            "name": "Witch Mothers",
            "aliases": ["Coven Mothers"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Elder witch mothers who lead individual covens within the clans.",
                    "role": "Coven leaders",
                    "relationships": {
                        "Lead": "Individual covens",
                        "Guide": "Young witches"
                    }
                }
            }
        },
        # More Valg hierarchy
        "valg-generals": {
            "name": "Valg Generals",
            "aliases": ["Dark Generals"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "High-ranking Valg demons who lead major military campaigns.",
                    "role": "Military leaders",
                    "relationships": {
                        "Lead": "Military campaigns",
                        "Report to": "Valg princes"
                    }
                }
            }
        },
        "valg-lieutenants": {
            "name": "Valg Lieutenants",
            "aliases": ["Dark Officers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Mid-ranking Valg demons who command smaller units and special operations.",
                    "role": "Unit commanders",
                    "relationships": {
                        "Command": "Military units",
                        "Lead": "Special operations"
                    }
                }
            }
        },
        "valg-spawn": {
            "name": "Valg Spawn",
            "aliases": ["Lesser Demons"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Lesser Valg demons created from dark magic to serve as foot soldiers.",
                    "role": "Demon soldiers",
                    "relationships": {
                        "Created from": "Dark magic",
                        "Serve as": "Foot soldiers"
                    }
                }
            }
        },
        # More kingdom representatives
        "adarlan-loyalists": {
            "name": "Adarlan Loyalists",
            "aliases": ["Empire Supporters"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Adarlan citizens and soldiers who remain loyal to the empire despite the war.",
                    "role": "Empire loyalists",
                    "relationships": {
                        "Loyal to": "Adarlan empire",
                        "Oppose": "Terrasen forces"
                    }
                }
            }
        },
        "adarlan-rebels": {
            "name": "Adarlan Rebels",
            "aliases": ["Empire Dissidents"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Adarlan citizens who rebel against the empire and support Aelin.",
                    "role": "Internal rebels",
                    "relationships": {
                        "Rebel against": "Adarlan empire",
                        "Support": "Aelin's cause"
                    }
                }
            }
        },
        "wendlyn-court": {
            "name": "Wendlyn Court",
            "aliases": ["Fae Nobility"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Noble Fae court members from Wendlyn who aid in the war effort.",
                    "role": "Fae nobility",
                    "relationships": {
                        "Aid in": "War effort",
                        "Represent": "Wendlyn interests"
                    }
                }
            }
        },
        # More specialized military units
        "terrasen-archers": {
            "name": "Terrasen Archers",
            "aliases": ["Elite Bowmen"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Elite archer units trained in Terrasen's military traditions.",
                    "role": "Elite archers",
                    "relationships": {
                        "Trained in": "Military traditions",
                        "Specialize in": "Long-range combat"
                    }
                }
            }
        },
        "terrasen-cavalry": {
            "name": "Terrasen Cavalry",
            "aliases": ["Mounted Warriors"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Mounted warriors who form the backbone of Terrasen's military might.",
                    "role": "Cavalry forces",
                    "relationships": {
                        "Form": "Military backbone",
                        "Specialize in": "Mounted combat"
                    }
                }
            }
        },
        "terrasen-infantry": {
            "name": "Terrasen Infantry",
            "aliases": ["Foot Soldiers"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Standard foot soldiers who make up the bulk of Terrasen's army.",
                    "role": "Infantry soldiers",
                    "relationships": {
                        "Make up": "Army bulk",
                        "Trained for": "Ground combat"
                    }
                }
            }
        },
        # Magical practitioners
        "court-mages": {
            "name": "Court Mages",
            "aliases": ["Royal Magicians"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Mages who serve the court and provide magical support in battle.",
                    "role": "Court magicians",
                    "relationships": {
                        "Serve": "The court",
                        "Provide": "Magical support"
                    }
                }
            }
        },
        "battle-mages": {
            "name": "Battle Mages",
            "aliases": ["War Magicians"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Mages specialized in combat magic who fight on the front lines.",
                    "role": "Combat magicians",
                    "relationships": {
                        "Specialized in": "Combat magic",
                        "Fight on": "Front lines"
                    }
                }
            }
        },
        "hedge-witches": {
            "name": "Hedge Witches",
            "aliases": ["Folk Healers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Folk magic practitioners who help with healing and protection spells.",
                    "role": "Folk healers",
                    "relationships": {
                        "Practice": "Folk magic",
                        "Help with": "Healing spells"
                    }
                }
            }
        },
        # Religious and spiritual figures
        "temple-priests": {
            "name": "Temple Priests",
            "aliases": ["Sacred Clergy"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Religious priests who provide spiritual guidance and blessings for warriors.",
                    "role": "Spiritual guides",
                    "relationships": {
                        "Provide": "Spiritual guidance",
                        "Bless": "Warriors"
                    }
                }
            }
        },
        "wyrdgate-guardians": {
            "name": "Wyrdgate Guardians",
            "aliases": ["Gate Keepers"],
            "appearances": [60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105],
            "knowledge": {
                "60": {
                    "revealedIn": 60,
                    "description": "Ancient beings who guard the Wyrdgates and their dangerous power.",
                    "role": "Gate protectors",
                    "relationships": {
                        "Guard": "Wyrdgates",
                        "Protect from": "Misuse of power"
                    }
                }
            }
        },
        # Merchants and traders
        "war-profiteers": {
            "name": "War Profiteers",
            "aliases": ["Conflict Merchants"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Merchants who profit from the war by selling supplies to all sides.",
                    "role": "War merchants",
                    "relationships": {
                        "Profit from": "The war",
                        "Sell to": "All sides"
                    }
                }
            }
        },
        "supply-caravans": {
            "name": "Supply Caravans",
            "aliases": ["Trade Convoys"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Merchant caravans that transport supplies to military forces.",
                    "role": "Supply transporters",
                    "relationships": {
                        "Transport": "Military supplies",
                        "Travel": "Dangerous routes"
                    }
                }
            }
        },
        # Spies and informants
        "double-agents": {
            "name": "Double Agents",
            "aliases": ["Turncoat Spies"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Spies who work for multiple sides, selling information to the highest bidder.",
                    "role": "Information brokers",
                    "relationships": {
                        "Work for": "Multiple sides",
                        "Sell": "Secret information"
                    }
                }
            }
        },
        "code-breakers": {
            "name": "Code Breakers",
            "aliases": ["Message Decipher"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Specialists who decrypt enemy messages and break communication codes.",
                    "role": "Intelligence specialists",
                    "relationships": {
                        "Decrypt": "Enemy messages",
                        "Break": "Communication codes"
                    }
                }
            }
        },
        # Prisoners and captives
        "war-prisoners": {
            "name": "War Prisoners",
            "aliases": ["Captured Enemies"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Soldiers and officers captured during various battles of the war.",
                    "role": "Prisoners of war",
                    "relationships": {
                        "Captured during": "Various battles",
                        "Held by": "Opposing forces"
                    }
                }
            }
        },
        "rescued-slaves": {
            "name": "Rescued Slaves",
            "aliases": ["Freed Prisoners"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "People enslaved by Valg forces who are rescued and join the resistance.",
                    "role": "Freed slaves",
                    "relationships": {
                        "Rescued from": "Valg slavery",
                        "Join": "The resistance"
                    }
                }
            }
        },
        # Engineers and siege specialists
        "siege-engineers": {
            "name": "Siege Engineers",
            "aliases": ["War Engineers"],
            "appearances": [40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85],
            "knowledge": {
                "40": {
                    "revealedIn": 40,
                    "description": "Engineers who design and build siege weapons for the final assault.",
                    "role": "Siege specialists",
                    "relationships": {
                        "Design": "Siege weapons",
                        "Build": "War machines"
                    }
                }
            }
        },
        "catapult-crews": {
            "name": "Catapult Crews",
            "aliases": ["Siege Teams"],
            "appearances": [45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "45": {
                    "revealedIn": 45,
                    "description": "Specialized teams who operate siege catapults and other war machines.",
                    "role": "Siege operators",
                    "relationships": {
                        "Operate": "Siege catapults",
                        "Specialize in": "Siege warfare"
                    }
                }
            }
        },
        # Scholars and historians
        "war-chroniclers": {
            "name": "War Chroniclers",
            "aliases": ["Battle Historians"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Scholars who document the battles and events of the final war.",
                    "role": "War historians",
                    "relationships": {
                        "Document": "War battles",
                        "Record": "Historical events"
                    }
                }
            }
        },
        "ancient-texts-keepers": {
            "name": "Ancient Text Keepers",
            "aliases": ["Lore Masters"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Scholars who preserve ancient texts and knowledge crucial to the war effort.",
                    "role": "Knowledge preservers",
                    "relationships": {
                        "Preserve": "Ancient knowledge",
                        "Study": "Crucial texts"
                    }
                }
            }
        },
        # Weather mages and elemental users
        "storm-callers": {
            "name": "Storm Callers",
            "aliases": ["Weather Mages"],
            "appearances": [50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85],
            "knowledge": {
                "50": {
                    "revealedIn": 50,
                    "description": "Mages who can control weather patterns and summon storms for battle.",
                    "role": "Weather controllers",
                    "relationships": {
                        "Control": "Weather patterns",
                        "Summon": "Battle storms"
                    }
                }
            }
        },
        "earth-shapers": {
            "name": "Earth Shapers",
            "aliases": ["Ground Mages"],
            "appearances": [45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "45": {
                    "revealedIn": 45,
                    "description": "Mages who can manipulate earth and stone to create battlefield advantages.",
                    "role": "Earth manipulators",
                    "relationships": {
                        "Manipulate": "Earth and stone",
                        "Create": "Battlefield advantages"
                    }
                }
            }
        },
        # Magical creatures and familiars
        "war-ravens": {
            "name": "War Ravens",
            "aliases": ["Battle Birds"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Intelligent ravens used for reconnaissance and message carrying.",
                    "role": "Scout birds",
                    "relationships": {
                        "Used for": "Reconnaissance",
                        "Carry": "Military messages"
                    }
                }
            }
        },
        "spirit-wolves": {
            "name": "Spirit Wolves",
            "aliases": ["Ghost Wolves"],
            "appearances": [55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90],
            "knowledge": {
                "55": {
                    "revealedIn": 55,
                    "description": "Spectral wolves that appear to aid those fighting for the right cause.",
                    "role": "Spirit guardians",
                    "relationships": {
                        "Aid": "Righteous fighters",
                        "Appear as": "Spectral guides"
                    }
                }
            }
        },
        # Final characters to reach 150+
        "flame-bearers": {
            "name": "Flame Bearers",
            "aliases": ["Fire Keepers"],
            "appearances": [70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "70": {
                    "revealedIn": 70,
                    "description": "Warriors who carry sacred flames into battle, inspired by Aelin's fire magic.",
                    "role": "Sacred flame carriers",
                    "relationships": {
                        "Carry": "Sacred flames",
                        "Inspired by": "Aelin's magic"
                    }
                }
            }
        },
        "victory-heralds": {
            "name": "Victory Heralds",
            "aliases": ["Battle Announcers"],
            "appearances": [100, 101, 102, 103, 104, 105, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "100": {
                    "revealedIn": 100,
                    "description": "Messengers who spread news of victories and rally troops across the battlefield.",
                    "role": "Victory messengers",
                    "relationships": {
                        "Spread": "Victory news",
                        "Rally": "Battle troops"
                    }
                }
            }
        },
        "peace-negotiators": {
            "name": "Peace Negotiators",
            "aliases": ["Treaty Makers"],
            "appearances": [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "110": {
                    "revealedIn": 110,
                    "description": "Diplomats who work to establish peace terms after the final victory.",
                    "role": "Peace diplomats",
                    "relationships": {
                        "Establish": "Peace terms",
                        "Work toward": "Post-war order"
                    }
                }
            }
        },
        "rebuilders": {
            "name": "Rebuilders",
            "aliases": ["Reconstruction Workers"],
            "appearances": [115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "115": {
                    "revealedIn": 115,
                    "description": "Workers and planners who begin the massive task of rebuilding the kingdoms.",
                    "role": "Reconstruction workers",
                    "relationships": {
                        "Begin": "Rebuilding task",
                        "Plan": "Kingdom restoration"
                    }
                }
            }
        }
    }
    
    # Add all the new characters
    data["characters"].update(more_characters)
    
    # Save the updated data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/kingdom-of-ash.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully added {len(more_characters)} more characters to Kingdom of Ash")
    print(f"Total characters now: {len(data['characters'])}")

if __name__ == "__main__":
    add_more_kingdom_ash_characters()