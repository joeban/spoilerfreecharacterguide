#!/usr/bin/env python3
import json

# Load existing data
with open('data/witcher/lady-of-the-lake.json', 'r') as f:
    data = json.load(f)

# Add more characters for Lady of the Lake
new_characters = {
    "lodge-associate-vera-loewenhaupt": {
        "name": "Sorceress Vera Loewenhaupt",
        "aliases": ["The Young Lodge Member"],
        "appearances": [5, 6, 7],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "A younger sorceress associated with the Lodge who represents the next generation of magical politicians.",
                "role": "Lodge associate",
                "relationships": {
                    "Lodge of Sorceresses": "Junior member of",
                    "Political Intrigue": "Learning"
                }
            }
        }
    },
    "lodge-servant-quartermaster": {
        "name": "Quartermaster Cantarella",
        "aliases": ["The Lodge's Servant"],
        "appearances": [5, 6, 7],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "A trusted servant who manages the Lodge's material needs and sometimes serves as a messenger between members.",
                "role": "Lodge quartermaster",
                "relationships": {
                    "Lodge of Sorceresses": "Serves",
                    "Secret Communications": "Facilitates"
                }
            }
        }
    },
    "aen-elle-court-guard-captain": {
        "name": "Captain Ge'els",
        "aliases": ["The Court Guardian"],
        "appearances": [6, 7, 8],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "The captain of Auberon's personal guard, representing the military might of the Aen Elle court.",
                "role": "Elven guard captain",
                "relationships": {
                    "Auberon Muircetach": "Personal guard of",
                    "Aen Elle Court": "Protects"
                }
            }
        }
    },
    "aen-elle-court-servant-attendant": {
        "name": "Court Attendant Lara",
        "aliases": ["The Faithful Servant"],
        "appearances": [6, 7, 8],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "A servant at the Aen Elle court who attends to the needs of the royal family and guests.",
                "role": "Court servant",
                "relationships": {
                    "Aen Elle Royalty": "Serves",
                    "Court Protocol": "Maintains"
                }
            }
        }
    },
    "future-chronicler-apprentice": {
        "name": "Chronicler Apprentice Marigold",
        "aliases": ["The Young Historian"],
        "appearances": [11, 12],
        "knowledge": {
            "11": {
                "revealedIn": 11,
                "description": "An apprentice historian who works with the future chroniclers to preserve the true stories of Geralt and Ciri.",
                "role": "Apprentice chronicler",
                "relationships": {
                    "Nimue": "Studies under",
                    "Historical Truth": "Dedicated to preserving"
                }
            }
        }
    },
    "future-chronicler-archivist": {
        "name": "Archivist Cornelius",
        "aliases": ["The Keeper of Records"],
        "appearances": [11, 12],
        "knowledge": {
            "11": {
                "revealedIn": 11,
                "description": "A future archivist who maintains the records and documents that chronicle the age of Geralt and the witchers.",
                "role": "Historical archivist",
                "relationships": {
                    "Historical Records": "Maintains",
                    "Future Generations": "Preserves knowledge for"
                }
            }
        }
    },
    "ceremony-attendee-noble-lady": {
        "name": "Lady Orianna of Beauclair",
        "aliases": ["The Noble Witness"],
        "appearances": [12],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "A noble lady who attends important ceremonies and represents the high society's witness to historical events.",
                "role": "Noble witness",
                "relationships": {
                    "High Society": "Member of",
                    "Important Ceremonies": "Attends"
                }
            }
        }
    },
    "ceremony-attendee-knight": {
        "name": "Sir Palmerin of Oliva",
        "aliases": ["The Ceremony Knight"],
        "appearances": [12],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "A knight who participates in the final ceremonies and represents the chivalric order's recognition of legendary deeds.",
                "role": "Ceremonial knight",
                "relationships": {
                    "Chivalric Order": "Member of",
                    "Final Ceremonies": "Participates in"
                }
            }
        }
    },
    "refugee-leader-elder": {
        "name": "Elder Refugee Blath",
        "aliases": ["The Survivor Elder"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "An elderly refugee who survived the various conflicts and represents the civilian cost of the wars.",
                "role": "Refugee elder",
                "relationships": {
                    "War Refugees": "Leads and protects",
                    "Survival Community": "Elder of"
                }
            }
        }
    },
    "refugee-child-orphan": {
        "name": "Orphan Child Milla",
        "aliases": ["The War Orphan"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "A child orphaned by the wars who represents the innocent victims and the future generation affected by the conflicts.",
                "role": "War orphan",
                "relationships": {
                    "Refugee Community": "Protected by",
                    "Future Generation": "Represents"
                }
            }
        }
    },
    "arthurian-squire-gareth": {
        "name": "Squire Bedevere",
        "aliases": ["Young Squire"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "A young squire in training at Arthur's court, representing the next generation of knights learning the chivalric code.",
                "role": "Knight-in-training",
                "relationships": {
                    "Round Table": "Aspires to join",
                    "Arthur's Court": "Serves"
                }
            }
        }
    },
    "arthurian-court-lady": {
        "name": "Lady Lynette",
        "aliases": ["Court Maiden"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "A lady of Arthur's court who represents the refined culture and courtly ideals of Camelot.",
                "role": "Court lady",
                "relationships": {
                    "Queen Guinevere": "Lady-in-waiting to",
                    "Camelot": "Embodies ideals of"
                }
            }
        }
    },
    "arthurian-herald": {
        "name": "Herald Blanchefleur",
        "aliases": ["The Royal Herald"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "The royal herald who announces important events and maintains the ceremonial traditions of Arthur's court.",
                "role": "Royal herald",
                "relationships": {
                    "King Arthur": "Official herald of",
                    "Court Ceremonies": "Conducts"
                }
            }
        }
    },
    "arthurian-bard": {
        "name": "Court Bard Taliesin",
        "aliases": ["The Storyteller"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "The court bard who preserves the legends and songs of Arthur's realm, similar to Dandelion's role.",
                "role": "Court chronicler",
                "relationships": {
                    "Arthurian Legend": "Preserves",
                    "Camelot": "Entertains court of"
                }
            }
        }
    },
    "arthurian-page": {
        "name": "Page Dinadan",
        "aliases": ["The Young Page"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "A young page at Arthur's court who serves the knights and learns the ways of chivalry.",
                "role": "Court page",
                "relationships": {
                    "Knights of Round Table": "Serves",
                    "Court Hierarchy": "Beginning of"
                }
            }
        }
    },
    "battle-brenna-archer-captain": {
        "name": "Archer Captain Milva-Minor",
        "aliases": ["The Bowmaster"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "An archer captain who leads ranged troops during the Battle of Brenna, drawing inspiration from Milva's legendary skill.",
                "role": "Archery commander",
                "relationships": {
                    "Archer Units": "Commands",
                    "Military Strategy": "Supports with range"
                }
            }
        }
    },
    "battle-brenna-engineer": {
        "name": "Siege Engineer Torrhen",
        "aliases": ["The Battlemaster"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A military engineer who designs and operates siege equipment during the Battle of Brenna.",
                "role": "Siege engineer",
                "relationships": {
                    "Siege Equipment": "Operates",
                    "Military Engineering": "Expert in"
                }
            }
        }
    },
    "battle-brenna-scout": {
        "name": "Scout Pathfinder Caed",
        "aliases": ["The Wayfinder"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A military scout who provides crucial intelligence during the Battle of Brenna, mapping enemy positions.",
                "role": "Military scout",
                "relationships": {
                    "Intelligence Gathering": "Specializes in",
                    "Battle Planning": "Supports"
                }
            }
        }
    },
    "battle-brenna-quartermaster": {
        "name": "Quartermaster Supplies-Keeper",
        "aliases": ["The Provisioner"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "The quartermaster who manages supplies and logistics during the Battle of Brenna, ensuring troops are fed and equipped.",
                "role": "Military quartermaster",
                "relationships": {
                    "Supply Lines": "Manages",
                    "Troop Support": "Provides"
                }
            }
        }
    },
    "battle-brenna-messenger": {
        "name": "Battle Messenger Swift-Runner",
        "aliases": ["The Courier"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A fast messenger who carries orders and reports across the battlefield during the Battle of Brenna.",
                "role": "Battlefield messenger",
                "relationships": {
                    "Command Structure": "Connects",
                    "Battle Communications": "Maintains"
                }
            }
        }
    },
    "rivia-civilian-baker": {
        "name": "Baker Goodwife Marta",
        "aliases": ["The Bread Maker"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "A civilian baker in Rivia who gets caught up in the pogrom, representing ordinary citizens affected by the violence.",
                "role": "Civilian baker",
                "relationships": {
                    "Rivia Community": "Serves",
                    "Pogrom Violence": "Victim of"
                }
            }
        }
    },
    "rivia-civilian-blacksmith": {
        "name": "Blacksmith Ironhand Jonas",
        "aliases": ["The Smith"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "A blacksmith in Rivia who witnesses the pogrom and represents the working class caught in racial violence.",
                "role": "Town blacksmith",
                "relationships": {
                    "Rivia Trades": "Important member of",
                    "Civil Unrest": "Witnesses"
                }
            }
        }
    },
    "rivia-civilian-merchant": {
        "name": "Merchant Tradesman Copper",
        "aliases": ["The Trader"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "A merchant in Rivia who loses his business during the pogrom, representing the economic cost of civil unrest.",
                "role": "Local merchant",
                "relationships": {
                    "Rivia Economy": "Contributes to",
                    "Pogrom Losses": "Suffers from"
                }
            }
        }
    },
    "rivia-healer-woman": {
        "name": "Healer Goodwoman Sage",
        "aliases": ["The Medicine Woman"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "A local healer in Rivia who tends to the wounded during the pogrom, representing those who help regardless of race.",
                "role": "Folk healer",
                "relationships": {
                    "Pogrom Wounded": "Treats all",
                    "Community Healing": "Provides"
                }
            }
        }
    },
    "rivia-tavern-keeper": {
        "name": "Tavern Keeper Old Henrik",
        "aliases": ["The Innkeeper"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "The keeper of a tavern in Rivia who sees his establishment destroyed in the pogrom violence.",
                "role": "Tavern owner",
                "relationships": {
                    "Rivia Hospitality": "Provides",
                    "Pogrom Destruction": "Victim of"
                }
            }
        }
    },
    "stygga-castle-archer": {
        "name": "Castle Archer Longbow-Lars",
        "aliases": ["The Defender"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A skilled archer defending Stygga castle against Geralt's assault, representing the rank-and-file defenders.",
                "role": "Castle archer",
                "relationships": {
                    "Castle Defenses": "Part of",
                    "Vilgefortz Forces": "Serves"
                }
            }
        }
    },
    "stygga-castle-guard": {
        "name": "Castle Guard Steel-Arm Sam",
        "aliases": ["The Sentinel"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A regular guard at Stygga castle who fights against Geralt's rescue mission.",
                "role": "Castle guard",
                "relationships": {
                    "Castle Security": "Maintains",
                    "Final Battle": "Participant in"
                }
            }
        }
    },
    "stygga-castle-servant": {
        "name": "Castle Servant Fearful-Flora",
        "aliases": ["The Domestic"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A servant at Stygga castle who gets caught up in the battle, representing innocent civilians in warzones.",
                "role": "Castle servant",
                "relationships": {
                    "Castle Household": "Serves",
                    "Battle Chaos": "Caught in"
                }
            }
        }
    },
    "stygga-castle-cook": {
        "name": "Castle Cook Hearth-Heart Hilda",
        "aliases": ["The Kitchen Master"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "The head cook at Stygga castle who maintains the kitchens even during the siege.",
                "role": "Castle cook",
                "relationships": {
                    "Castle Provisions": "Manages",
                    "Domestic Staff": "Leads"
                }
            }
        }
    },
    "wild-hunt-rider": {
        "name": "Wild Hunt Rider Frost-Mane",
        "aliases": ["The Spectral Rider"],
        "appearances": [6, 7, 9],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "A rider in the Wild Hunt who pursues Ciri across dimensions, representing the otherworldly threat.",
                "role": "Spectral hunter",
                "relationships": {
                    "Wild Hunt": "Rides with",
                    "Ciri": "Pursues"
                }
            }
        }
    },
    "wild-hunt-hound-master": {
        "name": "Hound Master of the Hunt",
        "aliases": ["The Beast Caller"],
        "appearances": [6, 7, 9],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "The master of the spectral hounds that accompany the Wild Hunt in their pursuit of Ciri.",
                "role": "Spectral beast master",
                "relationships": {
                    "Wild Hunt": "Provides beasts for",
                    "Spectral Hounds": "Commands"
                }
            }
        }
    }
}

# Add characters to existing data
for char_id, char_data in new_characters.items():
    data['characters'][char_id] = char_data

print(f"Adding {len(new_characters)} more characters to Lady of the Lake")
print(f"New total: {len(data['characters'])} characters")

# Save updated data
with open('data/witcher/lady-of-the-lake.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✅ Lady of the Lake updated successfully!")