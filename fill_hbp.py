#!/usr/bin/env python3
"""
Fills Half-Blood Prince with comprehensive character data in v2.0 format
"""

import json
import sys

def create_hbp_characters():
    """Create comprehensive character data for Half-Blood Prince"""
    return {
        "harry-potter": {
            "name": "Harry Potter",
            "aliases": ["The Boy Who Lived", "The Chosen One"],
            "appearances": list(range(1, 31)),  # Appears in all 30 chapters
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Sixteen-year-old wizard picked up by Dumbledore from the Dursleys. Learning about Voldemort's past.",
                    "role": "Sixth-year student",
                    "relationships": {
                        "Albus Dumbledore": "Private lessons with",
                        "Dursley family": "Living with reluctantly"
                    }
                },
                "9": {
                    "revealedIn": 9,
                    "description": "Excels in Potions using an old textbook annotated by 'The Half-Blood Prince.' Becomes Slughorn's favorite.",
                    "role": "Student, Potions prodigy",
                    "relationships": {
                        "Half-Blood Prince": "Using textbook of",
                        "Horace Slughorn": "Star student of"
                    }
                },
                "13": {
                    "revealedIn": 13,
                    "description": "Learning about Voldemort's transformation into a dark wizard through Dumbledore's pensieve memories.",
                    "role": "Student, Tom Riddle researcher",
                    "relationships": {
                        "Tom Riddle": "Studying past of",
                        "Albus Dumbledore": "Learning from"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Learns about Horcruxes and Voldemort's quest for immortality. Understands the magnitude of the task ahead.",
                    "role": "Student, Horcrux hunter",
                    "relationships": {
                        "Voldemort": "Must destroy Horcruxes of",
                        "Horace Slughorn": "Extracted memory from"
                    }
                },
                "27": {
                    "revealedIn": 27,
                    "description": "Accompanies Dumbledore to retrieve a Horcrux from a dangerous cave filled with Inferi.",
                    "role": "Student, Horcrux retriever",
                    "relationships": {
                        "Albus Dumbledore": "Helping retrieve Horcrux",
                        "Horcrux locket": "Retrieved from cave"
                    }
                },
                "29": {
                    "revealedIn": 29,
                    "description": "Witnesses Dumbledore's death at Snape's hands. Discovers the locket Horcrux was a fake.",
                    "role": "Student, Witness to murder",
                    "relationships": {
                        "Albus Dumbledore": "Watched die",
                        "Severus Snape": "Killer of Dumbledore"
                    }
                }
            }
        },
        "albus-dumbledore": {
            "name": "Albus Dumbledore",
            "aliases": ["Headmaster", "Professor Dumbledore"],
            "appearances": [3, 4, 6, 10, 13, 17, 20, 23, 25, 26, 27, 28, 29],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Hogwarts Headmaster recruiting Horace Slughorn to return as Potions Master. Shows a blackened, withered hand.",
                    "role": "Headmaster, Recruiter",
                    "relationships": {
                        "Horace Slughorn": "Recruiting",
                        "Harry Potter": "Teaching privately"
                    }
                },
                "10": {
                    "revealedIn": 10,
                    "description": "Begins showing Harry memories of Voldemort's past, starting with his childhood at the orphanage.",
                    "role": "Teacher, Memory keeper",
                    "relationships": {
                        "Harry Potter": "Teaching about Tom Riddle",
                        "Tom Riddle": "Researching past of"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Explains Horcruxes to Harry and reveals Voldemort split his soul into seven pieces for immortality.",
                    "role": "Teacher, Horcrux expert",
                    "relationships": {
                        "Harry Potter": "Preparing for war",
                        "Voldemort": "Enemy whose Horcruxes must be destroyed"
                    }
                },
                "27": {
                    "revealedIn": 27,
                    "description": "Weakened by drinking potion protecting the Horcrux. Shows vulnerability for the first time.",
                    "role": "Headmaster, Horcrux retriever",
                    "relationships": {
                        "Harry Potter": "Protected by",
                        "Inferi": "Fought against"
                    }
                },
                "29": {
                    "revealedIn": 29,
                    "description": "Killed by Severus Snape atop the Astronomy Tower. His death leaves Harry to complete the mission alone.",
                    "role": "Headmaster, Murder victim",
                    "relationships": {
                        "Severus Snape": "Killed by",
                        "Harry Potter": "Left mission to",
                        "Draco Malfoy": "Disarmed by before death"
                    }
                }
            }
        },
        "severus-snape": {
            "name": "Severus Snape",
            "aliases": ["Professor Snape", "The Half-Blood Prince"],
            "appearances": [2, 8, 9, 15, 19, 21, 24, 28, 29, 30],
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Makes an Unbreakable Vow with Narcissa Malfoy to protect Draco and complete his mission if necessary.",
                    "role": "Professor, Vow maker",
                    "relationships": {
                        "Narcissa Malfoy": "Made vow with",
                        "Draco Malfoy": "Vowed to protect",
                        "Bellatrix Lestrange": "Witness to vow"
                    }
                },
                "8": {
                    "revealedIn": 8,
                    "description": "Finally achieves his ambition to teach Defense Against the Dark Arts, replacing Umbridge.",
                    "role": "DADA Professor",
                    "relationships": {
                        "Students": "Teacher of",
                        "Horace Slughorn": "Replaced by in Potions"
                    }
                },
                "28": {
                    "revealedIn": 28,
                    "description": "Revealed to be the Half-Blood Prince whose textbook helped Harry excel in Potions.",
                    "role": "DADA Professor, Half-Blood Prince",
                    "relationships": {
                        "Harry Potter": "Unknowingly helped through textbook",
                        "Lily Evans": "Mother whose maiden name was Prince"
                    }
                },
                "29": {
                    "revealedIn": 29,
                    "description": "Kills Dumbledore with the Killing Curse and flees Hogwarts with Draco and Death Eaters.",
                    "role": "Death Eater, Murderer",
                    "relationships": {
                        "Albus Dumbledore": "Murdered",
                        "Draco Malfoy": "Helped complete mission",
                        "Harry Potter": "Now mortal enemy"
                    }
                }
            }
        },
        "draco-malfoy": {
            "name": "Draco Malfoy",
            "aliases": ["Draco"],
            "appearances": [6, 7, 11, 15, 21, 24, 27, 29],
            "knowledge": {
                "6": {
                    "revealedIn": 6,
                    "description": "Sixth-year student acting suspiciously at Borgin and Burkes. Seems to be on a secret mission.",
                    "role": "Student, Secret agent",
                    "relationships": {
                        "Lucius Malfoy": "Father (in Azkaban)",
                        "Borgin": "Threatened in shop"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Responsible for cursing Katie Bell and nearly poisoning Ron, trying to kill Dumbledore indirectly.",
                    "role": "Student, Would-be assassin",
                    "relationships": {
                        "Albus Dumbledore": "Trying to kill",
                        "Katie Bell": "Cursed with necklace",
                        "Death Eaters": "Working for"
                    }
                },
                "27": {
                    "revealedIn": 27,
                    "description": "Successfully allows Death Eaters into Hogwarts through a Vanishing Cabinet in the Room of Requirement.",
                    "role": "Student, Death Eater agent",
                    "relationships": {
                        "Death Eaters": "Allowed into castle",
                        "Vanishing Cabinet": "Repaired for infiltration"
                    }
                },
                "29": {
                    "revealedIn": 29,
                    "description": "Disarms Dumbledore atop the Astronomy Tower but cannot bring himself to kill him.",
                    "role": "Student, Conflicted killer",
                    "relationships": {
                        "Albus Dumbledore": "Disarmed but couldn't kill",
                        "Severus Snape": "Saved by",
                        "Voldemort": "Serving under threat"
                    }
                }
            }
        },
        "horace-slughorn": {
            "name": "Horace Slughorn",
            "aliases": ["Professor Slughorn"],
            "appearances": [4, 7, 8, 9, 11, 15, 17, 22, 23, 29, 30],
            "knowledge": {
                "4": {
                    "revealedIn": 4,
                    "description": "Former Hogwarts professor convinced to return as Potions Master. Collector of talented students.",
                    "role": "Potions Professor",
                    "relationships": {
                        "Albus Dumbledore": "Recruited by",
                        "Harry Potter": "New favorite student"
                    }
                },
                "8": {
                    "revealedIn": 8,
                    "description": "Forms the Slug Club of well-connected students. Clearly favors those with famous or influential connections.",
                    "role": "Professor, Social climber",
                    "relationships": {
                        "Slug Club": "Founder of",
                        "Harry Potter": "Prized student"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "Reveals he told Tom Riddle about Horcruxes when he was a student, feeling ashamed of his role.",
                    "role": "Professor, Horcrux informant",
                    "relationships": {
                        "Tom Riddle": "Former student, taught about Horcruxes",
                        "Harry Potter": "Shared crucial memory with"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Gives Harry the true memory of telling Tom Riddle about Horcruxes, revealing Voldemort's plan for seven.",
                    "role": "Professor, Memory provider",
                    "relationships": {
                        "Harry Potter": "Provided crucial information",
                        "Albus Dumbledore": "Helped understand Voldemort"
                    }
                }
            }
        },
        "tom-riddle": {
            "name": "Tom Marvolo Riddle",
            "aliases": ["Lord Voldemort", "Young Voldemort"],
            "appearances": [10, 13, 17, 20, 23],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Eleven-year-old boy at Wool's Orphanage, already showing signs of cruelty and magical ability.",
                    "role": "Orphan, Future dark wizard",
                    "relationships": {
                        "Mrs. Cole": "Orphanage matron",
                        "Albus Dumbledore": "Visited by"
                    }
                },
                "13": {
                    "revealedIn": 13,
                    "description": "Hogwarts student charming teachers but secretly opening the Chamber of Secrets and framing Hagrid.",
                    "role": "Student, Hidden monster",
                    "relationships": {
                        "Horace Slughorn": "Favored by",
                        "Rubeus Hagrid": "Framed for Chamber opening"
                    }
                },
                "17": {
                    "revealedIn": 17,
                    "description": "Learns about Horcruxes from Slughorn and begins planning to split his soul for immortality.",
                    "role": "Student, Horcrux researcher",
                    "relationships": {
                        "Horace Slughorn": "Learned about Horcruxes from"
                    }
                },
                "20": {
                    "revealedIn": 20,
                    "description": "Returns to Hogwarts years later as an adult, asking Dumbledore for the Defense Against the Dark Arts position.",
                    "role": "Job applicant, Dark wizard",
                    "relationships": {
                        "Albus Dumbledore": "Refused job by"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Revealed to have created multiple Horcruxes, splitting his soul into seven pieces to become immortal.",
                    "role": "Dark Lord, Horcrux creator",
                    "relationships": {
                        "Horcruxes": "Created multiple",
                        "Harry Potter": "Final Horcrux to be destroyed"
                    }
                }
            }
        },
        "ginny-weasley": {
            "name": "Ginny Weasley",
            "aliases": ["Ginny"],
            "appearances": [5, 6, 14, 18, 24, 25, 30],
            "knowledge": {
                "14": {
                    "revealedIn": 14,
                    "description": "Fifth-year student dating Dean Thomas but clearly still has feelings for Harry.",
                    "role": "Fifth-year student",
                    "relationships": {
                        "Dean Thomas": "Dating",
                        "Harry Potter": "Still interested in"
                    }
                },
                "24": {
                    "revealedIn": 24,
                    "description": "Finally gets together with Harry after a Quidditch victory. Their relationship becomes serious quickly.",
                    "role": "Student, Harry's girlfriend",
                    "relationships": {
                        "Harry Potter": "Girlfriend of",
                        "Dean Thomas": "Broke up with"
                    }
                },
                "30": {
                    "revealedIn": 30,
                    "description": "Heartbroken when Harry breaks up with her to protect her from Voldemort's vengeance.",
                    "role": "Student, Ex-girlfriend",
                    "relationships": {
                        "Harry Potter": "Broken up with for safety"
                    }
                }
            }
        },
        "narcissa-malfoy": {
            "name": "Narcissa Malfoy",
            "aliases": ["Narcissa Black"],
            "appearances": [2],
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Draco's mother, desperate to protect her son from Voldemort's dangerous mission. Makes Snape vow to help.",
                    "role": "Mother, Vow seeker",
                    "relationships": {
                        "Draco Malfoy": "Mother (desperately protecting)",
                        "Severus Snape": "Made Unbreakable Vow with",
                        "Bellatrix Lestrange": "Sister",
                        "Lucius Malfoy": "Wife of (imprisoned)"
                    }
                }
            }
        },
        "bellatrix-lestrange": {
            "name": "Bellatrix Lestrange",
            "aliases": ["Bellatrix Black"],
            "appearances": [2, 29],
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Death Eater and Narcissa's sister, suspicious of Snape's loyalty to Voldemort.",
                    "role": "Death Eater, Sister",
                    "relationships": {
                        "Narcissa Malfoy": "Sister (supporting)",
                        "Severus Snape": "Suspicious of",
                        "Voldemort": "Devoted follower"
                    }
                },
                "29": {
                    "revealedIn": 29,
                    "description": "Among the Death Eaters who infiltrate Hogwarts. Witnesses Snape killing Dumbledore.",
                    "role": "Death Eater, Invader",
                    "relationships": {
                        "Death Eaters": "Leading invasion with",
                        "Albus Dumbledore": "Witnessed murder of"
                    }
                }
            }
        },
        "ron-weasley": {
            "name": "Ron Weasley",
            "aliases": ["Ron"],
            "appearances": [5, 6, 7, 11, 14, 15, 18, 19, 21, 24, 29, 30],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Sixth-year student struggling in Potions while Harry excels with the Prince's book. Feeling overshadowed.",
                    "role": "Sixth-year student",
                    "relationships": {
                        "Harry Potter": "Best friend (feeling inferior to)",
                        "Hermione Granger": "Friend"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Poisoned by mead intended for Dumbledore. Saved by Harry's quick thinking with a bezoar.",
                    "role": "Student, Poison victim",
                    "relationships": {
                        "Harry Potter": "Life saved by",
                        "Draco Malfoy": "Poisoned by (indirectly)"
                    }
                },
                "18": {
                    "revealedIn": 18,
                    "description": "Dating Lavender Brown but still has feelings for Hermione, causing romantic tension.",
                    "role": "Student, Confused boyfriend",
                    "relationships": {
                        "Lavender Brown": "Dating",
                        "Hermione Granger": "Really in love with"
                    }
                }
            }
        },
        "hermione-granger": {
            "name": "Hermione Granger",
            "aliases": ["Hermione"],
            "appearances": [5, 6, 7, 9, 11, 14, 15, 18, 19, 21, 24, 29, 30],
            "knowledge": {
                "9": {
                    "revealedIn": 9,
                    "description": "Suspicious of Harry's sudden success in Potions. Correctly suspects he's getting help from somewhere.",
                    "role": "Sixth-year student, Investigator",
                    "relationships": {
                        "Harry Potter": "Suspicious of success",
                        "Half-Blood Prince": "Trying to identify"
                    }
                },
                "18": {
                    "revealedIn": 18,
                    "description": "Jealous of Ron's relationship with Lavender Brown. Attacks Ron with birds when upset.",
                    "role": "Student, Jealous friend",
                    "relationships": {
                        "Ron Weasley": "In love with but fighting",
                        "Lavender Brown": "Rival for Ron's affections"
                    }
                },
                "29": {
                    "revealedIn": 29,
                    "description": "Fights Death Eaters during the invasion of Hogwarts. Shows her loyalty and bravery.",
                    "role": "Student, Fighter",
                    "relationships": {
                        "Death Eaters": "Fighting against",
                        "Order of the Phoenix": "Fighting with"
                    }
                }
            }
        }
    }

def main():
    # Read the existing file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/half-blood-prince.json', 'r') as f:
        data = json.load(f)
    
    # Update schema version and add characters
    data["meta"]["schemaVersion"] = "2.0"
    data["characters"] = create_hbp_characters()
    
    # Write back to file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/half-blood-prince.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Successfully filled Half-Blood Prince with character data")
    print(f"Added {len(data['characters'])} characters")

if __name__ == "__main__":
    main()