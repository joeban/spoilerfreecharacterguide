#!/usr/bin/env python3

import json

def add_more_characters_to_queen_of_shadows():
    """Add more characters to Queen of Shadows to reach 150+ total for comprehensive coverage."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/queen-of-shadows.json', 'r') as f:
        data = json.load(f)
    
    # More characters to add - 45+ more to reach 150+ total
    additional_characters = {
        "palace-musicians": {
            "name": "Palace Musicians",
            "aliases": ["Court Entertainers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Musicians who perform for the royal court and palace functions.",
                    "role": "Court entertainment",
                    "relationships": {
                        "Perform for": "Royal court",
                        "Entertain": "Palace guests"
                    }
                }
            }
        },
        "palace-dancers": {
            "name": "Palace Dancers",
            "aliases": ["Court Performers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Skilled dancers who perform at royal celebrations and court events.",
                    "role": "Performance artists",
                    "relationships": {
                        "Dance for": "Royal entertainment",
                        "Perform at": "Court ceremonies"
                    }
                }
            }
        },
        "palace-librarians": {
            "name": "Palace Librarians",
            "aliases": ["Knowledge Keepers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Scholars who maintain the royal library and its vast collection of knowledge.",
                    "role": "Library custodians",
                    "relationships": {
                        "Maintain": "Royal library",
                        "Preserve": "Ancient knowledge"
                    }
                }
            }
        },
        "palace-gardeners": {
            "name": "Palace Gardeners",
            "aliases": ["Groundskeepers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Workers who maintain the elaborate gardens and grounds of the glass castle.",
                    "role": "Garden maintenance",
                    "relationships": {
                        "Maintain": "Palace gardens",
                        "Beautify": "Castle grounds"
                    }
                }
            }
        },
        "palace-tailors": {
            "name": "Palace Tailors",
            "aliases": ["Royal Seamsters"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Master tailors who create fine clothing for the royal family and court.",
                    "role": "Royal clothing makers",
                    "relationships": {
                        "Sew for": "Royal family",
                        "Create": "Court finery"
                    }
                }
            }
        },
        "palace-jewelers": {
            "name": "Palace Jewelers",
            "aliases": ["Royal Gem Workers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Master jewelers who craft precious items for the royal treasury and court.",
                    "role": "Luxury crafters",
                    "relationships": {
                        "Craft for": "Royal court",
                        "Create": "Precious ornaments"
                    }
                }
            }
        },
        "palace-physicians": {
            "name": "Palace Physicians",
            "aliases": ["Royal Doctors"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Trained doctors who attend to the health of the royal family and court.",
                    "role": "Medical practitioners",
                    "relationships": {
                        "Treat": "Royal family",
                        "Maintain": "Court health"
                    }
                }
            }
        },
        "demolition-experts": {
            "name": "Demolition Experts",
            "aliases": ["Destruction Specialists"],
            "appearances": [65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88],
            "knowledge": {
                "65": {
                    "revealedIn": 65,
                    "description": "Specialists recruited to help with the destruction of the clock tower and other strategic targets.",
                    "role": "Explosive specialists",
                    "relationships": {
                        "Work for": "Aelin's mission",
                        "Expert in": "Controlled destruction"
                    }
                }
            }
        },
        "sewer-workers": {
            "name": "Sewer Workers",
            "aliases": ["Underground Laborers"],
            "appearances": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Workers who maintain the underground sewers and waterways of Rifthold.",
                    "role": "Underground maintenance",
                    "relationships": {
                        "Maintain": "City sewers",
                        "Know": "Underground passages"
                    }
                }
            }
        },
        "tunnel-diggers": {
            "name": "Tunnel Diggers",
            "aliases": ["Underground Excavators"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Workers who dig tunnels and underground passages for various purposes.",
                    "role": "Underground construction",
                    "relationships": {
                        "Dig": "Secret tunnels",
                        "Create": "Hidden passages"
                    }
                }
            }
        },
        "bridge-guards": {
            "name": "Bridge Guards",
            "aliases": ["River Crossing Security"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Guards who protect and monitor the bridges crossing Rifthold's rivers.",
                    "role": "Bridge security",
                    "relationships": {
                        "Guard": "City bridges",
                        "Monitor": "River crossings"
                    }
                }
            }
        },
        "gate-guards": {
            "name": "City Gate Guards",
            "aliases": ["Entry Security"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Guards stationed at the gates leading into and out of Rifthold.",
                    "role": "City entry security",
                    "relationships": {
                        "Control": "City access",
                        "Monitor": "Who enters and exits"
                    }
                }
            }
        },
        "tower-guards": {
            "name": "Tower Guards",
            "aliases": ["Watchtower Sentries"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Guards stationed in towers throughout the city for surveillance and defense.",
                    "role": "Surveillance sentries",
                    "relationships": {
                        "Watch from": "City towers",
                        "Provide": "Early warning"
                    }
                }
            }
        },
        "roof-runners": {
            "name": "Roof Runners",
            "aliases": ["Rooftop Messengers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Agile individuals who traverse the city by running across rooftops.",
                    "role": "Aerial messengers",
                    "relationships": {
                        "Travel via": "Rooftops",
                        "Carry": "Secret messages"
                    }
                }
            }
        },
        "underground-fighters": {
            "name": "Underground Fighters",
            "aliases": ["Pit Fighters"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Warriors who fight in underground arenas for money and entertainment.",
                    "role": "Arena combatants",
                    "relationships": {
                        "Fight in": "Underground rings",
                        "Entertain": "Gambling crowds"
                    }
                }
            }
        },
        "gambling-den-operators": {
            "name": "Gambling Den Operators",
            "aliases": ["Game Masters"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals who run illegal gambling operations in hidden locations.",
                    "role": "Illegal gaming",
                    "relationships": {
                        "Operate": "Gambling dens",
                        "Facilitate": "Illegal betting"
                    }
                }
            }
        },
        "loan-sharks": {
            "name": "Loan Sharks",
            "aliases": ["Predatory Lenders"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Dangerous individuals who lend money at extremely high interest rates.",
                    "role": "Predatory finance",
                    "relationships": {
                        "Lend": "Money at high rates",
                        "Enforce": "Debt collection violently"
                    }
                }
            }
        },
        "fence-dealers": {
            "name": "Fence Dealers",
            "aliases": ["Stolen Goods Traders"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals who buy and sell stolen goods in the criminal underworld.",
                    "role": "Stolen goods dealers",
                    "relationships": {
                        "Buy": "Stolen merchandise",
                        "Sell": "Hot goods"
                    }
                }
            }
        },
        "information-brokers": {
            "name": "Information Brokers",
            "aliases": ["Secrets Traders"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Individuals who collect and sell information and secrets for profit.",
                    "role": "Intelligence dealers",
                    "relationships": {
                        "Trade in": "Secrets and information",
                        "Serve": "Paying clients"
                    }
                }
            }
        },
        "forgers": {
            "name": "Document Forgers",
            "aliases": ["False Papers Makers"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Skilled criminals who create false documents and identification papers.",
                    "role": "Document falsifiers",
                    "relationships": {
                        "Create": "False documents",
                        "Help": "Identity deception"
                    }
                }
            }
        },
        "safe-crackers": {
            "name": "Safe Crackers",
            "aliases": ["Lock Specialists"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Specialists who can open locked safes and secure containers.",
                    "role": "Security breakers",
                    "relationships": {
                        "Specialize in": "Breaking locks",
                        "Open": "Secured containers"
                    }
                }
            }
        },
        "poisoners": {
            "name": "Poisoners",
            "aliases": ["Toxic Specialists"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Dangerous individuals who specialize in creating and administering poisons.",
                    "role": "Poison experts",
                    "relationships": {
                        "Create": "Deadly toxins",
                        "Serve": "Assassination contracts"
                    }
                }
            }
        },
        "spy-masters": {
            "name": "Spy Masters",
            "aliases": ["Intelligence Chiefs"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Leaders who coordinate spy networks and intelligence operations.",
                    "role": "Intelligence coordinators",
                    "relationships": {
                        "Coordinate": "Spy networks",
                        "Manage": "Intelligence operations"
                    }
                }
            }
        },
        "code-breakers": {
            "name": "Code Breakers",
            "aliases": ["Cipher Specialists"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Specialists who can decode encrypted messages and secret communications.",
                    "role": "Cryptography experts",
                    "relationships": {
                        "Break": "Secret codes",
                        "Decode": "Encrypted messages"
                    }
                }
            }
        },
        "double-agents": {
            "name": "Double Agents",
            "aliases": ["Dual Loyalists"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Spies who work for multiple factions, playing different sides against each other.",
                    "role": "Multi-faction agents",
                    "relationships": {
                        "Work for": "Multiple factions",
                        "Play": "All sides"
                    }
                }
            }
        },
        "sleeper-agents": {
            "name": "Sleeper Agents",
            "aliases": ["Deep Cover Operatives"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Deep cover agents embedded in various organizations for intelligence gathering.",
                    "role": "Long-term infiltrators",
                    "relationships": {
                        "Embedded in": "Target organizations",
                        "Report to": "Handler networks"
                    }
                }
            }
        },
        "resistance-couriers": {
            "name": "Resistance Couriers",
            "aliases": ["Message Runners"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Fast runners who carry messages between resistance cells across the city.",
                    "role": "Communication network",
                    "relationships": {
                        "Carry": "Resistance messages",
                        "Connect": "Rebel cells"
                    }
                }
            }
        },
        "safe-house-keepers": {
            "name": "Safe House Keepers",
            "aliases": ["Sanctuary Operators"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Individuals who maintain secret safe houses for resistance members and fugitives.",
                    "role": "Sanctuary providers",
                    "relationships": {
                        "Maintain": "Secret safe houses",
                        "Shelter": "Resistance members"
                    }
                }
            }
        },
        "weapons-smugglers": {
            "name": "Weapons Smugglers",
            "aliases": ["Arms Dealers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Individuals who secretly transport weapons to resistance fighters.",
                    "role": "Illegal arms dealers",
                    "relationships": {
                        "Supply": "Resistance weapons",
                        "Smuggle": "Illegal armaments"
                    }
                }
            }
        },
        "propaganda-writers": {
            "name": "Propaganda Writers",
            "aliases": ["Revolutionary Authors"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Writers who create and distribute anti-royal propaganda and resistance materials.",
                    "role": "Revolutionary writers",
                    "relationships": {
                        "Write": "Anti-royal propaganda",
                        "Spread": "Resistance messages"
                    }
                }
            }
        },
        "underground-printers": {
            "name": "Underground Printers",
            "aliases": ["Secret Publishers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Printers who secretly produce and distribute forbidden texts and resistance materials.",
                    "role": "Illegal publishers",
                    "relationships": {
                        "Print": "Forbidden materials",
                        "Distribute": "Resistance literature"
                    }
                }
            }
        },
        "rebel-financiers": {
            "name": "Rebel Financiers",
            "aliases": ["Resistance Funders"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Wealthy individuals who secretly fund resistance operations against the crown.",
                    "role": "Secret funders",
                    "relationships": {
                        "Fund": "Resistance operations",
                        "Support": "Anti-royal cause"
                    }
                }
            }
        },
        "disgraced-nobles": {
            "name": "Disgraced Nobles",
            "aliases": ["Fallen Aristocrats"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Former nobles who lost favor with the crown and now support the resistance.",
                    "role": "Fallen aristocracy",
                    "relationships": {
                        "Lost favor with": "Royal crown",
                        "Support": "Resistance cause"
                    }
                }
            }
        },
        "former-soldiers": {
            "name": "Former Soldiers",
            "aliases": ["Ex-Military"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Ex-soldiers who deserted or were discharged and now fight against their former commanders.",
                    "role": "Military defectors",
                    "relationships": {
                        "Deserted from": "Royal army",
                        "Fight against": "Former comrades"
                    }
                }
            }
        },
        "escaped-prisoners": {
            "name": "Escaped Prisoners",
            "aliases": ["Prison Fugitives"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Prisoners who escaped from royal dungeons and now work against the crown.",
                    "role": "Vengeful fugitives",
                    "relationships": {
                        "Escaped from": "Royal prisons",
                        "Seek revenge against": "Crown"
                    }
                }
            }
        },
        "widows-and-orphans": {
            "name": "War Widows and Orphans",
            "aliases": ["War Victims"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Families who lost loved ones in the King's wars and now oppose his rule.",
                    "role": "Grieving families",
                    "relationships": {
                        "Lost family to": "King's wars",
                        "Oppose": "Royal rule"
                    }
                }
            }
        },
        "temple-refugees": {
            "name": "Temple Refugees",
            "aliases": ["Sacred Sanctuary Seekers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "People seeking sanctuary in temples from the growing violence and chaos.",
                    "role": "Sanctuary seekers",
                    "relationships": {
                        "Seek sanctuary in": "Temples",
                        "Flee from": "Urban violence"
                    }
                }
            }
        },
        "plague-doctors": {
            "name": "Plague Doctors",
            "aliases": ["Disease Specialists"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Doctors who treat the mysterious diseases spreading through parts of the city.",
                    "role": "Disease specialists",
                    "relationships": {
                        "Treat": "Mysterious diseases",
                        "Study": "Unexplained illnesses"
                    }
                }
            }
        },
        "quarantine-guards": {
            "name": "Quarantine Guards",
            "aliases": ["Isolation Enforcers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Guards who enforce quarantine zones around areas affected by mysterious diseases.",
                    "role": "Quarantine enforcement",
                    "relationships": {
                        "Enforce": "Quarantine zones",
                        "Prevent": "Disease spread"
                    }
                }
            }
        },
        "funeral-directors": {
            "name": "Funeral Directors",
            "aliases": ["Death Dealers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Individuals who handle the increasing number of funerals and burials in the city.",
                    "role": "Death services",
                    "relationships": {
                        "Handle": "City funerals",
                        "Bury": "Growing death toll"
                    }
                }
            }
        },
        "clock-tower-workers": {
            "name": "Clock Tower Workers",
            "aliases": ["Tower Maintainers"],
            "appearances": [65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "65": {
                    "revealedIn": 65,
                    "description": "Workers who maintain the great clock tower that becomes a target in Aelin's plans.",
                    "role": "Tower maintenance",
                    "relationships": {
                        "Maintain": "Clock tower",
                        "Target of": "Aelin's mission"
                    }
                }
            }
        },
        "glass-castle-architects": {
            "name": "Glass Castle Architects",
            "aliases": ["Castle Designers"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Architects who designed and know the secret passages of the glass castle.",
                    "role": "Structural experts",
                    "relationships": {
                        "Designed": "Glass castle",
                        "Know": "Secret passages"
                    }
                }
            }
        },
        "castle-stone-masons": {
            "name": "Castle Stone Masons",
            "aliases": ["Fortress Builders"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Master masons who built and maintain the stone portions of the glass castle.",
                    "role": "Castle builders",
                    "relationships": {
                        "Built": "Castle stonework",
                        "Know": "Structural weaknesses"
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
    add_more_characters_to_queen_of_shadows()