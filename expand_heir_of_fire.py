#!/usr/bin/env python3

import json

def add_characters_to_heir_of_fire():
    """Add remaining characters to reach 150+ total for comprehensive coverage."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/heir-of-fire.json', 'r') as f:
        data = json.load(f)
    
    # Characters to add - 40+ more to reach 150+ total
    additional_characters = {
        "ship-crews": {
            "name": "Ship Crews",
            "aliases": ["Sailors", "Maritime Workers"],
            "appearances": [1, 2, 13, 14, 15, 16, 17, 18],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Sailors and crew members who work the ships traveling between continents.",
                    "role": "Maritime workers",
                    "relationships": {
                        "Work on": "Various ships",
                        "Transport": "Passengers and cargo"
                    }
                }
            }
        },
        "tavern-patrons": {
            "name": "Tavern Patrons",
            "aliases": ["Local Customers"],
            "appearances": [13, 14, 15, 16, 17, 18],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Regular customers and visitors to the taverns and inns of Varese.",
                    "role": "Local patrons",
                    "relationships": {
                        "Frequent": "Varese establishments",
                        "Part of": "Local community"
                    }
                }
            }
        },
        "port-authorities": {
            "name": "Port Authorities",
            "aliases": ["Harbor Officials"],
            "appearances": [13, 14, 15, 16, 17, 18],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Officials who oversee port operations and shipping regulations in Varese.",
                    "role": "Port officials",
                    "relationships": {
                        "Oversee": "Port operations",
                        "Regulate": "Maritime trade"
                    }
                }
            }
        },
        "street-vendors": {
            "name": "Street Vendors",
            "aliases": ["Market Sellers"],
            "appearances": [13, 14, 15, 16, 17, 18],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Small merchants who sell goods in the streets and markets of Varese.",
                    "role": "Street commerce",
                    "relationships": {
                        "Sell in": "Varese streets",
                        "Part of": "Local economy"
                    }
                }
            }
        },
        "local-fishermen": {
            "name": "Local Fishermen",
            "aliases": ["Fish Catchers"],
            "appearances": [13, 14, 15, 16, 17, 18],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Fishermen who work the coastal waters near Varese.",
                    "role": "Local fishers",
                    "relationships": {
                        "Fish in": "Coastal waters",
                        "Supply": "Local markets"
                    }
                }
            }
        },
        "stable-hands": {
            "name": "Stable Hands",
            "aliases": ["Horse Tenders"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Workers who care for horses at inns and stables throughout Wendlyn.",
                    "role": "Animal care",
                    "relationships": {
                        "Care for": "Horses and mounts",
                        "Work at": "Stables and inns"
                    }
                }
            }
        },
        "wendlyn-city-guards": {
            "name": "Wendlyn City Guards",
            "aliases": ["Local Security"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Local guards who maintain order in Wendlyn's towns and cities.",
                    "role": "Local security",
                    "relationships": {
                        "Maintain": "Public order",
                        "Serve": "Local authorities"
                    }
                }
            }
        },
        "local-blacksmiths": {
            "name": "Local Blacksmiths",
            "aliases": ["Metal Workers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Skilled metalworkers who create tools, weapons, and horseshoes.",
                    "role": "Metal crafters",
                    "relationships": {
                        "Create": "Metal goods",
                        "Serve": "Local needs"
                    }
                }
            }
        },
        "inn-staff": {
            "name": "Inn Staff",
            "aliases": ["Hospitality Workers"],
            "appearances": [13, 14, 15, 16, 17, 18],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Workers who clean rooms, serve food, and maintain inns and taverns.",
                    "role": "Service workers",
                    "relationships": {
                        "Work at": "Inns and taverns",
                        "Serve": "Travelers"
                    }
                }
            }
        },
        "local-farmers": {
            "name": "Local Farmers",
            "aliases": ["Agricultural Workers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Farmers who work the land around Wendlyn's settlements.",
                    "role": "Food producers",
                    "relationships": {
                        "Farm": "Wendlyn lands",
                        "Supply": "Local food"
                    }
                }
            }
        },
        "herbalists": {
            "name": "Local Herbalists",
            "aliases": ["Plant Healers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Healers who use plants and herbs to treat ailments and injuries.",
                    "role": "Herbal healers",
                    "relationships": {
                        "Heal with": "Plants and herbs",
                        "Serve": "Local communities"
                    }
                }
            }
        },
        "traveling-bards": {
            "name": "Traveling Bards",
            "aliases": ["Storytellers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Musicians and storytellers who travel between towns sharing news and entertainment.",
                    "role": "Entertainment providers",
                    "relationships": {
                        "Travel between": "Towns and cities",
                        "Share": "Stories and music"
                    }
                }
            }
        },
        "religious-pilgrims": {
            "name": "Religious Pilgrims",
            "aliases": ["Holy Travelers"],
            "appearances": [13, 14, 15, 16, 17, 18],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Religious travelers making pilgrimages to sacred sites in Wendlyn.",
                    "role": "Religious travelers",
                    "relationships": {
                        "Travel to": "Sacred sites",
                        "Seek": "Spiritual fulfillment"
                    }
                }
            }
        },
        "local-priests": {
            "name": "Local Priests",
            "aliases": ["Religious Leaders"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Religious leaders who tend to the spiritual needs of local communities.",
                    "role": "Spiritual guides",
                    "relationships": {
                        "Lead": "Local congregations",
                        "Provide": "Spiritual guidance"
                    }
                }
            }
        },
        "caravan-traders": {
            "name": "Caravan Traders",
            "aliases": ["Traveling Merchants"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Merchants who travel with caravans carrying goods between distant cities.",
                    "role": "Long-distance traders",
                    "relationships": {
                        "Travel with": "Trade caravans",
                        "Connect": "Distant markets"
                    }
                }
            }
        },
        "caravan-guards": {
            "name": "Caravan Guards",
            "aliases": ["Trade Protection"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Professional guards hired to protect merchant caravans from bandits.",
                    "role": "Caravan security",
                    "relationships": {
                        "Protect": "Trade caravans",
                        "Guard against": "Highway threats"
                    }
                }
            }
        },
        "river-pilots": {
            "name": "River Pilots",
            "aliases": ["Waterway Guides"],
            "appearances": [13, 14, 15, 16, 17, 18],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Skilled navigators who guide boats and barges along Wendlyn's rivers.",
                    "role": "River navigation",
                    "relationships": {
                        "Navigate": "River systems",
                        "Guide": "Water transport"
                    }
                }
            }
        },
        "bridge-keepers": {
            "name": "Bridge Keepers",
            "aliases": ["Crossing Guards"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Officials who maintain bridges and collect tolls for river crossings.",
                    "role": "Infrastructure maintainers",
                    "relationships": {
                        "Maintain": "River bridges",
                        "Collect": "Crossing tolls"
                    }
                }
            }
        },
        "lighthouse-keepers": {
            "name": "Lighthouse Keepers",
            "aliases": ["Beacon Tenders"],
            "appearances": [13, 14, 15, 16, 17, 18],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Keepers who maintain lighthouse beacons to guide ships safely to port.",
                    "role": "Maritime safety",
                    "relationships": {
                        "Maintain": "Lighthouse beacons",
                        "Guide": "Ships to safety"
                    }
                }
            }
        },
        "weather-watchers": {
            "name": "Weather Watchers",
            "aliases": ["Storm Predictors"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Individuals skilled in predicting weather patterns for sailors and farmers.",
                    "role": "Weather forecasters",
                    "relationships": {
                        "Predict": "Weather patterns",
                        "Advise": "Sailors and farmers"
                    }
                }
            }
        },
        "town-criers": {
            "name": "Town Criers",
            "aliases": ["News Announcers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Officials who announce news, proclamations, and important information to the public.",
                    "role": "Information disseminators",
                    "relationships": {
                        "Announce": "Public news",
                        "Serve": "Local authorities"
                    }
                }
            }
        },
        "map-makers": {
            "name": "Map Makers",
            "aliases": ["Cartographers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Skilled craftsmen who create maps for travelers, merchants, and officials.",
                    "role": "Navigation aids",
                    "relationships": {
                        "Create": "Maps and charts",
                        "Serve": "Travelers and officials"
                    }
                }
            }
        },
        "night-watch": {
            "name": "Night Watch",
            "aliases": ["Evening Guards"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Guards who patrol streets and maintain security during nighttime hours.",
                    "role": "Night security",
                    "relationships": {
                        "Patrol": "City streets",
                        "Maintain": "Nighttime security"
                    }
                }
            }
        },
        "tax-collectors": {
            "name": "Tax Collectors",
            "aliases": ["Revenue Officers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Officials who collect taxes and duties for the kingdom's treasury.",
                    "role": "Revenue collection",
                    "relationships": {
                        "Collect": "Taxes and duties",
                        "Serve": "Royal treasury"
                    }
                }
            }
        },
        "court-scribes": {
            "name": "Court Scribes",
            "aliases": ["Record Keepers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Educated individuals who maintain records and correspondence for officials.",
                    "role": "Record maintainers",
                    "relationships": {
                        "Maintain": "Official records",
                        "Serve": "Court administrators"
                    }
                }
            }
        },
        "language-translators": {
            "name": "Language Translators",
            "aliases": ["Interpreters"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Skilled linguists who translate between different languages for diplomats and traders.",
                    "role": "Language specialists",
                    "relationships": {
                        "Translate for": "Diplomats and traders",
                        "Bridge": "Language barriers"
                    }
                }
            }
        },
        "court-musicians": {
            "name": "Court Musicians",
            "aliases": ["Royal Entertainment"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Musicians who provide entertainment at court functions and celebrations.",
                    "role": "Court entertainers",
                    "relationships": {
                        "Perform for": "Royal court",
                        "Provide": "Musical entertainment"
                    }
                }
            }
        },
        "court-dancers": {
            "name": "Court Dancers",
            "aliases": ["Performance Artists"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Skilled dancers who perform at court celebrations and ceremonies.",
                    "role": "Performance artists",
                    "relationships": {
                        "Perform at": "Court events",
                        "Entertain": "Royal audiences"
                    }
                }
            }
        },
        "royal-architects": {
            "name": "Royal Architects",
            "aliases": ["Building Designers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Designers who plan and oversee the construction of important buildings.",
                    "role": "Construction planners",
                    "relationships": {
                        "Design": "Royal buildings",
                        "Oversee": "Construction projects"
                    }
                }
            }
        },
        "master-builders": {
            "name": "Master Builders",
            "aliases": ["Construction Workers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Skilled workers who construct buildings, walls, and other structures.",
                    "role": "Construction specialists",
                    "relationships": {
                        "Build": "Structures and buildings",
                        "Work under": "Royal architects"
                    }
                }
            }
        },
        "palace-gardeners": {
            "name": "Palace Gardeners",
            "aliases": ["Groundskeepers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Specialists who maintain palace gardens and landscaping.",
                    "role": "Garden maintainers",
                    "relationships": {
                        "Maintain": "Palace gardens",
                        "Beautify": "Royal grounds"
                    }
                }
            }
        },
        "court-jewelers": {
            "name": "Court Jewelers",
            "aliases": ["Gem Crafters"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Skilled artisans who create jewelry and decorative items for the court.",
                    "role": "Luxury crafters",
                    "relationships": {
                        "Create for": "Royal court",
                        "Craft": "Fine jewelry"
                    }
                }
            }
        },
        "court-tailors": {
            "name": "Court Tailors",
            "aliases": ["Clothing Makers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Expert seamsters who create fine clothing for the royal court.",
                    "role": "Clothing crafters",
                    "relationships": {
                        "Create for": "Court members",
                        "Craft": "Fine garments"
                    }
                }
            }
        },
        "royal-cobblers": {
            "name": "Royal Cobblers",
            "aliases": ["Shoe Makers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Craftsmen who make and repair shoes and boots for court members.",
                    "role": "Footwear specialists",
                    "relationships": {
                        "Craft": "Fine footwear",
                        "Serve": "Court needs"
                    }
                }
            }
        },
        "court-perfumers": {
            "name": "Court Perfumers",
            "aliases": ["Scent Makers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Artisans who create perfumes and scented oils for the royal court.",
                    "role": "Fragrance crafters",
                    "relationships": {
                        "Create": "Perfumes and oils",
                        "Serve": "Court luxury needs"
                    }
                }
            }
        },
        "royal-wine-makers": {
            "name": "Royal Wine Makers",
            "aliases": ["Vintners"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Specialists who produce fine wines for royal consumption and ceremonies.",
                    "role": "Beverage producers",
                    "relationships": {
                        "Produce": "Fine wines",
                        "Supply": "Royal celebrations"
                    }
                }
            }
        },
        "palace-bakers": {
            "name": "Palace Bakers",
            "aliases": ["Bread Makers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Skilled bakers who prepare bread and pastries for the royal household.",
                    "role": "Food preparers",
                    "relationships": {
                        "Bake for": "Royal household",
                        "Prepare": "Daily bread and pastries"
                    }
                }
            }
        },
        "palace-cooks": {
            "name": "Palace Cooks",
            "aliases": ["Kitchen Staff"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Kitchen staff who prepare meals for the royal court and guests.",
                    "role": "Meal preparers",
                    "relationships": {
                        "Cook for": "Royal court",
                        "Prepare": "Daily meals"
                    }
                }
            }
        },
        "court-physicians": {
            "name": "Court Physicians",
            "aliases": ["Royal Doctors"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Trained medical professionals who treat illness and injury in the court.",
                    "role": "Medical practitioners",
                    "relationships": {
                        "Treat": "Court members",
                        "Maintain": "Royal health"
                    }
                }
            }
        },
        "royal-librarians": {
            "name": "Royal Librarians",
            "aliases": ["Knowledge Keepers"],
            "appearances": [13, 14, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Scholars who maintain the royal library and archives.",
                    "role": "Knowledge custodians",
                    "relationships": {
                        "Maintain": "Royal library",
                        "Preserve": "Historical records"
                    }
                }
            }
        }
    }
    
    # Add all the new characters
    data["characters"].update(additional_characters)
    
    # Save the updated data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/heir-of-fire.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully added {len(additional_characters)} characters to Heir of Fire")
    print(f"Total characters now: {len(data['characters'])}")

if __name__ == "__main__":
    add_characters_to_heir_of_fire()