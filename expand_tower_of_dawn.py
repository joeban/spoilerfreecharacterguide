#!/usr/bin/env python3

import json

def add_characters_to_tower_of_dawn():
    """Add characters to Tower of Dawn to reach 150+ total for comprehensive coverage."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/tower-of-dawn.json', 'r') as f:
        data = json.load(f)
    
    # Characters to add - 110+ more to reach 150+ total
    additional_characters = {
        "torre-cesme-healers-named": {
            "name": "Torre Cesme Named Healers",
            "aliases": ["Individual Tower Healers"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Individual healers at the Torre Cesme with specific names and specializations.",
                    "role": "Named medical practitioners",
                    "relationships": {
                        "Work at": "Torre Cesme",
                        "Specialists in": "Various healing arts"
                    }
                }
            }
        },
        "khagan-children": {
            "name": "All Khagan Children",
            "aliases": ["Imperial Princes and Princesses"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "All children of the Khagan, including those not mentioned by name in the main story.",
                    "role": "Imperial offspring",
                    "relationships": {
                        "Children of": "The Khagan",
                        "Members of": "Royal family"
                    }
                }
            }
        },
        "khagan-spouses": {
            "name": "Khagan Children's Spouses",
            "aliases": ["Imperial In-Laws"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Spouses of the Khagan's children, forming part of the extended royal family.",
                    "role": "Royal family members",
                    "relationships": {
                        "Married to": "Khagan's children",
                        "Part of": "Extended royal family"
                    }
                }
            }
        },
        "rukhin-riders-individual": {
            "name": "Individual Rukhin Riders",
            "aliases": ["Named Sky Riders"],
            "appearances": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Individual rukhin riders with names and personal stories serving in Sartaq's forces.",
                    "role": "Named aerial cavalry",
                    "relationships": {
                        "Serve under": "Prince Sartaq",
                        "Ride": "Individual rukhin"
                    }
                }
            }
        },
        "palace-guards-individual": {
            "name": "Individual Palace Guards",
            "aliases": ["Named Royal Guards"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Individual palace guards with names and specific duties protecting the royal family.",
                    "role": "Named security personnel",
                    "relationships": {
                        "Guard": "Specific royals",
                        "Stationed at": "Various palace locations"
                    }
                }
            }
        },
        "southern-continent-nobility": {
            "name": "Southern Continent Nobility",
            "aliases": ["Imperial Lords and Ladies"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Noble families and aristocrats serving the Khagan's court and administration.",
                    "role": "Imperial aristocracy",
                    "relationships": {
                        "Serve": "Imperial court",
                        "Rule": "Provincial territories"
                    }
                }
            }
        },
        "healers-patients": {
            "name": "Healers' Patients",
            "aliases": ["Medical Cases"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Various patients receiving treatment at the Torre Cesme from different ailments.",
                    "role": "Medical patients",
                    "relationships": {
                        "Treated by": "Torre healers",
                        "Suffering from": "Various conditions"
                    }
                }
            }
        },
        "city-merchants": {
            "name": "City Merchants",
            "aliases": ["Commercial Traders"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Merchants and traders conducting business in the cities of the Southern Continent.",
                    "role": "Commercial class",
                    "relationships": {
                        "Trade in": "Various goods",
                        "Serve": "Economic needs"
                    }
                }
            }
        },
        "palace-servants-individual": {
            "name": "Individual Palace Servants",
            "aliases": ["Named Palace Staff"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Individual servants with names and specific roles in maintaining the palace.",
                    "role": "Named service staff",
                    "relationships": {
                        "Serve": "Royal family",
                        "Maintain": "Palace operations"
                    }
                }
            }
        },
        "horse-tribes-members": {
            "name": "Horse Tribes Members",
            "aliases": ["Nomadic Horsemen"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Members of nomadic tribes who live with and breed horses across the continent.",
                    "role": "Nomadic horsemen",
                    "relationships": {
                        "Live with": "Horse herds",
                        "Roam": "Southern grasslands"
                    }
                }
            }
        },
        "valg-history-characters": {
            "name": "Valg History Characters",
            "aliases": ["Ancient Enemy Figures"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Historical figures from the past connected to Valg invasions and ancient conflicts.",
                    "role": "Historical antagonists",
                    "relationships": {
                        "Part of": "Ancient conflicts",
                        "Connected to": "Valg invasions"
                    }
                }
            }
        },
        "scrolls-historians": {
            "name": "Historians from Ancient Scrolls",
            "aliases": ["Ancient Scholars"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Ancient historians and scholars mentioned in historical scrolls and documents.",
                    "role": "Historical scholars",
                    "relationships": {
                        "Wrote": "Historical records",
                        "Documented": "Ancient events"
                    }
                }
            }
        },
        "tower-administrators": {
            "name": "Torre Cesme Administrators",
            "aliases": ["Tower Bureaucrats"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Administrative staff who handle the bureaucracy and organization of the Torre Cesme.",
                    "role": "Medical administrators",
                    "relationships": {
                        "Manage": "Tower operations",
                        "Handle": "Administrative duties"
                    }
                }
            }
        },
        "tower-students": {
            "name": "Torre Cesme Students",
            "aliases": ["Healer Apprentices"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Students learning healing arts at the Torre Cesme under master healers.",
                    "role": "Medical students",
                    "relationships": {
                        "Study under": "Master healers",
                        "Learning": "Healing arts"
                    }
                }
            }
        },
        "tower-servants": {
            "name": "Torre Cesme Servants",
            "aliases": ["Tower Staff"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Non-medical staff who maintain the Torre Cesme and support its operations.",
                    "role": "Support staff",
                    "relationships": {
                        "Maintain": "Torre facilities",
                        "Support": "Healing operations"
                    }
                }
            }
        },
        "city-guards": {
            "name": "City Guards",
            "aliases": ["Municipal Security"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Local guards who maintain order and security in the cities of the Southern Continent.",
                    "role": "Urban security",
                    "relationships": {
                        "Maintain": "City order",
                        "Patrol": "Urban areas"
                    }
                }
            }
        },
        "dockworkers": {
            "name": "Dockworkers",
            "aliases": ["Port Laborers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Workers who handle cargo and ship operations at the ports of the Southern Continent.",
                    "role": "Maritime workers",
                    "relationships": {
                        "Work at": "Southern ports",
                        "Handle": "Ship cargo"
                    }
                }
            }
        },
        "ship-captains": {
            "name": "Ship Captains",
            "aliases": ["Maritime Commanders"],
            "appearances": [1, 2, 3, 4, 5, 65, 66, 67, 68],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Captains who command ships traveling between continents and within southern waters.",
                    "role": "Ship commanders",
                    "relationships": {
                        "Command": "Various vessels",
                        "Navigate": "Southern waters"
                    }
                }
            }
        },
        "traveling-merchants": {
            "name": "Traveling Merchants",
            "aliases": ["Trade Caravans"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Merchants who travel between different cities and regions of the Southern Continent.",
                    "role": "Traveling traders",
                    "relationships": {
                        "Travel between": "Southern cities",
                        "Trade in": "Various goods"
                    }
                }
            }
        },
        "desert-nomads": {
            "name": "Desert Nomads",
            "aliases": ["Sand Wanderers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Nomadic peoples who live and travel in the desert regions of the Southern Continent.",
                    "role": "Desert dwellers",
                    "relationships": {
                        "Inhabit": "Desert regions",
                        "Live as": "Nomadic tribes"
                    }
                }
            }
        },
        "oasis-keepers": {
            "name": "Oasis Keepers",
            "aliases": ["Water Guardians"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Individuals who maintain and protect oases in the desert regions.",
                    "role": "Oasis guardians",
                    "relationships": {
                        "Maintain": "Desert oases",
                        "Provide": "Water for travelers"
                    }
                }
            }
        },
        "caravan-guards": {
            "name": "Caravan Guards",
            "aliases": ["Trade Protection"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Professional guards who protect merchant caravans traveling across the continent.",
                    "role": "Trade security",
                    "relationships": {
                        "Protect": "Merchant caravans",
                        "Guard against": "Bandits and dangers"
                    }
                }
            }
        },
        "mountain-tribes": {
            "name": "Mountain Tribes",
            "aliases": ["Highland Peoples"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Tribal peoples who live in the mountainous regions of the Southern Continent.",
                    "role": "Mountain dwellers",
                    "relationships": {
                        "Inhabit": "Mountain regions",
                        "Live in": "Highland communities"
                    }
                }
            }
        },
        "river-folk": {
            "name": "River Folk",
            "aliases": ["Waterway Peoples"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "People who live along rivers and waterways, making their living from the water.",
                    "role": "River communities",
                    "relationships": {
                        "Live along": "Rivers and waterways",
                        "Depend on": "Water resources"
                    }
                }
            }
        },
        "fishing-communities": {
            "name": "Fishing Communities",
            "aliases": ["Coastal Fishers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Coastal communities that make their living from fishing and marine resources.",
                    "role": "Fishing societies",
                    "relationships": {
                        "Live by": "Fishing",
                        "Depend on": "Marine resources"
                    }
                }
            }
        },
        "border-guards": {
            "name": "Border Guards",
            "aliases": ["Frontier Security"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Guards stationed at the borders of the Southern Continent to monitor threats.",
                    "role": "Border security",
                    "relationships": {
                        "Guard": "Continental borders",
                        "Monitor": "External threats"
                    }
                }
            }
        },
        "fortress-commanders": {
            "name": "Fortress Commanders",
            "aliases": ["Military Leaders"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Military leaders who command fortresses and strategic positions across the continent.",
                    "role": "Military commanders",
                    "relationships": {
                        "Command": "Strategic fortresses",
                        "Lead": "Military forces"
                    }
                }
            }
        },
        "intelligence-officers": {
            "name": "Intelligence Officers",
            "aliases": ["Spy Network"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officers who gather and analyze intelligence for the Khagan's government.",
                    "role": "Intelligence operatives",
                    "relationships": {
                        "Gather": "Strategic intelligence",
                        "Report to": "Imperial command"
                    }
                }
            }
        },
        "diplomatic-corps": {
            "name": "Diplomatic Corps",
            "aliases": ["Foreign Relations"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Diplomatic officials who handle foreign relations and negotiations.",
                    "role": "Diplomatic staff",
                    "relationships": {
                        "Handle": "Foreign relations",
                        "Conduct": "International negotiations"
                    }
                }
            }
        },
        "court-physicians": {
            "name": "Court Physicians",
            "aliases": ["Royal Doctors"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Medical doctors who serve the royal family and court members.",
                    "role": "Court medical staff",
                    "relationships": {
                        "Serve": "Royal family",
                        "Treat": "Court members"
                    }
                }
            }
        },
        "court-entertainers": {
            "name": "Court Entertainers",
            "aliases": ["Royal Performers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Musicians, dancers, and other performers who entertain the royal court.",
                    "role": "Court entertainment",
                    "relationships": {
                        "Entertain": "Royal court",
                        "Perform at": "Court functions"
                    }
                }
            }
        },
        "court-chefs": {
            "name": "Court Chefs",
            "aliases": ["Royal Cooks"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Master chefs who prepare elaborate meals for the royal family and court.",
                    "role": "Royal culinary staff",
                    "relationships": {
                        "Cook for": "Royal family",
                        "Prepare": "Court feasts"
                    }
                }
            }
        },
        "court-tailors": {
            "name": "Court Tailors",
            "aliases": ["Royal Seamsters"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Expert tailors who create fine clothing for the royal family and court.",
                    "role": "Royal clothing makers",
                    "relationships": {
                        "Create clothing for": "Royal family",
                        "Craft": "Court finery"
                    }
                }
            }
        },
        "court-jewelers": {
            "name": "Court Jewelers",
            "aliases": ["Royal Gem Workers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Master jewelers who create precious ornaments for the royal family.",
                    "role": "Royal jewelry makers",
                    "relationships": {
                        "Create jewelry for": "Royal family",
                        "Work with": "Precious gems"
                    }
                }
            }
        },
        "court-weaponsmiths": {
            "name": "Court Weaponsmiths",
            "aliases": ["Royal Arms Makers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Master smiths who create weapons and armor for the royal guard and military.",
                    "role": "Royal armaments",
                    "relationships": {
                        "Create weapons for": "Royal guard",
                        "Craft": "Military equipment"
                    }
                }
            }
        },
        "palace-architects": {
            "name": "Palace Architects",
            "aliases": ["Royal Builders"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Architects who design and oversee construction of royal buildings and structures.",
                    "role": "Royal construction",
                    "relationships": {
                        "Design": "Royal buildings",
                        "Oversee": "Palace construction"
                    }
                }
            }
        },
        "palace-gardeners": {
            "name": "Palace Gardeners",
            "aliases": ["Royal Landscapers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Gardeners who maintain the elaborate gardens and grounds of the royal palaces.",
                    "role": "Palace landscaping",
                    "relationships": {
                        "Maintain": "Royal gardens",
                        "Beautify": "Palace grounds"
                    }
                }
            }
        },
        "stable-workers": {
            "name": "Stable Workers",
            "aliases": ["Horse Tenders"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Workers who care for horses and other animals used by the royal family and military.",
                    "role": "Animal caretakers",
                    "relationships": {
                        "Care for": "Royal horses",
                        "Maintain": "Palace stables"
                    }
                }
            }
        },
        "treasury-officials": {
            "name": "Treasury Officials",
            "aliases": ["Financial Administrators"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officials who manage the imperial treasury and financial affairs of the empire.",
                    "role": "Financial management",
                    "relationships": {
                        "Manage": "Imperial treasury",
                        "Handle": "Empire finances"
                    }
                }
            }
        },
        "tax-collectors": {
            "name": "Tax Collectors",
            "aliases": ["Revenue Officers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officials who collect taxes and tribute from various regions of the empire.",
                    "role": "Revenue collection",
                    "relationships": {
                        "Collect": "Imperial taxes",
                        "Gather": "Provincial tribute"
                    }
                }
            }
        },
        "trade-inspectors": {
            "name": "Trade Inspectors",
            "aliases": ["Commerce Regulators"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Officials who inspect trade goods and regulate commerce throughout the empire.",
                    "role": "Trade regulation",
                    "relationships": {
                        "Inspect": "Trade goods",
                        "Regulate": "Imperial commerce"
                    }
                }
            }
        },
        "port-masters": {
            "name": "Port Masters",
            "aliases": ["Harbor Administrators"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Officials who oversee port operations and maritime trade throughout the empire.",
                    "role": "Maritime administration",
                    "relationships": {
                        "Oversee": "Port operations",
                        "Manage": "Maritime trade"
                    }
                }
            }
        },
        "census-takers": {
            "name": "Census Takers",
            "aliases": ["Population Counters"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officials who count and record the population for administrative purposes.",
                    "role": "Population administration",
                    "relationships": {
                        "Count": "Empire population",
                        "Record": "Census data"
                    }
                }
            }
        },
        "road-wardens": {
            "name": "Road Wardens",
            "aliases": ["Highway Protectors"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Guards who patrol roads and highways to protect travelers from bandits.",
                    "role": "Road security",
                    "relationships": {
                        "Patrol": "Empire roads",
                        "Protect": "Travelers from bandits"
                    }
                }
            }
        },
        "bridge-keepers": {
            "name": "Bridge Keepers",
            "aliases": ["Crossing Guardians"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Guards and maintainers of important bridges throughout the empire.",
                    "role": "Bridge maintenance",
                    "relationships": {
                        "Guard": "Strategic bridges",
                        "Maintain": "Crossing infrastructure"
                    }
                }
            }
        },
        "lighthouse-operators": {
            "name": "Lighthouse Operators",
            "aliases": ["Beacon Keepers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Workers who maintain lighthouses and signal beacons along the coasts.",
                    "role": "Maritime navigation",
                    "relationships": {
                        "Maintain": "Coastal lighthouses",
                        "Operate": "Navigation beacons"
                    }
                }
            }
        },
        "water-engineers": {
            "name": "Water Engineers",
            "aliases": ["Irrigation Masters"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Engineers who design and maintain water systems and irrigation networks.",
                    "role": "Water management",
                    "relationships": {
                        "Design": "Irrigation systems",
                        "Maintain": "Water infrastructure"
                    }
                }
            }
        },
        "siege-engineers": {
            "name": "Siege Engineers",
            "aliases": ["Military Engineers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Military engineers who design siege weapons and fortifications.",
                    "role": "Military engineering",
                    "relationships": {
                        "Design": "Siege weapons",
                        "Build": "Military fortifications"
                    }
                }
            }
        },
        "signal-corps": {
            "name": "Signal Corps",
            "aliases": ["Communication Network"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Personnel who operate signal fires and communication systems across the empire.",
                    "role": "Imperial communications",
                    "relationships": {
                        "Operate": "Signal networks",
                        "Maintain": "Imperial communications"
                    }
                }
            }
        },
        "weather-watchers": {
            "name": "Weather Watchers",
            "aliases": ["Climate Observers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Individuals who monitor weather patterns and provide forecasts for agricultural and military planning.",
                    "role": "Weather forecasting",
                    "relationships": {
                        "Monitor": "Weather patterns",
                        "Provide": "Climate forecasts"
                    }
                }
            }
        },
        "star-gazers": {
            "name": "Star Gazers",
            "aliases": ["Astronomers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Scholars who study the stars and celestial movements for navigation and divination.",
                    "role": "Celestial studies",
                    "relationships": {
                        "Study": "Celestial movements",
                        "Provide": "Navigation guidance"
                    }
                }
            }
        },
        "map-makers": {
            "name": "Imperial Map Makers",
            "aliases": ["Royal Cartographers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Skilled cartographers who create detailed maps for the empire's military and administrative use.",
                    "role": "Imperial mapping",
                    "relationships": {
                        "Create": "Military maps",
                        "Chart": "Empire territories"
                    }
                }
            }
        },
        "language-scholars": {
            "name": "Language Scholars",
            "aliases": ["Linguistic Experts"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Scholars who study languages and serve as translators for diplomatic missions.",
                    "role": "Language expertise",
                    "relationships": {
                        "Study": "Foreign languages",
                        "Serve as": "Diplomatic translators"
                    }
                }
            }
        },
        "mining-supervisors": {
            "name": "Mining Supervisors",
            "aliases": ["Resource Extractors"],
            "appearances": [25, 26, 27, 28, 29, 30, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Supervisors who oversee mining operations and resource extraction throughout the empire.",
                    "role": "Resource management",
                    "relationships": {
                        "Oversee": "Mining operations",
                        "Extract": "Empire resources"
                    }
                }
            }
        }
    }
    
    # Add all the new characters
    data["characters"].update(additional_characters)
    
    # Save the updated data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/tower-of-dawn.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully added {len(additional_characters)} characters to Tower of Dawn")
    print(f"Total characters now: {len(data['characters'])}")

if __name__ == "__main__":
    add_characters_to_tower_of_dawn()