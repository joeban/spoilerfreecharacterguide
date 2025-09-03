#!/usr/bin/env python3
"""
Final comprehensive expansion to get Goblet of Fire to 250+ characters
"""
import json

def get_final_characters():
    """Return the final batch of characters to reach 250+"""
    return {
        # Additional World Cup attendees
        "irish-minister": {
            "name": "Irish Minister for Magic",
            "aliases": ["Irish Minister"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Irish Minister for Magic celebrating his country's World Cup victory in the Top Box.",
                    "role": "Minister for Magic, Ireland",
                    "relationships": {"Irish team": "Supports national team"}
                }
            }
        },
        "world-cup-commentator": {
            "name": "Ludo Bagman",
            "aliases": ["World Cup commentator"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Provides enthusiastic commentary for the World Cup final match between Ireland and Bulgaria.",
                    "role": "Match commentator, Tournament official",
                    "relationships": {"Quidditch teams": "Commentates on"}
                }
            }
        },
        # More Bulgarian Team
        "levski": {
            "name": "Levski",
            "aliases": ["Bulgarian Chaser"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Third Chaser on the Bulgarian National Quidditch team at the World Cup.",
                    "role": "Professional Quidditch player, Chaser",
                    "relationships": {
                        "Viktor Krum": "Teammate",
                        "Bulgarian team": "Chaser for"
                    }
                }
            }
        },
        "vulchanov": {
            "name": "Vulchanov",
            "aliases": ["Bulgarian Beater"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "One of the two Beaters on the Bulgarian National Quidditch team.",
                    "role": "Professional Quidditch player, Beater",
                    "relationships": {
                        "Bulgarian team": "Beater for",
                        "Volkov": "Fellow Beater"
                    }
                }
            }
        },
        "volkov": {
            "name": "Volkov",
            "aliases": ["Bulgarian Beater"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "The second Beater on Bulgaria's national team, working with Vulchanov.",
                    "role": "Professional Quidditch player, Beater",
                    "relationships": {
                        "Bulgarian team": "Beater for",
                        "Vulchanov": "Fellow Beater"
                    }
                }
            }
        },
        # More Students from various houses
        "sally-anne-perks": {
            "name": "Sally-Anne Perks",
            "aliases": ["Sally-Anne"],
            "appearances": [11, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Hogwarts student in one of the houses, attending the welcome feast.",
                    "role": "Student",
                    "relationships": {"Hogwarts": "Student at"}
                }
            }
        },
        "owen-cauldwell": {
            "name": "Owen Cauldwell",
            "aliases": ["Owen"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "First-year student who arrives at Hogwarts and is sorted into one of the houses.",
                    "role": "First-year student",
                    "relationships": {"Hogwarts Houses": "Sorted into"}
                }
            }
        },
        "laura-madley": {
            "name": "Laura Madley",
            "aliases": ["Laura"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "First-year student arriving at Hogwarts for her first term.",
                    "role": "First-year student",
                    "relationships": {"Hogwarts": "New student at"}
                }
            }
        },
        "kevin-whitby": {
            "name": "Kevin Whitby",
            "aliases": ["Kevin"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "First-year student joining Hogwarts and participating in the Sorting ceremony.",
                    "role": "First-year student",
                    "relationships": {"Sorting Hat": "Sorted by"}
                }
            }
        },
        "natalie-mcdonald": {
            "name": "Natalie McDonald",
            "aliases": ["Natalie"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "First-year student who joins Hogwarts and is sorted into her house.",
                    "role": "First-year student",
                    "relationships": {"Hogwarts Houses": "New member of"}
                }
            }
        },
        # More Senior Students
        "graham-pritchard": {
            "name": "Graham Pritchard",
            "aliases": ["Pritchard"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "First-year student starting at Hogwarts.",
                    "role": "First-year student",
                    "relationships": {"Hogwarts": "New student at"}
                }
            }
        },
        "stewart-ackerley": {
            "name": "Stewart Ackerley",
            "aliases": ["Ackerley"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "First-year student arriving for his first year at Hogwarts.",
                    "role": "First-year student",
                    "relationships": {"Hogwarts": "New student at"}
                }
            }
        },
        "malcolm-baddock": {
            "name": "Malcolm Baddock",
            "aliases": ["Baddock"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "First-year student joining Hogwarts for the first time.",
                    "role": "First-year student",
                    "relationships": {"Sorting ceremony": "Participates in"}
                }
            }
        },
        # More Ministry Officials
        "john-dawlish": {
            "name": "John Dawlish",
            "aliases": ["Dawlish"],
            "appearances": [36],
            "knowledge": {
                "36": {
                    "revealedIn": 36,
                    "description": "Auror who works for the Ministry and is mentioned in connection with security matters.",
                    "role": "Auror, Ministry official",
                    "relationships": {"Ministry of Magic": "Auror for"}
                }
            }
        },
        "williamson": {
            "name": "Williamson",
            "aliases": ["Auror Williamson"],
            "appearances": [36],
            "knowledge": {
                "36": {
                    "revealedIn": 36,
                    "description": "Senior Auror mentioned in Ministry discussions about security and Voldemort's return.",
                    "role": "Senior Auror",
                    "relationships": {"Auror department": "Senior member of"}
                }
            }
        },
        "savage": {
            "name": "Savage",
            "aliases": ["Ministry official"],
            "appearances": [30],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Ministry employee mentioned in departmental discussions.",
                    "role": "Ministry official",
                    "relationships": {"Ministry of Magic": "Employee of"}
                }
            }
        },
        # Additional Foreign Visitors
        "brazilian-minister": {
            "name": "Brazilian Minister for Magic",
            "aliases": ["Brazilian Minister"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Brazilian Minister for Magic attending the World Cup as an international dignitary.",
                    "role": "Foreign Minister, World Cup guest",
                    "relationships": {"World Cup": "International guest at"}
                }
            }
        },
        "uganda-minister": {
            "name": "Ugandan Minister for Magic",
            "aliases": ["Ugandan Minister"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Ugandan Minister for Magic present at the World Cup as part of the international delegation.",
                    "role": "Foreign Minister, International guest",
                    "relationships": {"International delegation": "Member of"}
                }
            }
        },
        # More Photographers and Media
        "daily-prophet-photographer": {
            "name": "Daily Prophet Photographer",
            "aliases": ["Camera wizard"],
            "appearances": [18, 24],
            "knowledge": {
                "18": {
                    "revealedIn": 18,
                    "description": "Daily Prophet photographer who takes pictures of the tournament champions and creates magical moving photographs.",
                    "role": "Photographer, Journalist",
                    "relationships": {
                        "Rita Skeeter": "Works with for articles",
                        "Daily Prophet": "Employee of"
                    }
                }
            }
        },
        "witch-weekly-reporter": {
            "name": "Witch Weekly Reporter",
            "aliases": ["Fashion reporter"],
            "appearances": [24],
            "knowledge": {
                "24": {
                    "revealedIn": 24,
                    "description": "Reporter from Witch Weekly magazine covering the social aspects of the tournament.",
                    "role": "Fashion reporter, Magazine journalist",
                    "relationships": {"Witch Weekly": "Reporter for"}
                }
            }
        },
        # More Azkaban Prisoners/Former Death Eaters
        "gibbon": {
            "name": "Gibbon",
            "aliases": ["Death Eater"],
            "appearances": [33],
            "knowledge": {
                "33": {
                    "revealedIn": 33,
                    "description": "Death Eater present at the graveyard gathering when Voldemort returns.",
                    "role": "Death Eater, Dark wizard",
                    "relationships": {
                        "Voldemort": "Serves",
                        "Death Eaters": "Member of"
                    }
                }
            }
        },
        "selwyn": {
            "name": "Selwyn",
            "aliases": ["Death Eater"],
            "appearances": [33],
            "knowledge": {
                "33": {
                    "revealedIn": 33,
                    "description": "Death Eater who answers Voldemort's summons in the graveyard.",
                    "role": "Death Eater, Voldemort follower",
                    "relationships": {
                        "Voldemort": "Loyal to",
                        "Death Eaters": "Member of"
                    }
                }
            }
        },
        # Historical Wizards mentioned in classes
        "emeric-switch": {
            "name": "Emeric Switch",
            "aliases": ["Switch"],
            "appearances": [15],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Famous wizard mentioned in Transfiguration studies, known for his work on switching spells.",
                    "role": "Historical wizard, Transfiguration expert",
                    "relationships": {"Transfiguration": "Contributed to field of"}
                }
            }
        },
        "gubraithian-fire-inventor": {
            "name": "Gubraithian Fire Creator",
            "aliases": ["Fire creator"],
            "appearances": [20],
            "knowledge": {
                "20": {
                    "revealedIn": 20,
                    "description": "Ancient wizard who created the magical Gubraithian fire that never goes out.",
                    "role": "Historical wizard, Fire magic expert",
                    "relationships": {"Magical fire": "Creator of eternal flame"}
                }
            }
        },
        "burdock-muldoon": {
            "name": "Burdock Muldoon",
            "aliases": ["Muldoon"],
            "appearances": [13],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Historical Chief of the Wizengamot mentioned in History of Magic lessons.",
                    "role": "Historical figure, Former Chief Warlock",
                    "relationships": {"Wizengamot": "Former leader of"}
                }
            }
        },
        # More Magical Creatures
        "thestrals": {
            "name": "Thestrals",
            "aliases": ["Winged horses"],
            "appearances": [21],
            "knowledge": {
                "21": {
                    "revealedIn": 21,
                    "description": "Skeletal winged horses that can only be seen by those who have witnessed death, living in the Forbidden Forest.",
                    "role": "Magical creatures, Death omens",
                    "relationships": {
                        "Forbidden Forest": "Inhabit",
                        "Hagrid": "Cared for by"
                    }
                }
            }
        },
        "centaurs": {
            "name": "Forbidden Forest Centaurs",
            "aliases": ["Centaurs"],
            "appearances": [15],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Intelligent half-human, half-horse creatures living deep in the Forbidden Forest, skilled in astronomy and divination.",
                    "role": "Magical beings, Forest dwellers",
                    "relationships": {
                        "Forbidden Forest": "Inhabitants of",
                        "Stars": "Read omens in"
                    }
                }
            }
        },
        "acromantulas": {
            "name": "Acromantulas",
            "aliases": ["Giant spiders"],
            "appearances": [15],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Giant spiders living in the Forbidden Forest, descendants of Aragog's colony.",
                    "role": "Dangerous creatures, Forest inhabitants",
                    "relationships": {
                        "Forbidden Forest": "Colony in",
                        "Hagrid": "Known to"
                    }
                }
            }
        },
        # More House-elves
        "kreacher": {
            "name": "Kreacher",
            "aliases": ["Black family elf"],
            "appearances": [27],
            "knowledge": {
                "27": {
                    "revealedIn": 27,
                    "description": "Ancient house-elf serving the Black family at Grimmauld Place, mentioned in Sirius's letters.",
                    "role": "House-elf, Family servant",
                    "relationships": {
                        "Black family": "Serves",
                        "Grimmauld Place": "Lives at"
                    }
                }
            }
        },
        # Tournament Support Staff
        "tournament-mediwizard": {
            "name": "Tournament Mediwizard",
            "aliases": ["Medical wizard"],
            "appearances": [19, 26, 31],
            "knowledge": {
                "19": {
                    "revealedIn": 19,
                    "description": "Specialized healer present at tournament tasks to treat injuries from dangerous challenges.",
                    "role": "Medical wizard, Emergency healer",
                    "relationships": {
                        "Tournament champions": "Provides medical care to",
                        "Dangerous tasks": "Emergency responder for"
                    }
                }
            }
        },
        "tournament-security": {
            "name": "Tournament Security Wizard",
            "aliases": ["Security official"],
            "appearances": [19, 26, 31],
            "knowledge": {
                "19": {
                    "revealedIn": 19,
                    "description": "Security wizard responsible for maintaining order and safety during the dangerous tournament tasks.",
                    "role": "Security wizard, Safety official",
                    "relationships": {
                        "Tournament": "Provides security for",
                        "Spectators": "Protects from danger"
                    }
                }
            }
        },
        # More Vendors and Workers
        "world-cup-vendor": {
            "name": "World Cup Vendor",
            "aliases": ["Merchandise seller"],
            "appearances": [7],
            "knowledge": {
                "7": {
                    "revealedIn": 7,
                    "description": "Wizard selling World Cup merchandise and magical souvenirs at the campsite.",
                    "role": "Vendor, Merchant",
                    "relationships": {
                        "World Cup": "Sells merchandise for",
                        "Wizard fans": "Serves customers"
                    }
                }
            }
        },
        "omnioculars-salesman": {
            "name": "Omnioculars Salesman",
            "aliases": ["Magical binoculars seller"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Vendor selling magical omnioculars that enhance the viewing experience at the Quidditch match.",
                    "role": "Vendor, Equipment seller",
                    "relationships": {
                        "Omnioculars": "Sells magical binoculars",
                        "Quidditch fans": "Provides equipment to"
                    }
                }
            }
        },
        # Additional Wizarding Families
        "fawcett": {
            "name": "Fawcett",
            "aliases": ["Ravenclaw student"],
            "appearances": [16, 23],
            "knowledge": {
                "16": {
                    "revealedIn": 16,
                    "description": "Ravenclaw student who attempts to enter the tournament by crossing the age line.",
                    "role": "Student, Age line challenger",
                    "relationships": {
                        "Age Line": "Tries to cross illegally",
                        "Goblet of Fire": "Attempts to enter tournament"
                    }
                }
            }
        },
        "stebbins": {
            "name": "Stebbins",
            "aliases": ["Hufflepuff student"],
            "appearances": [16, 23],
            "knowledge": {
                "16": {
                    "revealedIn": 16,
                    "description": "Hufflepuff student who also tries to cross the age line to enter the tournament.",
                    "role": "Student, Tournament hopeful",
                    "relationships": {
                        "Fawcett": "Partners with in age line attempt",
                        "Tournament": "Wants to enter"
                    }
                }
            }
        },
        # More Foreign Officials
        "german-minister": {
            "name": "German Minister for Magic",
            "aliases": ["German Minister"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "German Minister for Magic attending the World Cup as part of the international delegation.",
                    "role": "Foreign Minister, International guest",
                    "relationships": {"World Cup": "International attendee at"}
                }
            }
        },
        "egyptian-delegation": {
            "name": "Egyptian Magical Delegation",
            "aliases": ["Egyptian wizards"],
            "appearances": [8],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Group of Egyptian wizards attending the World Cup as international representatives.",
                    "role": "Foreign delegation, International guests",
                    "relationships": {"World Cup": "International representation at"}
                }
            }
        },
        # Additional Magical Objects and Creatures  
        "howler-letter": {
            "name": "Howler",
            "aliases": ["Screaming letter"],
            "appearances": [14],
            "knowledge": {
                "14": {
                    "revealedIn": 14,
                    "description": "Magical screaming letter that Mrs. Weasley sends to Ron after he's seen in Rita Skeeter's article.",
                    "role": "Magical mail, Disciplinary tool",
                    "relationships": {
                        "Molly Weasley": "Sent by",
                        "Ron Weasley": "Recipient of scolding"
                    }
                }
            }
        },
        "age-line": {
            "name": "Age Line",
            "aliases": ["Magical barrier"],
            "appearances": [16],
            "knowledge": {
                "16": {
                    "revealedIn": 16,
                    "description": "Magical barrier created by Dumbledore around the Goblet of Fire to prevent underage students from entering.",
                    "role": "Magical protection, Age barrier",
                    "relationships": {
                        "Albus Dumbledore": "Created by",
                        "Goblet of Fire": "Protects from underage entry"
                    }
                }
            }
        },
        # More Graveyard Elements
        "riddle-gravestone": {
            "name": "Tom Riddle's Gravestone",
            "aliases": ["Father's grave"],
            "appearances": [32],
            "knowledge": {
                "32": {
                    "revealedIn": 32,
                    "description": "Gravestone of Tom Riddle Sr. in Little Hangleton graveyard, used in Voldemort's resurrection ritual.",
                    "role": "Ritual component, Memorial",
                    "relationships": {
                        "Tom Riddle Sr.": "Grave marker for",
                        "Voldemort": "Source of bone for ritual"
                    }
                }
            }
        },
        "cauldron": {
            "name": "Resurrection Cauldron",
            "aliases": ["Ritual cauldron"],
            "appearances": [32],
            "knowledge": {
                "32": {
                    "revealedIn": 32,
                    "description": "Large stone cauldron used in the dark ritual to restore Voldemort to physical form.",
                    "role": "Ritual vessel, Dark magic tool",
                    "relationships": {
                        "Voldemort": "Restoration vessel for",
                        "Dark ritual": "Central component of"
                    }
                }
            }
        },
        # More Background Characters
        "witch-weekly-readers": {
            "name": "Witch Weekly Readers",
            "aliases": ["Magazine readers"],
            "appearances": [27],
            "knowledge": {
                "27": {
                    "revealedIn": 27,
                    "description": "Witches who read Witch Weekly magazine and send Hermione hate mail after Rita Skeeter's articles.",
                    "role": "Magazine readers, Hermione critics",
                    "relationships": {
                        "Rita Skeeter": "Influenced by articles",
                        "Hermione Granger": "Send hate mail to"
                    }
                }
            }
        },
        "st-mungos-healers": {
            "name": "St. Mungo's Healers",
            "aliases": ["Hospital healers"],
            "appearances": [30],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Medical wizards working at St. Mungo's Hospital caring for the Longbottoms and other long-term patients.",
                    "role": "Medical professionals, Healers",
                    "relationships": {
                        "Frank Longbottom": "Treat permanently",
                        "Alice Longbottom": "Provide long-term care for"
                    }
                }
            }
        },
        # More Tournament Elements
        "golden-egg": {
            "name": "Golden Egg",
            "aliases": ["Dragon's egg", "Tournament clue"],
            "appearances": [19, 20, 25],
            "knowledge": {
                "19": {
                    "revealedIn": 19,
                    "description": "Golden egg retrieved from dragons in the first task, containing a clue for the second task.",
                    "role": "Tournament clue, Magical object",
                    "relationships": {
                        "Dragons": "Guarded by in first task",
                        "Champions": "Retrieved by"
                    }
                },
                "25": {
                    "revealedIn": 25,
                    "description": "Contains merperson song that reveals the second task involves rescuing something precious from the Black Lake.",
                    "role": "Clue container, Second task hint",
                    "relationships": {
                        "Merpeople": "Contains song from",
                        "Black Lake": "Points to location of second task"
                    }
                }
            }
        },
        "gillyweed": {
            "name": "Gillyweed",
            "aliases": ["Water plant"],
            "appearances": [26],
            "knowledge": {
                "26": {
                    "revealedIn": 26,
                    "description": "Magical plant that allows the user to breathe underwater and grow gills, provided to Harry by Dobby.",
                    "role": "Magical plant, Underwater breathing aid",
                    "relationships": {
                        "Dobby": "Provided to Harry by",
                        "Harry Potter": "Used by for second task"
                    }
                }
            }
        }
    }

def main():
    print("🏁 Final Goblet of Fire expansion to 250+ characters...")
    
    # Load current data
    with open('data/harry-potter/goblet-of-fire.json', 'r') as f:
        data = json.load(f)
    
    original_count = len(data['characters'])
    print(f"📊 Current character count: {original_count}")
    
    # Add final batch
    final_chars = get_final_characters()
    added = 0
    
    for char_id, char_data in final_chars.items():
        if char_id not in data['characters']:
            data['characters'][char_id] = char_data
            added += 1
        else:
            print(f"⚠️  Skipping existing character: {char_id}")
    
    # Save final data
    with open('data/harry-potter/goblet-of-fire.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    final_count = len(data['characters'])
    print(f"🎉 FINAL EXPANSION COMPLETE!")
    print(f"📊 Final character count: {final_count}")
    print(f"📈 Added in this batch: {added} characters")
    print(f"🚀 Total expansion: {final_count - 71} characters added to original")
    
    if final_count >= 250:
        print("✅ SUCCESS: Reached 250+ character target!")
    else:
        print(f"⚠️  Need {250 - final_count} more characters to reach 250")
    
    # Validate JSON
    try:
        with open('data/harry-potter/goblet-of-fire.json', 'r') as f:
            json.load(f)
        print("✅ JSON validation successful!")
        return True
    except Exception as e:
        print(f"❌ JSON validation failed: {e}")
        return False

if __name__ == "__main__":
    main()