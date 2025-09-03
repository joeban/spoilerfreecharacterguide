#!/usr/bin/env python3
import json

# Read existing data
with open('data/harry-potter/chamber-of-secrets.json', 'r') as f:
    data = json.load(f)

# Additional characters to add for Chamber of Secrets
new_characters = {
    # Lockhart's associates and fans
    "gladys-gudgeon": {
        "name": "Gladys Gudgeon",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Witch who writes fan mail to Gilderoy Lockhart, mentioned as one of his admirers.",
                "role": "Lockhart fan",
                "relationships": {
                    "Gilderoy Lockhart": "Admirer of"
                }
            }
        }
    },
    "veronica-smethley": {
        "name": "Veronica Smethley",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Witch who writes fan mail to Gilderoy Lockhart, mentioned as one of his admirers.",
                "role": "Lockhart fan",
                "relationships": {
                    "Gilderoy Lockhart": "Admirer of"
                }
            }
        }
    },
    
    # Tom Riddle's family and associates
    "tom-riddle-sr": {
        "name": "Tom Riddle Sr.",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Tom Riddle's father, a Muggle who abandoned his wife when he discovered she was a witch.",
                "role": "Tom Riddle's father",
                "relationships": {
                    "Tom Riddle": "Father of",
                    "Merope Gaunt": "Husband of (abandoned)"
                }
            }
        }
    },
    "merope-gaunt": {
        "name": "Merope Gaunt",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Tom Riddle's mother, a witch from the Gaunt family who died shortly after giving birth.",
                "role": "Tom Riddle's mother",
                "relationships": {
                    "Tom Riddle": "Mother of",
                    "Tom Riddle Sr.": "Wife of (abandoned by)",
                    "Marvolo Gaunt": "Daughter of"
                }
            }
        }
    },
    "marvolo-gaunt": {
        "name": "Marvolo Gaunt",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Tom Riddle's grandfather, descendant of Salazar Slytherin mentioned in diary memories.",
                "role": "Tom Riddle's grandfather",
                "relationships": {
                    "Merope Gaunt": "Father of",
                    "Tom Riddle": "Grandfather of",
                    "Salazar Slytherin": "Descendant of"
                }
            }
        }
    },
    
    # Headless Hunt members
    "sir-patrick-delaney-podmore": {
        "name": "Sir Patrick Delaney-Podmore",
        "aliases": ["Sir Patrick"],
        "appearances": [8],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "Leader of the Headless Hunt who refuses Nearly Headless Nick membership because his head isn't fully severed.",
                "role": "Headless Hunt leader",
                "relationships": {
                    "Nearly Headless Nick": "Rejects membership of"
                }
            }
        }
    },
    "sir-properly-decapitated": {
        "name": "Sir Properly Decapitated",
        "aliases": [],
        "appearances": [8],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "Member of the Headless Hunt who attends Nearly Headless Nick's deathday party.",
                "role": "Headless Hunt member",
                "relationships": {
                    "Sir Patrick Delaney-Podmore": "Follower of"
                }
            }
        }
    },
    
    # Historical victims and witnesses
    "myrtle-warren": {
        "name": "Myrtle Warren",
        "aliases": ["Moaning Myrtle's real name"],
        "appearances": [],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "The real name of Moaning Myrtle when she was alive, killed by the basilisk fifty years ago.",
                "role": "Former student (deceased)",
                "relationships": {
                    "Tom Riddle": "Killed during time of",
                    "Basilisk": "Killed by"
                }
            }
        }
    },
    "olive-hornby": {
        "name": "Olive Hornby",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Student who teased Myrtle about her glasses, causing her to hide in the bathroom where she died.",
                "role": "Former student",
                "relationships": {
                    "Moaning Myrtle": "Bullied",
                    "Myrtle Warren": "Teased"
                }
            }
        }
    },
    
    # Ministry officials
    "mafalda-hopkirk": {
        "name": "Mafalda Hopkirk",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "2": {
                "revealedIn": 2,
                "description": "Ministry employee from the Improper Use of Magic Office who sends Harry a warning letter.",
                "role": "Ministry official",
                "relationships": {
                    "Harry Potter": "Sends warning to"
                }
            }
        }
    },
    "barty-crouch": {
        "name": "Bartemius Crouch Sr.",
        "aliases": ["Mr. Crouch"],
        "appearances": [],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "Head of the Department of International Magical Cooperation mentioned in Ministry discussions.",
                "role": "Ministry official",
                "relationships": {
                    "Arthur Weasley": "Superior to"
                }
            }
        }
    },
    "amelia-bones": {
        "name": "Amelia Bones",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "Head of the Department of Magical Law Enforcement, Susan Bones' aunt mentioned in discussions.",
                "role": "Ministry official",
                "relationships": {
                    "Susan Bones": "Aunt of"
                }
            }
        }
    },
    
    # Quidditch commentators and players
    "zacharias-smith": {
        "name": "Zacharias Smith",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Hufflepuff student who plays Chaser on their Quidditch team.",
                "role": "Hufflepuff Chaser",
                "relationships": {
                    "Cedric Diggory": "Teammate of"
                }
            }
        }
    },
    "malcolm-baddock": {
        "name": "Malcolm Baddock",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Slytherin student who joins the Quidditch team as a Chaser.",
                "role": "Slytherin Chaser",
                "relationships": {
                    "Marcus Flint": "Teammate of"
                }
            }
        }
    },
    "graham-montague": {
        "name": "Graham Montague",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Slytherin Chaser on the Quidditch team.",
                "role": "Slytherin Chaser",
                "relationships": {
                    "Marcus Flint": "Teammate of",
                    "Draco Malfoy": "Teammate of"
                }
            }
        }
    },
    "cassius-warrington": {
        "name": "Cassius Warrington",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Large Slytherin student who plays Chaser on the Quidditch team.",
                "role": "Slytherin Chaser",
                "relationships": {
                    "Marcus Flint": "Teammate of"
                }
            }
        }
    },
    
    # Aragog's family
    "mosag": {
        "name": "Mosag",
        "aliases": [],
        "appearances": [15],
        "knowledge": {
            "15": {
                "revealedIn": 15,
                "description": "Aragog's wife, a massive Acromantula in the Forbidden Forest.",
                "role": "Acromantula",
                "relationships": {
                    "Aragog": "Wife of"
                }
            }
        }
    },
    
    # Lockhart's book characters
    "wagga-wagga-werewolf": {
        "name": "Wagga Wagga Werewolf",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Werewolf supposedly defeated by Gilderoy Lockhart, featured in 'Wanderings with Werewolves'.",
                "role": "Werewolf (in Lockhart's tales)",
                "relationships": {
                    "Gilderoy Lockhart": "Supposedly defeated by"
                }
            }
        }
    },
    "transylvanian-villagers": {
        "name": "Transylvanian Villagers",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "People supposedly saved by Lockhart from vampires in his book tales.",
                "role": "Lockhart's story subjects",
                "relationships": {
                    "Gilderoy Lockhart": "Supposedly saved by"
                }
            }
        }
    },
    
    # Additional students mentioned
    "moon": {
        "name": "Moon",
        "aliases": [],
        "appearances": [11],
        "knowledge": {
            "11": {
                "revealedIn": 11,
                "description": "Student at Hogwarts mentioned during the Dueling Club.",
                "role": "Hogwarts student",
                "relationships": {}
            }
        }
    },
    "boot": {
        "name": "Boot",
        "aliases": [],
        "appearances": [11],
        "knowledge": {
            "11": {
                "revealedIn": 11,
                "description": "Student at Hogwarts mentioned during classes.",
                "role": "Hogwarts student",
                "relationships": {}
            }
        }
    },
    
    # Portraits and paintings
    "violet": {
        "name": "Violet",
        "aliases": [],
        "appearances": [9],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Friend of the Fat Lady, a portrait who visits between frames.",
                "role": "Portrait",
                "relationships": {
                    "The Fat Lady": "Friend of"
                }
            }
        }
    },
    "sir-cadogan": {
        "name": "Sir Cadogan",
        "aliases": [],
        "appearances": [9],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Knight portrait who challenges people to duels and offers to guide lost students.",
                "role": "Portrait knight",
                "relationships": {}
            }
        }
    },
    
    # Weasley family friends and associates
    "mrs-fawcett": {
        "name": "Mrs. Fawcett",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "4": {
                "revealedIn": 4,
                "description": "Witch at Diagon Alley whose daughter is starting Hogwarts.",
                "role": "Parent",
                "relationships": {
                    "S. Fawcett": "Mother of"
                }
            }
        }
    },
    "s-fawcett": {
        "name": "S. Fawcett",
        "aliases": [],
        "appearances": [7],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Student starting at Hogwarts, sorted into Ravenclaw.",
                "role": "Ravenclaw student",
                "relationships": {
                    "Mrs. Fawcett": "Child of"
                }
            }
        }
    },
    
    # Historical Hogwarts figures
    "armando-dippet": {
        "name": "Armando Dippet",
        "aliases": ["Professor Dippet"],
        "appearances": [13],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Headmaster of Hogwarts fifty years ago when the Chamber was first opened. Appears in Tom Riddle's diary memories.",
                "role": "Former Headmaster",
                "relationships": {
                    "Tom Riddle": "Headmaster of",
                    "Albus Dumbledore": "Predecessor of"
                }
            }
        }
    },
    "professor-merrythought": {
        "name": "Professor Galatea Merrythought",
        "aliases": ["Professor Merrythought"],
        "appearances": [],
        "knowledge": {
            "13": {
                "revealedIn": 13,
                "description": "Defense Against the Dark Arts teacher fifty years ago, mentioned in diary memories.",
                "role": "Former DADA Professor",
                "relationships": {
                    "Tom Riddle": "Teacher of"
                }
            }
        }
    },
    
    # Diagon Alley shopkeepers and workers
    "mr-mulpepper": {
        "name": "Mr. Mulpepper",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "4": {
                "revealedIn": 4,
                "description": "Apothecary owner in Diagon Alley where students buy potion ingredients.",
                "role": "Shop owner",
                "relationships": {}
            }
        }
    },
    "madam-primpernelle": {
        "name": "Madam Primpernelle",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "4": {
                "revealedIn": 4,
                "description": "Owner of Madam Primpernelle's Beautifying Potions in Diagon Alley.",
                "role": "Shop owner",
                "relationships": {}
            }
        }
    },
    
    # Additional Ministry workers
    "perkins": {
        "name": "Perkins",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "Elderly wizard who works with Arthur Weasley at the Ministry. Lends the Weasleys a tent.",
                "role": "Ministry employee",
                "relationships": {
                    "Arthur Weasley": "Colleague of"
                }
            }
        }
    },
    "arnold-peasegood": {
        "name": "Arnold Peasegood",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "Obliviator mentioned as part of the Accidental Magic Reversal Squad.",
                "role": "Obliviator",
                "relationships": {}
            }
        }
    },
    
    # Famous wizards mentioned
    "wendelin-the-weird": {
        "name": "Wendelin the Weird",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Medieval witch mentioned in History of Magic who enjoyed being burned at the stake.",
                "role": "Historical witch",
                "relationships": {}
            }
        }
    },
    "emeric-the-evil": {
        "name": "Emeric the Evil",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Dark wizard mentioned in History of Magic class.",
                "role": "Historical dark wizard",
                "relationships": {}
            }
        }
    },
    "uric-the-oddball": {
        "name": "Uric the Oddball",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Eccentric wizard mentioned who wore a jellyfish for a hat.",
                "role": "Historical wizard",
                "relationships": {}
            }
        }
    },
    
    # Ghosts and spirits
    "wailing-widow": {
        "name": "Wailing Widow",
        "aliases": [],
        "appearances": [8],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "Ghost who attends Nearly Headless Nick's deathday party.",
                "role": "Ghost",
                "relationships": {
                    "Nearly Headless Nick": "Party guest of"
                }
            }
        }
    },
    
    # Additional creatures
    "fang": {
        "name": "Fang",
        "aliases": [],
        "appearances": [7, 15],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Hagrid's large boarhound dog who is actually quite cowardly despite his size.",
                "role": "Hagrid's pet",
                "relationships": {
                    "Rubeus Hagrid": "Pet of"
                }
            }
        }
    },
    
    # Wizard wireless and media
    "celestina-warbeck": {
        "name": "Celestina Warbeck",
        "aliases": ["The Singing Sorceress"],
        "appearances": [],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "Popular singing sorceress whose music Mrs. Weasley enjoys on the wireless.",
                "role": "Singer",
                "relationships": {
                    "Molly Weasley": "Favorite singer of"
                }
            }
        }
    },
    
    # Additional historical figures
    "herpo-the-foul": {
        "name": "Herpo the Foul",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "11": {
                "revealedIn": 11,
                "description": "Ancient Greek dark wizard who created the first basilisk and is considered the first person to create a Horcrux.",
                "role": "Historical dark wizard",
                "relationships": {
                    "Basilisk": "Creator of first"
                }
            }
        }
    },
    
    # Spell inventors
    "miranda-goshawk": {
        "name": "Miranda Goshawk",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Author of the Standard Book of Spells series used at Hogwarts.",
                "role": "Textbook author",
                "relationships": {}
            }
        }
    },
    "wilbert-slinkhard": {
        "name": "Wilbert Slinkhard",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "6": {
                "revealedIn": 6,
                "description": "Author of defensive magic theory books.",
                "role": "Author",
                "relationships": {}
            }
        }
    },
    
    # Additional Gryffindor students
    "romilda-vane": {
        "name": "Romilda Vane",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Younger Gryffindor student mentioned in the common room.",
                "role": "Gryffindor student",
                "relationships": {}
            }
        }
    },
    "mary-macdonald": {
        "name": "Mary Macdonald",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "Gryffindor student from an earlier generation mentioned in passing.",
                "role": "Former Gryffindor student",
                "relationships": {}
            }
        }
    },
    
    # Ravenclaw students
    "roger-davies": {
        "name": "Roger Davies",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Ravenclaw Quidditch team captain and Chaser.",
                "role": "Ravenclaw Quidditch Captain",
                "relationships": {
                    "Cho Chang": "Teammate of"
                }
            }
        }
    },
    "grant-page": {
        "name": "Grant Page",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Ravenclaw Beater on the Quidditch team.",
                "role": "Ravenclaw Beater",
                "relationships": {
                    "Roger Davies": "Teammate of"
                }
            }
        }
    },
    "randolph-burrow": {
        "name": "Randolph Burrow",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Ravenclaw Keeper on the Quidditch team.",
                "role": "Ravenclaw Keeper",
                "relationships": {
                    "Roger Davies": "Teammate of"
                }
            }
        }
    },
    "jeremy-stretton": {
        "name": "Jeremy Stretton",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Ravenclaw Chaser on the Quidditch team.",
                "role": "Ravenclaw Chaser",
                "relationships": {
                    "Roger Davies": "Teammate of"
                }
            }
        }
    },
    "jason-samuels": {
        "name": "Jason Samuels",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Ravenclaw Beater on the Quidditch team.",
                "role": "Ravenclaw Beater",
                "relationships": {
                    "Roger Davies": "Teammate of"
                }
            }
        }
    },
    "duncan-inglebee": {
        "name": "Duncan Inglebee",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Ravenclaw Chaser on the Quidditch team.",
                "role": "Ravenclaw Chaser",
                "relationships": {
                    "Roger Davies": "Teammate of"
                }
            }
        }
    },
    
    # Hufflepuff Quidditch team
    "tamsin-applebee": {
        "name": "Tamsin Applebee",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Hufflepuff Chaser on the Quidditch team.",
                "role": "Hufflepuff Chaser",
                "relationships": {
                    "Cedric Diggory": "Teammate of"
                }
            }
        }
    },
    "heidi-macavoy": {
        "name": "Heidi Macavoy",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Hufflepuff Chaser on the Quidditch team.",
                "role": "Hufflepuff Chaser",
                "relationships": {
                    "Cedric Diggory": "Teammate of"
                }
            }
        }
    },
    "malcolm-preece": {
        "name": "Malcolm Preece",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Hufflepuff Chaser on the Quidditch team.",
                "role": "Hufflepuff Chaser",
                "relationships": {
                    "Cedric Diggory": "Teammate of"
                }
            }
        }
    },
    "anthony-rickett": {
        "name": "Anthony Rickett",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Hufflepuff Beater on the Quidditch team.",
                "role": "Hufflepuff Beater",
                "relationships": {
                    "Cedric Diggory": "Teammate of"
                }
            }
        }
    },
    "maxine-ogrady": {
        "name": "Maxine O'Grady",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Hufflepuff Beater on the Quidditch team.",
                "role": "Hufflepuff Beater",
                "relationships": {
                    "Cedric Diggory": "Teammate of"
                }
            }
        }
    },
    "herbert-fleet": {
        "name": "Herbert Fleet",
        "aliases": [],
        "appearances": [10],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Hufflepuff Keeper on the Quidditch team.",
                "role": "Hufflepuff Keeper",
                "relationships": {
                    "Cedric Diggory": "Teammate of"
                }
            }
        }
    },
    
    # Additional portraits
    "phineas-nigellus-black": {
        "name": "Phineas Nigellus Black",
        "aliases": ["Phineas Nigellus"],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Former Headmaster of Hogwarts, least popular in history. Portrait hangs in the Headmaster's office.",
                "role": "Former Headmaster portrait",
                "relationships": {
                    "Sirius Black": "Ancestor of"
                }
            }
        }
    },
    "dilys-derwent": {
        "name": "Dilys Derwent",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Former Headmistress of Hogwarts and Healer at St. Mungo's. Her portrait can travel between locations.",
                "role": "Former Headmistress portrait",
                "relationships": {}
            }
        }
    },
    "everard": {
        "name": "Everard",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Former Headmaster whose portrait hangs in multiple locations including the Ministry.",
                "role": "Former Headmaster portrait",
                "relationships": {}
            }
        }
    },
    
    # Founders' era characters
    "godric-gryffindor": {
        "name": "Godric Gryffindor",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "One of the four founders of Hogwarts. Valued courage and chivalry. Owner of the sword that appears from the Sorting Hat.",
                "role": "Hogwarts founder",
                "relationships": {
                    "Salazar Slytherin": "Fellow founder (opposed)",
                    "Helga Hufflepuff": "Fellow founder",
                    "Rowena Ravenclaw": "Fellow founder"
                }
            }
        }
    },
    "helga-hufflepuff": {
        "name": "Helga Hufflepuff",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "One of the four founders of Hogwarts. Valued hard work, patience, and loyalty. Created Hufflepuff House.",
                "role": "Hogwarts founder",
                "relationships": {
                    "Godric Gryffindor": "Fellow founder",
                    "Salazar Slytherin": "Fellow founder",
                    "Rowena Ravenclaw": "Fellow founder"
                }
            }
        }
    },
    "rowena-ravenclaw": {
        "name": "Rowena Ravenclaw",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "One of the four founders of Hogwarts. Valued intelligence and wisdom. Created Ravenclaw House.",
                "role": "Hogwarts founder",
                "relationships": {
                    "Godric Gryffindor": "Fellow founder",
                    "Salazar Slytherin": "Fellow founder",
                    "Helga Hufflepuff": "Fellow founder",
                    "Helena Ravenclaw": "Mother of"
                }
            }
        }
    },
    "helena-ravenclaw": {
        "name": "Helena Ravenclaw",
        "aliases": ["The Grey Lady"],
        "appearances": [],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "Daughter of Rowena Ravenclaw who became the Grey Lady ghost of Ravenclaw House.",
                "role": "Ravenclaw ghost",
                "relationships": {
                    "Rowena Ravenclaw": "Daughter of"
                }
            }
        }
    },
    
    # Additional creatures and beings
    "winky": {
        "name": "Winky",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "2": {
                "revealedIn": 2,
                "description": "House-elf mentioned by Dobby as another elf who serves a wizarding family.",
                "role": "House-elf",
                "relationships": {
                    "Dobby": "Fellow house-elf"
                }
            }
        }
    },
    "kreacher": {
        "name": "Kreacher",
        "aliases": [],
        "appearances": [],
        "knowledge": {
            "2": {
                "revealedIn": 2,
                "description": "House-elf of the Black family mentioned in discussions about house-elf servitude.",
                "role": "Black family house-elf",
                "relationships": {
                    "Sirius Black": "Serves family of"
                }
            }
        }
    }
}

# Add new characters to existing data
data['characters'].update(new_characters)

# Save updated file
with open('data/harry-potter/chamber-of-secrets.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Successfully added {len(new_characters)} new characters")
print(f"Total characters now: {len(data['characters'])}")