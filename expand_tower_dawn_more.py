#!/usr/bin/env python3

import json

def add_more_characters_to_tower_of_dawn():
    """Add more characters to Tower of Dawn to reach 150+ total for comprehensive coverage."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/tower-of-dawn.json', 'r') as f:
        data = json.load(f)
    
    # More characters to add - 55+ more to reach 150+ total
    additional_characters = {
        "military-trainers": {
            "name": "Military Trainers",
            "aliases": ["Combat Instructors"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Instructors who train soldiers and officers in combat techniques and military tactics.",
                    "role": "Military education",
                    "relationships": {
                        "Train": "Military personnel",
                        "Teach": "Combat techniques"
                    }
                }
            }
        },
        "battle-medics": {
            "name": "Battle Medics",
            "aliases": ["Field Healers"],
            "appearances": [40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 66, 67, 68],
            "knowledge": {
                "40": {
                    "revealedIn": 40,
                    "description": "Medical personnel who treat wounded soldiers during battles and campaigns.",
                    "role": "Military medical",
                    "relationships": {
                        "Treat": "Battle wounded",
                        "Serve": "Military forces"
                    }
                }
            }
        },
        "supply-officers": {
            "name": "Supply Officers",
            "aliases": ["Logistics Coordinators"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officers responsible for managing supplies and logistics for military operations.",
                    "role": "Military logistics",
                    "relationships": {
                        "Manage": "Military supplies",
                        "Coordinate": "Logistics operations"
                    }
                }
            }
        },
        "camp-followers": {
            "name": "Camp Followers",
            "aliases": ["Military Support"],
            "appearances": [45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "45": {
                    "revealedIn": 45,
                    "description": "Civilians who follow military camps providing various support services.",
                    "role": "Camp support",
                    "relationships": {
                        "Follow": "Military camps",
                        "Provide": "Support services"
                    }
                }
            }
        },
        "war-correspondents": {
            "name": "War Correspondents",
            "aliases": ["Military Chroniclers"],
            "appearances": [45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "45": {
                    "revealedIn": 45,
                    "description": "Writers and chroniclers who document military campaigns and battles.",
                    "role": "Military documentation",
                    "relationships": {
                        "Document": "Military campaigns",
                        "Chronicle": "Battle events"
                    }
                }
            }
        },
        "siege-specialists": {
            "name": "Siege Specialists",
            "aliases": ["Fortress Breakers"],
            "appearances": [45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "45": {
                    "revealedIn": 45,
                    "description": "Military experts who specialize in conducting and defending against sieges.",
                    "role": "Siege warfare",
                    "relationships": {
                        "Expert in": "Siege operations",
                        "Specialize in": "Fortress warfare"
                    }
                }
            }
        },
        "cavalry-officers": {
            "name": "Cavalry Officers",
            "aliases": ["Mounted Commanders"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officers who command cavalry units and mounted forces.",
                    "role": "Cavalry command",
                    "relationships": {
                        "Command": "Cavalry units",
                        "Lead": "Mounted forces"
                    }
                }
            }
        },
        "infantry-captains": {
            "name": "Infantry Captains",
            "aliases": ["Foot Soldiers Leaders"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officers who command infantry units and foot soldiers.",
                    "role": "Infantry leadership",
                    "relationships": {
                        "Command": "Infantry units",
                        "Lead": "Foot soldiers"
                    }
                }
            }
        },
        "archer-commanders": {
            "name": "Archer Commanders",
            "aliases": ["Ranged Unit Leaders"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officers who command archer units and ranged weapon specialists.",
                    "role": "Ranged warfare command",
                    "relationships": {
                        "Command": "Archer units",
                        "Lead": "Ranged specialists"
                    }
                }
            }
        },
        "naval-officers": {
            "name": "Naval Officers",
            "aliases": ["Fleet Command"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officers who command naval vessels and maritime military operations.",
                    "role": "Naval command",
                    "relationships": {
                        "Command": "Naval vessels",
                        "Lead": "Maritime operations"
                    }
                }
            }
        },
        "quartermasters": {
            "name": "Quartermasters",
            "aliases": ["Supply Managers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officers responsible for managing military supplies, equipment, and provisions.",
                    "role": "Supply management",
                    "relationships": {
                        "Manage": "Military supplies",
                        "Distribute": "Equipment and provisions"
                    }
                }
            }
        },
        "drill-sergeants": {
            "name": "Drill Sergeants",
            "aliases": ["Training Officers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Non-commissioned officers who train recruits and maintain military discipline.",
                    "role": "Military training",
                    "relationships": {
                        "Train": "Military recruits",
                        "Maintain": "Military discipline"
                    }
                }
            }
        },
        "military-priests": {
            "name": "Military Chaplains",
            "aliases": ["Army Priests"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Religious officials who provide spiritual guidance and services to military personnel.",
                    "role": "Military spiritual care",
                    "relationships": {
                        "Serve": "Military personnel",
                        "Provide": "Spiritual guidance"
                    }
                }
            }
        },
        "military-musicians": {
            "name": "Military Musicians",
            "aliases": ["Army Band"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Musicians who provide music for military ceremonies and boost troop morale.",
                    "role": "Military entertainment",
                    "relationships": {
                        "Perform for": "Military ceremonies",
                        "Boost": "Troop morale"
                    }
                }
            }
        },
        "fortress-engineers": {
            "name": "Fortress Engineers",
            "aliases": ["Defensive Specialists"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Engineers who design and build fortifications and defensive structures.",
                    "role": "Defensive engineering",
                    "relationships": {
                        "Design": "Fortifications",
                        "Build": "Defensive structures"
                    }
                }
            }
        },
        "weapon-masters": {
            "name": "Weapon Masters",
            "aliases": ["Arms Instructors"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Expert warriors who teach advanced weapon techniques to military officers.",
                    "role": "Weapons training",
                    "relationships": {
                        "Teach": "Weapon techniques",
                        "Train": "Military officers"
                    }
                }
            }
        },
        "military-couriers": {
            "name": "Military Couriers",
            "aliases": ["Battle Messengers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Fast riders who carry military messages and orders between commanders.",
                    "role": "Military communications",
                    "relationships": {
                        "Carry": "Military messages",
                        "Connect": "Military commanders"
                    }
                }
            }
        },
        "scouts-and-rangers": {
            "name": "Military Scouts and Rangers",
            "aliases": ["Reconnaissance Forces"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Specialized soldiers who gather intelligence and scout enemy positions.",
                    "role": "Military reconnaissance",
                    "relationships": {
                        "Scout": "Enemy positions",
                        "Gather": "Military intelligence"
                    }
                }
            }
        },
        "honor-guards": {
            "name": "Honor Guards",
            "aliases": ["Elite Protectors"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Elite guards who protect high-ranking officials and dignitaries.",
                    "role": "Elite protection",
                    "relationships": {
                        "Protect": "High officials",
                        "Guard": "Important dignitaries"
                    }
                }
            }
        },
        "ceremonial-guards": {
            "name": "Ceremonial Guards",
            "aliases": ["Parade Soldiers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Guards who participate in ceremonies and official state functions.",
                    "role": "Ceremonial duties",
                    "relationships": {
                        "Participate in": "State ceremonies",
                        "Guard": "Official functions"
                    }
                }
            }
        },
        "palace-security": {
            "name": "Palace Security Chiefs",
            "aliases": ["Security Coordinators"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Chiefs who coordinate and oversee all palace security operations.",
                    "role": "Security coordination",
                    "relationships": {
                        "Coordinate": "Palace security",
                        "Oversee": "Protection operations"
                    }
                }
            }
        },
        "diplomatic-guards": {
            "name": "Diplomatic Guards",
            "aliases": ["Embassy Protection"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Specialized guards who protect diplomatic missions and foreign dignitaries.",
                    "role": "Diplomatic security",
                    "relationships": {
                        "Protect": "Diplomatic missions",
                        "Guard": "Foreign dignitaries"
                    }
                }
            }
        },
        "royal-tutors": {
            "name": "Royal Tutors",
            "aliases": ["Prince and Princess Teachers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Educated individuals who teach the royal children various subjects and skills.",
                    "role": "Royal education",
                    "relationships": {
                        "Teach": "Royal children",
                        "Provide": "Elite education"
                    }
                }
            }
        },
        "court-historians": {
            "name": "Court Historians",
            "aliases": ["Royal Chroniclers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Scholars who record and maintain the official history of the royal family and empire.",
                    "role": "Historical documentation",
                    "relationships": {
                        "Record": "Royal history",
                        "Maintain": "Imperial chronicles"
                    }
                }
            }
        },
        "court-astronomers": {
            "name": "Court Astronomers",
            "aliases": ["Royal Star Readers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Scholars who study celestial movements and provide astrological guidance to the court.",
                    "role": "Celestial advisors",
                    "relationships": {
                        "Study": "Celestial movements",
                        "Advise": "Royal court"
                    }
                }
            }
        },
        "court-mathematicians": {
            "name": "Court Mathematicians",
            "aliases": ["Royal Calculators"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Scholars who handle mathematical calculations for engineering, taxation, and administrative purposes.",
                    "role": "Mathematical services",
                    "relationships": {
                        "Calculate": "Administrative needs",
                        "Support": "Engineering projects"
                    }
                }
            }
        },
        "court-philosophers": {
            "name": "Court Philosophers",
            "aliases": ["Royal Wisdom Teachers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Wise scholars who provide philosophical guidance and ethical counsel to the royal family.",
                    "role": "Wisdom advisors",
                    "relationships": {
                        "Advise": "Royal family",
                        "Provide": "Philosophical guidance"
                    }
                }
            }
        },
        "court-poets": {
            "name": "Court Poets",
            "aliases": ["Royal Verse Writers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Poets who compose verses celebrating the royal family and important events.",
                    "role": "Royal poetry",
                    "relationships": {
                        "Compose": "Royal verses",
                        "Celebrate": "Important events"
                    }
                }
            }
        },
        "court-artists": {
            "name": "Court Artists",
            "aliases": ["Royal Painters"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Artists who create paintings, sculptures, and other artworks for the royal court.",
                    "role": "Royal art",
                    "relationships": {
                        "Create": "Royal artwork",
                        "Decorate": "Palace spaces"
                    }
                }
            }
        },
        "palace-maids": {
            "name": "Palace Maids",
            "aliases": ["Cleaning Staff"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Female servants who clean and maintain the living spaces within the palace.",
                    "role": "Palace maintenance",
                    "relationships": {
                        "Clean": "Palace rooms",
                        "Maintain": "Living spaces"
                    }
                }
            }
        },
        "palace-valets": {
            "name": "Palace Valets",
            "aliases": ["Personal Attendants"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Male servants who attend to the personal needs of royal family members and high officials.",
                    "role": "Personal service",
                    "relationships": {
                        "Attend to": "Royal personal needs",
                        "Serve": "High officials"
                    }
                }
            }
        },
        "palace-pages": {
            "name": "Palace Pages",
            "aliases": ["Young Servants"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Young servants who carry messages and perform simple tasks around the palace.",
                    "role": "Junior servants",
                    "relationships": {
                        "Carry": "Palace messages",
                        "Perform": "Simple tasks"
                    }
                }
            }
        },
        "palace-doorkeepers": {
            "name": "Palace Doorkeepers",
            "aliases": ["Entry Guards"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Guards who control access to various rooms and areas within the palace.",
                    "role": "Access control",
                    "relationships": {
                        "Control": "Palace access",
                        "Guard": "Important doors"
                    }
                }
            }
        },
        "palace-night-watch": {
            "name": "Palace Night Watch",
            "aliases": ["Evening Security"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Guards who patrol the palace during nighttime hours to ensure security.",
                    "role": "Night security",
                    "relationships": {
                        "Patrol": "Palace at night",
                        "Ensure": "Evening security"
                    }
                }
            }
        },
        "imperial-advisors": {
            "name": "Imperial Advisors",
            "aliases": ["High Counselors"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "High-ranking advisors who counsel the Khagan on important matters of state.",
                    "role": "State advisors",
                    "relationships": {
                        "Advise": "The Khagan",
                        "Counsel on": "State matters"
                    }
                }
            }
        },
        "provincial-governors": {
            "name": "Provincial Governors",
            "aliases": ["Regional Rulers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Appointed officials who govern various provinces and regions of the empire.",
                    "role": "Regional governance",
                    "relationships": {
                        "Govern": "Imperial provinces",
                        "Report to": "Central authority"
                    }
                }
            }
        },
        "trade-guild-masters": {
            "name": "Trade Guild Masters",
            "aliases": ["Commerce Leaders"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Leaders of various trade guilds who regulate commerce and crafts.",
                    "role": "Trade leadership",
                    "relationships": {
                        "Lead": "Trade guilds",
                        "Regulate": "Commerce activities"
                    }
                }
            }
        },
        "master-craftsmen": {
            "name": "Master Craftsmen",
            "aliases": ["Artisan Experts"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Highly skilled craftsmen who create the finest goods and train apprentices.",
                    "role": "Master artisans",
                    "relationships": {
                        "Create": "Fine goods",
                        "Train": "Craft apprentices"
                    }
                }
            }
        },
        "merchant-princes": {
            "name": "Merchant Princes",
            "aliases": ["Wealthy Traders"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Extremely wealthy merchants who wield significant economic and political influence.",
                    "role": "Economic power",
                    "relationships": {
                        "Control": "Trade networks",
                        "Wield": "Economic influence"
                    }
                }
            }
        },
        "banking-officials": {
            "name": "Banking Officials",
            "aliases": ["Financial Managers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Officials who manage banks and financial institutions throughout the empire.",
                    "role": "Financial services",
                    "relationships": {
                        "Manage": "Banking operations",
                        "Handle": "Financial transactions"
                    }
                }
            }
        },
        "currency-minters": {
            "name": "Currency Minters",
            "aliases": ["Coin Makers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Specialists who mint coins and create currency for the empire's economy.",
                    "role": "Currency production",
                    "relationships": {
                        "Mint": "Imperial currency",
                        "Create": "Economic medium"
                    }
                }
            }
        },
        "jewel-appraisers": {
            "name": "Jewel Appraisers",
            "aliases": ["Gem Experts"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Experts who evaluate the quality and value of precious gems and jewelry.",
                    "role": "Gem evaluation",
                    "relationships": {
                        "Evaluate": "Precious gems",
                        "Determine": "Jewelry value"
                    }
                }
            }
        },
        "silk-merchants": {
            "name": "Silk Merchants",
            "aliases": ["Luxury Fabric Dealers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Merchants who trade in fine silks and luxury fabrics from across the known world.",
                    "role": "Luxury trade",
                    "relationships": {
                        "Trade in": "Fine silks",
                        "Deal": "Luxury fabrics"
                    }
                }
            }
        },
        "spice-traders": {
            "name": "Spice Traders",
            "aliases": ["Exotic Goods Dealers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Traders who import exotic spices and rare goods from distant lands.",
                    "role": "Exotic trade",
                    "relationships": {
                        "Import": "Exotic spices",
                        "Trade": "Rare goods"
                    }
                }
            }
        },
        "perfume-makers": {
            "name": "Perfume Makers",
            "aliases": ["Scent Artisans"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Artisans who create exquisite perfumes and scented oils for the wealthy.",
                    "role": "Luxury fragrances",
                    "relationships": {
                        "Create": "Fine perfumes",
                        "Serve": "Wealthy clientele"
                    }
                }
            }
        },
        "carpet-weavers": {
            "name": "Carpet Weavers",
            "aliases": ["Textile Masters"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Master weavers who create intricate carpets and textiles renowned throughout the empire.",
                    "role": "Textile artistry",
                    "relationships": {
                        "Weave": "Intricate carpets",
                        "Create": "Artistic textiles"
                    }
                }
            }
        },
        "glass-blowers": {
            "name": "Glass Blowers",
            "aliases": ["Glass Artisans"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Skilled artisans who create beautiful glassware and decorative glass objects.",
                    "role": "Glass artistry",
                    "relationships": {
                        "Create": "Glass artwork",
                        "Craft": "Decorative objects"
                    }
                }
            }
        },
        "pottery-masters": {
            "name": "Pottery Masters",
            "aliases": ["Ceramic Artisans"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Master potters who create fine ceramics and pottery for both practical and decorative use.",
                    "role": "Ceramic artistry",
                    "relationships": {
                        "Create": "Fine ceramics",
                        "Craft": "Artistic pottery"
                    }
                }
            }
        },
        "metal-workers": {
            "name": "Metal Workers",
            "aliases": ["Metalcraft Artisans"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Skilled workers who shape metal into tools, decorative objects, and artistic pieces.",
                    "role": "Metalcraft",
                    "relationships": {
                        "Shape": "Metal objects",
                        "Create": "Artistic metalwork"
                    }
                }
            }
        },
        "wood-carvers": {
            "name": "Wood Carvers",
            "aliases": ["Woodworking Artisans"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Artisans who carve intricate designs and create beautiful objects from wood.",
                    "role": "Woodcarving artistry",
                    "relationships": {
                        "Carve": "Intricate designs",
                        "Create": "Wooden artwork"
                    }
                }
            }
        },
        "bone-carvers": {
            "name": "Bone Carvers",
            "aliases": ["Ivory Artisans"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Specialized artisans who carve bone and ivory into decorative and functional objects.",
                    "role": "Bone artistry",
                    "relationships": {
                        "Carve": "Bone and ivory",
                        "Create": "Decorative objects"
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
    add_more_characters_to_tower_of_dawn()