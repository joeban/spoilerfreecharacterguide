#!/usr/bin/env python3

import json
from typing import Dict, Any

def create_got_characters() -> Dict[str, Any]:
    """Create character data for A Game of Thrones"""
    
    characters = {
        # STARK FAMILY
        "eddard-stark": {
            "name": "Eddard Stark",
            "aliases": ["Ned Stark", "Lord Stark", "The Quiet Wolf"],
            "appearances": list(range(1, 66)),  # Appears until chapter 65
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Lord of Winterfell and Warden of the North. A man of rigid honor with grey eyes and brown hair streaked with grey.",
                    "role": "Lord of Winterfell",
                    "relationships": {
                        "Catelyn Stark": "Husband",
                        "Robert Baratheon": "Old friend",
                        "Jon Snow": "Father figure to"
                    }
                },
                "4": {
                    "revealedIn": 4,
                    "description": "Reluctantly agrees to become Hand of the King after Jon Arryn's death. Concerned about the danger in King's Landing.",
                    "role": "Hand of the King designate",
                    "relationships": {
                        "Robert Baratheon": "Named Hand by",
                        "Jon Arryn": "Investigating death of"
                    }
                },
                "25": {
                    "revealedIn": 25,
                    "description": "Discovers the truth about Cersei's children - they are Jaime's, not Robert's. Beginning to uncover the Lannister conspiracy.",
                    "role": "Hand of the King",
                    "relationships": {
                        "Cersei Lannister": "Investigating",
                        "Joffrey Baratheon": "Knows truth about"
                    }
                },
                "47": {
                    "revealedIn": 47,
                    "description": "Confronts Cersei about her children's parentage. Warns her to flee before Robert returns from hunting.",
                    "role": "Hand of the King",
                    "relationships": {
                        "Cersei Lannister": "Confronted",
                        "Robert Baratheon": "Planning to tell truth to"
                    }
                },
                "58": {
                    "revealedIn": 58,
                    "description": "Imprisoned in the black cells after being betrayed. Accused of treason against King Joffrey.",
                    "role": "Prisoner, Accused traitor",
                    "relationships": {
                        "Joffrey Baratheon": "Imprisoned by",
                        "Petyr Baelish": "Betrayed by"
                    }
                },
                "65": {
                    "revealedIn": 65,
                    "description": "Executed at the Sept of Baelor on King Joffrey's orders, despite agreeing to confess to save his daughters.",
                    "role": "Executed for treason",
                    "relationships": {
                        "Joffrey Baratheon": "Executed by order of",
                        "Sansa Stark": "Died trying to protect",
                        "Arya Stark": "Died trying to protect"
                    }
                }
            }
        },
        
        "catelyn-stark": {
            "name": "Catelyn Stark",
            "aliases": ["Cat", "Lady Stark"],
            "appearances": [2, 6, 11, 14, 18, 20, 28, 31, 34, 40, 43, 45, 55, 59, 63, 71],
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Lady of Winterfell, originally from House Tully. Auburn hair and blue eyes. Devoted mother of five.",
                    "role": "Lady of Winterfell",
                    "relationships": {
                        "Eddard Stark": "Wife",
                        "Robb Stark": "Mother",
                        "Jon Snow": "Cold toward"
                    }
                },
                "14": {
                    "revealedIn": 14,
                    "description": "Receives a letter from her sister Lysa claiming the Lannisters murdered Jon Arryn. Stays with Bran after his fall.",
                    "role": "Lady of Winterfell",
                    "relationships": {
                        "Lysa Arryn": "Sister",
                        "Bran Stark": "Caring for injured son"
                    }
                },
                "28": {
                    "revealedIn": 28,
                    "description": "Captures Tyrion Lannister at the inn, believing he tried to kill Bran. Taking him to the Eyrie for trial.",
                    "role": "Captor",
                    "relationships": {
                        "Tyrion Lannister": "Captured",
                        "Lysa Arryn": "Taking prisoner to"
                    }
                },
                "55": {
                    "revealedIn": 55,
                    "description": "At Riverrun with Robb's war council. Her father Lord Hoster Tully is dying.",
                    "role": "Mother, Advisor",
                    "relationships": {
                        "Robb Stark": "Advising",
                        "Hoster Tully": "Daughter"
                    }
                },
                "71": {
                    "revealedIn": 71,
                    "description": "Makes a deal with Jaime Lannister, releasing him in exchange for a promise to return her daughters.",
                    "role": "Desperate mother",
                    "relationships": {
                        "Jaime Lannister": "Released",
                        "Brienne of Tarth": "Sent with Jaime"
                    }
                }
            }
        },
        
        "jon-snow": {
            "name": "Jon Snow",
            "aliases": ["Lord Snow", "The Bastard of Winterfell"],
            "appearances": [5, 13, 19, 21, 26, 30, 37, 41, 48, 52, 60, 67, 70],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Ned Stark's bastard son with dark hair and grey eyes. Feels like an outsider despite Ned's love.",
                    "role": "Bastard of Winterfell",
                    "relationships": {
                        "Eddard Stark": "Bastard son of",
                        "Arya Stark": "Close to",
                        "Ghost": "Owner of direwolf"
                    }
                },
                "13": {
                    "revealedIn": 13,
                    "description": "Decides to join the Night's Watch. Leaves Winterfell with his uncle Benjen and Tyrion Lannister.",
                    "role": "Night's Watch recruit",
                    "relationships": {
                        "Benjen Stark": "Nephew",
                        "Tyrion Lannister": "Traveling companion"
                    }
                },
                "26": {
                    "revealedIn": 26,
                    "description": "Training at Castle Black under Ser Alliser Thorne's harsh instruction. Making friends with Sam Tarly.",
                    "role": "Night's Watch recruit",
                    "relationships": {
                        "Samwell Tarly": "Protecting and befriending",
                        "Alliser Thorne": "Antagonized by"
                    }
                },
                "48": {
                    "revealedIn": 48,
                    "description": "Sworn into the Night's Watch as a steward to Lord Commander Mormont, not a ranger as hoped.",
                    "role": "Steward of the Night's Watch",
                    "relationships": {
                        "Jeor Mormont": "Personal steward to",
                        "Night's Watch": "Sworn brother"
                    }
                },
                "60": {
                    "revealedIn": 60,
                    "description": "Saves Lord Commander Mormont from a wight attack. Badly burns his hand in the process.",
                    "role": "Night's Watch brother",
                    "relationships": {
                        "Jeor Mormont": "Saved life of",
                        "Ghost": "Warned by"
                    }
                },
                "70": {
                    "revealedIn": 70,
                    "description": "Learns of his father's execution. Attempts to desert but is brought back by friends. Chosen for the Great Ranging.",
                    "role": "Night's Watch brother",
                    "relationships": {
                        "Eddard Stark": "Mourning death of",
                        "Samwell Tarly": "Stopped from deserting by"
                    }
                }
            }
        },
        
        "daenerys-targaryen": {
            "name": "Daenerys Targaryen",
            "aliases": ["Dany", "Daenerys Stormborn", "Mother of Dragons", "Khaleesi"],
            "appearances": [3, 11, 23, 36, 46, 54, 61, 64, 68, 72],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Exiled princess with silver-gold hair and violet eyes. Sister to Viserys, last of the Targaryen dynasty.",
                    "role": "Exiled princess",
                    "relationships": {
                        "Viserys Targaryen": "Sister",
                        "Illyrio Mopatis": "Ward of"
                    }
                },
                "11": {
                    "revealedIn": 11,
                    "description": "Married to Khal Drogo in exchange for his army. Receives three petrified dragon eggs as a wedding gift.",
                    "role": "Khaleesi",
                    "relationships": {
                        "Khal Drogo": "Wife",
                        "Viserys Targaryen": "Sold by brother",
                        "Jorah Mormont": "Protected by"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Pregnant with Drogo's child. Beginning to embrace her role as Khaleesi and find her strength.",
                    "role": "Khaleesi, Mother-to-be",
                    "relationships": {
                        "Khal Drogo": "Carrying child of",
                        "Dragon eggs": "Growing attached to"
                    }
                },
                "46": {
                    "revealedIn": 46,
                    "description": "Witnesses Viserys's death by molten gold. Khal Drogo promises to conquer Westeros for their son.",
                    "role": "Khaleesi",
                    "relationships": {
                        "Viserys Targaryen": "Witnessed death of",
                        "Khal Drogo": "Promised Iron Throne by"
                    }
                },
                "68": {
                    "revealedIn": 68,
                    "description": "Drogo dies from an infected wound. Her son Rhaego is stillborn due to blood magic.",
                    "role": "Widow, Childless mother",
                    "relationships": {
                        "Khal Drogo": "Lost husband",
                        "Rhaego": "Lost son",
                        "Mirri Maz Duur": "Betrayed by"
                    }
                },
                "72": {
                    "revealedIn": 72,
                    "description": "Walks into Drogo's funeral pyre with dragon eggs. Emerges unburnt with three living dragons - the first in centuries.",
                    "role": "Mother of Dragons",
                    "relationships": {
                        "Drogon": "Dragon mother to",
                        "Rhaegal": "Dragon mother to",
                        "Viserion": "Dragon mother to"
                    }
                }
            }
        },
        
        "tyrion-lannister": {
            "name": "Tyrion Lannister",
            "aliases": ["The Imp", "Halfman", "The Demon Monkey"],
            "appearances": [9, 13, 21, 31, 38, 42, 56, 62, 66, 69],
            "knowledge": {
                "9": {
                    "revealedIn": 9,
                    "description": "Dwarf with mismatched eyes and white-blond hair. Sharp wit and love of books compensate for his stature.",
                    "role": "Lannister heir's brother",
                    "relationships": {
                        "Jaime Lannister": "Brother",
                        "Cersei Lannister": "Brother",
                        "Tywin Lannister": "Despised son of"
                    }
                },
                "21": {
                    "revealedIn": 21,
                    "description": "At the Wall, showing kindness to Jon Snow and designing a special saddle for Bran.",
                    "role": "Visitor to the Wall",
                    "relationships": {
                        "Jon Snow": "Befriending",
                        "Bran Stark": "Helping"
                    }
                },
                "31": {
                    "revealedIn": 31,
                    "description": "Captured by Catelyn Stark at the inn. Accused of attempting to murder Bran.",
                    "role": "Prisoner",
                    "relationships": {
                        "Catelyn Stark": "Captured by",
                        "Bronn": "Defended by"
                    }
                },
                "42": {
                    "revealedIn": 42,
                    "description": "Wins trial by combat at the Eyrie through his champion Bronn. Gains a sellsword ally.",
                    "role": "Free man",
                    "relationships": {
                        "Bronn": "Employed",
                        "Lysa Arryn": "Escaped from"
                    }
                },
                "62": {
                    "revealedIn": 62,
                    "description": "Appointed as acting Hand of the King by his father Tywin. Preparing to defend King's Landing.",
                    "role": "Acting Hand of the King",
                    "relationships": {
                        "Tywin Lannister": "Appointed by",
                        "Joffrey Baratheon": "Uncle and Hand to"
                    }
                }
            }
        },
        
        "arya-stark": {
            "name": "Arya Stark",
            "aliases": ["Arya Horseface", "Arya Underfoot", "Arry"],
            "appearances": [7, 10, 15, 22, 32, 35, 44, 50, 65],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Younger Stark daughter with brown hair and grey eyes. Wild and tomboyish, prefers swords to sewing.",
                    "role": "Stark daughter",
                    "relationships": {
                        "Jon Snow": "Close to half-brother",
                        "Sansa Stark": "Sister",
                        "Nymeria": "Owner of direwolf"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Training in sword fighting with Syrio Forel, the First Sword of Braavos.",
                    "role": "Student",
                    "relationships": {
                        "Syrio Forel": "Student of",
                        "Needle": "Owner of sword"
                    }
                },
                "50": {
                    "revealedIn": 50,
                    "description": "Escapes the Red Keep during the Lannister coup. Syrio Forel presumably dies protecting her.",
                    "role": "Fugitive",
                    "relationships": {
                        "Syrio Forel": "Protected by",
                        "Lannister soldiers": "Hunted by"
                    }
                },
                "65": {
                    "revealedIn": 65,
                    "description": "Witnesses her father's execution while hiding in the crowd. Yoren of the Night's Watch protects her.",
                    "role": "Orphan, Fugitive",
                    "relationships": {
                        "Eddard Stark": "Witnessed execution of",
                        "Yoren": "Protected by"
                    }
                }
            }
        },
        
        "sansa-stark": {
            "name": "Sansa Stark",
            "aliases": ["Little bird", "Lady Sansa"],
            "appearances": [7, 15, 29, 44, 51, 57, 65, 67],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Elder Stark daughter with auburn hair and blue eyes. Beautiful, proper, and dreams of knights and romance.",
                    "role": "Stark daughter",
                    "relationships": {
                        "Joffrey Baratheon": "Betrothed to",
                        "Arya Stark": "Sister",
                        "Lady": "Former owner of direwolf"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Infatuated with Prince Joffrey and life at court. Sides with Joffrey after he's attacked by Arya.",
                    "role": "Betrothed to prince",
                    "relationships": {
                        "Joffrey Baratheon": "Defending",
                        "Arya Stark": "Testified against"
                    }
                },
                "51": {
                    "revealedIn": 51,
                    "description": "Pleads for her father's life to King Joffrey and Queen Cersei. Still believes in their mercy.",
                    "role": "Hostage",
                    "relationships": {
                        "Eddard Stark": "Pleading for father",
                        "Cersei Lannister": "Begging"
                    }
                },
                "57": {
                    "revealedIn": 57,
                    "description": "Writes letters at Cersei's command, urging her family to bend the knee to Joffrey.",
                    "role": "Hostage",
                    "relationships": {
                        "Cersei Lannister": "Controlled by",
                        "Robb Stark": "Forced to write to"
                    }
                },
                "65": {
                    "revealedIn": 65,
                    "description": "Forced to watch her father's execution. Joffrey shows her his head on a spike.",
                    "role": "Hostage, Orphan",
                    "relationships": {
                        "Joffrey Baratheon": "Tormented by",
                        "Sandor Clegane": "Protected by"
                    }
                }
            }
        },
        
        "bran-stark": {
            "name": "Brandon Stark",
            "aliases": ["Bran"],
            "appearances": [8, 14, 17, 24, 29, 37, 49, 53, 66, 70],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Seven-year-old boy who loves climbing. Witnesses Jaime and Cersei together, then pushed from the tower.",
                    "role": "Stark son",
                    "relationships": {
                        "Summer": "Owner of direwolf",
                        "Jaime Lannister": "Pushed by"
                    }
                },
                "14": {
                    "revealedIn": 14,
                    "description": "In a coma after his fall. An assassin tries to kill him but is stopped by his mother and Summer.",
                    "role": "Injured heir",
                    "relationships": {
                        "Catelyn Stark": "Protected by mother",
                        "Summer": "Saved by direwolf"
                    }
                },
                "24": {
                    "revealedIn": 24,
                    "description": "Awakens from his coma but has no memory of the fall. Cannot use his legs.",
                    "role": "Crippled heir",
                    "relationships": {
                        "Hodor": "Carried by",
                        "Maester Luwin": "Cared for by"
                    }
                },
                "53": {
                    "revealedIn": 53,
                    "description": "Acting as Lord of Winterfell in Robb's absence. Using Tyrion's special saddle to ride.",
                    "role": "Acting Lord of Winterfell",
                    "relationships": {
                        "Rickon Stark": "Caring for brother",
                        "Osha": "Protected by"
                    }
                },
                "66": {
                    "revealedIn": 66,
                    "description": "Having strange dreams where he sees through Summer's eyes. The three-eyed crow calls to him.",
                    "role": "Heir with strange dreams",
                    "relationships": {
                        "Summer": "Warging into",
                        "Three-eyed crow": "Dreaming of"
                    }
                }
            }
        },
        
        "cersei-lannister": {
            "name": "Cersei Lannister",
            "aliases": ["Queen Cersei", "The Queen"],
            "appearances": [8, 12, 25, 30, 45, 47, 49, 51, 58, 65],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Beautiful golden-haired Queen of the Seven Kingdoms. Having an affair with her twin brother Jaime.",
                    "role": "Queen",
                    "relationships": {
                        "Robert Baratheon": "Wife",
                        "Jaime Lannister": "Secret lover and twin",
                        "Joffrey Baratheon": "Mother"
                    }
                },
                "25": {
                    "revealedIn": 25,
                    "description": "All three of her children are actually Jaime's, not Robert's. Deeply protective of them.",
                    "role": "Queen",
                    "relationships": {
                        "Joffrey Baratheon": "True father is Jaime",
                        "Myrcella Baratheon": "True father is Jaime",
                        "Tommen Baratheon": "True father is Jaime"
                    }
                },
                "45": {
                    "revealedIn": 45,
                    "description": "Confronted by Ned about her children's parentage. Refuses to flee and plans to fight.",
                    "role": "Queen",
                    "relationships": {
                        "Eddard Stark": "Confronted by",
                        "Robert Baratheon": "Planning husband's death"
                    }
                },
                "49": {
                    "revealedIn": 49,
                    "description": "Has Robert mortally wounded during his hunt. Takes control as Queen Regent for Joffrey.",
                    "role": "Queen Regent",
                    "relationships": {
                        "Robert Baratheon": "Arranged death of",
                        "Joffrey Baratheon": "Regent for"
                    }
                }
            }
        },
        
        "jaime-lannister": {
            "name": "Jaime Lannister",
            "aliases": ["The Kingslayer", "Ser Jaime"],
            "appearances": [8, 12, 30, 55, 63, 71],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Golden-haired knight of the Kingsguard. Twin brother and secret lover of Queen Cersei. Pushes Bran from the tower.",
                    "role": "Kingsguard",
                    "relationships": {
                        "Cersei Lannister": "Twin and lover",
                        "Bran Stark": "Attempted to murder",
                        "Aerys II Targaryen": "Killed the Mad King"
                    }
                },
                "30": {
                    "revealedIn": 30,
                    "description": "Attacks Ned Stark in the streets of King's Landing after learning Tyrion was captured.",
                    "role": "Kingsguard",
                    "relationships": {
                        "Eddard Stark": "Wounded",
                        "Tyrion Lannister": "Defending brother"
                    }
                },
                "55": {
                    "revealedIn": 55,
                    "description": "Leading Lannister forces in the Riverlands. Defeated and captured by Robb Stark at the Whispering Wood.",
                    "role": "Prisoner",
                    "relationships": {
                        "Robb Stark": "Captured by",
                        "Tywin Lannister": "Son of"
                    }
                },
                "71": {
                    "revealedIn": 71,
                    "description": "Released by Catelyn Stark in exchange for a promise to return her daughters. Sent with Brienne of Tarth.",
                    "role": "Released prisoner",
                    "relationships": {
                        "Catelyn Stark": "Released by",
                        "Brienne of Tarth": "Escorted by"
                    }
                }
            }
        },
        
        "robert-baratheon": {
            "name": "Robert Baratheon",
            "aliases": ["King Robert", "The Usurper"],
            "appearances": [4, 8, 12, 25, 30, 33, 39, 45, 47],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "King of the Seven Kingdoms. Once a great warrior, now grown fat with drink. Black-haired and bearded.",
                    "role": "King",
                    "relationships": {
                        "Eddard Stark": "Old friend",
                        "Cersei Lannister": "Husband",
                        "Lyanna Stark": "Still loves (deceased)"
                    }
                },
                "12": {
                    "revealedIn": 12,
                    "description": "Names Ned Stark as Hand of the King. Deeply in debt to the Lannisters and others.",
                    "role": "King",
                    "relationships": {
                        "Eddard Stark": "Named as Hand",
                        "Jon Arryn": "Former Hand (deceased)"
                    }
                },
                "47": {
                    "revealedIn": 47,
                    "description": "Mortally wounded by a boar during a hunt, likely due to strongwine provided by Lancel Lannister.",
                    "role": "Dying King",
                    "relationships": {
                        "Lancel Lannister": "Given strongwine by",
                        "Eddard Stark": "Named as Protector"
                    }
                }
            }
        },
        
        "joffrey-baratheon": {
            "name": "Joffrey Baratheon",
            "aliases": ["King Joffrey", "Joffrey the Illborn"],
            "appearances": [15, 29, 51, 57, 65, 67],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Crown Prince with golden hair and green eyes. Cruel and spoiled, torments others for amusement.",
                    "role": "Crown Prince",
                    "relationships": {
                        "Sansa Stark": "Betrothed to",
                        "Robert Baratheon": "Supposed son",
                        "Cersei Lannister": "Son"
                    }
                },
                "51": {
                    "revealedIn": 51,
                    "description": "Becomes King after Robert's death. Shows increasing cruelty and instability.",
                    "role": "King",
                    "relationships": {
                        "Cersei Lannister": "Son and king to",
                        "Sansa Stark": "Tormenting"
                    }
                },
                "65": {
                    "revealedIn": 65,
                    "description": "Orders Ned Stark's execution despite promises of mercy, shocking even his mother Cersei.",
                    "role": "King",
                    "relationships": {
                        "Eddard Stark": "Executed",
                        "Sansa Stark": "Showing Ned's head to"
                    }
                }
            }
        },
        
        "robb-stark": {
            "name": "Robb Stark",
            "aliases": ["The Young Wolf", "King in the North"],
            "appearances": [14, 16, 53, 55, 59, 63, 69, 71],
            "knowledge": {
                "14": {
                    "revealedIn": 14,
                    "description": "Eldest Stark son with auburn hair. Takes charge of Winterfell when his parents leave.",
                    "role": "Acting Lord of Winterfell",
                    "relationships": {
                        "Grey Wind": "Owner of direwolf",
                        "Theon Greyjoy": "Close friend"
                    }
                },
                "53": {
                    "revealedIn": 53,
                    "description": "Calls the banners and marches south to free his father. Shows natural military leadership.",
                    "role": "Military commander",
                    "relationships": {
                        "Northern lords": "Leading",
                        "Catelyn Stark": "Son"
                    }
                },
                "63": {
                    "revealedIn": 63,
                    "description": "Wins the Battle of the Whispering Wood, capturing Jaime Lannister through clever strategy.",
                    "role": "Military commander",
                    "relationships": {
                        "Jaime Lannister": "Captured",
                        "Tywin Lannister": "At war with"
                    }
                },
                "71": {
                    "revealedIn": 71,
                    "description": "Declared King in the North by his bannermen after Ned's execution. The North secedes from the Seven Kingdoms.",
                    "role": "King in the North",
                    "relationships": {
                        "Northern lords": "Declared king by",
                        "Iron Throne": "In rebellion against"
                    }
                }
            }
        },
        
        "theon-greyjoy": {
            "name": "Theon Greyjoy",
            "aliases": ["The Ironborn Prince", "Ward of Winterfell"],
            "appearances": [1, 14, 37, 53, 70],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Ward of Eddard Stark, taken as a boy after his father's rebellion. Cocky and ambitious.",
                    "role": "Ward of Winterfell",
                    "relationships": {
                        "Eddard Stark": "Ward of",
                        "Robb Stark": "Close friend",
                        "Balon Greyjoy": "Son"
                    }
                },
                "53": {
                    "revealedIn": 53,
                    "description": "Fights alongside Robb in his campaign. Dreams of glory and recognition.",
                    "role": "Warrior",
                    "relationships": {
                        "Robb Stark": "Fighting alongside",
                        "Grey Wind": "Fears direwolf"
                    }
                }
            }
        },
        
        "samwell-tarly": {
            "name": "Samwell Tarly",
            "aliases": ["Sam", "Ser Piggy", "Sam the Slayer"],
            "appearances": [26, 41, 48, 60, 70],
            "knowledge": {
                "26": {
                    "revealedIn": 26,
                    "description": "Extremely overweight new recruit to the Night's Watch. Cowardly but intelligent and kind.",
                    "role": "Night's Watch recruit",
                    "relationships": {
                        "Jon Snow": "Protected by",
                        "Randyll Tarly": "Disowned son of"
                    }
                },
                "48": {
                    "revealedIn": 48,
                    "description": "Becomes a steward alongside Jon. Sworn brother of the Night's Watch.",
                    "role": "Night's Watch steward",
                    "relationships": {
                        "Jon Snow": "Best friend",
                        "Maester Aemon": "Assistant to"
                    }
                }
            }
        },
        
        "petyr-baelish": {
            "name": "Petyr Baelish",
            "aliases": ["Littlefinger", "Lord Baelish"],
            "appearances": [18, 20, 25, 33, 35, 47, 49, 58],
            "knowledge": {
                "18": {
                    "revealedIn": 18,
                    "description": "Master of Coin on the Small Council. Small man with pointed beard and grey-green eyes. Owns brothels.",
                    "role": "Master of Coin",
                    "relationships": {
                        "Catelyn Stark": "Childhood love",
                        "Lysa Arryn": "Former lover"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Claims to be helping Ned but provides misleading information about the dagger used against Bran.",
                    "role": "Master of Coin",
                    "relationships": {
                        "Eddard Stark": "Pretending to help",
                        "Varys": "Political rival"
                    }
                },
                "49": {
                    "revealedIn": 49,
                    "description": "Betrays Ned Stark to Cersei. The City Watch turns on Ned at Littlefinger's command.",
                    "role": "Master of Coin, Betrayer",
                    "relationships": {
                        "Eddard Stark": "Betrayed",
                        "Cersei Lannister": "Allied with"
                    }
                }
            }
        },
        
        "varys": {
            "name": "Varys",
            "aliases": ["The Spider", "The Eunuch", "Lord Varys"],
            "appearances": [18, 20, 25, 30, 33, 35, 58],
            "knowledge": {
                "18": {
                    "revealedIn": 18,
                    "description": "Master of Whisperers, a perfumed eunuch with a bald head. Has spies everywhere called 'little birds'.",
                    "role": "Master of Whisperers",
                    "relationships": {
                        "Robert Baratheon": "Serves",
                        "Illyrio Mopatis": "Secret ally"
                    }
                },
                "30": {
                    "revealedIn": 30,
                    "description": "Visits Ned in the throne room, speaking in riddles about serving the realm.",
                    "role": "Master of Whisperers",
                    "relationships": {
                        "Eddard Stark": "Advising cryptically"
                    }
                },
                "58": {
                    "revealedIn": 58,
                    "description": "Visits Ned in the black cells. Claims to serve the realm but allowed Ned's imprisonment.",
                    "role": "Master of Whisperers",
                    "relationships": {
                        "Eddard Stark": "Visiting in prison",
                        "The realm": "Claims to serve"
                    }
                }
            }
        },
        
        "sandor-clegane": {
            "name": "Sandor Clegane",
            "aliases": ["The Hound", "Dog"],
            "appearances": [15, 29, 30, 51, 57, 65, 67],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Huge warrior with terrible burn scars on his face. Joffrey's sworn shield, not a knight.",
                    "role": "Sworn shield",
                    "relationships": {
                        "Joffrey Baratheon": "Sworn shield to",
                        "Gregor Clegane": "Brother",
                        "Sansa Stark": "Calls her 'little bird'"
                    }
                },
                "29": {
                    "revealedIn": 29,
                    "description": "Tells Sansa how his brother Gregor burned his face as a child. Hates knights and hypocrites.",
                    "role": "Sworn shield",
                    "relationships": {
                        "Gregor Clegane": "Burned by brother",
                        "Sansa Stark": "Confiding in"
                    }
                },
                "67": {
                    "revealedIn": 67,
                    "description": "Shows unexpected protection of Sansa, stopping her from pushing Joffrey to his death.",
                    "role": "Sworn shield",
                    "relationships": {
                        "Sansa Stark": "Protecting",
                        "Joffrey Baratheon": "Serving reluctantly"
                    }
                }
            }
        },
        
        "tywin-lannister": {
            "name": "Tywin Lannister",
            "aliases": ["Lord Tywin", "The Old Lion"],
            "appearances": [42, 56, 62, 69],
            "knowledge": {
                "42": {
                    "revealedIn": 42,
                    "description": "Lord of Casterly Rock and Warden of the West. Richest and most powerful lord in Westeros. Ruthless and brilliant.",
                    "role": "Lord of Casterly Rock",
                    "relationships": {
                        "Tyrion Lannister": "Despises son",
                        "Jaime Lannister": "Father",
                        "Cersei Lannister": "Father"
                    }
                },
                "56": {
                    "revealedIn": 56,
                    "description": "Leading Lannister forces against the Riverlands. Burning and pillaging to draw out Robb Stark.",
                    "role": "Military commander",
                    "relationships": {
                        "Robb Stark": "At war with",
                        "Gregor Clegane": "Commands"
                    }
                },
                "69": {
                    "revealedIn": 69,
                    "description": "Recognizes Tyrion's intelligence by making him acting Hand. Plans to crush the Stark rebellion.",
                    "role": "Lord of Casterly Rock",
                    "relationships": {
                        "Tyrion Lannister": "Appointed as Hand",
                        "Kevan Lannister": "Brother and advisor"
                    }
                }
            }
        },
        
        "viserys-targaryen": {
            "name": "Viserys Targaryen",
            "aliases": ["The Beggar King", "The Last Dragon"],
            "appearances": [3, 11, 23, 36, 46],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Exiled prince with silver-gold hair and lilac eyes. Cruel and increasingly unstable. Obsessed with reclaiming the Iron Throne.",
                    "role": "Exiled prince",
                    "relationships": {
                        "Daenerys Targaryen": "Brother",
                        "Illyrio Mopatis": "Guest of"
                    }
                },
                "11": {
                    "revealedIn": 11,
                    "description": "Sells his sister to Khal Drogo for an army. Growing impatient and disrespectful to the Dothraki.",
                    "role": "Beggar King",
                    "relationships": {
                        "Daenerys Targaryen": "Sold sister",
                        "Khal Drogo": "Brother-in-law"
                    }
                },
                "46": {
                    "revealedIn": 46,
                    "description": "Killed by Khal Drogo with molten gold after threatening Daenerys and her unborn child. 'A crown for a king.'",
                    "role": "Dead",
                    "relationships": {
                        "Khal Drogo": "Killed by",
                        "Daenerys Targaryen": "Died threatening"
                    }
                }
            }
        },
        
        "khal-drogo": {
            "name": "Khal Drogo",
            "aliases": ["Drogo", "The Great Khal"],
            "appearances": [11, 23, 36, 46, 54, 61, 64, 68],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Powerful Dothraki warlord with long braided hair never cut in defeat. Married to Daenerys.",
                    "role": "Khal",
                    "relationships": {
                        "Daenerys Targaryen": "Husband",
                        "Dothraki": "Leader of 40,000"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Growing to love Daenerys. She is pregnant with his son, prophesied to be 'the stallion who mounts the world'.",
                    "role": "Khal",
                    "relationships": {
                        "Daenerys Targaryen": "Loves wife",
                        "Rhaego": "Unborn son"
                    }
                },
                "46": {
                    "revealedIn": 46,
                    "description": "Kills Viserys with molten gold. Promises to conquer Westeros for his son.",
                    "role": "Khal",
                    "relationships": {
                        "Viserys Targaryen": "Killed",
                        "Iron Throne": "Promised to conquer"
                    }
                },
                "68": {
                    "revealedIn": 68,
                    "description": "Dies from infected wound and blood magic. His khalasar dissolves without him.",
                    "role": "Dead",
                    "relationships": {
                        "Mirri Maz Duur": "Killed by magic of",
                        "Daenerys Targaryen": "Left widow"
                    }
                }
            }
        },
        
        "jorah-mormont": {
            "name": "Jorah Mormont",
            "aliases": ["Ser Jorah", "Jorah the Andal"],
            "appearances": [3, 11, 23, 36, 46, 54, 61, 64, 68, 72],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Exiled knight from Bear Island. Middle-aged, balding, and hairy. Sworn to serve Viserys.",
                    "role": "Exiled knight",
                    "relationships": {
                        "Viserys Targaryen": "Sworn to",
                        "Jeor Mormont": "Son of"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Shifts his loyalty from Viserys to Daenerys. Secretly reporting to Varys for a pardon.",
                    "role": "Knight, Spy",
                    "relationships": {
                        "Daenerys Targaryen": "Protecting",
                        "Varys": "Reporting to"
                    }
                },
                "54": {
                    "revealedIn": 54,
                    "description": "Saves Daenerys from a poisoned wine assassination attempt. Truly loyal to her now.",
                    "role": "Protector",
                    "relationships": {
                        "Daenerys Targaryen": "Saved life of",
                        "Robert Baratheon": "Foiled assassination by"
                    }
                },
                "72": {
                    "revealedIn": 72,
                    "description": "First to call Daenerys 'Mother of Dragons' after she emerges from the fire with three dragons.",
                    "role": "Queensguard",
                    "relationships": {
                        "Daenerys Targaryen": "Devoted to",
                        "Dragons": "Witness to birth"
                    }
                }
            }
        }
    }
    
    return characters

def create_got_recaps():
    """Create chapter recaps for A Game of Thrones"""
    
    recaps = {
        "1": "Lord Eddard Stark executes a Night's Watch deserter who speaks of White Walkers. The Stark children find six direwolf pups.",
        "2": "Catelyn tells Ned that Jon Arryn is dead and King Robert is coming to Winterfell.",
        "3": "Daenerys meets Khal Drogo for the first time. Viserys plans to use Drogo's army to reclaim the Iron Throne.",
        "4": "King Robert arrives at Winterfell and asks Ned to be his Hand. He also proposes joining their houses through marriage.",
        "5": "Jon Snow decides to join the Night's Watch. He gives Arya a sword called Needle as a farewell gift.",
        "6": "Catelyn receives a secret message claiming the Lannisters murdered Jon Arryn.",
        "7": "Arya has her first 'dancing' lesson with Syrio Forel. Ned agrees to the betrothal of Sansa and Joffrey.",
        "8": "Bran climbs a tower and witnesses Jaime and Cersei together. Jaime pushes him from the window.",
        "9": "Tyrion travels north to see the Wall, showing kindness to Jon Snow along the way.",
        "10": "Jon arrives at Castle Black and begins training with the Night's Watch recruits.",
        "11": "Daenerys marries Khal Drogo and receives three dragon eggs as a wedding gift.",
        "12": "Ned accepts Robert's offer to become Hand of the King after learning of the threat to his friend.",
        "13": "Jon befriends Samwell Tarly and protects him from the other recruits' bullying.",
        "14": "An assassin tries to kill Bran while he's in a coma. Catelyn and Summer stop the attempt.",
        "15": "Sansa is enchanted by court life while Arya begins sword training. The conflict with Joffrey leads to Lady's death.",
        "16": "Bran awakens from his coma with no memory of his fall. He cannot use his legs.",
        "17": "At the Wall, Jon learns hard truths about the Night's Watch from Tyrion.",
        "18": "Ned arrives in King's Landing and joins the Small Council. Littlefinger offers his help.",
        "19": "Jon adjusts to life at Castle Black and continues protecting Sam from Ser Alliser Thorne.",
        "20": "Ned begins investigating Jon Arryn's death. He visits the armorer where Robert's bastard works.",
        "21": "Tyrion stops at Winterfell on his way south and gives Bran plans for a special saddle.",
        "22": "Arya accidentally overhears men plotting. She tries to warn her father but isn't believed.",
        "23": "Daenerys begins to find her strength as Khaleesi. She stands up to Viserys for the first time.",
        "24": "Bran goes riding with his new saddle but is attacked by wildlings. Theon and Robb save him.",
        "25": "Ned discovers that Joffrey and his siblings are not Robert's children but Jaime's.",
        "26": "Jon and Sam take their vows and officially join the Night's Watch.",
        "27": "Ned continues investigating the Baratheon bastards and realizes the truth about Cersei's children.",
        "28": "Catelyn captures Tyrion at the inn, accusing him of attempting to murder Bran.",
        "29": "Sansa pleads with Ned to let her stay in King's Landing and marry Joffrey.",
        "30": "Jaime confronts Ned in the streets about Tyrion's capture. Ned is wounded in the fight.",
        "31": "Tyrion is taken to the Eyrie to stand trial for allegedly trying to kill Bran.",
        "32": "Arya trains with Syrio while tensions rise in King's Landing.",
        "33": "Ned resigns as Hand after Robert insists on assassinating Daenerys. They later reconcile.",
        "34": "Catelyn arrives at the Eyrie with Tyrion. Her sister Lysa has become paranoid and unstable.",
        "35": "Ned continues his investigation and plans to tell Robert the truth about his children.",
        "36": "Daenerys saves the Lazzareen women from the Dothraki warriors. She is pregnant with Drogo's child.",
        "37": "Bran has his first wolf dream, seeing through Summer's eyes.",
        "38": "Tyrion demands trial by combat. Bronn volunteers to be his champion.",
        "39": "Ned makes plans to send his daughters away from King's Landing for their safety.",
        "40": "Catelyn meets Robb's army at Moat Cailin as they march south.",
        "41": "Jon saves Lord Commander Mormont from a wight attack, burning his hand in the process.",
        "42": "Tyrion wins his freedom when Bronn defeats Lysa's champion. He gains a sellsword ally.",
        "43": "Catelyn negotiates with Walder Frey for passage across the Twins.",
        "44": "Sansa goes to Cersei and reveals Ned's plan to send them away.",
        "45": "Ned confronts Cersei about her children and warns her to flee before Robert returns.",
        "46": "Viserys threatens Daenerys and her unborn child. Drogo kills him with molten gold.",
        "47": "Robert returns from his hunt, mortally wounded. On his deathbed, he names Ned as Lord Protector.",
        "48": "Jon receives Longclaw from Lord Commander Mormont as thanks for saving his life.",
        "49": "Ned refuses to seize the throne for Stannis. Littlefinger betrays him to Cersei.",
        "50": "Arya escapes the Red Keep as Lannister guards attack. Syrio Forel holds them off.",
        "51": "Sansa pleads for her father's life before Joffrey and Cersei.",
        "52": "Jon learns about Maester Aemon's true identity as a Targaryen.",
        "53": "Bran acts as Lord of Winterfell while Robb leads the army south.",
        "54": "Daenerys eats a horse heart in a Dothraki ritual. An assassin tries to poison her but Jorah saves her.",
        "55": "Catelyn waits anxiously as Robb splits his forces to face the Lannisters.",
        "56": "Tyrion fights in his first battle with his father's army, leading the mountain clans.",
        "57": "Sansa is forced to write letters asking her family to bend the knee to Joffrey.",
        "58": "Varys visits Ned in the black cells and tries to convince him to confess.",
        "59": "Catelyn waits in the woods while Robb wins the Battle of the Whispering Wood.",
        "60": "Jon and the Night's Watch discover two missing rangers frozen beyond the Wall.",
        "61": "Drogo's wound festers. Daenerys convinces him to let Mirri Maz Duur treat it.",
        "62": "Tyrion arrives in King's Landing. His father makes him acting Hand of the King.",
        "63": "Robb captures Jaime Lannister. News arrives of Ned's imprisonment.",
        "64": "Daenerys goes into labor as Drogo lies dying. Mirri performs blood magic.",
        "65": "Arya watches from the crowd as her father is executed at the Sept of Baelor.",
        "66": "Bran and Rickon share a prophetic dream about their father in the crypts.",
        "67": "Sansa is forced to look at her father's head on a spike. She contemplates pushing Joffrey to his death.",
        "68": "Daenerys wakes to find Drogo dead and her son stillborn - 'dead and twisted'.",
        "69": "Tyrion forges an alliance with the mountain clans and prepares to defend King's Landing.",
        "70": "Jon tries to desert to avenge Ned but Sam and his friends bring him back.",
        "71": "Catelyn and Robb learn of Ned's execution. The northern lords declare Robb King in the North.",
        "72": "Daenerys walks into Drogo's funeral pyre with the dragon eggs. She emerges unburnt with three baby dragons.",
        "73": "The Night's Watch prepares for the Great Ranging beyond the Wall to investigate the threat."
    }
    
    return recaps

def save_got_data():
    """Save A Game of Thrones data to JSON file"""
    
    characters = create_got_characters()
    recaps = create_got_recaps()
    
    book_data = {
        "meta": {
            "title": "A Game of Thrones",
            "author": "George R.R. Martin",
            "chapters": 73,
            "createdAt": "2024-01-01T00:00:00Z",
            "schemaVersion": "2.0"
        },
        "characters": characters,
        "recaps": recaps
    }
    
    output_file = "/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/song-ice-fire/game-of-thrones.json"
    
    with open(output_file, 'w') as f:
        json.dump(book_data, f, indent=2)
    
    print(f"Successfully created {output_file}")
    print(f"Added {len(characters)} characters")
    print(f"Added {len(recaps)} chapter recaps")

if __name__ == "__main__":
    save_got_data()