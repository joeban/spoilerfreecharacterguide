#!/usr/bin/env python3
import json

# Load existing data
with open('data/witcher/lady-of-the-lake.json', 'r') as f:
    data = json.load(f)

# Add new characters for Lady of the Lake
new_characters = {
    "sir-kay": {
        "name": "Sir Kay",
        "aliases": ["The Seneschal"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Arthur's seneschal and foster brother, one of the earliest knights of the Round Table. Known for his administrative duties and sometimes sharp tongue.",
                "role": "Seneschal of Camelot",
                "relationships": {
                    "King Arthur": "Foster brother and seneschal",
                    "Round Table": "Knight of"
                }
            }
        }
    },
    "sir-bors": {
        "name": "Sir Bors",
        "aliases": ["Bors the Younger"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "One of the three Grail knights alongside Galahad and Percival. Known for his piety and determination in the quest for spiritual perfection.",
                "role": "Grail knight",
                "relationships": {
                    "Galahad": "Fellow Grail knight",
                    "Percival": "Quest companion"
                }
            }
        }
    },
    "sir-gawain": {
        "name": "Sir Gawain",
        "aliases": ["The Knight of the Sun"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Arthur's nephew and one of the strongest knights, whose power waxes and wanes with the sun. A fierce warrior with a complex personality.",
                "role": "Solar knight",
                "relationships": {
                    "King Arthur": "Nephew of",
                    "Knights of Round Table": "Senior member of"
                }
            }
        }
    },
    "sir-tristan": {
        "name": "Sir Tristan",
        "aliases": ["The Knight of Lyonesse"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "A knight renowned for his tragic love story with Isolde and his skill in music and combat. Represents the romantic ideals of chivalry.",
                "role": "Romantic knight",
                "relationships": {
                    "Isolde": "Tragic love for",
                    "Round Table": "Honored member of"
                }
            }
        }
    },
    "sir-gareth": {
        "name": "Sir Gareth",
        "aliases": ["The Youngest Knight"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Gawain's youngest brother, known for his courtesy and gentle nature. Represents the idealistic youth among Arthur's knights.",
                "role": "Courteous knight",
                "relationships": {
                    "Sir Gawain": "Younger brother of",
                    "Round Table": "Gentle member of"
                }
            }
        }
    },
    "sir-gaheris": {
        "name": "Sir Gaheris",
        "aliases": ["The Middle Brother"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Another of Gawain's brothers, a capable knight who serves Arthur loyally. Known for his steady nature and combat skills.",
                "role": "Loyal knight",
                "relationships": {
                    "Sir Gawain": "Brother of",
                    "King Arthur": "Faithful to"
                }
            }
        }
    },
    "sir-bedivere": {
        "name": "Sir Bedivere",
        "aliases": ["The One-Handed"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "One of Arthur's oldest and most trusted companions, present from the very beginning. Known for his unwavering loyalty.",
                "role": "Arthur's companion",
                "relationships": {
                    "King Arthur": "Oldest companion of",
                    "Excalibur": "Tasked with returning"
                }
            }
        }
    },
    "sir-lucan": {
        "name": "Sir Lucan",
        "aliases": ["The Butler"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Arthur's butler and one of his most faithful retainers. Serves both in combat and in maintaining the royal household.",
                "role": "Royal butler",
                "relationships": {
                    "King Arthur": "Butler and knight to",
                    "Camelot": "Manages household of"
                }
            }
        }
    },
    "queen-guinevere": {
        "name": "Queen Guinevere",
        "aliases": ["Gwenhwyfar"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Arthur's queen, whose relationship with Lancelot creates the greatest tragedy of Camelot. Represents both the highest ideals and deepest flaws of courtly love.",
                "role": "Queen of Camelot",
                "relationships": {
                    "King Arthur": "Queen and wife of",
                    "Sir Lancelot": "Forbidden love with"
                }
            }
        }
    },
    "morgana-le-fay": {
        "name": "Morgana le Fay",
        "aliases": ["Morgan", "The Sorceress"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Arthur's half-sister and a powerful sorceress. Represents the magical opposition to Arthur's reign and the old ways conflicting with the new.",
                "role": "Antagonistic sorceress",
                "relationships": {
                    "King Arthur": "Half-sister and enemy of",
                    "Merlin": "Magical rival of"
                }
            }
        }
    },
    "mordred": {
        "name": "Mordred",
        "aliases": ["The Traitor Knight"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "Arthur's son and destroyer, representing the ultimate betrayal and the cyclical nature of heroic tragedy. His presence foreshadows the fall of Camelot.",
                "role": "Traitorous son",
                "relationships": {
                    "King Arthur": "Son and destroyer of",
                    "Camelot": "Brings downfall to"
                }
            }
        }
    },
    "lady-of-the-lake-original": {
        "name": "The Original Lady of the Lake",
        "aliases": ["Viviane"],
        "appearances": [10, 11],
        "knowledge": {
            "10": {
                "revealedIn": 10,
                "description": "The mystical figure who gave Arthur Excalibur and represents the connection between the mortal world and the realm of magic and legend.",
                "role": "Mystical guardian",
                "relationships": {
                    "Excalibur": "Guardian of",
                    "Ciri": "Role passed to"
                }
            }
        }
    },
    "battle-of-brenna-commander-voorhis": {
        "name": "General Voorhis",
        "aliases": ["The Strategic Commander"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A Nilfgaardian general who played a crucial role in the Battle of Brenna. His tactical decisions shaped the outcome of the war.",
                "role": "Military commander",
                "relationships": {
                    "Emperor Emhyr": "Serves loyally",
                    "Nilfgaardian Army": "Commands"
                }
            }
        }
    },
    "battle-of-brenna-field-surgeon": {
        "name": "Dr. Marti Marova",
        "aliases": ["The Field Surgeon"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A battlefield surgeon who saved countless lives during the Battle of Brenna, representing the healers who work behind the scenes of war.",
                "role": "Military surgeon",
                "relationships": {
                    "Wounded Soldiers": "Heals",
                    "Medical Corps": "Leads"
                }
            }
        }
    },
    "battle-of-brenna-cavalry-captain": {
        "name": "Captain Vreemde",
        "aliases": ["The Cavalry Officer"],
        "appearances": [1, 2, 3],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A cavalry captain who led mounted charges during the Battle of Brenna, demonstrating exceptional courage under fire.",
                "role": "Cavalry commander",
                "relationships": {
                    "Horse Units": "Commands",
                    "Battle Lines": "Breaks enemy"
                }
            }
        }
    },
    "rivian-pogrom-city-guard": {
        "name": "Guard Captain Novigrad",
        "aliases": ["The City Protector"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "A city guard captain who tried to maintain order during the pogrom in Rivia, representing those who stood against the mob violence.",
                "role": "City guard captain",
                "relationships": {
                    "Rivia Citizens": "Protects",
                    "Civil Order": "Maintains"
                }
            }
        }
    },
    "rivian-pogrom-mob-leader": {
        "name": "Mob Leader Caldemeyn",
        "aliases": ["The Inciter"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "A leader of the anti-nonhuman riots in Rivia who stirred up hatred and violence against elves and dwarves.",
                "role": "Riot instigator",
                "relationships": {
                    "Rioters": "Leads",
                    "Nonhuman Citizens": "Incites violence against"
                }
            }
        }
    },
    "rivian-pogrom-victim-elder": {
        "name": "Elder Yaevinn",
        "aliases": ["The Elven Elder"],
        "appearances": [8, 11],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "An elderly elf who becomes a victim of the pogrom in Rivia, representing the innocent casualties of racial hatred.",
                "role": "Pogrom victim",
                "relationships": {
                    "Elven Community": "Respected elder of",
                    "Rioters": "Victim of"
                }
            }
        }
    }
}

# Add characters to existing data
for char_id, char_data in new_characters.items():
    data['characters'][char_id] = char_data

print(f"Adding {len(new_characters)} characters to Lady of the Lake")
print(f"New total: {len(data['characters'])} characters")

# Save updated data
with open('data/witcher/lady-of-the-lake.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✅ Lady of the Lake updated successfully!")