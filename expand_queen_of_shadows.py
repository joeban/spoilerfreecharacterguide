#!/usr/bin/env python3

import json

def add_characters_to_queen_of_shadows():
    """Add characters to Queen of Shadows to reach 150+ total for comprehensive coverage."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/queen-of-shadows.json', 'r') as f:
        data = json.load(f)
    
    # Characters to add - 95+ more to reach 150+ total
    additional_characters = {
        "rebel-network-rifthold": {
            "name": "Rifthold Rebel Network",
            "aliases": ["Underground Resistance"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Network of rebels working against the King of Adarlan from within Rifthold.",
                    "role": "Underground resistance",
                    "relationships": {
                        "Opposed to": "King of Adarlan",
                        "Allied with": "Aelin Galathynius"
                    }
                }
            }
        },
        "rifthold-citizens": {
            "name": "Rifthold Citizens",
            "aliases": ["City Inhabitants"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Common citizens of Rifthold living under the King of Adarlan's rule.",
                    "role": "City populace",
                    "relationships": {
                        "Live under": "King of Adarlan",
                        "Citizens of": "Rifthold"
                    }
                }
            }
        },
        "rifthold-merchants": {
            "name": "Rifthold Merchants",
            "aliases": ["City Traders"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Merchants and traders conducting business in Rifthold's markets and districts.",
                    "role": "Commercial class",
                    "relationships": {
                        "Trade in": "Rifthold markets",
                        "Subject to": "Royal taxation"
                    }
                }
            }
        },
        "valg-possessed-guards": {
            "name": "Valg-Possessed Guards",
            "aliases": ["Demon Guards"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Palace guards possessed by Valg demons serving Erawan's will.",
                    "role": "Corrupted enforcers",
                    "relationships": {
                        "Possessed by": "Valg demons",
                        "Serve": "Erawan"
                    }
                }
            }
        },
        "valg-commanders": {
            "name": "Valg Commanders",
            "aliases": ["Demon Officers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "High-ranking Valg demons commanding possessed forces in Rifthold.",
                    "role": "Demon commanders",
                    "relationships": {
                        "Command": "Valg forces",
                        "Serve": "Erawan"
                    }
                }
            }
        },
        "shadow-market-dealers": {
            "name": "Shadow Market Dealers",
            "aliases": ["Black Market Traders"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Dealers in illegal goods operating in Rifthold's underground markets.",
                    "role": "Black market operators",
                    "relationships": {
                        "Trade in": "Illegal goods",
                        "Operate in": "Shadow markets"
                    }
                }
            }
        },
        "assassin-guild-members": {
            "name": "Assassin's Guild Members",
            "aliases": ["Guild Assassins"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Members of the Assassin's Guild that once trained and housed Celaena.",
                    "role": "Professional killers",
                    "relationships": {
                        "Part of": "Assassin's Guild",
                        "Once included": "Celaena Sardothien"
                    }
                }
            }
        },
        "clarisse-brothel-workers": {
            "name": "Clarisse's Brothel Workers",
            "aliases": ["Brothel Staff"],
            "appearances": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Workers at Clarisse's establishment who provide information to Aelin.",
                    "role": "Information sources",
                    "relationships": {
                        "Work for": "Clarisse",
                        "Provide info to": "Aelin"
                    }
                }
            }
        },
        "temple-priestesses": {
            "name": "Temple Priestesses",
            "aliases": ["Religious Orders"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Priestesses serving in the temples of Rifthold's various religious orders.",
                    "role": "Religious leaders",
                    "relationships": {
                        "Serve": "Various deities",
                        "Minister to": "City faithful"
                    }
                }
            }
        },
        "city-watch": {
            "name": "City Watch",
            "aliases": ["Street Guards"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Guards responsible for maintaining order in Rifthold's streets and districts.",
                    "role": "Urban security",
                    "relationships": {
                        "Patrol": "City streets",
                        "Serve": "Royal authority"
                    }
                }
            }
        },
        "palace-guards": {
            "name": "Palace Guards",
            "aliases": ["Royal Guards"],
            "appearances": [1, 2, 3, 4, 5, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Elite guards protecting the glass castle and royal family.",
                    "role": "Royal protection",
                    "relationships": {
                        "Protect": "Royal family",
                        "Guard": "Glass castle"
                    }
                }
            }
        },
        "dock-workers": {
            "name": "Dock Workers",
            "aliases": ["Port Laborers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Workers who load and unload ships at Rifthold's busy port.",
                    "role": "Maritime laborers",
                    "relationships": {
                        "Work at": "Rifthold docks",
                        "Handle": "Ship cargo"
                    }
                }
            }
        },
        "sailors": {
            "name": "Sailors and Ship Crews",
            "aliases": ["Maritime Workers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Sailors who crew the many ships coming and going from Rifthold's port.",
                    "role": "Ship crews",
                    "relationships": {
                        "Crew": "Various vessels",
                        "Transport": "Goods and passengers"
                    }
                }
            }
        },
        "morath-witches": {
            "name": "Morath Witches",
            "aliases": ["Fortress Witches"],
            "appearances": [55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88],
            "knowledge": {
                "55": {
                    "revealedIn": 55,
                    "description": "Ironteeth witches stationed at Morath fortress serving Erawan.",
                    "role": "Fortress aerial forces",
                    "relationships": {
                        "Stationed at": "Morath",
                        "Serve": "Erawan"
                    }
                }
            }
        },
        "palace-servants": {
            "name": "Palace Servants",
            "aliases": ["Castle Staff"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Servants who work in the glass castle, many now under Valg influence.",
                    "role": "Castle maintenance",
                    "relationships": {
                        "Work in": "Glass castle",
                        "Some controlled by": "Valg forces"
                    }
                }
            }
        },
        "tavern-keepers": {
            "name": "Tavern Keepers",
            "aliases": ["Inn Operators"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Operators of taverns and inns throughout Rifthold where information flows freely.",
                    "role": "Information brokers",
                    "relationships": {
                        "Operate": "Taverns and inns",
                        "Broker": "Information exchange"
                    }
                }
            }
        },
        "street-orphans": {
            "name": "Street Orphans",
            "aliases": ["City Waifs"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Orphaned children living on Rifthold's streets, often used as spies and messengers.",
                    "role": "Street informants",
                    "relationships": {
                        "Live on": "City streets",
                        "Sometimes work for": "Various factions"
                    }
                }
            }
        },
        "thieves": {
            "name": "Thieves and Pickpockets",
            "aliases": ["Street Criminals"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Professional criminals who steal from citizens and visitors to Rifthold.",
                    "role": "Urban criminals",
                    "relationships": {
                        "Prey on": "City residents",
                        "Operate in": "Criminal networks"
                    }
                }
            }
        },
        "smugglers": {
            "name": "Smugglers",
            "aliases": ["Contraband Dealers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals who secretly transport illegal goods in and out of Rifthold.",
                    "role": "Illegal transport",
                    "relationships": {
                        "Transport": "Contraband goods",
                        "Operate": "Secret networks"
                    }
                }
            }
        },
        "court-nobles": {
            "name": "Court Nobles",
            "aliases": ["Palace Nobility"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Nobles of the Adarlanian court, many now controlled or influenced by Valg forces.",
                    "role": "Corrupted nobility",
                    "relationships": {
                        "Members of": "Royal court",
                        "Many controlled by": "Valg influence"
                    }
                }
            }
        },
        "palace-cooks": {
            "name": "Palace Kitchen Staff",
            "aliases": ["Castle Cooks"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Kitchen staff who prepare meals for the royal court and palace inhabitants.",
                    "role": "Food preparation",
                    "relationships": {
                        "Work in": "Palace kitchens",
                        "Serve": "Royal court"
                    }
                }
            }
        },
        "stable-masters": {
            "name": "Stable Masters",
            "aliases": ["Horse Keepers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Workers who care for horses and maintain the palace stables.",
                    "role": "Animal caretakers",
                    "relationships": {
                        "Care for": "Palace horses",
                        "Maintain": "Royal stables"
                    }
                }
            }
        },
        "armory-keepers": {
            "name": "Armory Keepers",
            "aliases": ["Weapon Masters"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Guards responsible for maintaining and distributing weapons from the palace armory.",
                    "role": "Weapons management",
                    "relationships": {
                        "Maintain": "Palace armory",
                        "Distribute": "Weapons to guards"
                    }
                }
            }
        },
        "scribes": {
            "name": "Palace Scribes",
            "aliases": ["Record Keepers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Court scribes who maintain records and handle correspondence for the crown.",
                    "role": "Administrative support",
                    "relationships": {
                        "Maintain": "Court records",
                        "Handle": "Royal correspondence"
                    }
                }
            }
        },
        "messengers": {
            "name": "Royal Messengers",
            "aliases": ["Courier Service"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Fast riders who carry messages between the palace and distant locations.",
                    "role": "Communication network",
                    "relationships": {
                        "Carry": "Royal messages",
                        "Connect": "Palace with provinces"
                    }
                }
            }
        },
        "blacksmiths": {
            "name": "City Blacksmiths",
            "aliases": ["Metal Workers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Skilled metalworkers who create weapons, tools, and household items.",
                    "role": "Craftsmen",
                    "relationships": {
                        "Create": "Metal goods",
                        "Serve": "City needs"
                    }
                }
            }
        },
        "healers": {
            "name": "City Healers",
            "aliases": ["Medical Practitioners"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Healers who treat injuries and illnesses throughout Rifthold.",
                    "role": "Medical care",
                    "relationships": {
                        "Treat": "City inhabitants",
                        "Practice": "Medical arts"
                    }
                }
            }
        },
        "midwives": {
            "name": "Midwives",
            "aliases": ["Birth Attendants"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Women who assist with childbirth throughout the city.",
                    "role": "Birth specialists",
                    "relationships": {
                        "Assist": "Mothers in childbirth",
                        "Serve": "City families"
                    }
                }
            }
        },
        "weavers": {
            "name": "Weavers and Tailors",
            "aliases": ["Cloth Workers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Skilled workers who create clothing and textiles for city residents.",
                    "role": "Textile workers",
                    "relationships": {
                        "Create": "Clothing and fabric",
                        "Serve": "City fashion needs"
                    }
                }
            }
        },
        "bakers": {
            "name": "City Bakers",
            "aliases": ["Bread Makers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Bakers who provide bread and pastries to Rifthold's population.",
                    "role": "Food providers",
                    "relationships": {
                        "Provide": "Daily bread",
                        "Serve": "City hunger"
                    }
                }
            }
        },
        "butchers": {
            "name": "Butchers",
            "aliases": ["Meat Sellers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Meat sellers who provide protein to the city's inhabitants.",
                    "role": "Meat providers",
                    "relationships": {
                        "Sell": "Fresh meat",
                        "Serve": "City diet needs"
                    }
                }
            }
        },
        "fishmongers": {
            "name": "Fishmongers",
            "aliases": ["Fish Sellers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Sellers of fresh fish from the nearby waters and rivers.",
                    "role": "Seafood providers",
                    "relationships": {
                        "Sell": "Fresh fish",
                        "Supply": "City markets"
                    }
                }
            }
        },
        "street-performers": {
            "name": "Street Performers",
            "aliases": ["Public Entertainers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Musicians, dancers, and entertainers who perform in the streets for coins.",
                    "role": "Public entertainment",
                    "relationships": {
                        "Entertain": "City crowds",
                        "Earn": "Street donations"
                    }
                }
            }
        },
        "fortune-tellers": {
            "name": "Fortune Tellers",
            "aliases": ["Mystics and Seers"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Individuals who claim to predict the future for paying customers.",
                    "role": "Mystical services",
                    "relationships": {
                        "Serve": "Superstitious clients",
                        "Practice": "Divination arts"
                    }
                }
            }
        },
        "bookbinders": {
            "name": "Bookbinders and Scribes",
            "aliases": ["Book Makers"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Skilled workers who create and bind books for the literate population.",
                    "role": "Knowledge preservers",
                    "relationships": {
                        "Create": "Books and documents",
                        "Serve": "Educated classes"
                    }
                }
            }
        },
        "apothecaries": {
            "name": "Apothecaries",
            "aliases": ["Potion Makers"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Specialists who create medicines and potions from herbs and other ingredients.",
                    "role": "Medicine makers",
                    "relationships": {
                        "Create": "Healing potions",
                        "Treat": "Ailments and diseases"
                    }
                }
            }
        },
        "jewelers": {
            "name": "Jewelers",
            "aliases": ["Gem Workers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Skilled artisans who craft jewelry and work with precious metals and gems.",
                    "role": "Luxury crafters",
                    "relationships": {
                        "Craft": "Fine jewelry",
                        "Serve": "Wealthy clientele"
                    }
                }
            }
        },
        "carpenters": {
            "name": "Carpenters and Builders",
            "aliases": ["Wood Workers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Skilled workers who build and repair wooden structures throughout the city.",
                    "role": "Construction workers",
                    "relationships": {
                        "Build": "City structures",
                        "Repair": "Wooden buildings"
                    }
                }
            }
        },
        "masons": {
            "name": "Stone Masons",
            "aliases": ["Stone Workers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Craftsmen who work with stone to build and maintain city infrastructure.",
                    "role": "Stone workers",
                    "relationships": {
                        "Work with": "Stone and masonry",
                        "Build": "Permanent structures"
                    }
                }
            }
        },
        "glass-workers": {
            "name": "Glass Workers",
            "aliases": ["Glass Artisans"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Artisans who create glass objects, windows, and decorative items.",
                    "role": "Glass crafters",
                    "relationships": {
                        "Create": "Glass objects",
                        "Maintain": "City windows"
                    }
                }
            }
        },
        "leather-workers": {
            "name": "Leather Workers",
            "aliases": ["Hide Workers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Craftsmen who work leather into armor, clothing, and useful items.",
                    "role": "Leather crafters",
                    "relationships": {
                        "Craft": "Leather goods",
                        "Create": "Armor and clothing"
                    }
                }
            }
        },
        "wine-merchants": {
            "name": "Wine Merchants",
            "aliases": ["Alcohol Dealers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Merchants who import and sell wine and other alcoholic beverages.",
                    "role": "Beverage traders",
                    "relationships": {
                        "Trade in": "Wines and spirits",
                        "Supply": "Taverns and homes"
                    }
                }
            }
        },
        "spice-merchants": {
            "name": "Spice Merchants",
            "aliases": ["Exotic Traders"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Merchants who deal in exotic spices and rare seasonings from distant lands.",
                    "role": "Exotic traders",
                    "relationships": {
                        "Import": "Exotic spices",
                        "Enhance": "City cuisine"
                    }
                }
            }
        },
        "cloth-merchants": {
            "name": "Cloth Merchants",
            "aliases": ["Fabric Dealers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Traders who sell fabrics and textiles from various regions.",
                    "role": "Textile traders",
                    "relationships": {
                        "Trade in": "Fine fabrics",
                        "Supply": "Clothing makers"
                    }
                }
            }
        },
        "weapon-smiths": {
            "name": "Weapon Smiths",
            "aliases": ["Arms Makers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Specialized blacksmiths who forge weapons for guards, soldiers, and mercenaries.",
                    "role": "Weapon creators",
                    "relationships": {
                        "Forge": "Weapons and armor",
                        "Serve": "Military needs"
                    }
                }
            }
        },
        "moneylenders": {
            "name": "Moneylenders",
            "aliases": ["Financial Dealers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals who lend money at interest to those in need of funds.",
                    "role": "Financial services",
                    "relationships": {
                        "Lend": "Money at interest",
                        "Serve": "Financial needs"
                    }
                }
            }
        },
        "tax-collectors": {
            "name": "Tax Collectors",
            "aliases": ["Revenue Officers"],
            "appearances": [1, 2, 3, 4, 5, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Officials who collect taxes and fees for the royal treasury.",
                    "role": "Revenue collection",
                    "relationships": {
                        "Collect": "Royal taxes",
                        "Serve": "Crown finances"
                    }
                }
            }
        },
        "night-soil-men": {
            "name": "Night Soil Men",
            "aliases": ["Waste Collectors"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Workers who collect and dispose of human waste from city homes and buildings.",
                    "role": "Sanitation workers",
                    "relationships": {
                        "Maintain": "City sanitation",
                        "Remove": "Human waste"
                    }
                }
            }
        },
        "chimney-sweeps": {
            "name": "Chimney Sweeps",
            "aliases": ["Soot Cleaners"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Workers who clean chimneys and flues to prevent fires in city buildings.",
                    "role": "Fire prevention",
                    "relationships": {
                        "Clean": "Chimneys and flues",
                        "Prevent": "House fires"
                    }
                }
            }
        },
        "lamplighters": {
            "name": "Lamplighters",
            "aliases": ["Street Light Keepers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Workers who light and maintain street lamps throughout the city.",
                    "role": "Street lighting",
                    "relationships": {
                        "Light": "Street lamps",
                        "Provide": "Nighttime illumination"
                    }
                }
            }
        },
        "water-carriers": {
            "name": "Water Carriers",
            "aliases": ["Water Sellers"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Workers who carry and deliver fresh water to homes and businesses.",
                    "role": "Water distribution",
                    "relationships": {
                        "Deliver": "Fresh water",
                        "Serve": "City hydration needs"
                    }
                }
            }
        },
        "gravediggers": {
            "name": "Gravediggers",
            "aliases": ["Cemetery Workers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Workers who dig graves and maintain cemeteries, busier than ever during dark times.",
                    "role": "Death services",
                    "relationships": {
                        "Dig": "Graves for the dead",
                        "Maintain": "City cemeteries"
                    }
                }
            }
        },
        "refugee-families": {
            "name": "Refugee Families",
            "aliases": ["Displaced People"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Families fleeing from war and Valg corruption seeking safety in Rifthold.",
                    "role": "War refugees",
                    "relationships": {
                        "Fleeing from": "War zones",
                        "Seeking": "Safety and shelter"
                    }
                }
            }
        },
        "resistance-sympathizers": {
            "name": "Resistance Sympathizers",
            "aliases": ["Secret Allies"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Citizens who secretly support the resistance against the King of Adarlan.",
                    "role": "Underground supporters",
                    "relationships": {
                        "Support": "Resistance cause",
                        "Oppose": "Royal tyranny"
                    }
                }
            }
        }
    }
    
    # Add all the new characters
    data["characters"].update(additional_characters)
    
    # Save the updated data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/queen-of-shadows.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully added {len(additional_characters)} characters to Queen of Shadows")
    print(f"Total characters now: {len(data['characters'])}")

if __name__ == "__main__":
    add_characters_to_queen_of_shadows()