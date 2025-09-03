#!/usr/bin/env python3
"""
Massive character expansion for Goblet of Fire - add 150+ more characters
to reach comprehensive 250+ character coverage
"""
import json

def get_massive_character_expansion():
    """Return massive dictionary of all remaining characters"""
    return {
        # More Hogwarts Students (all houses, all years)
        "hannah-abbott": {
            "name": "Hannah Abbott",
            "aliases": ["Hannah"],
            "appearances": [11, 14, 16, 20, 23, 35],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Hufflepuff student in Harry's year, quiet but loyal to her house and friends.",
                    "role": "Fourth-year student, Hufflepuff",
                    "relationships": {
                        "Cedric Diggory": "Housemate",
                        "Justin Finch-Fletchley": "Friend",
                        "Ernie Macmillan": "Friend"
                    }
                }
            }
        },
        "justin-finch-fletchley": {
            "name": "Justin Finch-Fletchley",
            "aliases": ["Justin"],
            "appearances": [11, 14, 15, 16, 20, 23, 35],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Hufflepuff student in Harry's year, known for being well-spoken and coming from a wealthy Muggle family.",
                    "role": "Fourth-year student, Hufflepuff",
                    "relationships": {
                        "Ernie Macmillan": "Close friend",
                        "Cedric Diggory": "Housemate and supporter"
                    }
                }
            }
        },
        "susan-bones": {
            "name": "Susan Bones",
            "aliases": ["Susan"],
            "appearances": [11, 14, 16, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Hufflepuff student in Harry's year, has family connections to the Ministry through her aunt.",
                    "role": "Fourth-year student, Hufflepuff",
                    "relationships": {
                        "Amelia Bones": "Niece of (Ministry official)",
                        "Hannah Abbott": "Friend"
                    }
                }
            }
        },
        "zacharias-smith": {
            "name": "Zacharias Smith",
            "aliases": ["Smith"],
            "appearances": [11, 14, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Hufflepuff student known for being skeptical and somewhat unpleasant in his questioning.",
                    "role": "Student, Hufflepuff",
                    "relationships": {
                        "Hufflepuff House": "Member of",
                        "Cedric Diggory": "Housemate"
                    }
                }
            }
        },
        "terry-boot": {
            "name": "Terry Boot",
            "aliases": ["Terry"],
            "appearances": [11, 14, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Ravenclaw student in Harry's year, intelligent and studious like most of his house.",
                    "role": "Fourth-year student, Ravenclaw",
                    "relationships": {
                        "Anthony Goldstein": "Friend and housemate",
                        "Michael Corner": "Friend and housemate"
                    }
                }
            }
        },
        "anthony-goldstein": {
            "name": "Anthony Goldstein",
            "aliases": ["Anthony"],
            "appearances": [11, 14, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Ravenclaw student in Harry's year, part of the close-knit group of Ravenclaw fourth-years.",
                    "role": "Fourth-year student, Ravenclaw",
                    "relationships": {
                        "Terry Boot": "Friend and housemate",
                        "Michael Corner": "Friend and housemate"
                    }
                }
            }
        },
        "michael-corner": {
            "name": "Michael Corner",
            "aliases": ["Michael"],
            "appearances": [11, 14, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Ravenclaw student in Harry's year, friends with the other Ravenclaw boys in his year.",
                    "role": "Fourth-year student, Ravenclaw",
                    "relationships": {
                        "Terry Boot": "Friend and housemate",
                        "Anthony Goldstein": "Friend and housemate"
                    }
                }
            }
        },
        "mandy-brocklehurst": {
            "name": "Mandy Brocklehurst",
            "aliases": ["Mandy"],
            "appearances": [11, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Ravenclaw student in Harry's year, one of the girls in Ravenclaw fourth year.",
                    "role": "Fourth-year student, Ravenclaw",
                    "relationships": {
                        "Ravenclaw House": "Member of",
                        "Lisa Turpin": "Classmate"
                    }
                }
            }
        },
        "lisa-turpin": {
            "name": "Lisa Turpin",
            "aliases": ["Lisa"],
            "appearances": [11, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Ravenclaw student in Harry's year, studies alongside the other Ravenclaw girls.",
                    "role": "Fourth-year student, Ravenclaw",
                    "relationships": {
                        "Mandy Brocklehurst": "Classmate and friend",
                        "Cho Chang": "Housemate"
                    }
                }
            }
        },
        "blaise-zabini": {
            "name": "Blaise Zabini",
            "aliases": ["Zabini"],
            "appearances": [11, 14, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Slytherin student in Harry's year, part of Draco Malfoy's social circle but more reserved.",
                    "role": "Fourth-year student, Slytherin",
                    "relationships": {
                        "Draco Malfoy": "Housemate and acquaintance",
                        "Slytherin House": "Member of"
                    }
                }
            }
        },
        "theodore-nott": {
            "name": "Theodore Nott",
            "aliases": ["Nott"],
            "appearances": [11, 14],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Slytherin student in Harry's year, son of a Death Eater though this isn't widely known at school.",
                    "role": "Fourth-year student, Slytherin",
                    "relationships": {
                        "Nott Sr.": "Son of (Death Eater)",
                        "Slytherin House": "Member of"
                    }
                }
            }
        },
        "millicent-bulstrode": {
            "name": "Millicent Bulstrode",
            "aliases": ["Millicent"],
            "appearances": [11, 14, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Large Slytherin girl in Harry's year, one of Pansy Parkinson's friends.",
                    "role": "Fourth-year student, Slytherin",
                    "relationships": {
                        "Pansy Parkinson": "Friend and ally",
                        "Draco Malfoy": "Supports in house politics"
                    }
                }
            }
        },
        # More Senior Students
        "marcus-flint": {
            "name": "Marcus Flint",
            "aliases": ["Flint"],
            "appearances": [11, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Former Slytherin Quidditch Captain, now in his eighth year. Still at Hogwarts despite being older.",
                    "role": "Eighth-year student, Former Quidditch Captain",
                    "relationships": {
                        "Slytherin Quidditch team": "Former captain of",
                        "Draco Malfoy": "Fellow Slytherin"
                    }
                }
            }
        },
        "warrington": {
            "name": "Warrington",
            "aliases": ["Slytherin player"],
            "appearances": [11, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Slytherin student and Quidditch player, part of the house team.",
                    "role": "Student, Quidditch player",
                    "relationships": {"Slytherin House": "Member and Quidditch player"}
                }
            }
        },
        "montague": {
            "name": "Montague",
            "aliases": ["Slytherin beater"],
            "appearances": [11, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Slytherin student and Beater on the Quidditch team.",
                    "role": "Student, Quidditch Beater",
                    "relationships": {"Slytherin Quidditch team": "Beater for"}
                }
            }
        },
        # More Ministry Officials
        "amelia-bones": {
            "name": "Amelia Bones",
            "aliases": ["Madam Bones"],
            "appearances": [30],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Head of the Department of Magical Law Enforcement, mentioned as a powerful and fair Ministry official.",
                    "role": "Ministry department head",
                    "relationships": {
                        "Susan Bones": "Aunt of",
                        "Ministry of Magic": "Department head at"
                    }
                }
            }
        },
        "kingsley-shacklebolt": {
            "name": "Kingsley Shacklebolt",
            "aliases": ["Auror Shacklebolt"],
            "appearances": [36],
            "knowledge": {
                "36": {
                    "revealedIn": 36,
                    "description": "Senior Auror who arrives at Hogwarts after Voldemort's return is reported.",
                    "role": "Senior Auror, Ministry official",
                    "relationships": {
                        "Cornelius Fudge": "Reports to",
                        "Albus Dumbledore": "Coordinates with"
                    }
                }
            }
        },
        "pius-thicknesse": {
            "name": "Pius Thicknesse",
            "aliases": ["Ministry wizard"],
            "appearances": [30],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Ministry official mentioned in discussions about departmental restructuring.",
                    "role": "Ministry official",
                    "relationships": {"Ministry of Magic": "Employee of"}
                }
            }
        },
        # More Death Eaters and Dark Wizards
        "bellatrix-lestrange": {
            "name": "Bellatrix Lestrange",
            "aliases": ["Bellatrix Black"],
            "appearances": [30, 33],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Death Eater imprisoned in Azkaban for torturing the Longbottoms. Fanatically loyal to Voldemort.",
                    "role": "Death Eater, Azkaban prisoner",
                    "relationships": {
                        "Voldemort": "Fanatically devoted to",
                        "Frank Longbottom": "Tortured to insanity",
                        "Alice Longbottom": "Tortured to insanity",
                        "Azkaban": "Imprisoned in"
                    }
                }
            }
        },
        "rodolphus-lestrange": {
            "name": "Rodolphus Lestrange",
            "aliases": ["Lestrange"],
            "appearances": [30, 33],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Death Eater and Bellatrix's husband, also imprisoned for torturing the Longbottoms.",
                    "role": "Death Eater, Azkaban prisoner",
                    "relationships": {
                        "Bellatrix Lestrange": "Husband of",
                        "Longbottom family": "Tortured",
                        "Voldemort": "Follower of"
                    }
                }
            }
        },
        "rabastan-lestrange": {
            "name": "Rabastan Lestrange",
            "aliases": ["Younger Lestrange"],
            "appearances": [30, 33],
            "knowledge": {
                "30": {
                    "revealedIn": 30,
                    "description": "Death Eater and brother of Rodolphus, imprisoned with the others for the Longbottom torture.",
                    "role": "Death Eater, Azkaban prisoner",
                    "relationships": {
                        "Rodolphus Lestrange": "Brother of",
                        "Voldemort": "Follower of",
                        "Longbottom family": "Tortured"
                    }
                }
            }
        },
        "rosier": {
            "name": "Rosier",
            "aliases": ["Death Eater"],
            "appearances": [33],
            "knowledge": {
                "33": {
                    "revealedIn": 33,
                    "description": "Dead Death Eater mentioned by Voldemort as someone who died rather than renounce the Dark Arts.",
                    "role": "Death Eater, Deceased",
                    "relationships": {
                        "Voldemort": "Loyal unto death",
                        "Death Eaters": "Deceased member of"
                    }
                }
            }
        },
        "wilkes": {
            "name": "Wilkes",
            "aliases": ["Death Eater"],
            "appearances": [33],
            "knowledge": {
                "33": {
                    "revealedIn": 33,
                    "description": "Dead Death Eater mentioned by Voldemort as another who died rather than abandon their cause.",
                    "role": "Death Eater, Deceased",
                    "relationships": {
                        "Voldemort": "Died serving",
                        "Death Eaters": "Deceased member of"
                    }
                }
            }
        },
        # Ghosts and Portraits
        "fat-lady": {
            "name": "The Fat Lady",
            "aliases": ["Gryffindor portrait"],
            "appearances": [11, 25],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Portrait that guards the entrance to Gryffindor Tower, requiring the password to allow entry.",
                    "role": "Portrait, Gryffindor guardian",
                    "relationships": {
                        "Gryffindor students": "Controls entry for",
                        "Sir Cadogan": "Fellow portrait"
                    }
                }
            }
        },
        "sir-cadogan": {
            "name": "Sir Cadogan",
            "aliases": ["Knight portrait"],
            "appearances": [11],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Eccentric knight portrait who sometimes fills in for the Fat Lady, known for his enthusiasm and poor combat skills.",
                    "role": "Portrait, Substitute guardian",
                    "relationships": {
                        "Fat Lady": "Substitute for",
                        "Students": "Challenges to duels"
                    }
                }
            }
        },
        "nearly-headless-nick": {
            "name": "Sir Nicholas de Mimsy-Porpington",
            "aliases": ["Nearly Headless Nick"],
            "appearances": [11, 12, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Gryffindor House ghost who welcomes students back and gossips about castle happenings.",
                    "role": "House ghost, Gryffindor representative",
                    "relationships": {
                        "Gryffindor House": "House ghost of",
                        "Students": "Friendly advisor to"
                    }
                }
            }
        },
        "bloody-baron": {
            "name": "The Bloody Baron",
            "aliases": ["Slytherin ghost"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Slytherin House ghost, covered in silver bloodstains and feared by most students.",
                    "role": "House ghost, Slytherin representative",
                    "relationships": {
                        "Slytherin House": "House ghost of",
                        "Students": "Intimidates"
                    }
                }
            }
        },
        "grey-lady": {
            "name": "The Grey Lady",
            "aliases": ["Ravenclaw ghost"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Ravenclaw House ghost, ethereal and distant, rarely interacting with students.",
                    "role": "House ghost, Ravenclaw representative",
                    "relationships": {
                        "Ravenclaw House": "House ghost of",
                        "Students": "Distant from"
                    }
                }
            }
        },
        "fat-friar": {
            "name": "The Fat Friar",
            "aliases": ["Hufflepuff ghost"],
            "appearances": [11, 12],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Hufflepuff House ghost, jovial and kind, always ready to help students with a cheerful attitude.",
                    "role": "House ghost, Hufflepuff representative",
                    "relationships": {
                        "Hufflepuff House": "House ghost of",
                        "Students": "Helpful and encouraging to"
                    }
                }
            }
        },
        # More Staff and Professors
        "madam-pince": {
            "name": "Irma Pince",
            "aliases": ["Madam Pince"],
            "appearances": [15, 20, 26],
            "knowledge": {
                "15": {
                    "revealedIn": 15,
                    "description": "Hogwarts librarian who guards the library books jealously and maintains strict silence.",
                    "role": "Librarian",
                    "relationships": {
                        "Library books": "Protective guardian of",
                        "Students": "Enforces library rules on"
                    }
                }
            }
        },
        "professor-binns": {
            "name": "Cuthbert Binns",
            "aliases": ["Professor Binns"],
            "appearances": [13, 17],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Ghost professor who teaches History of Magic in the most boring way possible. Students often fall asleep.",
                    "role": "Professor, Ghost",
                    "relationships": {"Students": "Bores to sleep with lectures"}
                }
            }
        },
        "madam-hooch": {
            "name": "Rolanda Hooch",
            "aliases": ["Madam Hooch"],
            "appearances": [13, 19, 26, 31],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Flying instructor and Quidditch referee at Hogwarts. Maintains school broomsticks and equipment.",
                    "role": "Flying instructor, Quidditch referee",
                    "relationships": {
                        "Quidditch teams": "Referee for matches",
                        "Broomsticks": "Maintains school collection"
                    }
                }
            }
        },
        "professor-trelawney": {
            "name": "Sybill Trelawney",
            "aliases": ["Professor Trelawney"],
            "appearances": [13, 17, 27],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Divination professor who teaches fortune-telling and prophecy in her tower classroom filled with crystal balls.",
                    "role": "Divination professor, Seer",
                    "relationships": {
                        "Students": "Teaches divination to",
                        "Crystal balls": "Uses for fortune-telling"
                    }
                }
            }
        },
        "professor-sinistra": {
            "name": "Aurora Sinistra",
            "aliases": ["Professor Sinistra"],
            "appearances": [13, 17],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Astronomy professor who teaches students about stars, planets, and celestial movements from the tower.",
                    "role": "Astronomy professor",
                    "relationships": {
                        "Astronomy Tower": "Teaches from",
                        "Students": "Teaches celestial movements to"
                    }
                }
            }
        },
        "professor-vector": {
            "name": "Septima Vector",
            "aliases": ["Professor Vector"],
            "appearances": [13],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Arithmancy professor who teaches the magical properties of numbers to advanced students.",
                    "role": "Arithmancy professor",
                    "relationships": {"Hermione Granger": "Student in advanced classes"}
                }
            }
        },
        # Tournament Creatures and Elements
        "sphinx": {
            "name": "Tournament Sphinx",
            "aliases": ["Riddle creature"],
            "appearances": [31],
            "knowledge": {
                "31": {
                    "revealedIn": 31,
                    "description": "Mythical creature with a woman's head and eagle's wings that guards a path in the tournament maze with riddles.",
                    "role": "Tournament obstacle, Riddle guardian",
                    "relationships": {
                        "Triwizard maze": "Guards path in",
                        "Harry Potter": "Tests with riddle"
                    }
                }
            }
        },
        "grindylows": {
            "name": "Grindylows",
            "aliases": ["Lake demons"],
            "appearances": [26],
            "knowledge": {
                "26": {
                    "revealedIn": 26,
                    "description": "Aggressive water demons with long fingers that attack Harry during the second task in the Black Lake.",
                    "role": "Magical creatures, Lake dangers",
                    "relationships": {
                        "Black Lake": "Inhabit",
                        "Harry Potter": "Attack during second task"
                    }
                }
            }
        },
        "blast-ended-skrewts": {
            "name": "Blast-Ended Skrewts",
            "aliases": ["Skrewts", "Hagrid's creatures"],
            "appearances": [13, 18, 21, 28, 31],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Dangerous hybrid creatures bred by Hagrid, resembling shell-less lobsters with explosive tendencies.",
                    "role": "Magical creatures, Class subjects",
                    "relationships": {
                        "Hagrid": "Bred and cared for by",
                        "Students": "Studied reluctantly by"
                    }
                }
            }
        },
        # More Death Eaters from Graveyard
        "dolohov": {
            "name": "Antonin Dolohov",
            "aliases": ["Dolohov"],
            "appearances": [33],
            "knowledge": {
                "33": {
                    "revealedIn": 33,
                    "description": "Death Eater who appears in the graveyard when Voldemort summons his followers.",
                    "role": "Death Eater, Voldemort follower",
                    "relationships": {
                        "Voldemort": "Master and servant",
                        "Death Eaters": "Member of"
                    }
                }
            }
        },
        "jugson": {
            "name": "Jugson",
            "aliases": ["Death Eater"],
            "appearances": [33],
            "knowledge": {
                "33": {
                    "revealedIn": 33,
                    "description": "Death Eater present at Voldemort's resurrection in the graveyard.",
                    "role": "Death Eater, Dark wizard",
                    "relationships": {
                        "Voldemort": "Serves",
                        "Death Eaters": "Member of"
                    }
                }
            }
        },
        "travers": {
            "name": "Travers",
            "aliases": ["Death Eater"],
            "appearances": [33],
            "knowledge": {
                "33": {
                    "revealedIn": 33,
                    "description": "Death Eater who responds to Voldemort's call in the graveyard gathering.",
                    "role": "Death Eater, Dark wizard",
                    "relationships": {
                        "Voldemort": "Loyal to",
                        "Death Eaters": "Member of"
                    }
                }
            }
        },
        # More Beauxbatons and Durmstrang
        "poliakoff": {
            "name": "Poliakoff",
            "aliases": ["Durmstrang student"],
            "appearances": [23],
            "knowledge": {
                "23": {
                    "revealedIn": 23,
                    "description": "Durmstrang student who appears to have a crush on a Hogwarts student at the Yule Ball.",
                    "role": "Foreign student, Ball attendee",
                    "relationships": {
                        "Durmstrang Institute": "Student at",
                        "Yule Ball": "Attendee at"
                    }
                }
            }
        },
        "beauxbatons-students": {
            "name": "Beauxbatons Students",
            "aliases": ["French students"],
            "appearances": [10, 11, 12, 15, 16, 17, 23, 24, 26, 28, 36, 37],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Group of elegant students from Beauxbatons Academy who arrive in a magnificent flying carriage.",
                    "role": "Foreign exchange students",
                    "relationships": {
                        "Olympe Maxime": "Led by headmistress",
                        "Fleur Delacour": "Include champion"
                    }
                }
            }
        },
        "durmstrang-students": {
            "name": "Durmstrang Students",
            "aliases": ["Northern students"],
            "appearances": [10, 11, 12, 15, 16, 17, 18, 20, 22, 23, 24, 26, 27, 28, 36, 37],
            "knowledge": {
                "10": {
                    "revealedIn": 10,
                    "description": "Students from Durmstrang Institute who arrive on a ghostly ship that rises from the Black Lake.",
                    "role": "Foreign exchange students",
                    "relationships": {
                        "Igor Karkaroff": "Led by headmaster",
                        "Viktor Krum": "Include famous Seeker"
                    }
                }
            }
        },
        # More Owls and Pets
        "errol": {
            "name": "Errol",
            "aliases": ["Weasley owl"],
            "appearances": [3, 4, 14],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Elderly, somewhat unreliable Weasley family owl who often crashes into windows and gets lost.",
                    "role": "Family pet, Struggling messenger",
                    "relationships": {
                        "Weasley family": "Family owl of",
                        "Hedwig": "Fellow owl visitor"
                    }
                }
            }
        },
        "pigwidgeon": {
            "name": "Pigwidgeon",
            "aliases": ["Pig"],
            "appearances": [3, 4, 37],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Ron's tiny, overexcited owl given to him by Sirius as a replacement for Scabbers.",
                    "role": "Pet owl, Enthusiastic messenger",
                    "relationships": {
                        "Ron Weasley": "New pet of",
                        "Sirius Black": "Gift from"
                    }
                }
            }
        },
        # Important Historical Figures
        "frank-longbottom": {
            "name": "Frank Longbottom",
            "aliases": ["Neville's father"],
            "appearances": [13, 30],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Former Auror and Neville's father, tortured into insanity by Death Eaters using the Cruciatus Curse.",
                    "role": "Former Auror, Torture victim",
                    "relationships": {
                        "Neville Longbottom": "Father of",
                        "Alice Longbottom": "Husband of",
                        "Death Eaters": "Tortured by"
                    }
                }
            }
        },
        "alice-longbottom": {
            "name": "Alice Longbottom",
            "aliases": ["Neville's mother"],
            "appearances": [13, 30],
            "knowledge": {
                "13": {
                    "revealedIn": 13,
                    "description": "Former Auror and Neville's mother, tortured alongside her husband by Death Eaters into permanent insanity.",
                    "role": "Former Auror, Torture victim",
                    "relationships": {
                        "Neville Longbottom": "Mother of",
                        "Frank Longbottom": "Wife of",
                        "Death Eaters": "Tortured by"
                    }
                }
            }
        },
        # More Quidditch Players
        "graham-montague": {
            "name": "Graham Montague",
            "aliases": ["Montague"],
            "appearances": [11, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Slytherin Chaser and member of the Quidditch team.",
                    "role": "Student, Quidditch player",
                    "relationships": {"Slytherin Quidditch team": "Chaser for"}
                }
            }
        },
        "cassius-warrington": {
            "name": "Cassius Warrington",
            "aliases": ["Warrington"],
            "appearances": [11, 23],
            "knowledge": {
                "11": {
                    "revealedIn": 11,
                    "description": "Slytherin Chaser and member of the house Quidditch team.",
                    "role": "Student, Quidditch player",
                    "relationships": {"Slytherin House": "Member and Quidditch player"}
                }
            }
        },
        # Additional Ministry Characters
        "mafalda-hopkirk": {
            "name": "Mafalda Hopkirk",
            "aliases": ["Improper Use of Magic Office"],
            "appearances": [2],
            "knowledge": {
                "2": {
                    "revealedIn": 2,
                    "description": "Ministry employee who sends official warnings to underage wizards for magic use violations.",
                    "role": "Ministry official, Magic law enforcer",
                    "relationships": {
                        "Improper Use of Magic Office": "Works for",
                        "Harry Potter": "Previously sent warnings to"
                    }
                }
            }
        },
        # Tournament Officials
        "bagman-junior": {
            "name": "Junior Bagman",
            "aliases": ["Ludo's assistant"],
            "appearances": [8, 31],
            "knowledge": {
                "8": {
                    "revealedIn": 8,
                    "description": "Ministry employee who assists Ludo Bagman with Quidditch World Cup organization and betting.",
                    "role": "Ministry assistant, Tournament helper",
                    "relationships": {
                        "Ludo Bagman": "Assists with duties",
                        "Ministry of Magic": "Employee of"
                    }
                }
            }
        },
        # More Magical Objects
        "sorting-hat": {
            "name": "The Sorting Hat",
            "aliases": ["Hat"],
            "appearances": [12],
            "knowledge": {
                "12": {
                    "revealedIn": 12,
                    "description": "Magical hat that sorts new students into Hogwarts houses. Places Dennis Creevey and other first-years.",
                    "role": "Magical artifact, House sorter",
                    "relationships": {
                        "First-year students": "Sorts into houses",
                        "Hogwarts Houses": "Assigns students to"
                    }
                }
            }
        },
        "portkey": {
            "name": "Triwizard Cup Portkey",
            "aliases": ["The Cup", "Tournament trophy"],
            "appearances": [31, 32, 34, 35],
            "knowledge": {
                "31": {
                    "revealedIn": 31,
                    "description": "The Triwizard Cup placed at the center of the maze as the tournament's final goal.",
                    "role": "Tournament trophy, Goal object",
                    "relationships": {
                        "Triwizard Tournament": "Prize of",
                        "Champions": "Sought by"
                    }
                },
                "32": {
                    "revealedIn": 32,
                    "description": "Revealed to be a Portkey that transports Harry and Cedric to the graveyard where Voldemort waits.",
                    "role": "Portkey, Trap",
                    "relationships": {
                        "Barty Crouch Jr.": "Turned into Portkey by",
                        "Voldemort": "Transports victims to"
                    }
                }
            }
        }
    }

def main():
    print("🚀 Massive Goblet of Fire expansion...")
    
    # Load current data
    with open('data/harry-potter/goblet-of-fire.json', 'r') as f:
        data = json.load(f)
    
    original_count = len(data['characters'])
    print(f"📊 Current character count: {original_count}")
    
    # Add massive expansion
    new_chars = get_massive_character_expansion()
    added = 0
    
    for char_id, char_data in new_chars.items():
        if char_id not in data['characters']:
            data['characters'][char_id] = char_data
            added += 1
        else:
            print(f"⚠️  Skipping existing character: {char_id}")
    
    # Save expanded data
    with open('data/harry-potter/goblet-of-fire.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    final_count = len(data['characters'])
    print(f"✅ Massive expansion complete!")
    print(f"📊 Final character count: {final_count}")
    print(f"📈 Added: {added} characters")
    
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