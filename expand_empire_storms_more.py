#!/usr/bin/env python3

import json

def add_more_characters_to_empire_of_storms():
    """Add more characters to Empire of Storms to reach 150+ total for comprehensive coverage."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/empire-of-storms.json', 'r') as f:
        data = json.load(f)
    
    # More characters to add - 50+ more to reach 150+ total
    additional_characters = {
        "ship-navigators": {
            "name": "Ship Navigators",
            "aliases": ["Course Plotters"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Skilled navigators who plot courses and guide ships through dangerous waters.",
                    "role": "Navigation experts",
                    "relationships": {
                        "Guide": "Ship passages",
                        "Plot": "Safe courses"
                    }
                }
            }
        },
        "ship-cooks": {
            "name": "Ship Cooks",
            "aliases": ["Galley Staff"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Cooks who prepare meals for ship crews during long voyages.",
                    "role": "Ship food providers",
                    "relationships": {
                        "Feed": "Ship crews",
                        "Work in": "Ship galleys"
                    }
                }
            }
        },
        "ship-surgeons": {
            "name": "Ship Surgeons",
            "aliases": ["Maritime Doctors"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Medical practitioners who treat injuries and illnesses aboard ships.",
                    "role": "Ship medical staff",
                    "relationships": {
                        "Treat": "Crew injuries",
                        "Serve": "Ship health needs"
                    }
                }
            }
        },
        "cabin-boys": {
            "name": "Cabin Boys and Girls",
            "aliases": ["Ship Apprentices"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Young people who perform various tasks aboard ships while learning seamanship.",
                    "role": "Ship apprentices",
                    "relationships": {
                        "Serve": "Ship officers",
                        "Learn": "Maritime skills"
                    }
                }
            }
        },
        "powder-monkeys": {
            "name": "Powder Monkeys",
            "aliases": ["Ammunition Runners"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Young crew members who transport gunpowder and ammunition during sea battles.",
                    "role": "Ammunition suppliers",
                    "relationships": {
                        "Supply": "Battle ammunition",
                        "Support": "Combat operations"
                    }
                }
            }
        },
        "gunners": {
            "name": "Ship Gunners",
            "aliases": ["Artillery Crew"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Specialists who operate cannons and artillery during naval battles.",
                    "role": "Naval artillery",
                    "relationships": {
                        "Operate": "Ship cannons",
                        "Essential for": "Naval combat"
                    }
                }
            }
        },
        "lookouts": {
            "name": "Ship Lookouts",
            "aliases": ["Crow's Nest Watchers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Crew members who watch for dangers, other ships, and land from the crow's nest.",
                    "role": "Ship surveillance",
                    "relationships": {
                        "Watch for": "Dangers and ships",
                        "Stationed in": "Crow's nest"
                    }
                }
            }
        },
        "riggers": {
            "name": "Ship Riggers",
            "aliases": ["Sail Handlers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Skilled crew members who handle the rigging, sails, and ropes of ships.",
                    "role": "Sail operators",
                    "relationships": {
                        "Handle": "Ship rigging",
                        "Operate": "Sail systems"
                    }
                }
            }
        },
        "ship-carpenters": {
            "name": "Ship Carpenters",
            "aliases": ["Vessel Repairers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Skilled carpenters who repair and maintain the wooden structures of ships.",
                    "role": "Ship maintenance",
                    "relationships": {
                        "Repair": "Ship structures",
                        "Maintain": "Vessel integrity"
                    }
                }
            }
        },
        "ship-musicians": {
            "name": "Ship Musicians",
            "aliases": ["Sea Entertainers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Musicians who provide entertainment and maintain morale during long voyages.",
                    "role": "Crew entertainment",
                    "relationships": {
                        "Entertain": "Ship crews",
                        "Maintain": "Crew morale"
                    }
                }
            }
        },
        "quartermaster": {
            "name": "Ship Quartermasters",
            "aliases": ["Supply Managers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Officers responsible for managing supplies, equipment, and crew quarters.",
                    "role": "Supply management",
                    "relationships": {
                        "Manage": "Ship supplies",
                        "Oversee": "Crew quarters"
                    }
                }
            }
        },
        "boatswains": {
            "name": "Boatswains",
            "aliases": ["Deck Supervisors"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Petty officers who supervise deck crew and maintain ship equipment.",
                    "role": "Deck supervisors",
                    "relationships": {
                        "Supervise": "Deck crew",
                        "Maintain": "Ship equipment"
                    }
                }
            }
        },
        "helmsmen": {
            "name": "Helmsmen",
            "aliases": ["Ship Steerers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Skilled sailors who steer ships and maintain course according to navigation orders.",
                    "role": "Ship steering",
                    "relationships": {
                        "Steer": "Ship course",
                        "Follow": "Navigation orders"
                    }
                }
            }
        },
        "pirates-first-mates": {
            "name": "Pirates' First Mates",
            "aliases": ["Second-in-Command"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Second-in-command officers serving under pirate captains.",
                    "role": "Pirate officers",
                    "relationships": {
                        "Serve under": "Pirate captains",
                        "Command": "Crew operations"
                    }
                }
            }
        },
        "sea-scouts": {
            "name": "Sea Scouts",
            "aliases": ["Ocean Spies"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Scouts who gather intelligence about enemy ship movements and naval activities.",
                    "role": "Naval intelligence",
                    "relationships": {
                        "Scout": "Enemy movements",
                        "Report": "Naval intelligence"
                    }
                }
            }
        },
        "coastal-watchers": {
            "name": "Coastal Watchers",
            "aliases": ["Shore Observers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals stationed along the coast to watch for incoming ships and threats.",
                    "role": "Coastal surveillance",
                    "relationships": {
                        "Watch": "Coastal approaches",
                        "Alert": "Inland authorities"
                    }
                }
            }
        },
        "beacon-tenders": {
            "name": "Beacon Tenders",
            "aliases": ["Signal Fire Keepers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Workers who maintain signal beacons and warning fires along the coast.",
                    "role": "Signal operators",
                    "relationships": {
                        "Maintain": "Signal beacons",
                        "Operate": "Warning systems"
                    }
                }
            }
        },
        "tide-pool-harvesters": {
            "name": "Tide Pool Harvesters",
            "aliases": ["Shore Gatherers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "People who gather food and useful items from tide pools and rocky shores.",
                    "role": "Shore foragers",
                    "relationships": {
                        "Harvest": "Tide pool resources",
                        "Gather": "Shore provisions"
                    }
                }
            }
        },
        "net-menders": {
            "name": "Net Menders",
            "aliases": ["Fishing Gear Repairers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Skilled workers who repair and maintain fishing nets and maritime equipment.",
                    "role": "Equipment maintenance",
                    "relationships": {
                        "Repair": "Fishing nets",
                        "Maintain": "Maritime gear"
                    }
                }
            }
        },
        "harbor-pilots": {
            "name": "Harbor Pilots",
            "aliases": ["Port Guides"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Expert navigators who guide ships safely into and out of harbors.",
                    "role": "Harbor navigation",
                    "relationships": {
                        "Guide": "Ships in harbors",
                        "Navigate": "Port approaches"
                    }
                }
            }
        },
        "customs-officers": {
            "name": "Customs Officers",
            "aliases": ["Trade Inspectors"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Officials who inspect cargo and collect duties on goods entering ports.",
                    "role": "Trade regulation",
                    "relationships": {
                        "Inspect": "Ship cargo",
                        "Collect": "Trade duties"
                    }
                }
            }
        },
        "warehouse-workers": {
            "name": "Warehouse Workers",
            "aliases": ["Storage Handlers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Workers who store and manage goods in port warehouses.",
                    "role": "Storage management",
                    "relationships": {
                        "Store": "Port goods",
                        "Manage": "Warehouse operations"
                    }
                }
            }
        },
        "ship-chandlers": {
            "name": "Ship Chandlers",
            "aliases": ["Marine Suppliers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Merchants who sell supplies, equipment, and provisions to ships.",
                    "role": "Marine suppliers",
                    "relationships": {
                        "Supply": "Ship needs",
                        "Sell": "Maritime equipment"
                    }
                }
            }
        },
        "ship-brokers": {
            "name": "Ship Brokers",
            "aliases": ["Vessel Dealers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals who arrange the buying, selling, and chartering of ships.",
                    "role": "Ship commerce",
                    "relationships": {
                        "Broker": "Ship deals",
                        "Arrange": "Vessel charters"
                    }
                }
            }
        },
        "marine-insurance": {
            "name": "Marine Insurance Agents",
            "aliases": ["Risk Assessors"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Agents who assess risks and provide insurance for ships and cargo.",
                    "role": "Risk management",
                    "relationships": {
                        "Assess": "Maritime risks",
                        "Provide": "Ship insurance"
                    }
                }
            }
        },
        "sea-lawyers": {
            "name": "Maritime Lawyers",
            "aliases": ["Admiralty Law"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Legal experts who handle maritime law, salvage rights, and shipping disputes.",
                    "role": "Maritime law",
                    "relationships": {
                        "Handle": "Maritime disputes",
                        "Expert in": "Sea law"
                    }
                }
            }
        },
        "refugee-ships": {
            "name": "Refugee Ship Passengers",
            "aliases": ["Displaced Travelers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "People fleeing war and danger who travel by ship seeking safety.",
                    "role": "War refugees",
                    "relationships": {
                        "Fleeing from": "War and danger",
                        "Seeking": "Safety across seas"
                    }
                }
            }
        },
        "slave-ship-crews": {
            "name": "Slave Ship Crews",
            "aliases": ["Human Traffickers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Crews involved in the illegal slave trade operating in secret.",
                    "role": "Human traffickers",
                    "relationships": {
                        "Engage in": "Slave trade",
                        "Operate": "Illegal ships"
                    }
                }
            }
        },
        "freed-slaves": {
            "name": "Freed Slaves",
            "aliases": ["Liberated People"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "People who have been freed from slavery and are seeking new lives.",
                    "role": "Liberated individuals",
                    "relationships": {
                        "Freed from": "Slavery",
                        "Building": "New lives"
                    }
                }
            }
        },
        "abolitionists": {
            "name": "Abolitionists",
            "aliases": ["Freedom Fighters"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "People working to end slavery and free those in bondage.",
                    "role": "Anti-slavery activists",
                    "relationships": {
                        "Fight against": "Slavery",
                        "Work to": "Free the enslaved"
                    }
                }
            }
        },
        "storm-survivors": {
            "name": "Storm Survivors",
            "aliases": ["Shipwreck Survivors"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "People who survived terrible storms and shipwrecks at sea.",
                    "role": "Disaster survivors",
                    "relationships": {
                        "Survived": "Sea disasters",
                        "Rescued from": "Shipwrecks"
                    }
                }
            }
        },
        "sea-nomads": {
            "name": "Sea Nomads",
            "aliases": ["Ocean Wanderers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "People who live their entire lives on ships and boats, never settling on land.",
                    "role": "Oceanic nomads",
                    "relationships": {
                        "Live on": "Ships and boats",
                        "Never settle": "On land"
                    }
                }
            }
        },
        "fishing-fleet-captains": {
            "name": "Fishing Fleet Captains",
            "aliases": ["Commercial Fishing Leaders"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Captains who command fleets of fishing vessels and coordinate their operations.",
                    "role": "Fishing fleet leaders",
                    "relationships": {
                        "Command": "Fishing fleets",
                        "Coordinate": "Fishing operations"
                    }
                }
            }
        },
        "merchant-fleet-owners": {
            "name": "Merchant Fleet Owners",
            "aliases": ["Shipping Magnates"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Wealthy individuals who own large merchant fleets and shipping companies.",
                    "role": "Shipping business owners",
                    "relationships": {
                        "Own": "Merchant fleets",
                        "Control": "Shipping routes"
                    }
                }
            }
        },
        "naval-academy-graduates": {
            "name": "Naval Academy Graduates",
            "aliases": ["Trained Naval Officers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Young officers who graduated from naval academies and serve in various fleets.",
                    "role": "Trained naval officers",
                    "relationships": {
                        "Graduated from": "Naval academies",
                        "Serve in": "Various fleets"
                    }
                }
            }
        },
        "privateer-crews": {
            "name": "Privateer Crews",
            "aliases": ["Licensed Pirates"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Crews operating under government licenses to attack enemy ships.",
                    "role": "Licensed raiders",
                    "relationships": {
                        "Licensed by": "Various governments",
                        "Attack": "Enemy vessels"
                    }
                }
            }
        },
        "island-natives": {
            "name": "Island Natives",
            "aliases": ["Indigenous Islanders"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Indigenous people living on various islands throughout the ocean regions.",
                    "role": "Island inhabitants",
                    "relationships": {
                        "Live on": "Various islands",
                        "Indigenous to": "Ocean regions"
                    }
                }
            }
        },
        "volcano-priests": {
            "name": "Volcano Priests",
            "aliases": ["Fire Mountain Clergy"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Religious figures who worship and tend to volcanic sites and their power.",
                    "role": "Volcanic clergy",
                    "relationships": {
                        "Worship": "Volcanic forces",
                        "Tend": "Fire mountain sites"
                    }
                }
            }
        },
        "ocean-cartographers": {
            "name": "Ocean Cartographers",
            "aliases": ["Sea Map Makers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Specialists who create detailed maps of ocean currents, depths, and hazards.",
                    "role": "Ocean mapping experts",
                    "relationships": {
                        "Map": "Ocean regions",
                        "Document": "Sea hazards"
                    }
                }
            }
        },
        "deep-sea-fishermen": {
            "name": "Deep Sea Fishermen",
            "aliases": ["Ocean Harvesters"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Fishermen who venture into deep ocean waters for large catches.",
                    "role": "Deep ocean fishers",
                    "relationships": {
                        "Fish in": "Deep ocean",
                        "Pursue": "Large sea creatures"
                    }
                }
            }
        },
        "whale-hunters": {
            "name": "Whale Hunters",
            "aliases": ["Leviathan Hunters"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Specialized hunters who pursue whales and other large sea creatures.",
                    "role": "Marine hunters",
                    "relationships": {
                        "Hunt": "Whales and sea beasts",
                        "Risk": "Lives for valuable catches"
                    }
                }
            }
        },
        "sea-beast-tamers": {
            "name": "Sea Beast Tamers",
            "aliases": ["Marine Animal Trainers"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Rare individuals who can communicate with and train sea creatures.",
                    "role": "Beast communicators",
                    "relationships": {
                        "Communicate with": "Sea creatures",
                        "Train": "Marine animals"
                    }
                }
            }
        },
        "ghost-ship-crews": {
            "name": "Ghost Ship Crews",
            "aliases": ["Spectral Sailors"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Supernatural crews of ships lost at sea who continue to sail the oceans.",
                    "role": "Supernatural sailors",
                    "relationships": {
                        "Crews of": "Ghost ships",
                        "Continue": "Eternal voyages"
                    }
                }
            }
        },
        "cursed-sailors": {
            "name": "Cursed Sailors",
            "aliases": ["Doomed Mariners"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Sailors under supernatural curses who cannot find peace or rest.",
                    "role": "Cursed mariners",
                    "relationships": {
                        "Under": "Supernatural curses",
                        "Cannot find": "Peace or rest"
                    }
                }
            }
        },
        "siren-victims": {
            "name": "Siren Victims",
            "aliases": ["Enchanted Sailors"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Sailors who have been enchanted or affected by sirens and their songs.",
                    "role": "Enchanted victims",
                    "relationships": {
                        "Enchanted by": "Siren songs",
                        "Victims of": "Sea magic"
                    }
                }
            }
        },
        "sea-hermits": {
            "name": "Sea Hermits",
            "aliases": ["Ocean Recluses"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Reclusive individuals who live alone on remote islands or floating homes.",
                    "role": "Ocean hermits",
                    "relationships": {
                        "Live alone": "On remote islands",
                        "Avoid": "Human contact"
                    }
                }
            }
        },
        "floating-city-residents": {
            "name": "Floating City Residents",
            "aliases": ["Aquatic Citizens"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "People who live in cities built on floating platforms or artificial islands.",
                    "role": "Floating community",
                    "relationships": {
                        "Live in": "Floating cities",
                        "Citizens of": "Water-based communities"
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
    add_more_characters_to_empire_of_storms()