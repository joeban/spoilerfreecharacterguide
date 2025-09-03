#!/usr/bin/env python3
"""
Fills Goblet of Fire with comprehensive character data in v2.0 format
"""

import json
import sys

def create_gof_characters():
    """Create comprehensive character data for Goblet of Fire"""
    return {
        "harry-potter": {
            "name": "Harry Potter",
            "aliases": ["The Boy Who Lived", "Fourth Champion"],
            "appearances": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Fourteen-year-old wizard having disturbing dreams about Voldemort. His scar hurts more than usual.",
                    "role": "Fourth-year student",
                    "relationships": {
                        "Voldemort": "Connected through scar",
                        "Vernon Dursley": "Nephew of",
                        "Sirius Black": "Correspondence with"
                    }
                },
                "4": {
                    "revealedIn": 4,
                    "description": "Excited about attending the Quidditch World Cup with the Weasleys. Escaping another miserable summer.",
                    "role": "Guest of the Weasleys",
                    "relationships": {
                        "Arthur Weasley": "Guest of",
                        "Ron Weasley": "Best friend"
                    }
                },
                "12": {
                    "revealedIn": 12,
                    "description": "Shocked when the Goblet of Fire selects him as a fourth champion. Insists he didn't enter his name.",
                    "role": "Triwizard Champion",
                    "relationships": {
                        "Ron Weasley": "Best friend (doubting)",
                        "Hermione Granger": "Supporter",
                        "Cedric Diggory": "Fellow champion"
                    }
                },
                "19": {
                    "revealedIn": 19,
                    "description": "Successfully retrieves the golden egg from a Hungarian Horntail dragon using his broomstick.",
                    "role": "Champion, Dragon fighter",
                    "relationships": {
                        "Hagrid": "Given advance warning by",
                        "Mad-Eye Moody": "Advised by"
                    }
                },
                "26": {
                    "revealedIn": 26,
                    "description": "Rescues Ron from the Black Lake using gillyweed. Stays behind to ensure all hostages are safe.",
                    "role": "Champion, Rescuer",
                    "relationships": {
                        "Dobby": "Given gillyweed by",
                        "Ron Weasley": "Rescued from lake"
                    }
                },
                "31": {
                    "revealedIn": 31,
                    "description": "Navigates the dangerous maze in the third task alongside Cedric Diggory.",
                    "role": "Champion, Maze runner",
                    "relationships": {
                        "Cedric Diggory": "Ally in maze"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Transported to a graveyard via Portkey with Cedric. Witnesses Voldemort's return to physical form.",
                    "role": "Witness, Captive",
                    "relationships": {
                        "Voldemort": "Dueled with",
                        "Cedric Diggory": "Witnessed murder of"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Returns from the graveyard with Cedric's body. Traumatized by the events he witnessed.",
                    "role": "Survivor, Witness",
                    "relationships": {
                        "Mad-Eye Moody": "Revealed as Barty Crouch Jr."
                    }
                }
            }
        },
        "ron-weasley": {
            "name": "Ron Weasley",
            "aliases": ["Ron"],
            "appearances": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
            "knowledge": {
                "12": {
                    "revealedIn": 12,
                    "description": "Jealous and hurt that Harry was selected as champion without telling him. Their friendship is strained.",
                    "role": "Fourth-year student, Former best friend",
                    "relationships": {
                        "Harry Potter": "Jealous of",
                        "Hermione Granger": "Friend"
                    }
                },
                "18": {
                    "revealedIn": 18,
                    "description": "Reconciles with Harry after seeing the danger of the first task. Realizes Harry didn't seek the glory.",
                    "role": "Fourth-year student, Loyal friend",
                    "relationships": {
                        "Harry Potter": "Best friend (reconciled)",
                        "Hermione Granger": "Friend"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Struggles to find a date for the Yule Ball. Eventually asks Hermione but she already has a date.",
                    "role": "Fourth-year student, Dateless",
                    "relationships": {
                        "Hermione Granger": "Wants as date",
                        "Padma Patil": "Reluctant date"
                    }
                },
                "26": {
                    "revealedIn": 26,
                    "description": "Serves as Harry's hostage in the second task. Unconscious at the bottom of the lake.",
                    "role": "Hostage, What Harry would miss most",
                    "relationships": {
                        "Harry Potter": "Most important to"
                    }
                }
            }
        },
        "hermione-granger": {
            "name": "Hermione Granger", 
            "aliases": ["Hermione"],
            "appearances": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
            "knowledge": {
                "12": {
                    "revealedIn": 12,
                    "description": "Believes Harry when he says he didn't enter his name in the Goblet. Supports him when Ron doesn't.",
                    "role": "Fourth-year student, Loyal friend",
                    "relationships": {
                        "Harry Potter": "Supporting",
                        "Ron Weasley": "Friend (distant due to his jealousy)"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Stuns everyone at the Yule Ball by arriving as Viktor Krum's date, looking beautiful in elegant dress robes.",
                    "role": "Fourth-year student, Ball attendee",
                    "relationships": {
                        "Viktor Krum": "Date to Yule Ball",
                        "Ron Weasley": "Arguing with"
                    }
                },
                "27": {
                    "revealedIn": 27,
                    "description": "Argues with Ron about her relationship with Viktor Krum. Defends her right to attend the ball with whomever she chooses.",
                    "role": "Fourth-year student, Independent",
                    "relationships": {
                        "Viktor Krum": "Romantically interested in",
                        "Ron Weasley": "Frustrated with"
                    }
                }
            }
        },
        "albus-dumbledore": {
            "name": "Albus Dumbledore",
            "aliases": ["Headmaster", "Professor Dumbledore"],
            "appearances": [10, 11, 12, 13, 17, 24, 28, 35, 36, 37],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Welcomes students from Beauxbatons and Durmstrang. Announces the return of the Triwizard Tournament.",
                    "role": "Headmaster, Tournament host",
                    "relationships": {
                        "Olympe Maxime": "Fellow headmaster",
                        "Igor Karkaroff": "Fellow headmaster"
                    }
                },
                "12": {
                    "revealedIn": 12,
                    "description": "Troubled when Harry's name comes out of the Goblet. Accepts that Harry must compete despite his age.",
                    "role": "Headmaster, Concerned guardian",
                    "relationships": {
                        "Harry Potter": "Worried about",
                        "Mad-Eye Moody": "Trusts"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Immediately believes Harry's account of Voldemort's return. Takes action to prepare for the coming war.",
                    "role": "Headmaster, War leader",
                    "relationships": {
                        "Harry Potter": "Protects and believes",
                        "Cornelius Fudge": "Disputes with",
                        "Severus Snape": "Sends on secret mission"
                    }
                }
            }
        },
        "voldemort": {
            "name": "Lord Voldemort",
            "aliases": ["Tom Marvolo Riddle", "The Dark Lord", "He-Who-Must-Not-Be-Named"],
            "appearances": [1, 32, 33, 34],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Appears in Harry's dream/vision planning something sinister with a servant. Stronger than before.",
                    "role": "Dark wizard, Disembodied",
                    "relationships": {
                        "Peter Pettigrew": "Servant",
                        "Harry Potter": "Connected through scar"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Returns to physical form using a dark ritual involving Harry's blood, his father's bone, and Wormtail's flesh.",
                    "role": "Dark wizard, Reborn",
                    "relationships": {
                        "Harry Potter": "Using blood of",
                        "Peter Pettigrew": "Served by",
                        "Death Eaters": "Master of"
                    }
                },
                "33": {
                    "revealedIn": 33,
                    "description": "Summons his Death Eaters and reveals he has regained his power. Punishes those who did not seek him.",
                    "role": "Dark Lord, Master",
                    "relationships": {
                        "Death Eaters": "Commands",
                        "Lucius Malfoy": "Follower",
                        "Severus Snape": "Former follower (absent)"
                    }
                },
                "34": {
                    "revealedIn": 34,
                    "description": "Duels Harry in the graveyard. Their wands connect in Priori Incantatum, allowing Harry to escape.",
                    "role": "Dark Lord, Duelist",
                    "relationships": {
                        "Harry Potter": "Failed to kill",
                        "James Potter": "Killed (spirit appears)",
                        "Lily Potter": "Killed (spirit appears)",
                        "Cedric Diggory": "Murdered"
                    }
                }
            }
        },
        "barty-crouch-jr": {
            "name": "Barty Crouch Jr.",
            "aliases": ["Mad-Eye Moody", "Alastor Moody"],
            "appearances": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 35, 36],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Appears as the new Defence Against the Dark Arts teacher. Gruff, paranoid ex-Auror with a magical eye and wooden leg.",
                    "role": "Professor, Disguised Death Eater",
                    "relationships": {
                        "Students": "Teacher of",
                        "Albus Dumbledore": "Trusted by"
                    }
                },
                "13": {
                    "revealedIn": 13,
                    "description": "Teaches students about the Unforgivable Curses using live demonstrations. Particularly harsh on Neville.",
                    "role": "Professor, Cruel teacher",
                    "relationships": {
                        "Neville Longbottom": "Cruel to",
                        "Students": "Frightens"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Revealed to be Barty Crouch Jr. under Polyjuice Potion. Death Eater who helped engineer Harry's participation in tournament.",
                    "role": "Death Eater, Impostor",
                    "relationships": {
                        "Voldemort": "Loyal servant of",
                        "Barty Crouch Sr.": "Son of",
                        "Harry Potter": "Used for master's plan",
                        "Alastor Moody": "Impersonated"
                    }
                }
            }
        },
        "cedric-diggory": {
            "name": "Cedric Diggory",
            "aliases": ["Hufflepuff Champion"],
            "appearances": [11, 12, 15, 16, 17, 18, 19, 20, 22, 23, 24, 26, 27, 28, 31, 32, 34],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Handsome seventh-year Hufflepuff selected as Hogwarts champion. Popular and talented student.",
                    "role": "Triwizard Champion",
                    "relationships": {
                        "Hufflepuff House": "Champion of",
                        "Cho Chang": "Dating"
                    }
                },
                "19": {
                    "revealedIn": 19,
                    "description": "Faces a Common Welsh Green dragon in the first task. Successfully retrieves his golden egg.",
                    "role": "Champion, Dragon fighter",
                    "relationships": {
                        "Harry Potter": "Fellow champion"
                    }
                },
                "31": {
                    "revealedIn": 31,
                    "description": "Teams up with Harry in the maze, showing good sportsmanship and loyalty to Hogwarts.",
                    "role": "Champion, Ally",
                    "relationships": {
                        "Harry Potter": "Ally in tournament"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Murdered by Peter Pettigrew on Voldemort's orders after being transported to the graveyard.",
                    "role": "Champion, Murder victim",
                    "relationships": {
                        "Voldemort": "Killed by order of",
                        "Peter Pettigrew": "Murdered by"
                    }
                }
            }
        },
        "viktor-krum": {
            "name": "Viktor Krum",
            "aliases": ["Durmstrang Champion"],
            "appearances": [6, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 36, 37],
            "knowledge": {
                "6": {
                    "revealedIn": 6,
                    "description": "Star Seeker for Bulgaria at the Quidditch World Cup. International celebrity despite his team's loss.",
                    "role": "Professional Quidditch player",
                    "relationships": {
                        "Bulgaria team": "Seeker for"
                    }
                },
                "11": {
                    "revealedIn": 11,
                    "description": "Arrives at Hogwarts as a student from Durmstrang Institute. Still surly and famous.",
                    "role": "Student, International celebrity",
                    "relationships": {
                        "Igor Karkaroff": "Headmaster of"
                    }
                },
                "12": {
                    "revealedIn": 12,
                    "description": "Selected as Durmstrang's champion for the Triwizard Tournament. Youngest champion until Harry is chosen.",
                    "role": "Triwizard Champion",
                    "relationships": {
                        "Durmstrang Institute": "Champion of"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Attends the Yule Ball with Hermione Granger as his date. Shows a softer, more romantic side.",
                    "role": "Champion, Ball attendee",
                    "relationships": {
                        "Hermione Granger": "Romantic interest"
                    }
                }
            }
        },
        "fleur-delacour": {
            "name": "Fleur Delacour",
            "aliases": ["Beauxbatons Champion"],
            "appearances": [10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 31, 36, 37],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Stunning part-Veela student from Beauxbatons Academy. Has a magical aura that enchants nearby males.",
                    "role": "Student, Part-Veela",
                    "relationships": {
                        "Olympe Maxime": "Headmistress of",
                        "Ron Weasley": "Enchants with Veela charm"
                    }
                },
                "12": {
                    "revealedIn": 12,
                    "description": "Selected as Beauxbatons' champion for the Triwizard Tournament. Confident in her magical abilities.",
                    "role": "Triwizard Champion",
                    "relationships": {
                        "Beauxbatons Academy": "Champion of"
                    }
                },
                "19": {
                    "revealedIn": 19,
                    "description": "Faces a Common Welsh Green dragon in the first task using charm work.",
                    "role": "Champion, Dragon fighter",
                    "relationships": {
                        "Harry Potter": "Fellow champion"
                    }
                },
                "26": {
                    "revealedIn": 26,
                    "description": "Fails to complete the second task, unable to rescue her hostage from the grotto.",
                    "role": "Champion, Task failure",
                    "relationships": {
                        "Gabrielle Delacour": "Sister (hostage)"
                    }
                }
            }
        },
        "cornelius-fudge": {
            "name": "Cornelius Fudge",
            "aliases": ["Minister Fudge", "Minister"],
            "appearances": [5, 6, 7, 8, 9, 35, 36],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Minister for Magic attending the Quidditch World Cup. Tries to maintain order during the Death Eater attack.",
                    "role": "Minister of Magic",
                    "relationships": {
                        "Arthur Weasley": "Ministry colleague",
                        "Barty Crouch Sr.": "Ministry colleague"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Refuses to believe Harry and Dumbledore's account of Voldemort's return. Prefers denial to facing the truth.",
                    "role": "Minister of Magic, In denial",
                    "relationships": {
                        "Albus Dumbledore": "Disputes with",
                        "Harry Potter": "Doesn't believe"
                    }
                }
            }
        },
        "severus-snape": {
            "name": "Severus Snape",
            "aliases": ["Professor Snape"],
            "appearances": [11, 13, 17, 27, 28, 35, 36, 37],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Still the unpleasant Potions Master. Shows particular contempt for Mad-Eye Moody's teaching methods.",
                    "role": "Potions Master",
                    "relationships": {
                        "Mad-Eye Moody": "Suspicious of",
                        "Harry Potter": "Still antagonistic toward"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Sent on a secret mission by Dumbledore after Voldemort's return. His role remains mysterious.",
                    "role": "Potions Master, Secret agent",
                    "relationships": {
                        "Albus Dumbledore": "Takes orders from",
                        "Voldemort": "Former Death Eater"
                    }
                }
            }
        },
        "sirius-black": {
            "name": "Sirius Black",
            "aliases": ["Padfoot", "Snuffles"],
            "appearances": [1, 19, 27, 28, 36, 37],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Harry's godfather, still in hiding but maintaining contact through letters. Concerned about Harry's wellbeing.",
                    "role": "Godfather, Fugitive",
                    "relationships": {
                        "Harry Potter": "Godson",
                        "Ministry of Magic": "Still fugitive from"
                    }
                },
                "19": {
                    "revealedIn": 19,
                    "description": "Secretly returns to support Harry during the tournament, living in caves near Hogsmeade.",
                    "role": "Godfather, Hidden supporter",
                    "relationships": {
                        "Harry Potter": "Supporting secretly"
                    }
                },
                "27": {
                    "revealedIn": 27,
                    "description": "Communicates with Harry through the fireplace at Grimmauld Place, offering advice and support.",
                    "role": "Godfather, Advisor", 
                    "relationships": {
                        "Harry Potter": "Advising",
                        "Ron Weasley": "Concerned about",
                        "Hermione Granger": "Concerned about"
                    }
                }
            }
        },
        "rubeus-hagrid": {
            "name": "Rubeus Hagrid",
            "aliases": ["Hagrid"],
            "appearances": [4, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 28, 36, 37],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Teaching Care of Magical Creatures with his usual enthusiasm for dangerous animals. Shows the class Blast-Ended Skrewts.",
                    "role": "Professor, Creature enthusiast",
                    "relationships": {
                        "Students": "Teacher of",
                        "Blast-Ended Skrewts": "Breeder of"
                    }
                },
                "19": {
                    "revealedIn": 19,
                    "description": "Shows Harry the dragons before the first task, indirectly helping him prepare.",
                    "role": "Professor, Helpful friend",
                    "relationships": {
                        "Harry Potter": "Helping prepare",
                        "Olympe Maxime": "Romantic interest"
                    }
                },
                "28": {
                    "revealedIn": 28,
                    "description": "Reveals he is half-giant, which causes some students and parents to demand his dismissal.",
                    "role": "Professor, Half-giant",
                    "relationships": {
                        "Olympe Maxime": "Fellow half-giant",
                        "Rita Skeeter": "Exposed by"
                    }
                }
            }
        },
        "peter-pettigrew": {
            "name": "Peter Pettigrew", 
            "aliases": ["Wormtail"],
            "appearances": [1, 32, 33, 34],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Voldemort's servant, helping him plan his return. Still in his human form after escaping in the previous year.",
                    "role": "Death Eater, Servant",
                    "relationships": {
                        "Voldemort": "Servant of",
                        "Harry Potter": "Enemy"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Performs the ritual to restore Voldemort's body, sacrificing his own hand in the process.",
                    "role": "Death Eater, Ritualist",
                    "relationships": {
                        "Voldemort": "Restored to body",
                        "Cedric Diggory": "Murders on orders"
                    }
                },
                "33": {
                    "revealedIn": 33,
                    "description": "Rewarded with a new silver hand by Voldemort for his faithful service.",
                    "role": "Death Eater, Rewarded servant",
                    "relationships": {
                        "Voldemort": "Rewarded by"
                    }
                }
            }
        },
        "igor-karkaroff": {
            "name": "Igor Karkaroff",
            "aliases": ["Headmaster Karkaroff"],
            "appearances": [10, 11, 12, 17, 18, 19, 20, 23, 24, 26, 27, 28, 30, 36],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Headmaster of Durmstrang Institute. Thin man with a goatee who brings his students to Hogwarts.",
                    "role": "Headmaster",
                    "relationships": {
                        "Viktor Krum": "Student of",
                        "Albus Dumbledore": "Fellow headmaster"
                    }
                },
                "27": {
                    "revealedIn": 27,
                    "description": "Revealed to be a former Death Eater who turned informant to avoid Azkaban. Nervous about Voldemort's return.",
                    "role": "Former Death Eater, Informant",
                    "relationships": {
                        "Voldemort": "Former follower",
                        "Severus Snape": "Former fellow Death Eater"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Flees Hogwarts in fear after Voldemort's return, knowing his former master will seek revenge.",
                    "role": "Fugitive, Coward",
                    "relationships": {
                        "Voldemort": "Fleeing from"
                    }
                }
            }
        },
        "olympe-maxime": {
            "name": "Olympe Maxime",
            "aliases": ["Madame Maxime", "Headmistress Maxime"],
            "appearances": [10, 11, 12, 17, 18, 19, 20, 23, 24, 26, 27, 28, 36],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Elegant headmistress of Beauxbatons Academy. Extremely tall and imposing woman.",
                    "role": "Headmistress", 
                    "relationships": {
                        "Fleur Delacour": "Student of",
                        "Albus Dumbledore": "Fellow headmaster"
                    }
                },
                "19": {
                    "revealedIn": 19,
                    "description": "Accompanies Hagrid to see the dragons, showing romantic interest in him.",
                    "role": "Headmistress, Romantic interest",
                    "relationships": {
                        "Rubeus Hagrid": "Romantic interest"
                    }
                },
                "28": {
                    "revealedIn": 28,
                    "description": "Revealed to be half-giant like Hagrid, though she initially denies it.",
                    "role": "Headmistress, Half-giant",
                    "relationships": {
                        "Rubeus Hagrid": "Fellow half-giant"
                    }
                }
            }
        },
        "rita-skeeter": {
            "name": "Rita Skeeter",
            "aliases": ["Reporter"],
            "appearances": [18, 24, 26, 28],
            "knowledge": {
                "18": {
                    "revealedIn": 18,
                    "description": "Unscrupulous Daily Prophet reporter who writes sensational articles about the tournament and Harry.",
                    "role": "Journalist",
                    "relationships": {
                        "Harry Potter": "Writes lies about",
                        "Daily Prophet": "Works for"
                    }
                },
                "24": {
                    "revealedIn": 24,
                    "description": "Publishes damaging articles about Harry's supposed romance troubles and mental instability.",
                    "role": "Journalist, Scandal writer",
                    "relationships": {
                        "Harry Potter": "Defames in print",
                        "Hermione Granger": "Targets in articles"
                    }
                },
                "28": {
                    "revealedIn": 28,
                    "description": "Exposes Hagrid as a half-giant, causing public outcry and calls for his dismissal.",
                    "role": "Journalist, Exposer of secrets",
                    "relationships": {
                        "Rubeus Hagrid": "Exposes heritage of"
                    }
                }
            }
        },
        "barty-crouch-sr": {
            "name": "Barty Crouch Sr.",
            "aliases": ["Mr. Crouch"],
            "appearances": [5, 6, 7, 8, 9, 24, 27, 28, 29, 30, 35],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Senior Ministry official who oversees international magical cooperation. Organizing the tournament.",
                    "role": "Ministry official",
                    "relationships": {
                        "Ludo Bagman": "Ministry colleague",
                        "Cornelius Fudge": "Reports to"
                    }
                },
                "28": {
                    "revealedIn": 28,
                    "description": "Behaving strangely and appears ill. Shows signs of being under magical control.",
                    "role": "Ministry official, Under Imperius",
                    "relationships": {
                        "Barty Crouch Jr.": "Son (controlling him)",
                        "Winky": "House-elf"
                    }
                },
                "29": {
                    "revealedIn": 29,
                    "description": "Escapes the Imperius Curse temporarily and tries to warn Dumbledore about his son before being killed.",
                    "role": "Ministry official, Murder victim",
                    "relationships": {
                        "Barty Crouch Jr.": "Murdered by son",
                        "Albus Dumbledore": "Tried to warn"
                    }
                }
            }
        },
        "ludo-bagman": {
            "name": "Ludo Bagman",
            "aliases": ["Bagman"],
            "appearances": [5, 6, 7, 8, 9, 12, 19, 20, 26, 31, 35, 36, 37],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Head of the Department of Magical Games and Sports. Enthusiastic and jovial former Quidditch player.",
                    "role": "Ministry official",
                    "relationships": {
                        "Barty Crouch Sr.": "Ministry colleague"
                    }
                },
                "8": {
                    "revealedIn": 8,
                    "description": "Takes bets on the World Cup match and seems overly friendly with Fred and George Weasley.",
                    "role": "Ministry official, Gambler",
                    "relationships": {
                        "Fred Weasley": "Taking bet from",
                        "George Weasley": "Taking bet from"
                    }
                },
                "37": {
                    "revealedIn": 37,
                    "description": "Revealed to be deeply in debt to goblins and has been trying to pay them with leprechaun gold.",
                    "role": "Ministry official, Debtor",
                    "relationships": {
                        "Goblins": "In debt to"
                    }
                }
            }
        },
        "dobby": {
            "name": "Dobby",
            "aliases": ["The Free Elf"],
            "appearances": [21, 26, 27],
            "knowledge": {
                "21": {
                    "revealedIn": 21,
                    "description": "Works in the Hogwarts kitchens as a free elf. Still devoted to Harry and eager to help him.",
                    "role": "Free house-elf, Kitchen worker",
                    "relationships": {
                        "Harry Potter": "Devoted to helping",
                        "Hogwarts kitchens": "Works in"
                    }
                },
                "26": {
                    "revealedIn": 26,
                    "description": "Provides Harry with gillyweed for the second task, helping him breathe underwater.",
                    "role": "Free house-elf, Helper",
                    "relationships": {
                        "Harry Potter": "Provides gillyweed to"
                    }
                }
            }
        },
        "winky": {
            "name": "Winky",
            "aliases": ["Crouch's elf"],
            "appearances": [5, 8, 9, 21, 27, 28, 35],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "House-elf belonging to Barty Crouch Sr. Found with Harry's wand after the Dark Mark incident.",
                    "role": "House-elf, Accused",
                    "relationships": {
                        "Barty Crouch Sr.": "Servant of",
                        "Barty Crouch Jr.": "Secretly caring for"
                    }
                },
                "9": {
                    "revealedIn": 9,
                    "description": "Dismissed by Barty Crouch for the wand incident. Devastated by her dismissal from service.",
                    "role": "Dismissed house-elf",
                    "relationships": {
                        "Barty Crouch Sr.": "Dismissed by"
                    }
                },
                "21": {
                    "revealedIn": 21,
                    "description": "Works in Hogwarts kitchens but is depressed and drinking heavily. Misses her old family.",
                    "role": "Free house-elf, Alcoholic",
                    "relationships": {
                        "Dobby": "Fellow kitchen worker",
                        "Barty Crouch Sr.": "Misses serving"
                    }
                }
            }
        }
    }

def main():
    # Read the existing file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/goblet-of-fire.json', 'r') as f:
        data = json.load(f)
    
    # Update schema version and add characters
    data["meta"]["schemaVersion"] = "2.0"
    data["characters"] = create_gof_characters()
    
    # Write back to file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/goblet-of-fire.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Successfully filled Goblet of Fire with character data")
    print(f"Added {len(data['characters'])} characters")

if __name__ == "__main__":
    main()