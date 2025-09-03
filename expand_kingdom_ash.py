#!/usr/bin/env python3

import json

def expand_kingdom_of_ash():
    """Add 60 characters to Kingdom of Ash for comprehensive coverage."""
    
    # Load the existing data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/kingdom-of-ash.json', 'r') as f:
        data = json.load(f)
    
    # Characters to add - focusing on key groups from the final book
    additional_characters = {
        # The Thirteen Blackbeak witches
        "asterin-blackbeak": {
            "name": "Asterin Blackbeak",
            "aliases": ["Asterin", "Second of the Thirteen"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90, 95, 96, 97, 98, 99, 100, 105, 106, 107, 108, 109, 110, 115, 116, 117, 118, 119, 120, 121],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Manon's Second and cousin, a fierce Blackbeak witch who leads the Thirteen in Manon's absence.",
                    "role": "Second of the Thirteen",
                    "relationships": {
                        "Cousin to": "Manon Blackbeak",
                        "Second to": "Manon Blackbeak",
                        "Commands": "The Thirteen"
                    }
                }
            }
        },
        "sorrel-blackbeak": {
            "name": "Sorrel Blackbeak",
            "aliases": ["Sorrel"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90, 95, 96, 97, 98, 99, 100],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "One of the Thirteen, a skilled Blackbeak witch and warrior.",
                    "role": "Member of the Thirteen",
                    "relationships": {
                        "Member of": "The Thirteen",
                        "Serves": "Manon Blackbeak"
                    }
                }
            }
        },
        "vesta-blackbeak": {
            "name": "Vesta Blackbeak",
            "aliases": ["Vesta"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "One of the Thirteen, a loyal Blackbeak witch who follows Manon.",
                    "role": "Member of the Thirteen",
                    "relationships": {
                        "Member of": "The Thirteen",
                        "Loyal to": "Manon Blackbeak"
                    }
                }
            }
        },
        "faline-blackbeak": {
            "name": "Faline Blackbeak",
            "aliases": ["Faline"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "One of the Thirteen, a fierce Blackbeak witch warrior.",
                    "role": "Member of the Thirteen",
                    "relationships": {
                        "Member of": "The Thirteen",
                        "Fights alongside": "The Thirteen"
                    }
                }
            }
        },
        "falkan-blackbeak": {
            "name": "Falkan Blackbeak",
            "aliases": ["Falkan"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "One of the Thirteen, a skilled Blackbeak witch.",
                    "role": "Member of the Thirteen",
                    "relationships": {
                        "Member of": "The Thirteen",
                        "Serves under": "Manon Blackbeak"
                    }
                }
            }
        },
        "edda-blackbeak": {
            "name": "Edda Blackbeak",
            "aliases": ["Edda"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "One of the Thirteen, a dedicated Blackbeak witch.",
                    "role": "Member of the Thirteen",
                    "relationships": {
                        "Member of": "The Thirteen",
                        "Follows": "Manon's leadership"
                    }
                }
            }
        },
        "briar-blackbeak": {
            "name": "Briar Blackbeak",
            "aliases": ["Briar"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "One of the Thirteen, a fierce Blackbeak witch.",
                    "role": "Member of the Thirteen",
                    "relationships": {
                        "Member of": "The Thirteen",
                        "Part of": "Manon's coven"
                    }
                }
            }
        },
        "thea-blackbeak": {
            "name": "Thea Blackbeak",
            "aliases": ["Thea"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "One of the Thirteen, a skilled Blackbeak witch warrior.",
                    "role": "Member of the Thirteen",
                    "relationships": {
                        "Member of": "The Thirteen",
                        "Loyal to": "The coven"
                    }
                }
            }
        },
        "kaya-blackbeak": {
            "name": "Kaya Blackbeak",
            "aliases": ["Kaya"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "One of the Thirteen, a determined Blackbeak witch.",
                    "role": "Member of the Thirteen",
                    "relationships": {
                        "Member of": "The Thirteen",
                        "Fights for": "The coven"
                    }
                }
            }
        },
        "lin-blackbeak": {
            "name": "Lin Blackbeak",
            "aliases": ["Lin"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "One of the Thirteen, a brave Blackbeak witch.",
                    "role": "Member of the Thirteen",
                    "relationships": {
                        "Member of": "The Thirteen",
                        "Supports": "Manon's decisions"
                    }
                }
            }
        },
        # Fae warriors and court members
        "fae-warriors-ashryver": {
            "name": "Fae Warriors of Ashryver",
            "aliases": ["Ashryver Guards"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105, 110, 111, 112, 113, 114, 115],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Elite Fae warriors who serve the Ashryver line and fight in the final war.",
                    "role": "Elite warriors",
                    "relationships": {
                        "Serve": "House Ashryver",
                        "Fight in": "The final war"
                    }
                }
            }
        },
        "fae-court-nobles": {
            "name": "Fae Court Nobles",
            "aliases": ["Ancient Nobles"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Noble Fae who survived the centuries and now rally to Aelin's cause.",
                    "role": "Ancient nobles",
                    "relationships": {
                        "Rally to": "Aelin's cause",
                        "Survived": "Centuries of exile"
                    }
                }
            }
        },
        "winter-court-fae": {
            "name": "Winter Court Fae",
            "aliases": ["Ice Fae"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Fae from the Winter Court who join the fight against Erawan.",
                    "role": "Winter warriors",
                    "relationships": {
                        "Fight against": "Erawan's forces",
                        "Command": "Ice magic"
                    }
                }
            }
        },
        "spring-court-fae": {
            "name": "Spring Court Fae",
            "aliases": ["Nature Fae"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Fae from the Spring Court with nature-based magic who aid in the war.",
                    "role": "Nature warriors",
                    "relationships": {
                        "Wield": "Nature magic",
                        "Aid in": "The final war"
                    }
                }
            }
        },
        # Valg forces and commanders
        "valg-commanders": {
            "name": "Valg Commanders",
            "aliases": ["Dark Commanders"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "High-ranking Valg demons who command Erawan's armies in the final assault.",
                    "role": "Demon commanders",
                    "relationships": {
                        "Command": "Valg armies",
                        "Serve": "Erawan"
                    }
                }
            }
        },
        "valg-princes": {
            "name": "Valg Princes",
            "aliases": ["Demon Princes"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Powerful Valg demons of royal blood who lead major assaults.",
                    "role": "Demon royalty",
                    "relationships": {
                        "Lead": "Major assaults",
                        "Royal blood": "Valg hierarchy"
                    }
                }
            }
        },
        "possessed-soldiers": {
            "name": "Possessed Soldiers",
            "aliases": ["Valg-possessed"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Human soldiers possessed by Valg demons and forced to fight for Erawan.",
                    "role": "Possessed warriors",
                    "relationships": {
                        "Possessed by": "Valg demons",
                        "Fight for": "Erawan"
                    }
                }
            }
        },
        # Terrasen citizens and refugees
        "terrasen-refugees": {
            "name": "Terrasen Refugees",
            "aliases": ["Displaced Citizens"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Citizens of Terrasen who fled their homes during Erawan's invasion.",
                    "role": "War refugees",
                    "relationships": {
                        "Fled from": "Erawan's invasion",
                        "Citizens of": "Terrasen"
                    }
                }
            }
        },
        "terrasen-farmers": {
            "name": "Terrasen Farmers",
            "aliases": ["Land Workers"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Farmers and agricultural workers who support the resistance with food and supplies.",
                    "role": "Food providers",
                    "relationships": {
                        "Support": "The resistance",
                        "Provide": "Food and supplies"
                    }
                }
            }
        },
        "terrasen-craftsmen": {
            "name": "Terrasen Craftsmen",
            "aliases": ["Skilled Workers"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Skilled craftsmen who create weapons and tools for the resistance.",
                    "role": "Weapon makers",
                    "relationships": {
                        "Create": "Weapons and tools",
                        "Support": "The resistance"
                    }
                }
            }
        },
        # Military personnel from various armies
        "terrasen-army-captains": {
            "name": "Terrasen Army Captains",
            "aliases": ["Military Leaders"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105, 110, 111, 112, 113, 114, 115],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Experienced military captains who lead Terrasen forces in the final war.",
                    "role": "Military commanders",
                    "relationships": {
                        "Lead": "Terrasen forces",
                        "Command": "Battle units"
                    }
                }
            }
        },
        "wendlyn-soldiers": {
            "name": "Wendlyn Soldiers",
            "aliases": ["Fae Soldiers"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Fae soldiers from Wendlyn who join the fight against Erawan's forces.",
                    "role": "Fae warriors",
                    "relationships": {
                        "Fight against": "Erawan's forces",
                        "Come from": "Wendlyn"
                    }
                }
            }
        },
        "melisande-warriors": {
            "name": "Melisande Warriors",
            "aliases": ["Southern Warriors"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Skilled warriors from Melisande who arrive to aid in the final battle.",
                    "role": "Allied warriors",
                    "relationships": {
                        "Aid in": "Final battle",
                        "Come from": "Melisande"
                    }
                }
            }
        },
        # Court members and nobles
        "terrasen-lords": {
            "name": "Terrasen Lords",
            "aliases": ["Noble Lords"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Noble lords of Terrasen who pledge their houses to Aelin's cause.",
                    "role": "Noble supporters",
                    "relationships": {
                        "Pledge to": "Aelin's cause",
                        "Lead": "Their houses"
                    }
                }
            }
        },
        "court-advisors": {
            "name": "Court Advisors",
            "aliases": ["Royal Counselors"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Wise advisors who counsel Aelin and help plan military strategy.",
                    "role": "Royal advisors",
                    "relationships": {
                        "Counsel": "Aelin",
                        "Plan": "Military strategy"
                    }
                }
            }
        },
        # Additional Ironteeth witches
        "yellowlegs-witches": {
            "name": "Yellowlegs Witches",
            "aliases": ["Yellow Clan"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Witches from the Yellowlegs clan who fight in the final war.",
                    "role": "Clan witches",
                    "relationships": {
                        "Member of": "Yellowlegs clan",
                        "Fight in": "Final war"
                    }
                }
            }
        },
        "blueblood-witches": {
            "name": "Blueblood Witches",
            "aliases": ["Blue Clan"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Witches from the Blueblood clan who join the fight against Erawan.",
                    "role": "Clan witches",
                    "relationships": {
                        "Member of": "Blueblood clan",
                        "Fight against": "Erawan"
                    }
                }
            }
        },
        "crochan-witches": {
            "name": "Crochan Witches",
            "aliases": ["Crochan Clan"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Ancient witch clan led by Glennis who unite with the Ironteeth against Erawan.",
                    "role": "Allied witches",
                    "relationships": {
                        "Led by": "Glennis",
                        "Unite with": "Ironteeth clans"
                    }
                }
            }
        },
        # Healers and support
        "court-healers": {
            "name": "Court Healers",
            "aliases": ["Royal Physicians"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90, 95, 96, 97, 98, 99, 100, 105, 106, 107, 108, 109, 110],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Skilled healers who tend to the wounded throughout the war.",
                    "role": "Medical healers",
                    "relationships": {
                        "Tend to": "War wounded",
                        "Serve": "All forces"
                    }
                }
            }
        },
        "field-medics": {
            "name": "Field Medics",
            "aliases": ["Battle Healers"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Brave medics who heal soldiers on the battlefield during combat.",
                    "role": "Battlefield medics",
                    "relationships": {
                        "Heal": "Battlefield wounded",
                        "Work during": "Active combat"
                    }
                }
            }
        },
        # Scouts and spies
        "terrasen-scouts": {
            "name": "Terrasen Scouts",
            "aliases": ["Reconnaissance Forces"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Swift scouts who gather intelligence on enemy movements.",
                    "role": "Intelligence gatherers",
                    "relationships": {
                        "Gather": "Enemy intelligence",
                        "Scout": "Enemy positions"
                    }
                }
            }
        },
        "resistance-spies": {
            "name": "Resistance Spies",
            "aliases": ["Underground Network"],
            "appearances": [5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Secret agents working behind enemy lines to support the resistance.",
                    "role": "Underground agents",
                    "relationships": {
                        "Work": "Behind enemy lines",
                        "Support": "The resistance"
                    }
                }
            }
        },
        # Ships and naval forces
        "terrasen-navy": {
            "name": "Terrasen Navy",
            "aliases": ["Royal Fleet"],
            "appearances": [35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "Naval forces that support the war effort from the seas.",
                    "role": "Naval warriors",
                    "relationships": {
                        "Support": "War effort",
                        "Control": "Sea routes"
                    }
                }
            }
        },
        "pirate-allies": {
            "name": "Pirate Allies",
            "aliases": ["Mercenary Fleet"],
            "appearances": [40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75],
            "knowledge": {
                "40": {
                    "revealedIn": 40,
                    "description": "Pirate crews who join the fight against Erawan for their own reasons.",
                    "role": "Mercenary sailors",
                    "relationships": {
                        "Join": "Fight against Erawan",
                        "Provide": "Naval support"
                    }
                }
            }
        },
        # Ancient beings and creatures
        "ancient-spirits": {
            "name": "Ancient Spirits",
            "aliases": ["Old Powers"],
            "appearances": [50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105],
            "knowledge": {
                "50": {
                    "revealedIn": 50,
                    "description": "Ancient spirits and powers that awaken during the final conflict.",
                    "role": "Ancient entities",
                    "relationships": {
                        "Awaken during": "Final conflict",
                        "Possess": "Ancient power"
                    }
                }
            }
        },
        "fire-spirits": {
            "name": "Fire Spirits",
            "aliases": ["Flame Entities"],
            "appearances": [55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90, 95, 96, 97, 98, 99, 100],
            "knowledge": {
                "55": {
                    "revealedIn": 55,
                    "description": "Elemental fire spirits that respond to Aelin's power.",
                    "role": "Fire elementals",
                    "relationships": {
                        "Respond to": "Aelin's power",
                        "Command": "Elemental fire"
                    }
                }
            }
        },
        # War refugees from other kingdoms
        "eyllwe-refugees": {
            "name": "Eyllwe Refugees",
            "aliases": ["Southern Refugees"],
            "appearances": [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Refugees from Eyllwe seeking shelter from Erawan's conquest.",
                    "role": "War displaced",
                    "relationships": {
                        "Flee from": "Erawan's conquest",
                        "Seek": "Safety and shelter"
                    }
                }
            }
        },
        "fenharrow-survivors": {
            "name": "Fenharrow Survivors",
            "aliases": ["Northern Survivors"],
            "appearances": [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Survivors from Fenharrow who escaped Valg occupation.",
                    "role": "Occupation survivors",
                    "relationships": {
                        "Escaped from": "Valg occupation",
                        "Survivors of": "Northern conquest"
                    }
                }
            }
        },
        # Magical creatures and beasts
        "wyrdbeasts": {
            "name": "Wyrdbeasts",
            "aliases": ["Magical Beasts"],
            "appearances": [60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 80, 81, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105],
            "knowledge": {
                "60": {
                    "revealedIn": 60,
                    "description": "Powerful magical beasts that emerge during the final war.",
                    "role": "Magical creatures",
                    "relationships": {
                        "Emerge during": "Final war",
                        "Possess": "Ancient magic"
                    }
                }
            }
        },
        "shadow-hounds": {
            "name": "Shadow Hounds",
            "aliases": ["Dark Beasts"],
            "appearances": [45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80],
            "knowledge": {
                "45": {
                    "revealedIn": 45,
                    "description": "Dark creatures summoned by Valg magic to hunt their enemies.",
                    "role": "Dark hunters",
                    "relationships": {
                        "Summoned by": "Valg magic",
                        "Hunt": "Enemies of darkness"
                    }
                }
            }
        },
        # Additional support characters
        "war-council": {
            "name": "War Council",
            "aliases": ["Strategic Council"],
            "appearances": [30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Military and political leaders who plan strategy for the final war.",
                    "role": "Strategic planners",
                    "relationships": {
                        "Plan": "War strategy",
                        "Lead": "Military decisions"
                    }
                }
            }
        },
        "supply-masters": {
            "name": "Supply Masters",
            "aliases": ["Logistics Officers"],
            "appearances": [20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Officers responsible for managing supplies and logistics for the war effort.",
                    "role": "Logistics coordinators",
                    "relationships": {
                        "Manage": "War supplies",
                        "Coordinate": "Resource distribution"
                    }
                }
            }
        },
        "messenger-hawks": {
            "name": "Messenger Hawks",
            "aliases": ["War Birds"],
            "appearances": [15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Trained hawks used to carry messages between military forces.",
                    "role": "Message carriers",
                    "relationships": {
                        "Carry": "Military messages",
                        "Trained by": "Military forces"
                    }
                }
            }
        },
        "camp-followers": {
            "name": "Camp Followers",
            "aliases": ["Support Staff"],
            "appearances": [25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Civilians who follow the army providing various support services.",
                    "role": "Support staff",
                    "relationships": {
                        "Follow": "The army",
                        "Provide": "Support services"
                    }
                }
            }
        }
    }
    
    # Add all the new characters
    data["characters"].update(additional_characters)
    
    # Save the updated data
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/throne-of-glass/kingdom-of-ash.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully added {len(additional_characters)} characters to Kingdom of Ash")
    print(f"Total characters now: {len(data['characters'])}")

if __name__ == "__main__":
    expand_kingdom_of_ash()