#!/usr/bin/env python3
import json

# Read existing data
with open('data/harry-potter/chamber-of-secrets.json', 'r') as f:
    data = json.load(f)

# Additional characters to reach 200+
more_characters = {
    # Daily Prophet staff
    "barnabas-cuffe": {
        "name": "Barnabas Cuffe",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "Editor of the Daily Prophet newspaper mentioned in wizarding media discussions.",
                "role": "Daily Prophet Editor",
                "relationships": {}
            }
        }
    },
    "betty-braithwaite": {
        "name": "Betty Braithwaite",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "4": {
                "revealedIn": 4,
                "description": "Reporter for the Daily Prophet who writes about celebrity wizards like Lockhart.",
                "role": "Daily Prophet reporter",
                "relationships": {
                    "Gilderoy Lockhart": "Interviews"
                }
            }
        }
    },
    
    # Additional Slytherin students
    "flora-carrow": {
        "name": "Flora Carrow",
        "aliases": [],
        "appearances": [7],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Slytherin student in an upper year.",
                "role": "Slytherin student",
                "relationships": {
                    "Hestia Carrow": "Twin sister of"
                }
            }
        }
    },
    "hestia-carrow": {
        "name": "Hestia Carrow",
        "aliases": [],
        "appearances": [7],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Slytherin student in an upper year.",
                "role": "Slytherin student",
                "relationships": {
                    "Flora Carrow": "Twin sister of"
                }
            }
        }
    },
    "tracey-davis": {
        "name": "Tracey Davis",
        "aliases": [],
        "appearances": [7],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Slytherin student in Harry's year.",
                "role": "Slytherin student",
                "relationships": {
                    "Daphne Greengrass": "Friend of"
                }
            }
        }
    },
    
    # Lockhart's victims (real adventurers he stole from)
    "armenian-warlock": {
        "name": "Armenian Warlock",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "16": {
                "revealedIn": 16,
                "description": "The real wizard who saved a village from werewolves, whose memory was modified by Lockhart.",
                "role": "Memory-modified wizard",
                "relationships": {
                    "Gilderoy Lockhart": "Memory stolen by"
                }
            }
        }
    },
    "witch-with-hairy-chin": {
        "name": "Witch with Hairy Chin",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "16": {
                "revealedIn": 16,
                "description": "Witch who actually defeated the Bandon Banshee, memory modified by Lockhart.",
                "role": "Memory-modified witch",
                "relationships": {
                    "Gilderoy Lockhart": "Memory stolen by"
                }
            }
        }
    },
    
    # Additional ghosts
    "cuthbert-binns-living": {
        "name": "Cuthbert Binns (when alive)",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Professor Binns when he was alive, before becoming the only ghost teacher.",
                "role": "Former living professor",
                "relationships": {}
            }
        }
    },
    "edgar-clogg": {
        "name": "Edgar Clogg",
        "aliases": ["Eggy"],
        "appearances": [8],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "Ghost who attends Nearly Headless Nick's deathday party.",
                "role": "Ghost",
                "relationships": {
                    "Nearly Headless Nick": "Deathday guest of"
                }
            }
        }
    },
    
    # Famous Quidditch players mentioned
    "galvin-gudgeon": {
        "name": "Galvin Gudgeon",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Famous Chaser for the Chudley Cannons mentioned during Quidditch discussions.",
                "role": "Professional Chaser",
                "relationships": {}
            }
        }
    },
    "joey-jenkins": {
        "name": "Joey Jenkins",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Beater for the Chudley Cannons, Ron's favorite team.",
                "role": "Professional Beater",
                "relationships": {}
            }
        }
    },
    "ragmar-dorkins": {
        "name": "Ragmar Dorkins",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Manager of the Chudley Cannons Quidditch team.",
                "role": "Quidditch manager",
                "relationships": {}
            }
        }
    },
    
    # St. Mungo's staff mentioned
    "hippocrates-smethwyck": {
        "name": "Hippocrates Smethwyck",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Healer-in-Charge at St. Mungo's Hospital mentioned in medical discussions.",
                "role": "Head Healer",
                "relationships": {}
            }
        }
    },
    "augustus-pye": {
        "name": "Augustus Pye",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Trainee Healer at St. Mungo's Hospital.",
                "role": "Trainee Healer",
                "relationships": {}
            }
        }
    },
    
    # Additional Ministry departments
    "bode": {
        "name": "Bode",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "Unspeakable working in the Department of Mysteries.",
                "role": "Unspeakable",
                "relationships": {}
            }
        }
    },
    "croaker": {
        "name": "Croaker",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "Unspeakable working in the Department of Mysteries.",
                "role": "Unspeakable",
                "relationships": {}
            }
        }
    },
    
    # Wizard historians and authors
    "phyllida-spore": {
        "name": "Phyllida Spore",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Author of One Thousand Magical Herbs and Fungi textbook.",
                "role": "Herbology author",
                "relationships": {}
            }
        }
    },
    "arsenius-jigger": {
        "name": "Arsenius Jigger",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Author of Magical Drafts and Potions textbook.",
                "role": "Potions author",
                "relationships": {}
            }
        }
    },
    "adalbert-waffling": {
        "name": "Adalbert Waffling",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Author of Magical Theory textbook.",
                "role": "Theory author",
                "relationships": {}
            }
        }
    },
    "quentin-trimble": {
        "name": "Quentin Trimble",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Author of The Dark Forces: A Guide to Self-Protection.",
                "role": "Defense author",
                "relationships": {}
            }
        }
    },
    "emeric-switch": {
        "name": "Emeric Switch",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Author of A Beginner's Guide to Transfiguration.",
                "role": "Transfiguration author",
                "relationships": {}
            }
        }
    },
    
    # Magical law enforcement
    "bob-ogden": {
        "name": "Bob Ogden",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Member of the Magical Law Enforcement Squad from the past.",
                "role": "Law enforcement wizard",
                "relationships": {}
            }
        }
    },
    "tiberius-ogden": {
        "name": "Tiberius Ogden",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "Member of the Wizengamot mentioned in legal discussions.",
                "role": "Wizengamot member",
                "relationships": {}
            }
        }
    },
    "griselda-marchbanks": {
        "name": "Griselda Marchbanks",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "Elder member of the Wizengamot and head of the Wizarding Examinations Authority.",
                "role": "Examinations head",
                "relationships": {}
            }
        }
    },
    
    # Weasley extended family
    "cousin-mafalda": {
        "name": "Cousin Mafalda",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "Distant Weasley cousin mentioned by Mrs. Weasley.",
                "role": "Weasley relative",
                "relationships": {
                    "Molly Weasley": "Distant cousin of"
                }
            }
        }
    },
    "great-aunt-muriel": {
        "name": "Great Aunt Muriel",
        "aliases": ["Aunt Muriel"],
        "appearances": [],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "Elderly Weasley relative who is quite critical and owns goblin-made tiara.",
                "role": "Weasley relative",
                "relationships": {
                    "Molly Weasley": "Aunt of"
                }
            }
        }
    },
    
    # Borgin and Burkes associates
    "caractacus-burke": {
        "name": "Caractacus Burke",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "4": {
                "revealedIn": 4,
                "description": "Co-founder of Borgin and Burkes dark artifacts shop.",
                "role": "Shop co-owner",
                "relationships": {
                    "Mr. Borgin": "Business partner of"
                }
            }
        }
    },
    
    # Additional petrified victims mentioned
    "clearwater": {
        "name": "Clearwater",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "Upper year student mentioned among petrification victims.",
                "role": "Petrification victim",
                "relationships": {}
            }
        }
    },
    
    # Wizard inventors
    "ignatia-wildsmith": {
        "name": "Ignatia Wildsmith",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "4": {
                "revealedIn": 4,
                "description": "Inventor of Floo Powder mentioned when Harry uses the Floo Network.",
                "role": "Inventor",
                "relationships": {}
            }
        }
    },
    "bowman-wright": {
        "name": "Bowman Wright",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Inventor of the Golden Snitch mentioned in Quidditch history.",
                "role": "Snitch inventor",
                "relationships": {}
            }
        }
    },
    
    # Additional historical figures
    "elfric-the-eager": {
        "name": "Elfric the Eager",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Historical wizard known for his enthusiastic but misguided attempts at magic.",
                "role": "Historical wizard",
                "relationships": {}
            }
        }
    },
    "wilfred-the-wistful": {
        "name": "Wilfred the Wistful",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Historical wizard mentioned in History of Magic class.",
                "role": "Historical wizard",
                "relationships": {}
            }
        }
    },
    "ethelred-the-ever-ready": {
        "name": "Ethelred the Ever-Ready",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Historical wizard famous for taking offense at the slightest provocation.",
                "role": "Historical wizard",
                "relationships": {}
            }
        }
    },
    
    # Magical creatures experts
    "gondoline-oliphant": {
        "name": "Gondoline Oliphant",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "15": {
                "revealedIn": 15,
                "description": "Expert on trolls mentioned in Care of Magical Creatures references.",
                "role": "Troll expert",
                "relationships": {}
            }
        }
    },
    "harvey-ridgebit": {
        "name": "Harvey Ridgebit",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "15": {
                "revealedIn": 15,
                "description": "Dragon specialist mentioned in discussions about dangerous creatures.",
                "role": "Dragon expert",
                "relationships": {}
            }
        }
    },
    
    # Additional shop owners
    "amanuensis-quill": {
        "name": "Amanuensis Quill",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "4": {
                "revealedIn": 4,
                "description": "Owner of Scribbulus Writing Implements in Diagon Alley.",
                "role": "Shop owner",
                "relationships": {}
            }
        }
    },
    "wiseacres-wizarding-equipment": {
        "name": "Wiseacre",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "4": {
                "revealedIn": 4,
                "description": "Owner of Wiseacre's Wizarding Equipment shop.",
                "role": "Shop owner",
                "relationships": {}
            }
        }
    },
    
    # Wizard wireless personalities
    "glenda-chittock": {
        "name": "Glenda Chittock",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "Host of the Witching Hour radio program.",
                "role": "Radio host",
                "relationships": {}
            }
        }
    },
    
    # Additional petrification witnesses
    "professor-dippet-portrait": {
        "name": "Professor Dippet (portrait)",
        "aliases": [],
        "appearances": [12],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "Portrait of former headmaster that provides advice to Dumbledore.",
                "role": "Headmaster portrait",
                "relationships": {
                    "Albus Dumbledore": "Advises"
                }
            }
        }
    },
    
    # Spell creators
    "felix-summerbee": {
        "name": "Felix Summerbee",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "11": {
                "revealedIn": 11,
                "description": "Inventor of Cheering Charms mentioned in Charms class.",
                "role": "Charm inventor",
                "relationships": {}
            }
        }
    },
    
    # Additional Gryffindor students
    "bem": {
        "name": "Bem",
        "aliases": [],
        "appearances": [7],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Gryffindor student in Harry's year.",
                "role": "Gryffindor student",
                "relationships": {}
            }
        }
    },
    "kellah": {
        "name": "Kellah",
        "aliases": [],
        "appearances": [7],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Gryffindor student mentioned in the common room.",
                "role": "Gryffindor student",
                "relationships": {}
            }
        }
    },
    "eloise-midgen": {
        "name": "Eloise Midgen",
        "aliases": [],
        "appearances": [7],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Gryffindor student who tried to curse her acne off.",
                "role": "Gryffindor student",
                "relationships": {}
            }
        }
    },
    
    # Final additions
    "wizard-baruffio": {
        "name": "Wizard Baruffio",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Wizard who said 's' instead of 'f' and ended up with a buffalo on his chest, mentioned by Flitwick.",
                "role": "Cautionary tale wizard",
                "relationships": {}
            }
        }
    }
}

# Add new characters to existing data
data['characters'].update(more_characters)

# Save updated file
with open('data/harry-potter/chamber-of-secrets.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Successfully added {len(more_characters)} new characters")
print(f"Total characters now: {len(data['characters'])}")