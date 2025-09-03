#!/usr/bin/env python3
"""
Fills Deathly Hallows with comprehensive character data in v2.0 format
"""

import json
import sys

def create_dh_characters():
    """Create comprehensive character data for Deathly Hallows"""
    return {
        "harry-potter": {
            "name": "Harry Potter",
            "aliases": ["The Boy Who Lived", "The Chosen One", "Undesirable No. 1"],
            "appearances": list(range(1, 38)),  # Appears in all 37 chapters
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Seventeen-year-old wizard preparing to leave Privet Drive forever. No longer protected by his mother's blood.",
                    "role": "Horcrux hunter, Fugitive",
                    "relationships": {
                        "Dursley family": "Saying final goodbye to",
                        "Privet Drive": "Leaving forever"
                    }
                },
                "4": {
                    "revealedIn": 4,
                    "description": "Survives the aerial battle while fleeing Privet Drive. Hedwig dies protecting him.",
                    "role": "Fugitive, Battle survivor",
                    "relationships": {
                        "Hedwig": "Pet owl killed protecting him",
                        "Death Eaters": "Hunted by"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Devastated when his wand is accidentally broken by Hermione. Feels more vulnerable than ever.",
                    "role": "Horcrux hunter, Wandless wizard",
                    "relationships": {
                        "Holly wand": "Accidentally destroyed",
                        "Hermione Granger": "Accidentally broke his wand"
                    }
                },
                "19": {
                    "revealedIn": 19,
                    "description": "Learns about the Deathly Hallows and realizes he already possesses the Invisibility Cloak.",
                    "role": "Horcrux hunter, Hallows seeker",
                    "relationships": {
                        "Deathly Hallows": "Seeking",
                        "Invisibility Cloak": "Owns one of the Hallows"
                    }
                },
                "24": {
                    "revealedIn": 24,
                    "description": "Captured by Snatchers and taken to Malfoy Manor. Identity barely concealed by swelling.",
                    "role": "Prisoner, Disguised",
                    "relationships": {
                        "Snatchers": "Captured by",
                        "Hermione Granger": "Disguised his face"
                    }
                },
                "33": {
                    "revealedIn": 33,
                    "description": "Learns he is the final Horcrux and must die for Voldemort to be mortal.",
                    "role": "Horcrux, Sacrifice",
                    "relationships": {
                        "Voldemort": "Part of soul inside",
                        "Severus Snape": "Learned truth from memories"
                    }
                },
                "34": {
                    "revealedIn": 34,
                    "description": "Walks into the Forbidden Forest to sacrifice himself to Voldemort. Killed but comes back.",
                    "role": "Sacrifice, Master of Death",
                    "relationships": {
                        "Voldemort": "Killed by but survives",
                        "James Potter": "Met spirit of",
                        "Lily Potter": "Met spirit of"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Defeats Voldemort in final duel when Elder Wand's allegiance is revealed to be his.",
                    "role": "Victor, True master of Elder Wand",
                    "relationships": {
                        "Voldemort": "Finally defeated",
                        "Elder Wand": "True master of"
                    }
                }
            }
        },
        "hermione-granger": {
            "name": "Hermione Granger",
            "aliases": ["Hermione"],
            "appearances": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37],
            "knowledge": {
                "6": {
                    "revealedIn": 6,
                    "description": "Modified her parents' memories and sent them to Australia to protect them from Death Eaters.",
                    "role": "Daughter, Memory modifier",
                    "relationships": {
                        "Parents": "Memory-modified for safety",
                        "Death Eaters": "Protecting family from"
                    }
                },
                "11": {
                    "revealedIn": 11,
                    "description": "Infiltrates the Ministry disguised as a Ministry worker to steal the Horcrux locket.",
                    "role": "Horcrux hunter, Infiltrator",
                    "relationships": {
                        "Ministry of Magic": "Infiltrating",
                        "Dolores Umbridge": "Stealing locket from"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Accidentally breaks Harry's wand while defending against Nagini. Feels terrible guilt.",
                    "role": "Horcrux hunter, Accidental destroyer",
                    "relationships": {
                        "Harry Potter": "Accidentally broke wand of",
                        "Nagini": "Defending against"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Tortured by Bellatrix Lestrange at Malfoy Manor with the Cruciatus Curse.",
                    "role": "Prisoner, Torture victim",
                    "relationships": {
                        "Bellatrix Lestrange": "Tortured by",
                        "Ron Weasley": "Heard screaming by"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Fights in the Battle of Hogwarts, helping to destroy Hufflepuff's cup Horcrux.",
                    "role": "Fighter, Horcrux destroyer",
                    "relationships": {
                        "Hufflepuff's cup": "Helped destroy",
                        "Ron Weasley": "Fighting alongside"
                    }
                }
            }
        },
        "ron-weasley": {
            "name": "Ron Weasley",
            "aliases": ["Ron"],
            "appearances": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Infiltrates the Ministry disguised as a worker to help steal the Horcrux locket.",
                    "role": "Horcrux hunter, Infiltrator",
                    "relationships": {
                        "Ministry of Magic": "Infiltrating",
                        "Harry Potter": "Mission partner"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Abandons Harry and Hermione due to the Horcrux's influence and frustration with their progress.",
                    "role": "Former Horcrux hunter, Deserter",
                    "relationships": {
                        "Harry Potter": "Abandoned",
                        "Hermione Granger": "Abandoned",
                        "Horcrux locket": "Influenced by"
                    }
                },
                "19": {
                    "revealedIn": 19,
                    "description": "Returns to save Harry from drowning and destroys the Horcrux locket with Gryffindor's sword.",
                    "role": "Horcrux hunter, Destroyer",
                    "relationships": {
                        "Harry Potter": "Saved from drowning",
                        "Horcrux locket": "Destroyed",
                        "Sword of Gryffindor": "Used to destroy Horcrux"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Captured at Malfoy Manor and forced to listen to Hermione being tortured.",
                    "role": "Prisoner, Helpless witness",
                    "relationships": {
                        "Hermione Granger": "Heard being tortured",
                        "Bellatrix Lestrange": "Helpless against"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Fights in the Battle of Hogwarts and helps destroy Hufflepuff's cup with basilisk fangs.",
                    "role": "Fighter, Horcrux destroyer",
                    "relationships": {
                        "Hufflepuff's cup": "Helped destroy",
                        "Hermione Granger": "Fighting with"
                    }
                }
            }
        },
        "lord-voldemort": {
            "name": "Lord Voldemort",
            "aliases": ["Tom Marvolo Riddle", "The Dark Lord", "He-Who-Must-Not-Be-Named"],
            "appearances": [1, 17, 23, 24, 32, 33, 34, 35, 36],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Holds council with Death Eaters at Malfoy Manor. Takes Lucius's wand and plans Harry's capture.",
                    "role": "Dark Lord, Wand seeker",
                    "relationships": {
                        "Death Eaters": "Commands",
                        "Lucius Malfoy": "Took wand from"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "His soul fragment in the locket Horcrux taunts Ron with his deepest fears and insecurities.",
                    "role": "Soul fragment, Tormentor",
                    "relationships": {
                        "Ron Weasley": "Tormented through Horcrux",
                        "Horcrux locket": "Soul piece within"
                    }
                },
                "24": {
                    "revealedIn": 24,
                    "description": "Furious that Harry escaped Malfoy Manor. Seeks the Elder Wand to overcome their wand connection.",
                    "role": "Dark Lord, Elder Wand seeker",
                    "relationships": {
                        "Elder Wand": "Seeking",
                        "Harry Potter": "Frustrated by escapes of"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Attacks Hogwarts in the final battle. Becomes increasingly desperate as Horcruxes are destroyed.",
                    "role": "Dark Lord, Attacker",
                    "relationships": {
                        "Hogwarts": "Attacking",
                        "Nagini": "Last remaining Horcrux"
                    }
                },
                "34": {
                    "revealedIn": 34,
                    "description": "Kills Harry in the Forbidden Forest, unknowingly destroying his own soul fragment.",
                    "role": "Dark Lord, Self-destroyer",
                    "relationships": {
                        "Harry Potter": "Killed (temporarily)",
                        "Soul fragment": "Destroyed own piece"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Dies when his Killing Curse rebounds from the Elder Wand, which recognizes Harry as its master.",
                    "role": "Dark Lord, Deceased",
                    "relationships": {
                        "Elder Wand": "Killed by own spell through",
                        "Harry Potter": "Finally defeated by"
                    }
                }
            }
        },
        "severus-snape": {
            "name": "Severus Snape",
            "aliases": ["Professor Snape", "The Half-Blood Prince"],
            "appearances": [1, 28, 30, 32, 33],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Present at Death Eater meeting, providing information about Harry's movements to Voldemort.",
                    "role": "Death Eater, Double agent",
                    "relationships": {
                        "Voldemort": "Serving (seemingly)",
                        "Order of the Phoenix": "Actually serving"
                    }
                },
                "30": {
                    "revealedIn": 30,
                    "description": "Headmaster of Hogwarts under Death Eater control. Secretly helps students when possible.",
                    "role": "Headmaster, Secret protector",
                    "relationships": {
                        "Students": "Secretly protecting",
                        "Death Eaters": "Working for (outwardly)"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Killed by Nagini on Voldemort's orders in the Shrieking Shack.",
                    "role": "Death Eater, Murder victim",
                    "relationships": {
                        "Nagini": "Killed by",
                        "Voldemort": "Murdered by order of"
                    }
                },
                "33": {
                    "revealedIn": 33,
                    "description": "Memories reveal he loved Lily Potter and spent years protecting Harry for her sake.",
                    "role": "Double agent, Protector",
                    "relationships": {
                        "Lily Potter": "Always loved",
                        "Harry Potter": "Protected for Lily's sake",
                        "Albus Dumbledore": "Worked with to protect Harry"
                    }
                }
            }
        },
        "albus-dumbledore": {
            "name": "Albus Dumbledore",
            "aliases": ["Professor Dumbledore"],
            "appearances": [18, 33, 35],
            "knowledge": {
                "18": {
                    "revealedIn": 18,
                    "description": "His past revealed through Rita Skeeter's biography, including his friendship with Grindelwald.",
                    "role": "Former Headmaster (deceased)",
                    "relationships": {
                        "Gellert Grindelwald": "Former friend",
                        "Rita Skeeter": "Scandalous biography by"
                    }
                },
                "33": {
                    "revealedIn": 33,
                    "description": "His plan revealed through Snape's memories - he knew Harry was a Horcrux and must die.",
                    "role": "Deceased mastermind",
                    "relationships": {
                        "Harry Potter": "Planned death of",
                        "Severus Snape": "Worked with"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Appears to Harry in limbo-like King's Cross, explaining the nature of their connection.",
                    "role": "Spirit guide",
                    "relationships": {
                        "Harry Potter": "Guided in limbo"
                    }
                }
            }
        },
        "dobby": {
            "name": "Dobby",
            "aliases": ["Free Elf"],
            "appearances": [10, 23],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Helps Harry track down Mundungus Fletcher to recover stolen items from Grimmauld Place.",
                    "role": "Free house-elf, Helper",
                    "relationships": {
                        "Harry Potter": "Helping find items",
                        "Mundungus Fletcher": "Tracked down for Harry"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Dies saving Harry and friends from Malfoy Manor, killed by Bellatrix's knife.",
                    "role": "Free house-elf, Hero",
                    "relationships": {
                        "Harry Potter": "Died saving",
                        "Bellatrix Lestrange": "Killed by",
                        "Hermione Granger": "Died protecting"
                    }
                }
            }
        },
        "bellatrix-lestrange": {
            "name": "Bellatrix Lestrange",
            "aliases": ["Bellatrix Black"],
            "appearances": [1, 23, 32],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Present at Death Eater meeting at Malfoy Manor, devoted follower of Voldemort.",
                    "role": "Death Eater, Fanatic",
                    "relationships": {
                        "Voldemort": "Fanatically devoted to",
                        "Death Eaters": "Leading member"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Tortures Hermione at Malfoy Manor and kills Dobby while he helps the prisoners escape.",
                    "role": "Death Eater, Torturer",
                    "relationships": {
                        "Hermione Granger": "Tortured",
                        "Dobby": "Killed",
                        "Harry Potter": "Tormented"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Killed by Molly Weasley during the Battle of Hogwarts after threatening Ginny.",
                    "role": "Death Eater, Casualty",
                    "relationships": {
                        "Molly Weasley": "Killed by",
                        "Ginny Weasley": "Threatened before death"
                    }
                }
            }
        },
        "nagini": {
            "name": "Nagini",
            "aliases": ["The Snake"],
            "appearances": [1, 16, 17, 32, 33, 34],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Voldemort's snake and Horcrux, present at Death Eater meetings and used for executions.",
                    "role": "Snake, Horcrux",
                    "relationships": {
                        "Voldemort": "Pet and Horcrux of",
                        "Death Eaters": "Present at meetings"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "Attacks Harry and Hermione at Godric's Hollow, disguised as Bathilda Bagshot.",
                    "role": "Snake, Attacker",
                    "relationships": {
                        "Harry Potter": "Attacked",
                        "Bathilda Bagshot": "Used corpse of as disguise"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Kills Severus Snape on Voldemort's orders in the Shrieking Shack.",
                    "role": "Snake, Executioner",
                    "relationships": {
                        "Severus Snape": "Killed",
                        "Voldemort": "Following orders of"
                    }
                },
                "33": {
                    "revealedIn": 33,
                    "description": "Beheaded by Neville Longbottom with Gryffindor's sword, destroying the final Horcrux.",
                    "role": "Snake, Destroyed Horcrux",
                    "relationships": {
                        "Neville Longbottom": "Killed by",
                        "Sword of Gryffindor": "Destroyed by"
                    }
                }
            }
        },
        "neville-longbottom": {
            "name": "Neville Longbottom",
            "aliases": ["Neville"],
            "appearances": [29, 30, 31, 32, 33, 36],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Leads student resistance at Hogwarts against the Carrows and Snape's regime.",
                    "role": "Resistance leader",
                    "relationships": {
                        "Students": "Leading resistance of",
                        "Carrows": "Fighting against",
                        "Severus Snape": "Resisting"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Fights bravely in the Battle of Hogwarts, showing remarkable leadership and courage.",
                    "role": "Fighter, Leader",
                    "relationships": {
                        "Dumbledore's Army": "Leading",
                        "Death Eaters": "Fighting"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Kills Nagini with Gryffindor's sword, destroying the final Horcrux and making Voldemort mortal.",
                    "role": "Hero, Horcrux destroyer",
                    "relationships": {
                        "Nagini": "Beheaded",
                        "Sword of Gryffindor": "Wielded to destroy Horcrux",
                        "Voldemort": "Made mortal by destroying Horcrux"
                    }
                }
            }
        },
        "luna-lovegood": {
            "name": "Luna Lovegood",
            "aliases": ["Loony Lovegood"],
            "appearances": [20, 21, 25, 32, 36],
            "knowledge": {
                "21": {
                    "revealedIn": 21,
                    "description": "Captured by Death Eaters and held prisoner at Malfoy Manor with Ollivander and Griphook.",
                    "role": "Prisoner",
                    "relationships": {
                        "Death Eaters": "Captured by",
                        "Ollivander": "Fellow prisoner",
                        "Griphook": "Fellow prisoner"
                    }
                },
                "25": {
                    "revealedIn": 25,
                    "description": "Rescued from Malfoy Manor by Dobby along with Harry, Ron, Hermione, and others.",
                    "role": "Rescued prisoner",
                    "relationships": {
                        "Dobby": "Rescued by",
                        "Harry Potter": "Rescued with"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Fights in the Battle of Hogwarts alongside other DA members.",
                    "role": "Fighter",
                    "relationships": {
                        "Dumbledore's Army": "Fighting with",
                        "Death Eaters": "Fighting against"
                    }
                }
            }
        },
        "draco-malfoy": {
            "name": "Draco Malfoy",
            "aliases": ["Draco"],
            "appearances": [1, 23, 32],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Present at Death Eater meeting at his family home, clearly uncomfortable with Voldemort's presence.",
                    "role": "Reluctant Death Eater ally",
                    "relationships": {
                        "Voldemort": "Afraid of",
                        "Lucius Malfoy": "Father serving Voldemort",
                        "Narcissa Malfoy": "Mother protecting him"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Present when Harry is brought to Malfoy Manor but doesn't positively identify him.",
                    "role": "Reluctant identifier",
                    "relationships": {
                        "Harry Potter": "Didn't identify clearly",
                        "Bellatrix Lestrange": "Pressured by aunt"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Saved by Harry during the Battle of Hogwarts when the Room of Requirement catches fire.",
                    "role": "Rescued enemy",
                    "relationships": {
                        "Harry Potter": "Saved by",
                        "Vincent Crabbe": "Friend who died",
                        "Gregory Goyle": "Escaped with"
                    }
                }
            }
        },
        "ginny-weasley": {
            "name": "Ginny Weasley",
            "aliases": ["Ginny"],
            "appearances": [6, 7, 30, 32, 36, 37],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Attends Bill and Fleur's wedding before it's attacked by Death Eaters.",
                    "role": "Wedding guest, Student",
                    "relationships": {
                        "Harry Potter": "Still in love with",
                        "Bill Weasley": "Brother"
                    }
                },
                "30": {
                    "revealedIn": 30,
                    "description": "Helps Neville lead student resistance at Hogwarts against Death Eater control.",
                    "role": "Resistance member",
                    "relationships": {
                        "Neville Longbottom": "Co-leader of resistance",
                        "Students": "Leading with"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Fights in the Battle of Hogwarts, nearly killed by Bellatrix before Molly intervenes.",
                    "role": "Fighter",
                    "relationships": {
                        "Bellatrix Lestrange": "Nearly killed by",
                        "Molly Weasley": "Protected by mother"
                    }
                },
                "37": {
                    "revealedIn": 37,
                    "description": "Reunited with Harry after Voldemort's defeat. Their relationship can now continue safely.",
                    "role": "Harry's girlfriend",
                    "relationships": {
                        "Harry Potter": "Reunited with"
                    }
                }
            }
        },
        "molly-weasley": {
            "name": "Molly Weasley",
            "aliases": ["Mrs. Weasley"],
            "appearances": [6, 7, 32, 36, 37],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Organizes Bill and Fleur's wedding despite the dangerous times.",
                    "role": "Mother, Wedding organizer",
                    "relationships": {
                        "Bill Weasley": "Son getting married",
                        "Fleur Delacour": "New daughter-in-law"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Fights fiercely in the Battle of Hogwarts to protect her children, kills Bellatrix Lestrange.",
                    "role": "Fighter, Protective mother",
                    "relationships": {
                        "Bellatrix Lestrange": "Killed to protect Ginny",
                        "Ginny Weasley": "Protecting from Bellatrix",
                        "Weasley children": "Fighting to protect"
                    }
                }
            }
        }
    }

def main():
    # Read the existing file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/deathly-hallows.json', 'r') as f:
        data = json.load(f)
    
    # Update schema version and add characters
    data["meta"]["schemaVersion"] = "2.0"
    data["characters"] = create_dh_characters()
    
    # Write back to file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/deathly-hallows.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Successfully filled Deathly Hallows with character data")
    print(f"Added {len(data['characters'])} characters")

if __name__ == "__main__":
    main()