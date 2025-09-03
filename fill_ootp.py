#!/usr/bin/env python3
"""
Fills Order of the Phoenix with comprehensive character data in v2.0 format
"""

import json
import sys

def create_ootp_characters():
    """Create comprehensive character data for Order of the Phoenix"""
    return {
        "harry-potter": {
            "name": "Harry Potter",
            "aliases": ["The Boy Who Lived", "The Chosen One"],
            "appearances": list(range(1, 39)),  # Appears in all 38 chapters
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Fifteen-year-old wizard attacked by Dementors in Little Whinging. Facing disciplinary action for using magic outside school.",
                    "role": "Fifth-year student, Accused",
                    "relationships": {
                        "Dudley Dursley": "Saved from Dementors",
                        "Ministry of Magic": "Being disciplined by"
                    }
                },
                "4": {
                    "revealedIn": 4,
                    "description": "Brought to Grimmauld Place, headquarters of the Order of the Phoenix. Frustrated by being kept out of important discussions.",
                    "role": "Order member's godson",
                    "relationships": {
                        "Sirius Black": "Godfather",
                        "Order of the Phoenix": "Protected by"
                    }
                },
                "11": {
                    "revealedIn": 11,
                    "description": "Cleared of charges at his Ministry hearing. Returns to Hogwarts for fifth year under a cloud of skepticism.",
                    "role": "Fifth-year student",
                    "relationships": {
                        "Dolores Umbridge": "Antagonized by",
                        "Daily Prophet": "Vilified by"
                    }
                },
                "13": {
                    "revealedIn": 13,
                    "description": "Suffers detention with Umbridge, who forces him to write 'I must not tell lies' with a blood quill.",
                    "role": "Student, Torture victim",
                    "relationships": {
                        "Dolores Umbridge": "Tortured by"
                    }
                },
                "16": {
                    "revealedIn": 16,
                    "description": "Forms Dumbledore's Army to teach Defense Against the Dark Arts. Becomes a teacher to his fellow students.",
                    "role": "Student, DA teacher",
                    "relationships": {
                        "Dumbledore's Army": "Teacher and leader of"
                    }
                },
                "24": {
                    "revealedIn": 24,
                    "description": "Has visions of the Department of Mysteries through his connection to Voldemort. Sees Arthur Weasley being attacked.",
                    "role": "Student, Seer",
                    "relationships": {
                        "Voldemort": "Mentally connected to",
                        "Arthur Weasley": "Saved through vision"
                    }
                },
                "26": {
                    "revealedIn": 26,
                    "description": "Begins Occlumency lessons with Snape to block his connection to Voldemort.",
                    "role": "Student, Occlumency student",
                    "relationships": {
                        "Severus Snape": "Reluctant student of"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Leads DA members to the Ministry to save Sirius, falling into Voldemort's trap.",
                    "role": "Student, Rescuer",
                    "relationships": {
                        "Sirius Black": "Trying to save",
                        "Death Eaters": "Fighting against"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Witnesses Sirius's death and duels with Bellatrix. Possessed briefly by Voldemort.",
                    "role": "Student, Bereaved godson",
                    "relationships": {
                        "Sirius Black": "Lost godfather",
                        "Bellatrix Lestrange": "Enemy who killed Sirius"
                    }
                },
                "37": {
                    "revealedIn": 37,
                    "description": "Learns the full prophecy about him and Voldemort from Dumbledore. Understands his destiny.",
                    "role": "The Chosen One",
                    "relationships": {
                        "Voldemort": "Must kill or be killed",
                        "Albus Dumbledore": "Told the truth by"
                    }
                }
            }
        },
        "dolores-umbridge": {
            "name": "Dolores Jane Umbridge",
            "aliases": ["Professor Umbridge", "High Inquisitor", "Headmistress"],
            "appearances": [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "New Defence Against the Dark Arts teacher sent by the Ministry. Gives a speech about progress for progress's sake.",
                    "role": "Professor, Ministry agent",
                    "relationships": {
                        "Ministry of Magic": "Sent by",
                        "Students": "Teacher of"
                    }
                },
                "12": {
                    "revealedIn": 12,
                    "description": "Refuses to teach practical Defense magic, insisting theory is sufficient. Clashes with Harry about Voldemort's return.",
                    "role": "Professor, Theory-only teacher",
                    "relationships": {
                        "Harry Potter": "Antagonistic toward",
                        "Cornelius Fudge": "Reports to"
                    }
                },
                "13": {
                    "revealedIn": 13,
                    "description": "Uses a blood quill to torture Harry during detention, making him carve words into his own skin.",
                    "role": "Professor, Torturer",
                    "relationships": {
                        "Harry Potter": "Tortures"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Appointed High Inquisitor of Hogwarts with powers to inspect teachers and dismiss them.",
                    "role": "High Inquisitor",
                    "relationships": {
                        "Teachers": "Has power over",
                        "Ministry of Magic": "Agent of"
                    }
                },
                "28": {
                    "revealedIn": 28,
                    "description": "Becomes Headmistress after Dumbledore's departure. Rules with increasingly authoritarian control.",
                    "role": "Headmistress",
                    "relationships": {
                        "Albus Dumbledore": "Replaced",
                        "Students": "Oppresses"
                    }
                },
                "33": {
                    "revealedIn": 33,
                    "description": "Discovers Dumbledore's Army and uses Veritaserum to try to extract information from students.",
                    "role": "Headmistress, Interrogator",
                    "relationships": {
                        "Dumbledore's Army": "Discovered and punishing"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Forced to admit Voldemort's return when he appears in the Ministry atrium.",
                    "role": "Former Headmistress",
                    "relationships": {
                        "Voldemort": "Witnessed return of"
                    }
                }
            }
        },
        "sirius-black": {
            "name": "Sirius Black",
            "aliases": ["Padfoot", "Snuffles"],
            "appearances": [3, 4, 5, 6, 22, 23, 24, 27, 35, 36],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Harry's godfather hosting Order meetings at his ancestral home, Grimmauld Place. Feeling trapped and frustrated.",
                    "role": "Order member, Godfather",
                    "relationships": {
                        "Harry Potter": "Godson",
                        "Order of the Phoenix": "Member of",
                        "Kreacher": "Hated house-elf"
                    }
                },
                "6": {
                    "revealedIn": 6,
                    "description": "Explains the Order of the Phoenix to Harry and reveals the prophecy's existence.",
                    "role": "Order member, Informant",
                    "relationships": {
                        "Order of the Phoenix": "Founding member",
                        "Voldemort": "Fighting against"
                    }
                },
                "22": {
                    "revealedIn": 22,
                    "description": "Appears in the fire at Grimmauld Place to talk with Harry, offering comfort and advice.",
                    "role": "Godfather, Advisor",
                    "relationships": {
                        "Harry Potter": "Supporting"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Comes to Harry's rescue at the Department of Mysteries with other Order members.",
                    "role": "Order member, Rescuer",
                    "relationships": {
                        "Harry Potter": "Rescuing",
                        "Death Eaters": "Fighting"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Killed by Bellatrix Lestrange, falling through the veil in the Death Chamber.",
                    "role": "Order member, Murder victim",
                    "relationships": {
                        "Bellatrix Lestrange": "Killed by",
                        "Harry Potter": "Beloved godfather of"
                    }
                }
            }
        },
        "albus-dumbledore": {
            "name": "Albus Dumbledore",
            "aliases": ["Headmaster", "Professor Dumbledore"],
            "appearances": [3, 4, 6, 8, 9, 11, 22, 23, 27, 28, 36, 37, 38],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Leader of the Order of the Phoenix, fighting against Voldemort. Avoiding Harry to protect him.",
                    "role": "Headmaster, Order leader",
                    "relationships": {
                        "Order of the Phoenix": "Leader of",
                        "Harry Potter": "Protecting by avoiding"
                    }
                },
                "11": {
                    "revealedIn": 11,
                    "description": "Defends Harry at his Ministry hearing, helping him avoid expulsion from Hogwarts.",
                    "role": "Headmaster, Defender",
                    "relationships": {
                        "Harry Potter": "Defending",
                        "Ministry of Magic": "Opposing"
                    }
                },
                "27": {
                    "revealedIn": 27,
                    "description": "Takes responsibility for Dumbledore's Army and escapes from Ministry officials.",
                    "role": "Headmaster, Fugitive",
                    "relationships": {
                        "Dumbledore's Army": "Takes responsibility for",
                        "Ministry of Magic": "Fugitive from"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Arrives at the Ministry and duels Voldemort in the atrium, proving the Dark Lord's return.",
                    "role": "Order leader, Powerful wizard",
                    "relationships": {
                        "Voldemort": "Dueled with",
                        "Harry Potter": "Saved"
                    }
                },
                "37": {
                    "revealedIn": 37,
                    "description": "Reveals the full prophecy to Harry and explains why he's been distant all year.",
                    "role": "Headmaster, Truth teller",
                    "relationships": {
                        "Harry Potter": "Revealed destiny to"
                    }
                }
            }
        },
        "severus-snape": {
            "name": "Severus Snape",
            "aliases": ["Professor Snape"],
            "appearances": [4, 6, 9, 15, 24, 26, 28, 36, 37],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Member of the Order of the Phoenix, reporting on Death Eater activities. Still unpleasant toward Harry.",
                    "role": "Order member, Double agent",
                    "relationships": {
                        "Order of the Phoenix": "Member",
                        "Death Eaters": "Spy among"
                    }
                },
                "24": {
                    "revealedIn": 24,
                    "description": "Alerts the Order when Harry has his vision of Arthur Weasley being attacked.",
                    "role": "Order member, Informant",
                    "relationships": {
                        "Harry Potter": "Reluctantly helps",
                        "Arthur Weasley": "Helped save"
                    }
                },
                "26": {
                    "revealedIn": 26,
                    "description": "Begins teaching Harry Occlumency to prevent Voldemort from accessing his mind.",
                    "role": "Occlumency teacher",
                    "relationships": {
                        "Harry Potter": "Reluctant student",
                        "Voldemort": "Protecting Harry from"
                    }
                },
                "28": {
                    "revealedIn": 28,
                    "description": "Harry sees Snape's worst memory in the Pensieve, witnessing James Potter humiliating Snape at school.",
                    "role": "Former student, Victim",
                    "relationships": {
                        "James Potter": "Humiliated by",
                        "Lily Evans": "Friend who defended him"
                    }
                }
            }
        },
        "order-of-the-phoenix": {
            "name": "Order of the Phoenix",
            "aliases": ["The Order"],
            "appearances": [3, 4, 5, 6, 9, 22, 24, 35, 36],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Secret organization fighting against Voldemort, headquartered at Grimmauld Place.",
                    "role": "Resistance organization",
                    "relationships": {
                        "Albus Dumbledore": "Led by",
                        "Voldemort": "Fighting against",
                        "Ministry of Magic": "Working against"
                    }
                },
                "6": {
                    "revealedIn": 6,
                    "description": "Reformed after Voldemort's return, with many original members rejoining the fight.",
                    "role": "Reformed resistance",
                    "relationships": {
                        "Death Eaters": "Opposing",
                        "Harry Potter": "Protecting"
                    }
                }
            }
        },
        "luna-lovegood": {
            "name": "Luna Lovegood",
            "aliases": ["Loony Lovegood"],
            "appearances": [10, 16, 18, 21, 27, 33, 34, 35, 36, 38],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Dreamy fourth-year Ravenclaw who can see Thestrals. Believes in many strange creatures and conspiracy theories.",
                    "role": "Fourth-year student",
                    "relationships": {
                        "Xenophilius Lovegood": "Father",
                        "The Quibbler": "Father publishes"
                    }
                },
                "16": {
                    "revealedIn": 16,
                    "description": "Joins Dumbledore's Army and proves to be a surprisingly capable witch despite her odd beliefs.",
                    "role": "DA member",
                    "relationships": {
                        "Dumbledore's Army": "Member of",
                        "Harry Potter": "Friend"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Fights alongside Harry at the Department of Mysteries, showing courage and skill.",
                    "role": "DA member, Fighter",
                    "relationships": {
                        "Harry Potter": "Fighting with",
                        "Death Eaters": "Fighting against"
                    }
                }
            }
        },
        "neville-longbottom": {
            "name": "Neville Longbottom",
            "aliases": ["Neville"],
            "appearances": [7, 9, 16, 23, 27, 29, 33, 34, 35, 36, 37],
            "knowledge": {
                "16": {
                    "revealedIn": 16,
                    "description": "Joins Dumbledore's Army and begins to show real improvement in Defense Against the Dark Arts.",
                    "role": "DA member, Improving student",
                    "relationships": {
                        "Dumbledore's Army": "Member of",
                        "Harry Potter": "Student of"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Reveals his parents were tortured into insanity by Bellatrix Lestrange and other Death Eaters.",
                    "role": "Fifth-year student, Victim's son",
                    "relationships": {
                        "Frank Longbottom": "Father (in St. Mungo's)",
                        "Alice Longbottom": "Mother (in St. Mungo's)",
                        "Bellatrix Lestrange": "Tortured parents"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Fights bravely at the Department of Mysteries, showing remarkable courage and growth.",
                    "role": "DA member, Fighter",
                    "relationships": {
                        "Harry Potter": "Fighting with",
                        "Death Eaters": "Fighting against"
                    }
                },
                "37": {
                    "revealedIn": 37,
                    "description": "Could have been the subject of the prophecy instead of Harry, as he was also born at the end of July.",
                    "role": "Alternative Chosen One",
                    "relationships": {
                        "Prophecy": "Possible subject of",
                        "Harry Potter": "Parallel destiny"
                    }
                }
            }
        },
        "ginny-weasley": {
            "name": "Ginny Weasley",
            "aliases": ["Ginny"],
            "appearances": [4, 5, 6, 9, 16, 27, 29, 33, 34, 35, 36, 38],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Fourth-year Gryffindor and youngest Weasley. Growing more confident and outspoken.",
                    "role": "Fourth-year student",
                    "relationships": {
                        "Ron Weasley": "Brother",
                        "Harry Potter": "Crush on"
                    }
                },
                "16": {
                    "revealedIn": 16,
                    "description": "Joins Dumbledore's Army and proves to be a talented witch with particular skill at hexes.",
                    "role": "DA member",
                    "relationships": {
                        "Dumbledore's Army": "Member of",
                        "Michael Corner": "Dating"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Fights at the Department of Mysteries, showing she's become a formidable witch.",
                    "role": "DA member, Fighter",
                    "relationships": {
                        "Harry Potter": "Fighting with"
                    }
                }
            }
        },
        "bellatrix-lestrange": {
            "name": "Bellatrix Lestrange",
            "aliases": ["Bellatrix Black"],
            "appearances": [6, 35, 36],
            "knowledge": {
                "6": {
                    "revealedIn": 6,
                    "description": "Dangerous Death Eater imprisoned in Azkaban for torturing the Longbottoms. Sirius's cousin.",
                    "role": "Death Eater, Prisoner",
                    "relationships": {
                        "Sirius Black": "Cousin",
                        "Voldemort": "Devoted follower",
                        "Frank Longbottom": "Tortured",
                        "Alice Longbottom": "Tortured"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Escapes from Azkaban and fights at the Department of Mysteries.",
                    "role": "Death Eater, Escaped prisoner",
                    "relationships": {
                        "Death Eaters": "Leader among",
                        "Harry Potter": "Enemy"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Kills Sirius Black with a curse that sends him through the veil in the Death Chamber.",
                    "role": "Death Eater, Murderer",
                    "relationships": {
                        "Sirius Black": "Murdered",
                        "Harry Potter": "Mortal enemy"
                    }
                }
            }
        },
        "cornelius-fudge": {
            "name": "Cornelius Fudge",
            "aliases": ["Minister Fudge", "Minister"],
            "appearances": [1, 2, 36, 38],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Minister for Magic who refuses to believe Voldemort has returned. Campaigns against Harry and Dumbledore.",
                    "role": "Minister of Magic, Denier",
                    "relationships": {
                        "Harry Potter": "Discrediting",
                        "Albus Dumbledore": "Opposing",
                        "Daily Prophet": "Using to spread lies"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Finally sees Voldemort for himself at the Ministry and is forced to admit his return.",
                    "role": "Minister of Magic, Converted",
                    "relationships": {
                        "Voldemort": "Witnessed",
                        "Harry Potter": "Must now believe"
                    }
                }
            }
        },
        "kingsley-shacklebolt": {
            "name": "Kingsley Shacklebolt",
            "aliases": ["Kingsley"],
            "appearances": [3, 4, 5, 6, 35],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Auror and member of the Order of the Phoenix. Helps escort Harry from Privet Drive.",
                    "role": "Auror, Order member",
                    "relationships": {
                        "Order of the Phoenix": "Member",
                        "Ministry of Magic": "Employee"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Fights at the Department of Mysteries, proving his skill as both an Auror and Order member.",
                    "role": "Auror, Fighter",
                    "relationships": {
                        "Death Eaters": "Fighting"
                    }
                }
            }
        },
        "remus-lupin": {
            "name": "Remus Lupin",
            "aliases": ["Professor Lupin", "Moony"],
            "appearances": [3, 4, 5, 6, 9, 24, 35],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Former Hogwarts professor and member of the Order of the Phoenix. Still a werewolf, living on the margins.",
                    "role": "Order member, Werewolf",
                    "relationships": {
                        "Order of the Phoenix": "Member",
                        "Harry Potter": "Former teacher"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Fights at the Department of Mysteries alongside other Order members.",
                    "role": "Order member, Fighter",
                    "relationships": {
                        "Harry Potter": "Fighting with",
                        "Sirius Black": "Old friend"
                    }
                }
            }
        },
        "mad-eye-moody": {
            "name": "Alastor Moody",
            "aliases": ["Mad-Eye Moody"],
            "appearances": [3, 4, 5, 6, 9, 35],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Real Mad-Eye Moody, paranoid ex-Auror and Order member. Freed after being imprisoned by Barty Crouch Jr.",
                    "role": "Ex-Auror, Order member",
                    "relationships": {
                        "Order of the Phoenix": "Member",
                        "Barty Crouch Jr.": "Imprisoned by"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Fights at the Department of Mysteries with his usual paranoid vigilance.",
                    "role": "Ex-Auror, Fighter",
                    "relationships": {
                        "Death Eaters": "Fighting"
                    }
                }
            }
        },
        "arthur-weasley": {
            "name": "Arthur Weasley",
            "aliases": ["Mr. Weasley"],
            "appearances": [3, 4, 5, 6, 7, 9, 22, 23, 24, 25, 38],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Ministry employee and Order member. Working on guard duty for the Order while maintaining his day job.",
                    "role": "Ministry employee, Order member",
                    "relationships": {
                        "Order of the Phoenix": "Member",
                        "Ministry of Magic": "Employee"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Attacked by Nagini while on guard duty at the Department of Mysteries. Saved by Harry's vision.",
                    "role": "Order member, Attack victim",
                    "relationships": {
                        "Nagini": "Attacked by",
                        "Harry Potter": "Saved by vision of"
                    }
                },
                "24": {
                    "revealedIn": 24,
                    "description": "Recovering at St. Mungo's from severe snake bite wounds. Grateful to Harry for saving his life.",
                    "role": "Order member, Patient",
                    "relationships": {
                        "Harry Potter": "Owes life to",
                        "St. Mungo's": "Patient at"
                    }
                }
            }
        },
        "molly-weasley": {
            "name": "Molly Weasley",
            "aliases": ["Mrs. Weasley"],
            "appearances": [3, 4, 5, 6, 9, 22, 23, 24, 25, 38],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Order member and Weasley family matriarch. Protective of Harry and worried about her family's safety.",
                    "role": "Order member, Mother",
                    "relationships": {
                        "Order of the Phoenix": "Member",
                        "Harry Potter": "Protective of",
                        "Sirius Black": "Argues with about Harry"
                    }
                },
                "5": {
                    "revealedIn": 5,
                    "description": "Faces a boggart that transforms into the dead bodies of her family members, revealing her greatest fear.",
                    "role": "Order member, Frightened mother",
                    "relationships": {
                        "Weasley family": "Fears losing",
                        "Harry Potter": "Fears losing"
                    }
                },
                "24": {
                    "revealedIn": 24,
                    "description": "Devastated by Arthur's attack but grateful to Harry for his warning vision.",
                    "role": "Order member, Wife",
                    "relationships": {
                        "Arthur Weasley": "Wife of (injured)",
                        "Harry Potter": "Grateful to"
                    }
                }
            }
        },
        "mundungus-fletcher": {
            "name": "Mundungus Fletcher",
            "aliases": ["Dung"],
            "appearances": [1, 2, 3, 4, 5],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Unreliable Order member who was supposed to be watching Harry but abandoned his post.",
                    "role": "Order member, Deserter",
                    "relationships": {
                        "Order of the Phoenix": "Unreliable member",
                        "Harry Potter": "Failed to protect"
                    }
                },
                "4": {
                    "revealedIn": 4,
                    "description": "Small-time criminal and con artist who provides intelligence to the Order despite his unreliability.",
                    "role": "Order member, Criminal",
                    "relationships": {
                        "Order of the Phoenix": "Informant for"
                    }
                }
            }
        },
        "cho-chang": {
            "name": "Cho Chang",
            "aliases": ["Cho"],
            "appearances": [12, 16, 18, 21, 26, 27, 28],
            "knowledge": {
                "16": {
                    "revealedIn": 16,
                    "description": "Sixth-year Ravenclaw who joins Dumbledore's Army. Still grieving Cedric Diggory's death.",
                    "role": "DA member, Grieving girlfriend",
                    "relationships": {
                        "Dumbledore's Army": "Member of",
                        "Cedric Diggory": "Late boyfriend",
                        "Harry Potter": "Romantic interest"
                    }
                },
                "21": {
                    "revealedIn": 21,
                    "description": "Kisses Harry under the mistletoe but their relationship is complicated by her grief and his awkwardness.",
                    "role": "DA member, Love interest",
                    "relationships": {
                        "Harry Potter": "Kissed",
                        "Marietta Edgecombe": "Best friend"
                    }
                },
                "28": {
                    "revealedIn": 28,
                    "description": "Defends Marietta when she betrays the DA, causing tension with Harry.",
                    "role": "DA member, Loyal friend",
                    "relationships": {
                        "Marietta Edgecombe": "Defending",
                        "Harry Potter": "Relationship strained"
                    }
                }
            }
        }
    }

def main():
    # Read the existing file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/order-of-phoenix.json', 'r') as f:
        data = json.load(f)
    
    # Update schema version and add characters
    data["meta"]["schemaVersion"] = "2.0"
    data["characters"] = create_ootp_characters()
    
    # Write back to file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/order-of-phoenix.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Successfully filled Order of the Phoenix with character data")
    print(f"Added {len(data['characters'])} characters")

if __name__ == "__main__":
    main()