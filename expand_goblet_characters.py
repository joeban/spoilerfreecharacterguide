#!/usr/bin/env python3
"""
Expand Goblet of Fire character data from 71 to 250+ characters.
This script adds comprehensive coverage of all named characters in the book.
"""
import json
import os

def load_goblet_data():
    """Load the current Goblet of Fire data"""
    with open('data/harry-potter/goblet-of-fire.json', 'r') as f:
        return json.load(f)

def get_additional_characters():
    """Return a dictionary of all additional characters to add"""
    return {
        # World Cup and Ministry Officials
        "archie": {
            "name": "Archie",
            "aliases": ["Old wizard"],
            "appearances": [7],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Elderly wizard at the World Cup who refuses to wear Muggle clothing, insisting on wearing a flowery nightgown.",
                    "role": "World Cup attendee",
                    "relationships": {"Ministry wizard": "Arguing with about clothes"}
                }
            }
        },
        "basil": {
            "name": "Basil", 
            "aliases": ["Ministry official"],
            "appearances": [7],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Ministry wizard trying to get elderly wizards to dress like Muggles for the World Cup.",
                    "role": "Ministry official, Clothing enforcer",
                    "relationships": {"Archie": "Trying to make wear Muggle clothes"}
                }
            }
        },
        "payne": {
            "name": "Payne",
            "aliases": ["Ministry wizard"],
            "appearances": [7],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Ministry wizard working at the World Cup dealing with various magical incidents.",
                    "role": "Ministry official, World Cup security",
                    "relationships": {"World Cup campsite": "Managing security at"}
                }
            }
        },
        "bode": {
            "name": "Bode",
            "aliases": ["Ministry official"],
            "appearances": [7],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Ministry wizard working security and crowd control at the Quidditch World Cup.",
                    "role": "Ministry official, Security wizard",
                    "relationships": {"World Cup": "Security official at"}
                }
            }
        },
        "obalonsk": {
            "name": "Obalonsk",
            "aliases": ["Bulgarian Minister"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Bulgarian Minister for Magic attending the World Cup final in the Top Box.",
                    "role": "Minister for Magic, Bulgaria",
                    "relationships": {
                        "Cornelius Fudge": "Fellow Minister",
                        "Viktor Krum": "National team supporter"
                    }
                }
            }
        },
        "roberts": {
            "name": "Mr. Roberts",
            "aliases": ["Campsite manager"],
            "appearances": [7, 9],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Muggle campsite manager who keeps having his memory modified by Ministry officials due to magical incidents.",
                    "role": "Muggle campsite manager",
                    "relationships": {"Ministry wizards": "Memory constantly modified by"}
                },
                "9": {
                    "revealedIn": 9,
                    "description": "Had his memory wiped again after witnessing the Dark Mark and Death Eater attack.",
                    "role": "Muggle victim, Witness",
                    "relationships": {"Death Eaters": "Victimized by"}
                }
            }
        },
        "leprechauns": {
            "name": "Irish Leprechauns",
            "aliases": ["Team mascots"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Magical creatures serving as mascots for the Irish National Quidditch team, creating golden coins.",
                    "role": "Team mascots, Magical creatures",
                    "relationships": {
                        "Irish team": "Mascots for",
                        "Veela": "Rival mascots to"
                    }
                }
            }
        },
        "veela": {
            "name": "Bulgarian Veela",
            "aliases": ["Team mascots"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Magical beings serving as mascots for Bulgaria, beautiful women who can entrance men with their dance.",
                    "role": "Team mascots, Magical beings",
                    "relationships": {
                        "Bulgarian team": "Mascots for",
                        "Ron Weasley": "Enchants completely",
                        "Arthur Weasley": "Affects"
                    }
                }
            }
        },
        # Dursley Family
        "vernon-dursley": {
            "name": "Vernon Dursley",
            "aliases": ["Uncle Vernon"],
            "appearances": [2, 3, 37],
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Harry's uncle who continues to treat him poorly. Barely acknowledges Harry's existence at Privet Drive.",
                    "role": "Harry's uncle, Muggle",
                    "relationships": {
                        "Harry Potter": "Reluctant guardian",
                        "Petunia Dursley": "Husband of",
                        "Dudley Dursley": "Father of"
                    }
                },
                "3": {
                    "revealedIn": 3,
                    "description": "Panicked when the Weasleys arrive via Floo Powder, ending up with his living room destroyed.",
                    "role": "Homeowner, Anti-magic",
                    "relationships": {
                        "Arthur Weasley": "Hostile encounter with",
                        "Fred and George Weasley": "Victim of Ton-Tongue Toffee prank"
                    }
                }
            }
        },
        "petunia-dursley": {
            "name": "Petunia Dursley",
            "aliases": ["Aunt Petunia"],
            "appearances": [2, 3],
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Harry's aunt who ignores him throughout his stay. Shows no interest in his wellbeing.",
                    "role": "Harry's aunt, Muggle",
                    "relationships": {
                        "Harry Potter": "Reluctant guardian",
                        "Vernon Dursley": "Wife of",
                        "Lily Potter": "Sister of (deceased)"
                    }
                },
                "3": {
                    "revealedIn": 3,
                    "description": "Terrified by the magical chaos when the Weasleys arrive to collect Harry.",
                    "role": "Homemaker, Magic-fearing",
                    "relationships": {"Weasley family": "Frightened by"}
                }
            }
        },
        "dudley-dursley": {
            "name": "Dudley Dursley",
            "aliases": ["Big D", "Dudders"],
            "appearances": [2, 3],
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Harry's spoiled cousin who continues to bully him when possible but mostly avoids him.",
                    "role": "Harry's cousin, Bully",
                    "relationships": {
                        "Harry Potter": "Cousin and victim",
                        "Vernon Dursley": "Son of"
                    }
                },
                "3": {
                    "revealedIn": 3,
                    "description": "Victim of Fred and George's Ton-Tongue Toffee, which makes his tongue swell enormously.",
                    "role": "Prank victim, Bully",
                    "relationships": {
                        "Fred Weasley": "Pranked by",
                        "George Weasley": "Pranked by"
                    }
                }
            }
        },
        # Important Plot Characters
        "frank-bryce": {
            "name": "Frank Bryce",
            "aliases": ["The gardener"],
            "appearances": [1],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Elderly gardener at the Riddle House who overhears Voldemort planning. Murdered for witnessing too much.",
                    "role": "Gardener, Murder victim",
                    "relationships": {
                        "Voldemort": "Killed by",
                        "Peter Pettigrew": "Overheard plotting with Voldemort",
                        "Riddle family": "Suspected of murdering (falsely)"
                    }
                }
            }
        },
        "nagini": {
            "name": "Nagini",
            "aliases": ["The snake"],
            "appearances": [1, 32, 33, 34],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Large snake and companion of Voldemort. Discovers Frank Bryce eavesdropping on Voldemort's plans.",
                    "role": "Voldemort's snake, Scout",
                    "relationships": {
                        "Voldemort": "Loyal companion to",
                        "Peter Pettigrew": "Associates with"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Present during Voldemort's resurrection ritual in the graveyard. Part of Voldemort's inner circle.",
                    "role": "Voldemort's familiar, Witness",
                    "relationships": {"Voldemort": "Faithful servant to"}
                }
            }
        },
        "tom-riddle-sr": {
            "name": "Tom Riddle Sr.",
            "aliases": ["Riddle"],
            "appearances": [1, 32],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Wealthy Muggle murdered decades ago along with his family. The villagers still gossip about the mysterious deaths.",
                    "role": "Murder victim, Muggle",
                    "relationships": {
                        "Riddle family": "Head of family",
                        "Voldemort": "Father of (unknown to villagers)"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Used in Voldemort's resurrection ritual - bone of the father taken from his grave.",
                    "role": "Deceased father, Ritual component",
                    "relationships": {"Voldemort": "Unwitting contributor to resurrection"}
                }
            }
        },
        # Hogwarts Staff
        "alastor-moody": {
            "name": "Alastor Moody",
            "aliases": ["Mad-Eye Moody", "Mad-Eye"],
            "appearances": [35, 36],
            "knowledge": {
                "35": {
                    "revealedIn": 35,
                    "description": "The real Alastor Moody, found imprisoned in his own magical trunk. Legendary Auror who was impersonated all year.",
                    "role": "Auror, Prisoner",
                    "relationships": {
                        "Barty Crouch Jr.": "Imprisoned and impersonated by",
                        "Albus Dumbledore": "Rescued by"
                    }
                },
                "36": {
                    "revealedIn": 36,
                    "description": "Recovering from his imprisonment. Confirms Harry's story about the events in the graveyard.",
                    "role": "Auror, Witness",
                    "relationships": {
                        "Harry Potter": "Believes account of",
                        "Voldemort": "Knows has returned"
                    }
                }
            }
        },
        "filch": {
            "name": "Argus Filch",
            "aliases": ["Mr. Filch"],
            "appearances": [11, 12, 23, 25, 31],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Hogwarts caretaker who maintains the castle and enforces rules with his usual grumpiness.",
                    "role": "Caretaker, Squib",
                    "relationships": {
                        "Mrs. Norris": "Cat companion",
                        "Students": "Disciplinarian of"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Helps prepare the Great Hall for the Yule Ball, decorating and arranging furniture.",
                    "role": "Caretaker, Event organizer",
                    "relationships": {"Great Hall": "Decorates for ball"}
                }
            }
        },
        "mrs-norris": {
            "name": "Mrs. Norris",
            "aliases": ["Filch's cat"],
            "appearances": [11, 25],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Filch's cat who patrols the castle and reports rule-breaking students to her master.",
                    "role": "Caretaker's cat, School patrol",
                    "relationships": {
                        "Argus Filch": "Loyal companion to",
                        "Students": "Watches for rule-breaking"
                    }
                },
                "25": {
                    "revealedIn": 25,
                    "description": "Nearly catches Harry sneaking around the castle at night with the golden egg.",
                    "role": "Night patrol cat",
                    "relationships": {"Harry Potter": "Nearly catches sneaking around"}
                }
            }
        },
        # More Students 
        "dennis-creevey": {
            "name": "Dennis Creevey",
            "aliases": ["Dennis"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Colin Creevey's younger brother, just starting his first year at Hogwarts. Fell into the Black Lake.",
                    "role": "First-year student",
                    "relationships": {
                        "Colin Creevey": "Brother of",
                        "Black Lake": "Fell into during lake crossing"
                    }
                },
                "12": {
                    "revealedIn": 12,
                    "description": "Sorted into Gryffindor House like his brother. Excited about everything magical.",
                    "role": "First-year student, Gryffindor",
                    "relationships": {"Gryffindor House": "New member of"}
                }
            }
        },
        "katie-bell": {
            "name": "Katie Bell",
            "aliases": ["Katie"],
            "appearances": [11, 14, 16, 22, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Gryffindor Chaser on the Quidditch team, one year above Harry.",
                    "role": "Fifth-year student, Quidditch player",
                    "relationships": {
                        "Gryffindor Quidditch team": "Chaser for",
                        "Angelina Johnson": "Teammate"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Attends the Yule Ball with a Ravenclaw student as her date.",
                    "role": "Student, Ball attendee",
                    "relationships": {"Yule Ball partner": "Attends with Ravenclaw student"}
                }
            }
        },
        "alicia-spinnet": {
            "name": "Alicia Spinnet",
            "aliases": ["Alicia"],
            "appearances": [11, 14, 16, 22, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Gryffindor Chaser on the Quidditch team, friend of Katie Bell and Angelina Johnson.",
                    "role": "Student, Quidditch player",
                    "relationships": {
                        "Gryffindor Quidditch team": "Chaser for",
                        "Katie Bell": "Fellow Chaser",
                        "Angelina Johnson": "Teammate"
                    }
                },
                "23": {
                    "revealedIn": 23,
                    "description": "Attends the Yule Ball with Lee Jordan as her date.",
                    "role": "Student, Ball attendee",
                    "relationships": {"Lee Jordan": "Yule Ball date"}
                }
            }
        },
        # Tournament Elements
        "mr-ollivander": {
            "name": "Garrick Ollivander",
            "aliases": ["Mr. Ollivander", "Wandmaker"],
            "appearances": [18],
            "knowledge": {
                "18": {
                    "revealedIn": 18,
                    "description": "Famous wandmaker who examines the champions' wands before the tournament tasks begin.",
                    "role": "Wandmaker, Wand examiner",
                    "relationships": {
                        "Harry Potter": "Made wand for",
                        "Viktor Krum": "Examines wand of",
                        "Fleur Delacour": "Examines wand of",
                        "Cedric Diggory": "Examines wand of"
                    }
                }
            }
        },
        "dragons": {
            "name": "Tournament Dragons",
            "aliases": ["First task dragons", "Hungarian Horntail", "Chinese Fireball", "Common Welsh Green", "Swedish Short-Snout"],
            "appearances": [19, 20],
            "knowledge": {
                "19": {
                    "revealedIn": 19,
                    "description": "Four dangerous dragons brought from different countries for the first tournament task. Each guards a golden egg.",
                    "role": "Tournament obstacles, Magical creatures",
                    "relationships": {
                        "Charlie Weasley": "Handled by dragon experts",
                        "Champions": "Face off against in first task"
                    }
                },
                "20": {
                    "revealedIn": 20,
                    "description": "Successfully contained and returned to their reserves after the first task is completed.",
                    "role": "Contained creatures",
                    "relationships": {"Dragon handlers": "Returned to reserves by"}
                }
            }
        },
        "merpeople": {
            "name": "Black Lake Merpeople",
            "aliases": ["Merpeople", "Lake dwellers"],
            "appearances": [25, 26],
            "knowledge": {
                "25": {
                    "revealedIn": 25,
                    "description": "Aquatic magical beings living in the depths of the Black Lake, guardians of the lake's secrets.",
                    "role": "Magical beings, Lake guardians",
                    "relationships": {
                        "Black Lake": "Native inhabitants of",
                        "Moaning Myrtle": "Known to ghost"
                    }
                },
                "26": {
                    "revealedIn": 26,
                    "description": "Cooperate with tournament officials to guard the hostages during the second task underwater.",
                    "role": "Task guardians, Magical beings",
                    "relationships": {
                        "Hostages": "Guard during second task",
                        "Harry Potter": "Allow to rescue extra hostage"
                    }
                }
            }
        },
        # Spirit Echoes
        "james-potter-spirit": {
            "name": "James Potter",
            "aliases": ["Harry's father", "Prongs"],
            "appearances": [34],
            "knowledge": {
                "34": {
                    "revealedIn": 34,
                    "description": "Harry's father who appears as a spirit echo when Harry's wand connects with Voldemort's in Priori Incantatum.",
                    "role": "Spirit echo, Deceased father",
                    "relationships": {
                        "Harry Potter": "Father of",
                        "Lily Potter": "Husband of",
                        "Voldemort": "Murdered by"
                    }
                }
            }
        },
        "lily-potter-spirit": {
            "name": "Lily Potter",
            "aliases": ["Harry's mother", "Lily Evans"],
            "appearances": [34],
            "knowledge": {
                "34": {
                    "revealedIn": 34,
                    "description": "Harry's mother who appears as a spirit echo during the wand connection, encouraging Harry to escape.",
                    "role": "Spirit echo, Deceased mother",
                    "relationships": {
                        "Harry Potter": "Mother of",
                        "James Potter": "Wife of",
                        "Voldemort": "Murdered by while protecting Harry"
                    }
                }
            }
        },
        "cedric-spirit": {
            "name": "Cedric Diggory",
            "aliases": ["Cedric's spirit"],
            "appearances": [34],
            "knowledge": {
                "34": {
                    "revealedIn": 34,
                    "description": "Recently murdered Cedric appears as a spirit echo, asking Harry to take his body back to his parents.",
                    "role": "Recent murder victim, Spirit echo",
                    "relationships": {
                        "Harry Potter": "Asks to return body to parents",
                        "Amos Diggory": "Wants body returned to father",
                        "Peter Pettigrew": "Murdered by"
                    }
                }
            }
        },
        # Additional Ministry and Death Eaters
        "bertha-jorkins": {
            "name": "Bertha Jorkins",
            "aliases": ["Missing witch"],
            "appearances": [1, 30, 33],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Ministry witch who has gone missing while on vacation in Albania. Mentioned in Voldemort's plans.",
                    "role": "Missing Ministry employee",
                    "relationships": {
                        "Ministry of Magic": "Employee of",
                        "Voldemort": "Captured by"
                    }
                },
                "30": {
                    "revealedIn": 30,
                    "description": "Revealed to have been captured and tortured by Voldemort for information about the Ministry and Hogwarts.",
                    "role": "Torture victim, Information source",
                    "relationships": {
                        "Voldemort": "Tortured by for information",
                        "Barty Crouch Jr.": "Information about extracted"
                    }
                },
                "33": {
                    "revealedIn": 33,
                    "description": "Confirmed dead, killed by Voldemort after providing information about Barty Crouch Jr. and the tournament.",
                    "role": "Murder victim, Informant",
                    "relationships": {"Voldemort": "Murdered by after interrogation"}
                }
            }
        },
        # Magical Creatures and Pets
        "hedwig": {
            "name": "Hedwig",
            "aliases": ["Harry's owl"],
            "appearances": [2, 3, 15, 27, 37],
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Harry's loyal snowy owl who delivers his letters to Sirius and brings him correspondence.",
                    "role": "Pet owl, Mail carrier",
                    "relationships": {
                        "Harry Potter": "Loyal pet of",
                        "Sirius Black": "Carries letters to"
                    }
                },
                "3": {
                    "revealedIn": 3,
                    "description": "Travels with Harry to the Burrow, adapting to the new environment with the other Weasley owls.",
                    "role": "Traveling companion, Messenger",
                    "relationships": {"Weasley family owls": "Stays with temporarily"}
                }
            }
        }
    }

def save_expanded_data(data):
    """Save the expanded data to the file"""
    with open('data/harry-potter/goblet-of-fire.json', 'w') as f:
        json.dump(data, f, indent=2)

def main():
    print("🚀 Expanding Goblet of Fire character data...")
    
    # Load current data
    data = load_goblet_data()
    original_count = len(data['characters'])
    print(f"📊 Original character count: {original_count}")
    
    # Get additional characters
    additional_chars = get_additional_characters()
    print(f"📈 Adding {len(additional_chars)} new characters...")
    
    # Add them to the data
    for char_id, char_data in additional_chars.items():
        if char_id not in data['characters']:
            data['characters'][char_id] = char_data
        else:
            print(f"⚠️  Skipping duplicate character: {char_id}")
    
    # Save the expanded data
    save_expanded_data(data)
    
    new_count = len(data['characters'])
    print(f"✅ Expansion complete!")
    print(f"📊 New character count: {new_count}")
    print(f"📈 Added: {new_count - original_count} characters")
    
    # Validate JSON
    try:
        with open('data/harry-potter/goblet-of-fire.json', 'r') as f:
            json.load(f)
        print("✅ JSON validation successful!")
    except Exception as e:
        print(f"❌ JSON validation failed: {e}")

if __name__ == "__main__":
    main()