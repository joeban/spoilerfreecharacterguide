#!/usr/bin/env python3
"""
Fills Prisoner of Azkaban with comprehensive character data in v2.0 format
"""

import json
import sys

def create_poa_characters():
    """Create comprehensive character data for Prisoner of Azkaban"""
    return {
        "harry-potter": {
            "name": "Harry Potter",
            "aliases": ["The Boy Who Lived"],
            "appearances": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Thirteen-year-old wizard spending another miserable summer at the Dursleys. Learning about escaped prisoner Sirius Black.",
                    "role": "Third-year student",
                    "relationships": {
                        "Sirius Black": "Threatened by",
                        "Vernon Dursley": "Nephew of",
                        "Petunia Dursley": "Nephew of"
                    }
                },
                "2": {
                    "revealedIn": 2,
                    "description": "Accidentally inflated Aunt Marge and fled Privet Drive in anger. Picked up by the Knight Bus.",
                    "role": "Runaway student",
                    "relationships": {
                        "Marge Dursley": "Inflated",
                        "Stan Shunpike": "Passenger of"
                    }
                },
                "5": {
                    "revealedIn": 5,
                    "description": "Faints when Dementors board the Hogwarts Express. Saved by Professor Lupin who teaches him about the creatures.",
                    "role": "Student, Dementor victim",
                    "relationships": {
                        "Remus Lupin": "Rescued by",
                        "Dementors": "Affected by"
                    }
                },
                "9": {
                    "revealedIn": 9,
                    "description": "Begins taking private lessons with Professor Lupin to learn the Patronus Charm. Still faints around Dementors.",
                    "role": "Student, Patronus learner",
                    "relationships": {
                        "Remus Lupin": "Taught by",
                        "James Potter": "Son of (deceased)"
                    }
                },
                "12": {
                    "revealedIn": 12,
                    "description": "Learns that Sirius Black was his father's best friend and supposedly betrayed his parents to Voldemort.",
                    "role": "Student, Target",
                    "relationships": {
                        "Sirius Black": "Betrayed parents of",
                        "James Potter": "Son of",
                        "Lily Potter": "Son of"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "Discovers Peter Pettigrew is alive and that Sirius is innocent. Saves Sirius from the Dementors' kiss.",
                    "role": "Student, Truth seeker",
                    "relationships": {
                        "Sirius Black": "Godson of",
                        "Peter Pettigrew": "Enemy of",
                        "James Potter": "Son of"
                    }
                },
                "21": {
                    "revealedIn": 21,
                    "description": "Uses the Time-Turner to save Buckbeak and Sirius. Successfully casts a full Patronus to save his past self.",
                    "role": "Student, Time traveler",
                    "relationships": {
                        "Hermione Granger": "Time traveling with",
                        "Buckbeak": "Rescued",
                        "Sirius Black": "Rescued"
                    }
                }
            }
        },
        "hermione-granger": {
            "name": "Hermione Granger",
            "aliases": ["Hermione"],
            "appearances": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Third-year student taking an unusually heavy course load. Seems to be everywhere at once.",
                    "role": "Student, Overachiever", 
                    "relationships": {
                        "Harry Potter": "Best friend",
                        "Ron Weasley": "Best friend"
                    }
                },
                "16": {
                    "revealedIn": 16,
                    "description": "Punches Draco Malfoy and walks out of Divination class. Shows unusual knowledge of magical creatures.",
                    "role": "Student, Activist",
                    "relationships": {
                        "Draco Malfoy": "Punched",
                        "Sybill Trelawney": "Walked out on"
                    }
                },
                "21": {
                    "revealedIn": 21,
                    "description": "Revealed to have been using a Time-Turner all year to attend multiple classes. Helps Harry save Sirius and Buckbeak.",
                    "role": "Student, Time traveler",
                    "relationships": {
                        "Minerva McGonagall": "Trusted by with Time-Turner",
                        "Harry Potter": "Time traveling with"
                    }
                }
            }
        },
        "ron-weasley": {
            "name": "Ron Weasley",
            "aliases": ["Ron"],
            "appearances": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Harry's best friend, now in his third year. His rat Scabbers seems ill and keeps trying to hide.",
                    "role": "Third-year student",
                    "relationships": {
                        "Harry Potter": "Best friend",
                        "Scabbers": "Pet owner of",
                        "Crookshanks": "Cat enemy"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Scabbers has disappeared. Ron blames Hermione's cat and their friendship is strained.",
                    "role": "Student, Pet owner",
                    "relationships": {
                        "Hermione Granger": "Arguing with",
                        "Crookshanks": "Blames for Scabbers' disappearance"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "Learns that his rat Scabbers was actually Peter Pettigrew in Animagus form. Feels betrayed and disgusted.",
                    "role": "Student, Betrayed owner",
                    "relationships": {
                        "Peter Pettigrew": "Betrayed by",
                        "Sirius Black": "Apologized to"
                    }
                }
            }
        },
        "sirius-black": {
            "name": "Sirius Black",
            "aliases": ["Padfoot", "The Prisoner"],
            "appearances": [1, 3, 4, 16, 17, 18, 19, 20, 21, 22],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Dangerous wizard who escaped from Azkaban prison. First wizard ever to break out of the supposedly escape-proof prison.",
                    "role": "Escaped prisoner",
                    "relationships": {
                        "Harry Potter": "Hunting",
                        "Ministry of Magic": "Fugitive from"
                    }
                },
                "12": {
                    "revealedIn": 12,
                    "description": "Revealed to have been James Potter's best friend and Harry's godfather. Accused of betraying the Potters to Voldemort.",
                    "role": "Alleged traitor",
                    "relationships": {
                        "James Potter": "Former best friend",
                        "Lily Potter": "Betrayed to Voldemort",
                        "Harry Potter": "Godfather of",
                        "Peter Pettigrew": "Allegedly murdered"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "Actually innocent - was framed by Peter Pettigrew. Has been hunting Pettigrew to prove his innocence and protect Harry.",
                    "role": "Innocent prisoner, Animagus",
                    "relationships": {
                        "Harry Potter": "Protecting godson",
                        "Peter Pettigrew": "Hunting for betrayal",
                        "James Potter": "Loyal friend of",
                        "Remus Lupin": "Old friend"
                    }
                },
                "21": {
                    "revealedIn": 21,
                    "description": "Escaped on Buckbeak after being saved by Harry and Hermione. Still a fugitive but free to help Harry from hiding.",
                    "role": "Free fugitive",
                    "relationships": {
                        "Harry Potter": "Rescued by",
                        "Buckbeak": "Escaped on"
                    }
                }
            }
        },
        "remus-lupin": {
            "name": "Remus John Lupin",
            "aliases": ["Professor Lupin", "Moony"],
            "appearances": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "New Defence Against the Dark Arts teacher. Shabby but kind wizard who saves Harry from the Dementors.",
                    "role": "Professor, DADA teacher",
                    "relationships": {
                        "Harry Potter": "Teacher of",
                        "Dementors": "Can repel"
                    }
                },
                "8": {
                    "revealedIn": 8,
                    "description": "Excellent teacher who makes Defence classes practical and engaging. Students love his lessons after years of poor teaching.",
                    "role": "Professor, Popular teacher",
                    "relationships": {
                        "Students": "Beloved teacher of",
                        "Neville Longbottom": "Encouraging"
                    }
                },
                "18": {
                    "revealedIn": 18,
                    "description": "Revealed to be a werewolf. Transforms under the full moon and nearly attacks Harry, Hermione, and Sirius.",
                    "role": "Professor, Werewolf",
                    "relationships": {
                        "Sirius Black": "Old friend",
                        "Peter Pettigrew": "Former friend, betrayed by",
                        "James Potter": "Friend of (deceased)",
                        "Severus Snape": "Dislikes"
                    }
                },
                "22": {
                    "revealedIn": 22,
                    "description": "Resigns from Hogwarts after Snape reveals his werewolf identity. Returns Harry's Invisibility Cloak and the Marauder's Map.",
                    "role": "Former professor",
                    "relationships": {
                        "Harry Potter": "Fond of",
                        "Severus Snape": "Exposed by"
                    }
                }
            }
        },
        "peter-pettigrew": {
            "name": "Peter Pettigrew",
            "aliases": ["Wormtail", "Scabbers"],
            "appearances": [4, 5, 15, 17, 18, 19],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Ron's pet rat who seems sickly and nervous. Has been with the Weasley family for twelve years.",
                    "role": "Pet rat",
                    "relationships": {
                        "Ron Weasley": "Pet of",
                        "Weasley family": "Pet of"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "Revealed to be an Animagus who has been hiding as Ron's rat. Actually the wizard who betrayed Harry's parents to Voldemort.",
                    "role": "Traitor, Animagus",
                    "relationships": {
                        "James Potter": "Betrayed to Voldemort",
                        "Lily Potter": "Betrayed to Voldemort", 
                        "Sirius Black": "Framed for murder",
                        "Voldemort": "Servant of"
                    }
                },
                "19": {
                    "revealedIn": 19,
                    "description": "Escapes when Lupin transforms into a werewolf. Returns to serve Voldemort after twelve years in hiding.",
                    "role": "Escaped traitor",
                    "relationships": {
                        "Voldemort": "Fleeing to serve"
                    }
                }
            }
        },
        "rubeus-hagrid": {
            "name": "Rubeus Hagrid",
            "aliases": ["Hagrid"],
            "appearances": [4, 6, 7, 8, 11, 14, 16, 17, 20, 21, 22],
            "knowledge": {
                "6": {
                    "revealedIn": 6,
                    "description": "Gamekeeper and teacher of Care of Magical Creatures. Introduces the class to Buckbeak the hippogriff.",
                    "role": "Gamekeeper, Professor",
                    "relationships": {
                        "Buckbeak": "Caretaker of",
                        "Students": "Teacher of"
                    }
                },
                "7": {
                    "revealedIn": 7,
                    "description": "Worried about Buckbeak after Draco's injury. Fears what the Ministry might do to his beloved creature.",
                    "role": "Professor, Animal protector",
                    "relationships": {
                        "Buckbeak": "Protecting",
                        "Draco Malfoy": "Student who was injured"
                    }
                },
                "20": {
                    "revealedIn": 20,
                    "description": "Devastated when Buckbeak is sentenced to death. Drinks heavily as the execution approaches.",
                    "role": "Professor, Grief-stricken",
                    "relationships": {
                        "Buckbeak": "Mourning for",
                        "Executioner": "Dreading visit from"
                    }
                }
            }
        },
        "severus-snape": {
            "name": "Severus Snape",
            "aliases": ["Professor Snape"],
            "appearances": [5, 8, 9, 16, 17, 18, 19, 22],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Still the unpleasant Potions Master. Clearly dislikes the new Defence teacher, Professor Lupin.",
                    "role": "Potions Master",
                    "relationships": {
                        "Remus Lupin": "Dislikes intensely",
                        "Harry Potter": "Still antagonistic toward"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "Arrives at the Shrieking Shack and tries to arrest Sirius. Reveals deep hatred for the Marauders from their school days.",
                    "role": "Potions Master, Grudge holder",
                    "relationships": {
                        "Sirius Black": "Hates from school",
                        "Remus Lupin": "Hates from school",
                        "James Potter": "Hated (deceased)"
                    }
                },
                "22": {
                    "revealedIn": 22,
                    "description": "Reveals Lupin's werewolf identity to the school, forcing Lupin's resignation. Takes satisfaction in his revenge.",
                    "role": "Potions Master, Revenge seeker",
                    "relationships": {
                        "Remus Lupin": "Exposed secret of"
                    }
                }
            }
        },
        "albus-dumbledore": {
            "name": "Albus Dumbledore",
            "aliases": ["Headmaster", "Professor Dumbledore"],
            "appearances": [4, 5, 14, 17, 20, 21, 22],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Hogwarts Headmaster concerned about the Dementors stationed at school. Trusts his teachers completely.",
                    "role": "Headmaster",
                    "relationships": {
                        "Dementors": "Reluctantly allows at school",
                        "Remus Lupin": "Hired despite knowing secret"
                    }
                },
                "21": {
                    "revealedIn": 21,
                    "description": "Suggests that Harry and Hermione can save more than one innocent life by using time wisely.",
                    "role": "Headmaster, Wise guide",
                    "relationships": {
                        "Harry Potter": "Guides subtly",
                        "Hermione Granger": "Trusts with Time-Turner"
                    }
                }
            }
        },
        "dementors": {
            "name": "Dementors",
            "aliases": ["Soul-sucking creatures"],
            "appearances": [1, 3, 5, 9, 13, 20, 21],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "Hooded, soul-sucking creatures guarding Hogwarts to catch Sirius Black. Drain happiness and hope from people nearby.",
                    "role": "Prison guards",
                    "relationships": {
                        "Harry Potter": "Particularly affects",
                        "Ministry of Magic": "Employed by"
                    }
                },
                "9": {
                    "revealedIn": 9,
                    "description": "Can only be repelled by the Patronus Charm. Feed on happy memories and positive emotions.",
                    "role": "Dark creatures",
                    "relationships": {
                        "Patronus Charm": "Repelled by",
                        "Sirius Black": "Hunting"
                    }
                },
                "20": {
                    "revealedIn": 20,
                    "description": "Perform the Dementor's Kiss - sucking out a person's soul, leaving them an empty shell.",
                    "role": "Executioners",
                    "relationships": {
                        "Sirius Black": "Ordered to execute"
                    }
                }
            }
        },
        "buckbeak": {
            "name": "Buckbeak",
            "aliases": ["The Hippogriff"],
            "appearances": [6, 7, 11, 14, 16, 20, 21, 22],
            "knowledge": {
                "6": {
                    "revealedIn": 6,
                    "description": "Magnificent hippogriff with the head and wings of an eagle and body of a horse. Very proud creature that demands respect.",
                    "role": "Magical creature",
                    "relationships": {
                        "Rubeus Hagrid": "Cared for by",
                        "Harry Potter": "Likes and respects"
                    }
                },
                "7": {
                    "revealedIn": 7,
                    "description": "Attacks Draco Malfoy after Draco insults him. Draco claims to be badly injured.",
                    "role": "Magical creature, Accused attacker",
                    "relationships": {
                        "Draco Malfoy": "Attacked for disrespect"
                    }
                },
                "20": {
                    "revealedIn": 20,
                    "description": "Sentenced to death by the Committee for Disposal of Dangerous Creatures. Awaits execution.",
                    "role": "Condemned creature",
                    "relationships": {
                        "Ministry executioner": "To be killed by"
                    }
                },
                "21": {
                    "revealedIn": 21,
                    "description": "Rescued by Harry and Hermione using the Time-Turner. Flies Sirius to freedom.",
                    "role": "Rescued creature, Escape vehicle",
                    "relationships": {
                        "Harry Potter": "Rescued by",
                        "Sirius Black": "Carried to freedom"
                    }
                }
            }
        },
        "draco-malfoy": {
            "name": "Draco Malfoy", 
            "aliases": ["Draco"],
            "appearances": [4, 6, 7, 11, 16, 20],
            "knowledge": {
                "6": {
                    "revealedIn": 6,
                    "description": "Third-year Slytherin student. Shows off and insults Buckbeak during Hagrid's first class.",
                    "role": "Student, Slytherin",
                    "relationships": {
                        "Buckbeak": "Insulted and attacked by",
                        "Rubeus Hagrid": "Student of"
                    }
                },
                "7": {
                    "revealedIn": 7,
                    "description": "Claims to be seriously injured by Buckbeak. Milks the injury for sympathy and attention.",
                    "role": "Student, Injury faker",
                    "relationships": {
                        "Lucius Malfoy": "Father reporting to",
                        "Poppy Pomfrey": "Treated by"
                    }
                },
                "16": {
                    "revealedIn": 16,
                    "description": "Punched in the face by Hermione Granger. Cowardly runs away from the confrontation.",
                    "role": "Student, Coward",
                    "relationships": {
                        "Hermione Granger": "Punched by"
                    }
                }
            }
        },
        "cornelius-fudge": {
            "name": "Cornelius Fudge",
            "aliases": ["Minister Fudge", "Minister"],
            "appearances": [3, 4, 20, 21],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Minister for Magic who meets Harry at the Leaky Cauldron. Concerned about Harry's safety from Sirius Black.",
                    "role": "Minister of Magic",
                    "relationships": {
                        "Harry Potter": "Protecting from Black",
                        "Sirius Black": "Hunting escaped prisoner"
                    }
                },
                "20": {
                    "revealedIn": 20,
                    "description": "Arrives at Hogwarts with the Dementor to perform the Kiss on Sirius Black. Refuses to believe in Black's innocence.",
                    "role": "Minister of Magic, Dementor overseer",
                    "relationships": {
                        "Sirius Black": "Wants executed",
                        "Dementors": "Brought to execute"
                    }
                }
            }
        },
        "sybill-trelawney": {
            "name": "Sybill Patricia Trelawney",
            "aliases": ["Professor Trelawney"],
            "appearances": [6, 8, 11, 16, 17],
            "knowledge": {
                "6": {
                    "revealedIn": 6,
                    "description": "New Divination teacher with huge glasses and many shawls. Predicts death and doom dramatically but seems like a fraud.",
                    "role": "Professor, Divination",
                    "relationships": {
                        "Harry Potter": "Predicts death of",
                        "Students": "Teacher of"
                    }
                },
                "16": {
                    "revealedIn": 16,
                    "description": "Hermione walks out of her class, calling Divination rubbish. Trelawney is offended by the dismissal.",
                    "role": "Professor, Offended teacher",
                    "relationships": {
                        "Hermione Granger": "Abandoned by student"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "Makes a genuine prophecy about the servant returning to his master. Doesn't remember making the prediction.",
                    "role": "Professor, True Seer",
                    "relationships": {
                        "Peter Pettigrew": "Prophesied about (unknowingly)"
                    }
                }
            }
        },
        "neville-longbottom": {
            "name": "Neville Longbottom",
            "aliases": ["Neville"],
            "appearances": [5, 6, 7, 8, 13],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Third-year Gryffindor who is terrified of Professor Snape. Performs better in other classes.",
                    "role": "Student, Gryffindor",
                    "relationships": {
                        "Severus Snape": "Terrified of",
                        "Remus Lupin": "Helped by"
                    }
                },
                "8": {
                    "revealedIn": 8,
                    "description": "Successfully faces a boggart that takes the form of Snape. Gains confidence from Professor Lupin's teaching.",
                    "role": "Student, Improving confidence",
                    "relationships": {
                        "Remus Lupin": "Encouraged by",
                        "Boggart": "Successfully defeated"
                    }
                }
            }
        }
    }

def main():
    # Read the existing file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/prisoner-of-azkaban.json', 'r') as f:
        data = json.load(f)
    
    # Update schema version and add characters
    data["meta"]["schemaVersion"] = "2.0"
    data["characters"] = create_poa_characters()
    
    # Write back to file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/prisoner-of-azkaban.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Successfully filled Prisoner of Azkaban with character data")
    print(f"Added {len(data['characters'])} characters")

if __name__ == "__main__":
    main()