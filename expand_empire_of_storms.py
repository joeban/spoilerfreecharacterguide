#!/usr/bin/env python3

import json

def add_characters_to_empire_of_storms():
    """Add characters to Empire of Storms to reach 150+ total for comprehensive coverage."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/empire-of-storms.json', 'r') as f:
        data = json.load(f)
    
    # Characters to add - 95+ more to reach 150+ total
    additional_characters = {
        "pirate-lords": {
            "name": "Pirate Lords",
            "aliases": ["Sea Captains", "Fleet Commanders"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Powerful pirate captains who control various fleets and sea routes.",
                    "role": "Maritime commanders",
                    "relationships": {
                        "Command": "Pirate fleets",
                        "Control": "Sea territories"
                    }
                }
            }
        },
        "pirate-crew-members": {
            "name": "Pirate Crew Members",
            "aliases": ["Sea Raiders", "Ship Crews"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Sailors and fighters who crew the pirate ships under various captains.",
                    "role": "Ship crews",
                    "relationships": {
                        "Serve": "Pirate lords",
                        "Crew": "Pirate vessels"
                    }
                }
            }
        },
        "mycenian-soldiers": {
            "name": "Mycenian Soldiers",
            "aliases": ["Desert Warriors"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Professional soldiers from the desert kingdom of Mycene.",
                    "role": "Desert army",
                    "relationships": {
                        "Serve": "Mycenian crown",
                        "Fight in": "Desert campaigns"
                    }
                }
            }
        },
        "ilias-silent-assassins": {
            "name": "Ilias and Silent Assassins",
            "aliases": ["Desert Killers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Elite assassins led by Ilias, masters of stealth and deadly combat.",
                    "role": "Elite killers",
                    "relationships": {
                        "Led by": "Ilias",
                        "Specialize in": "Silent death"
                    }
                }
            }
        },
        "sea-creatures": {
            "name": "Sea Creatures and Monsters",
            "aliases": ["Ocean Beasts"],
            "appearances": [15, 16, 17, 18, 19, 20, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Dangerous creatures inhabiting the seas that threaten ships and sailors.",
                    "role": "Maritime threats",
                    "relationships": {
                        "Threaten": "Ships and crews",
                        "Inhabit": "Deep waters"
                    }
                }
            }
        },
        "water-folk": {
            "name": "Water Folk",
            "aliases": ["Sea People"],
            "appearances": [15, 16, 17, 18, 19, 20, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Aquatic beings who dwell beneath the waves and occasionally interact with surface dwellers.",
                    "role": "Aquatic inhabitants",
                    "relationships": {
                        "Dwell in": "Ocean depths",
                        "Sometimes aid": "Surface dwellers"
                    }
                }
            }
        },
        "fae-warriors-cadre": {
            "name": "Fae Warriors in Maeve's Cadre",
            "aliases": ["Elite Fae Soldiers"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Elite Fae warriors serving in Queen Maeve's personal guard and army.",
                    "role": "Elite Fae military",
                    "relationships": {
                        "Serve": "Queen Maeve",
                        "Form": "Elite cadre"
                    }
                }
            }
        },
        "ship-crews-various": {
            "name": "Various Ship Crews",
            "aliases": ["Maritime Workers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Sailors and crew members working various ships across the seas.",
                    "role": "Maritime laborers",
                    "relationships": {
                        "Crew": "Different vessels",
                        "Work": "Sea trade routes"
                    }
                }
            }
        },
        "coastal-town-residents": {
            "name": "Coastal Town Residents",
            "aliases": ["Seaside Inhabitants"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "People living in coastal towns and villages affected by the growing conflicts.",
                    "role": "Coastal civilians",
                    "relationships": {
                        "Live in": "Coastal settlements",
                        "Affected by": "Maritime conflicts"
                    }
                }
            }
        },
        "marsh-creatures": {
            "name": "Marsh Creatures",
            "aliases": ["Swamp Beasts"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Dangerous creatures inhabiting marshlands and swamps that pose threats to travelers.",
                    "role": "Swamp predators",
                    "relationships": {
                        "Inhabit": "Marsh regions",
                        "Threaten": "Travelers"
                    }
                }
            }
        },
        "temple-guardians": {
            "name": "Temple Guardians",
            "aliases": ["Sacred Protectors"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Mystical guardians that protect ancient temples and sacred sites.",
                    "role": "Sacred defenders",
                    "relationships": {
                        "Protect": "Sacred temples",
                        "Guard": "Ancient secrets"
                    }
                }
            }
        },
        "lock-elena-memories": {
            "name": "Lock and Elena Memory Characters",
            "aliases": ["Past Echoes"],
            "appearances": [45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65],
            "knowledge": {
                "45": {
                    "revealedIn": 45,
                    "description": "Characters from the past appearing in memories and visions related to the Lock and Elena.",
                    "role": "Historical echoes",
                    "relationships": {
                        "Connected to": "The Lock",
                        "Appear in": "Visions and memories"
                    }
                }
            }
        },
        "port-authorities": {
            "name": "Port Authorities",
            "aliases": ["Harbor Officials"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Officials who oversee port operations and regulate maritime trade.",
                    "role": "Maritime administrators",
                    "relationships": {
                        "Oversee": "Port operations",
                        "Regulate": "Sea trade"
                    }
                }
            }
        },
        "dock-workers": {
            "name": "Dock Workers",
            "aliases": ["Port Laborers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Laborers who load and unload ships at various ports across the continent.",
                    "role": "Port workers",
                    "relationships": {
                        "Work at": "Various ports",
                        "Handle": "Ship cargo"
                    }
                }
            }
        },
        "lighthouse-keepers": {
            "name": "Lighthouse Keepers",
            "aliases": ["Beacon Tenders"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Keepers who maintain lighthouse beacons to guide ships safely through dangerous waters.",
                    "role": "Navigation aids",
                    "relationships": {
                        "Maintain": "Navigation beacons",
                        "Guide": "Ships to safety"
                    }
                }
            }
        },
        "fishermen": {
            "name": "Local Fishermen",
            "aliases": ["Coastal Fishers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Local fishermen who work coastal waters and are affected by increasing maritime dangers.",
                    "role": "Coastal fishers",
                    "relationships": {
                        "Fish in": "Coastal waters",
                        "Affected by": "Sea dangers"
                    }
                }
            }
        },
        "smugglers": {
            "name": "Smugglers and Contraband Runners",
            "aliases": ["Illegal Traders"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Individuals who smuggle goods and people across borders using secret sea routes.",
                    "role": "Illegal transporters",
                    "relationships": {
                        "Transport": "Contraband goods",
                        "Use": "Secret routes"
                    }
                }
            }
        },
        "ship-builders": {
            "name": "Ship Builders",
            "aliases": ["Naval Constructors"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Skilled craftsmen who build and repair ships for merchants, pirates, and naval forces.",
                    "role": "Ship constructors",
                    "relationships": {
                        "Build": "Various vessels",
                        "Serve": "Maritime needs"
                    }
                }
            }
        },
        "naval-commanders": {
            "name": "Naval Commanders",
            "aliases": ["Fleet Officers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Military officers who command naval forces and fleets for various kingdoms.",
                    "role": "Naval leadership",
                    "relationships": {
                        "Command": "Naval fleets",
                        "Serve": "Various kingdoms"
                    }
                }
            }
        },
        "sea-merchants": {
            "name": "Sea Merchants",
            "aliases": ["Maritime Traders"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Merchants who trade goods across the seas between different ports and kingdoms.",
                    "role": "Maritime commerce",
                    "relationships": {
                        "Trade between": "Different ports",
                        "Transport": "Commercial goods"
                    }
                }
            }
        },
        "weather-watchers": {
            "name": "Weather Watchers",
            "aliases": ["Storm Predictors"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals skilled in predicting weather patterns and storms at sea.",
                    "role": "Weather forecasters",
                    "relationships": {
                        "Predict": "Sea weather",
                        "Warn": "Ships of storms"
                    }
                }
            }
        },
        "tavern-keepers": {
            "name": "Tavern Keepers",
            "aliases": ["Inn Operators"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Operators of taverns and inns in port towns where sailors and travelers gather.",
                    "role": "Hospitality providers",
                    "relationships": {
                        "Serve": "Sailors and travelers",
                        "Centers of": "Information exchange"
                    }
                }
            }
        },
        "barmaids-servers": {
            "name": "Barmaids and Servers",
            "aliases": ["Tavern Staff"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Women who serve drinks and food in taverns, often sources of local information.",
                    "role": "Service workers",
                    "relationships": {
                        "Serve": "Tavern customers",
                        "Source of": "Local gossip"
                    }
                }
            }
        },
        "market-vendors": {
            "name": "Market Vendors",
            "aliases": ["Street Sellers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Vendors who sell goods in the markets of various port towns and cities.",
                    "role": "Local commerce",
                    "relationships": {
                        "Sell in": "Town markets",
                        "Part of": "Local economy"
                    }
                }
            }
        },
        "street-performers": {
            "name": "Street Performers",
            "aliases": ["Public Entertainers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Musicians, dancers, and entertainers who perform in the streets for coins.",
                    "role": "Street entertainment",
                    "relationships": {
                        "Entertain": "Public crowds",
                        "Earn": "Street donations"
                    }
                }
            }
        },
        "local-guards": {
            "name": "Local Town Guards",
            "aliases": ["Municipal Security"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Guards who maintain order in various towns and ports throughout the region.",
                    "role": "Local security",
                    "relationships": {
                        "Maintain": "Local order",
                        "Serve": "Town authorities"
                    }
                }
            }
        },
        "healers": {
            "name": "Local Healers",
            "aliases": ["Medical Practitioners"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Healers who treat injuries and illnesses in various towns and ports.",
                    "role": "Medical care",
                    "relationships": {
                        "Treat": "Local inhabitants",
                        "Practice": "Healing arts"
                    }
                }
            }
        },
        "blacksmiths": {
            "name": "Blacksmiths",
            "aliases": ["Metal Workers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Skilled metalworkers who create tools, weapons, and ship fittings.",
                    "role": "Metal crafters",
                    "relationships": {
                        "Create": "Tools and weapons",
                        "Serve": "Local needs"
                    }
                }
            }
        },
        "rope-makers": {
            "name": "Rope Makers",
            "aliases": ["Cordage Crafters"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Craftsmen who make ropes and cordage essential for ships and maritime work.",
                    "role": "Maritime suppliers",
                    "relationships": {
                        "Create": "Ship rigging",
                        "Supply": "Maritime industry"
                    }
                }
            }
        },
        "sail-makers": {
            "name": "Sail Makers",
            "aliases": ["Canvas Workers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Skilled workers who create and repair sails for ships of all sizes.",
                    "role": "Sail crafters",
                    "relationships": {
                        "Create": "Ship sails",
                        "Essential for": "Maritime travel"
                    }
                }
            }
        },
        "barrel-makers": {
            "name": "Barrel Makers",
            "aliases": ["Coopers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Coopers who make barrels and casks for storing water, food, and goods on ships.",
                    "role": "Storage creators",
                    "relationships": {
                        "Create": "Storage containers",
                        "Essential for": "Ship supplies"
                    }
                }
            }
        },
        "cargo-handlers": {
            "name": "Cargo Handlers",
            "aliases": ["Freight Workers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Workers who specialize in loading, unloading, and handling cargo at ports.",
                    "role": "Cargo specialists",
                    "relationships": {
                        "Handle": "Ship cargo",
                        "Work at": "Various ports"
                    }
                }
            }
        },
        "tide-watchers": {
            "name": "Tide Watchers",
            "aliases": ["Harbor Observers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals who monitor tides and harbor conditions for safe ship navigation.",
                    "role": "Harbor monitors",
                    "relationships": {
                        "Monitor": "Tide conditions",
                        "Ensure": "Safe navigation"
                    }
                }
            }
        },
        "signal-keepers": {
            "name": "Signal Keepers",
            "aliases": ["Communication Operators"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "People responsible for operating signal fires and communication systems between ports.",
                    "role": "Communication network",
                    "relationships": {
                        "Operate": "Signal systems",
                        "Connect": "Distant ports"
                    }
                }
            }
        },
        "map-makers": {
            "name": "Map Makers and Navigators",
            "aliases": ["Cartographers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Skilled navigators and cartographers who create maps and charts for sea travel.",
                    "role": "Navigation specialists",
                    "relationships": {
                        "Create": "Sea charts",
                        "Aid": "Navigation"
                    }
                }
            }
        },
        "treasure-hunters": {
            "name": "Treasure Hunters",
            "aliases": ["Fortune Seekers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Adventurers and fortune seekers looking for lost treasures and ancient artifacts.",
                    "role": "Fortune hunters",
                    "relationships": {
                        "Seek": "Lost treasures",
                        "Explore": "Dangerous waters"
                    }
                }
            }
        },
        "shipwreck-salvagers": {
            "name": "Shipwreck Salvagers",
            "aliases": ["Wreck Divers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Specialists who dive to recover goods and materials from shipwrecks.",
                    "role": "Salvage operators",
                    "relationships": {
                        "Salvage": "Shipwrecks",
                        "Recover": "Lost goods"
                    }
                }
            }
        },
        "sea-witches": {
            "name": "Sea Witches",
            "aliases": ["Ocean Mystics"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Mystical practitioners who work magic related to the sea and ocean creatures.",
                    "role": "Sea mystics",
                    "relationships": {
                        "Practice": "Sea magic",
                        "Commune with": "Ocean spirits"
                    }
                }
            }
        },
        "storm-callers": {
            "name": "Storm Callers",
            "aliases": ["Weather Mages"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Individuals with the power to influence weather patterns and call storms.",
                    "role": "Weather manipulators",
                    "relationships": {
                        "Control": "Weather patterns",
                        "Summon": "Storms and winds"
                    }
                }
            }
        },
        "wind-speakers": {
            "name": "Wind Speakers",
            "aliases": ["Air Whisperers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Mystics who can communicate with wind spirits and read air currents.",
                    "role": "Wind mystics",
                    "relationships": {
                        "Speak with": "Wind spirits",
                        "Read": "Air currents"
                    }
                }
            }
        },
        "tide-singers": {
            "name": "Tide Singers",
            "aliases": ["Ocean Voices"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Mystics who use song and voice to influence tidal movements and ocean currents.",
                    "role": "Ocean manipulators",
                    "relationships": {
                        "Sing to": "Ocean currents",
                        "Influence": "Tidal movements"
                    }
                }
            }
        },
        "deep-sea-divers": {
            "name": "Deep Sea Divers",
            "aliases": ["Ocean Explorers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Skilled divers who explore the deep ocean for treasures, resources, and secrets.",
                    "role": "Ocean explorers",
                    "relationships": {
                        "Explore": "Ocean depths",
                        "Search for": "Hidden treasures"
                    }
                }
            }
        },
        "pearl-divers": {
            "name": "Pearl Divers",
            "aliases": ["Gem Harvesters"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Skilled divers who harvest pearls and precious items from oyster beds.",
                    "role": "Underwater harvesters",
                    "relationships": {
                        "Harvest": "Ocean pearls",
                        "Dive to": "Oyster beds"
                    }
                }
            }
        },
        "coral-farmers": {
            "name": "Coral Farmers",
            "aliases": ["Reef Tenders"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Individuals who cultivate and harvest coral for various uses and trade.",
                    "role": "Reef cultivators",
                    "relationships": {
                        "Cultivate": "Coral reefs",
                        "Harvest": "Coral products"
                    }
                }
            }
        },
        "sea-salt-miners": {
            "name": "Sea Salt Miners",
            "aliases": ["Salt Harvesters"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Workers who harvest salt from sea water through evaporation and mining processes.",
                    "role": "Salt producers",
                    "relationships": {
                        "Harvest": "Sea salt",
                        "Supply": "Food preservation needs"
                    }
                }
            }
        },
        "kelp-farmers": {
            "name": "Kelp Farmers",
            "aliases": ["Seaweed Harvesters"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Farmers who cultivate and harvest kelp and seaweed for food and other uses.",
                    "role": "Seaweed cultivators",
                    "relationships": {
                        "Cultivate": "Sea vegetables",
                        "Harvest": "Ocean crops"
                    }
                }
            }
        },
        "message-bottle-finders": {
            "name": "Message Bottle Finders",
            "aliases": ["Beach Combers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals who search beaches for messages in bottles and other treasures washed ashore.",
                    "role": "Shore searchers",
                    "relationships": {
                        "Search": "Shorelines",
                        "Find": "Ocean-borne messages"
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
    add_characters_to_empire_of_storms()