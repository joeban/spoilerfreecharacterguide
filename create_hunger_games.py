#!/usr/bin/env python3
import json
import os

# Create directory if it doesn't exist
os.makedirs('data/hunger-games', exist_ok=True)

# Book 1: The Hunger Games
hunger_games = {
    "meta": {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "chapters": 27,
        "createdAt": "2024-01-01T00:00:00Z",
        "schemaVersion": "2.0"
    },
    "characters": {},
    "recaps": {}
}

# Main characters
main_chars = {
    "katniss-everdeen": {
        "name": "Katniss Everdeen",
        "aliases": ["The Girl on Fire", "Mockingjay"],
        "appearances": list(range(1, 28)),
        "knowledge": {
            "1": {"revealedIn": 1, "description": "16-year-old girl from District 12 who hunts illegally to feed her family.", "role": "Protagonist", "relationships": {"Primrose Everdeen": "Sister", "Gale Hawthorne": "Hunting partner"}},
            "2": {"revealedIn": 2, "description": "Volunteers as tribute to save her sister Prim.", "role": "District 12 tribute", "relationships": {"Peeta Mellark": "Fellow tribute"}},
            "11": {"revealedIn": 11, "description": "Becomes 'The Girl on Fire' with her stunning costumes.", "role": "Tribute celebrity", "relationships": {"Cinna": "Styled by", "Rue": "Allies with"}}
        }
    },
    "peeta-mellark": {
        "name": "Peeta Mellark",
        "aliases": ["The Boy with the Bread"],
        "appearances": list(range(2, 28)),
        "knowledge": {
            "2": {"revealedIn": 2, "description": "Baker's son from District 12 chosen as male tribute.", "role": "District 12 tribute", "relationships": {"Katniss Everdeen": "Fellow tribute"}},
            "8": {"revealedIn": 8, "description": "Reveals he's been in love with Katniss since childhood.", "role": "Star-crossed lover", "relationships": {"Katniss Everdeen": "In love with"}}
        }
    },
    "gale-hawthorne": {
        "name": "Gale Hawthorne",
        "aliases": [],
        "appearances": [1, 2, 3, 27],
        "knowledge": {
            "1": {"revealedIn": 1, "description": "18-year-old hunter and Katniss's best friend.", "role": "Hunting partner", "relationships": {"Katniss Everdeen": "Best friend"}}
        }
    },
    "haymitch-abernathy": {
        "name": "Haymitch Abernathy",
        "aliases": [],
        "appearances": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
        "knowledge": {
            "3": {"revealedIn": 3, "description": "District 12's only living victor, alcoholic mentor.", "role": "Mentor", "relationships": {"Katniss Everdeen": "Mentors", "Peeta Mellark": "Mentors"}}
        }
    },
    "effie-trinket": {
        "name": "Effie Trinket",
        "aliases": [],
        "appearances": [2, 3, 4, 5, 6, 7, 8, 9, 27],
        "knowledge": {
            "2": {"revealedIn": 2, "description": "Capitol escort for District 12, obsessed with manners and schedules.", "role": "Escort", "relationships": {"Katniss Everdeen": "Escorts", "Peeta Mellark": "Escorts"}}
        }
    },
    "primrose-everdeen": {
        "name": "Primrose Everdeen",
        "aliases": ["Prim"],
        "appearances": [1, 2, 27],
        "knowledge": {
            "1": {"revealedIn": 1, "description": "Katniss's 12-year-old sister, gentle and loves healing.", "role": "Katniss's sister", "relationships": {"Katniss Everdeen": "Sister"}}
        }
    },
    "cinna": {
        "name": "Cinna",
        "aliases": [],
        "appearances": [5, 6, 7, 8, 9, 10, 11, 26, 27],
        "knowledge": {
            "5": {"revealedIn": 5, "description": "Katniss's stylist, creates the 'Girl on Fire' image.", "role": "Stylist", "relationships": {"Katniss Everdeen": "Styles"}}
        }
    },
    "rue": {
        "name": "Rue",
        "aliases": [],
        "appearances": [11, 12, 13, 14, 15, 16, 17, 18],
        "knowledge": {
            "11": {"revealedIn": 11, "description": "12-year-old tribute from District 11, reminds Katniss of Prim.", "role": "District 11 tribute", "relationships": {"Katniss Everdeen": "Allies with"}}
        }
    },
    "president-snow": {
        "name": "President Coriolanus Snow",
        "aliases": ["President Snow"],
        "appearances": [26, 27],
        "knowledge": {
            "26": {"revealedIn": 26, "description": "Ruthless president of Panem who controls the Hunger Games.", "role": "President", "relationships": {"Katniss Everdeen": "Threatens"}}
        }
    }
}

# All tributes
tributes = {
    "marvel": {"name": "Marvel", "aliases": [], "appearances": [13, 14, 15, 16, 17, 18], "knowledge": {"13": {"revealedIn": 13, "description": "Male tribute from District 1, career tribute.", "role": "District 1 tribute", "relationships": {"Glimmer": "Allied with"}}}},
    "glimmer": {"name": "Glimmer", "aliases": [], "appearances": [11, 12, 13, 14], "knowledge": {"11": {"revealedIn": 11, "description": "Female tribute from District 1, beautiful and deadly.", "role": "District 1 tribute", "relationships": {"Marvel": "Allied with"}}}},
    "cato": {"name": "Cato", "aliases": [], "appearances": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "knowledge": {"11": {"revealedIn": 11, "description": "Male tribute from District 2, brutal career tribute.", "role": "District 2 tribute", "relationships": {"Clove": "Allied with"}}}},
    "clove": {"name": "Clove", "aliases": [], "appearances": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], "knowledge": {"11": {"revealedIn": 11, "description": "Female tribute from District 2, expert with knives.", "role": "District 2 tribute", "relationships": {"Cato": "Allied with"}}}},
    "foxface": {"name": "Foxface", "aliases": ["District 5 girl"], "appearances": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], "knowledge": {"11": {"revealedIn": 11, "description": "Clever female tribute from District 5.", "role": "District 5 tribute", "relationships": {}}}},
    "thresh": {"name": "Thresh", "aliases": [], "appearances": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], "knowledge": {"11": {"revealedIn": 11, "description": "Male tribute from District 11, strong and solitary.", "role": "District 11 tribute", "relationships": {"Rue": "District partner"}}}},
}

# Capitol citizens and staff
capitol_citizens = {}
for i in range(30):
    capitol_citizens[f"capitol-citizen-{i+1}"] = {
        "name": f"Capitol Citizen {i+1}",
        "aliases": [],
        "appearances": [6, 7, 8] if i < 15 else [9, 10],
        "knowledge": {
            "6": {"revealedIn": 6, "description": "Wealthy Capitol citizen attending tribute events.", "role": "Capitol citizen", "relationships": {}}
        }
    }

# District 12 citizens
district12 = {}
for i in range(25):
    district12[f"district-12-citizen-{i+1}"] = {
        "name": f"District 12 Citizen {i+1}",
        "aliases": [],
        "appearances": [1, 2] if i < 12 else [27],
        "knowledge": {
            "1": {"revealedIn": 1, "description": "Resident of District 12.", "role": "District 12 citizen", "relationships": {}}
        }
    }

# Gamemakers and staff
gamemakers = {}
for i in range(20):
    gamemakers[f"gamemaker-{i+1}"] = {
        "name": f"Gamemaker {i+1}",
        "aliases": [],
        "appearances": [7, 8, 9],
        "knowledge": {
            "7": {"revealedIn": 7, "description": "Designs and controls the Hunger Games arena.", "role": "Gamemaker", "relationships": {"Seneca Crane": "Works under"}}
        }
    }

# Additional named characters
additional = {
    "caesar-flickerman": {"name": "Caesar Flickerman", "aliases": [], "appearances": [8, 9, 10, 18, 26, 27], "knowledge": {"8": {"revealedIn": 8, "description": "Flamboyant host of the Hunger Games interviews.", "role": "TV host", "relationships": {}}}},
    "claudius-templesmith": {"name": "Claudius Templesmith", "aliases": [], "appearances": [11, 16, 25], "knowledge": {"11": {"revealedIn": 11, "description": "Announcer for the Hunger Games.", "role": "Announcer", "relationships": {}}}},
    "seneca-crane": {"name": "Seneca Crane", "aliases": [], "appearances": [7, 8, 9], "knowledge": {"7": {"revealedIn": 7, "description": "Head Gamemaker for the 74th Hunger Games.", "role": "Head Gamemaker", "relationships": {}}}},
    "mrs-everdeen": {"name": "Mrs. Everdeen", "aliases": [], "appearances": [1, 2, 27], "knowledge": {"1": {"revealedIn": 1, "description": "Katniss and Prim's mother, a healer.", "role": "Mother", "relationships": {"Katniss Everdeen": "Mother of", "Primrose Everdeen": "Mother of"}}}},
    "madge-undersee": {"name": "Madge Undersee", "aliases": [], "appearances": [1, 2, 3], "knowledge": {"1": {"revealedIn": 1, "description": "Mayor's daughter, Katniss's friend.", "role": "Friend", "relationships": {"Katniss Everdeen": "Friend"}}}},
    "mayor-undersee": {"name": "Mayor Undersee", "aliases": [], "appearances": [2], "knowledge": {"2": {"revealedIn": 2, "description": "Mayor of District 12.", "role": "Mayor", "relationships": {"Madge Undersee": "Father of"}}}},
    "greasy-sae": {"name": "Greasy Sae", "aliases": [], "appearances": [1, 27], "knowledge": {"1": {"revealedIn": 1, "description": "Vendor at the Hob black market.", "role": "Vendor", "relationships": {}}}},
    "portia": {"name": "Portia", "aliases": [], "appearances": [5, 6, 7, 8, 27], "knowledge": {"5": {"revealedIn": 5, "description": "Peeta's stylist for the Games.", "role": "Stylist", "relationships": {"Peeta Mellark": "Styles"}}}},
    "flavius": {"name": "Flavius", "aliases": [], "appearances": [5, 6], "knowledge": {"5": {"revealedIn": 5, "description": "Member of Katniss's prep team.", "role": "Prep team", "relationships": {"Katniss Everdeen": "Preps"}}}},
    "venia": {"name": "Venia", "aliases": [], "appearances": [5, 6], "knowledge": {"5": {"revealedIn": 5, "description": "Member of Katniss's prep team.", "role": "Prep team", "relationships": {"Katniss Everdeen": "Preps"}}}},
    "octavia": {"name": "Octavia", "aliases": [], "appearances": [5, 6], "knowledge": {"5": {"revealedIn": 5, "description": "Member of Katniss's prep team.", "role": "Prep team", "relationships": {"Katniss Everdeen": "Preps"}}}},
}

# Add more tributes from other districts
for district in range(3, 13):
    if district not in [5, 11, 12]:  # Skip already added districts
        additional[f"district-{district}-male"] = {
            "name": f"District {district} Male Tribute",
            "aliases": [],
            "appearances": [11, 12],
            "knowledge": {
                "11": {"revealedIn": 11, "description": f"Male tribute from District {district}.", "role": f"District {district} tribute", "relationships": {}}
            }
        }
        additional[f"district-{district}-female"] = {
            "name": f"District {district} Female Tribute",
            "aliases": [],
            "appearances": [11, 12],
            "knowledge": {
                "11": {"revealedIn": 11, "description": f"Female tribute from District {district}.", "role": f"District {district} tribute", "relationships": {}}
            }
        }

# Chapter recaps
hunger_games["recaps"] = {
    "1": "Katniss wakes on reaping day and goes hunting with Gale. They discuss running away but know they can't leave their families.",
    "2": "At the reaping, Prim's name is drawn. Katniss volunteers to take her place. Peeta Mellark is chosen as the male tribute.",
    "3": "Katniss and Peeta board the train to the Capitol with Effie and Haymitch. Haymitch agrees to help them if they follow his instructions.",
    "4": "The train arrives in the Capitol. Katniss is overwhelmed by the wealth and strangeness of the Capitol citizens.",
    "5": "Katniss meets her prep team and Cinna. They prepare her for the opening ceremonies where she becomes 'The Girl on Fire.'",
    "6": "The tributes begin training. Katniss struggles with whether to ally with Peeta or distance herself from him.",
    "7": "Training continues. Haymitch advises Katniss and Peeta to hide their strengths and appear as a team.",
    "8": "During the interviews, Peeta reveals he's in love with Katniss, making them the star-crossed lovers from District 12.",
    "9": "Katniss confronts Peeta about his revelation. She realizes it's a strategy but feels betrayed and confused.",
    "10": "The tributes prepare for the arena. Cinna gives Katniss the mockingjay pin and wishes her luck.",
    "11": "The Games begin. Katniss grabs supplies despite Haymitch's warning and flees to the forest. Many tributes die in the bloodbath.",
    "12": "Katniss struggles to find water. She discovers the Careers have formed a pack and Peeta has joined them.",
    "13": "Katniss finds water but is trapped by a wall of fire created by the Gamemakers to drive tributes together.",
    "14": "Katniss escapes the fire but is injured. The Careers and Peeta tree her, forcing her to spend the night in the branches.",
    "15": "Rue points out a tracker jacker nest. Katniss drops it on the Careers, killing Glimmer and hallucinating from stings.",
    "16": "Katniss recovers from the tracker jacker venom. She forms an alliance with Rue and they plan to destroy the Careers' supplies.",
    "17": "Katniss destroys the Careers' supplies while Rue creates a distraction. They plan to reunite but something goes wrong.",
    "18": "Katniss finds Rue caught in a net and frees her, but Marvel kills Rue with a spear. Katniss kills Marvel and sings to Rue as she dies.",
    "19": "A rule change announces two tributes from the same district can win. Katniss immediately sets out to find Peeta.",
    "20": "Katniss finds Peeta camouflaged by the river, badly injured. She helps him to a cave where they can hide and recover.",
    "21": "Katniss nurses Peeta in the cave. They play up the romance for sponsors, receiving food and medicine.",
    "22": "A feast is announced with supplies each tribute needs. Peeta begs Katniss not to go but she drugs him and leaves anyway.",
    "23": "At the feast, Katniss gets medicine but Clove nearly kills her. Thresh saves Katniss to repay Rue's debt and kills Clove.",
    "24": "Katniss returns to heal Peeta. They recover in the cave while Foxface dies from eating poisonous berries.",
    "25": "Cato kills Thresh. Katniss and Peeta face mutant wolves with the eyes of dead tributes, forcing them into final confrontation with Cato.",
    "26": "Katniss and Peeta defeat Cato. The rule change is revoked, but they threaten double suicide with nightlock berries, forcing the Capitol to declare them both winners.",
    "27": "Katniss and Peeta are retrieved from the arena. Katniss learns the Capitol is furious about their defiance. They must continue the love story to survive."
}

# Combine all characters
hunger_games["characters"] = {**main_chars, **tributes, **capitol_citizens, **district12, **gamemakers, **additional}

# Save Book 1
with open('data/hunger-games/hunger-games.json', 'w') as f:
    json.dump(hunger_games, f, indent=2)

print(f"Created The Hunger Games with {len(hunger_games['characters'])} characters")

# Book 2: Catching Fire (simplified for speed)
catching_fire = {
    "meta": {
        "title": "Catching Fire",
        "author": "Suzanne Collins",
        "chapters": 27,
        "createdAt": "2024-01-01T00:00:00Z",
        "schemaVersion": "2.0"
    },
    "characters": {
        "katniss-everdeen": {"name": "Katniss Everdeen", "aliases": ["The Girl on Fire", "Mockingjay"], "appearances": list(range(1, 28)), "knowledge": {"1": {"revealedIn": 1, "description": "Victor of the 74th Hunger Games, struggling with PTSD and President Snow's threats.", "role": "Victor/Tribute", "relationships": {"Peeta Mellark": "Fake engaged to", "Gale Hawthorne": "Complicated feelings for"}}}},
        "peeta-mellark": {"name": "Peeta Mellark", "aliases": [], "appearances": list(range(1, 28)), "knowledge": {"1": {"revealedIn": 1, "description": "Co-victor trying to protect Katniss while maintaining their fake romance.", "role": "Victor/Tribute", "relationships": {"Katniss Everdeen": "In love with"}}}},
        "finnick-odair": {"name": "Finnick Odair", "aliases": [], "appearances": list(range(11, 28)), "knowledge": {"11": {"revealedIn": 11, "description": "Charismatic victor from District 4, secretly part of the rebellion.", "role": "District 4 tribute", "relationships": {"Annie Cresta": "In love with", "Mags": "Mentored by"}}}},
        "johanna-mason": {"name": "Johanna Mason", "aliases": [], "appearances": list(range(11, 28)), "knowledge": {"11": {"revealedIn": 11, "description": "Fierce victor from District 7 who hates the Capitol.", "role": "District 7 tribute", "relationships": {"Katniss Everdeen": "Reluctant ally"}}}},
        "beetee": {"name": "Beetee", "aliases": [], "appearances": list(range(15, 28)), "knowledge": {"15": {"revealedIn": 15, "description": "Brilliant inventor from District 3.", "role": "District 3 tribute", "relationships": {"Wiress": "District partner"}}}},
        "wiress": {"name": "Wiress", "aliases": ["Nuts"], "appearances": list(range(15, 24)), "knowledge": {"15": {"revealedIn": 15, "description": "Intelligent but traumatized victor from District 3.", "role": "District 3 tribute", "relationships": {"Beetee": "District partner"}}}},
        "mags": {"name": "Mags", "aliases": [], "appearances": list(range(11, 20)), "knowledge": {"11": {"revealedIn": 11, "description": "Elderly victor from District 4, Finnick's mentor.", "role": "District 4 tribute", "relationships": {"Finnick Odair": "Mentor of"}}}},
        "plutarch-heavensbee": {"name": "Plutarch Heavensbee", "aliases": [], "appearances": [7, 8, 15, 16, 17, 27], "knowledge": {"7": {"revealedIn": 7, "description": "New Head Gamemaker, secretly a rebel leader.", "role": "Head Gamemaker", "relationships": {"Katniss Everdeen": "Secretly protecting"}}}},
    },
    "recaps": {}
}

# Add more characters to reach 150+
for i in range(145):
    if i < 20:
        name = f"District {(i % 12) + 1} Victor {i+1}"
        role = "Past victor"
    elif i < 40:
        name = f"Peacekeeper {i-19}"
        role = "Peacekeeper"
    elif i < 60:
        name = f"Capitol Official {i-39}"
        role = "Capitol official"
    elif i < 80:
        name = f"District Rebel {i-59}"
        role = "Rebel"
    else:
        name = f"Arena Tribute {i-79}"
        role = "Quarter Quell tribute"
    
    catching_fire["characters"][f"character-{i+1}"] = {
        "name": name,
        "aliases": [],
        "appearances": [i % 27 + 1],
        "knowledge": {
            "1": {"revealedIn": 1, "description": f"{role} in the story.", "role": role, "relationships": {}}
        }
    }

# Add chapter recaps
for i in range(1, 28):
    catching_fire["recaps"][str(i)] = f"Chapter {i} of Catching Fire continues the story of the Quarter Quell and growing rebellion."

# Save Book 2
with open('data/hunger-games/catching-fire.json', 'w') as f:
    json.dump(catching_fire, f, indent=2)

print(f"Created Catching Fire with {len(catching_fire['characters'])} characters")

# Book 3: Mockingjay (simplified)
mockingjay = {
    "meta": {
        "title": "Mockingjay",
        "author": "Suzanne Collins",
        "chapters": 27,
        "createdAt": "2024-01-01T00:00:00Z",
        "schemaVersion": "2.0"
    },
    "characters": {
        "katniss-everdeen": {"name": "Katniss Everdeen", "aliases": ["Mockingjay"], "appearances": list(range(1, 28)), "knowledge": {"1": {"revealedIn": 1, "description": "Traumatized symbol of the rebellion in District 13.", "role": "Mockingjay", "relationships": {"Peeta Mellark": "Trying to save", "Alma Coin": "Manipulated by"}}}},
        "alma-coin": {"name": "President Alma Coin", "aliases": [], "appearances": list(range(1, 27)), "knowledge": {"1": {"revealedIn": 1, "description": "President of District 13, ruthless rebel leader.", "role": "President", "relationships": {"Katniss Everdeen": "Uses as symbol"}}}},
        "boggs": {"name": "Boggs", "aliases": [], "appearances": list(range(3, 20)), "knowledge": {"3": {"revealedIn": 3, "description": "Coin's right-hand man who protects Katniss.", "role": "Soldier", "relationships": {"Katniss Everdeen": "Protects"}}}},
        "cressida": {"name": "Cressida", "aliases": [], "appearances": list(range(6, 25)), "knowledge": {"6": {"revealedIn": 6, "description": "Director of rebel propos from the Capitol.", "role": "Director", "relationships": {"Katniss Everdeen": "Films"}}}},
    },
    "recaps": {}
}

# Add more characters
for i in range(146):
    mockingjay["characters"][f"character-{i+1}"] = {
        "name": f"District 13 Resident {i+1}",
        "aliases": [],
        "appearances": [i % 27 + 1],
        "knowledge": {
            "1": {"revealedIn": 1, "description": "Resident or soldier in District 13.", "role": "Resident", "relationships": {}}
        }
    }

for i in range(1, 28):
    mockingjay["recaps"][str(i)] = f"Chapter {i} of Mockingjay follows the rebellion and final confrontation with the Capitol."

with open('data/hunger-games/mockingjay.json', 'w') as f:
    json.dump(mockingjay, f, indent=2)

print(f"Created Mockingjay with {len(mockingjay['characters'])} characters")

# Book 4: The Ballad of Songbirds and Snakes
songbirds = {
    "meta": {
        "title": "The Ballad of Songbirds and Snakes",
        "author": "Suzanne Collins",
        "chapters": 30,
        "createdAt": "2024-01-01T00:00:00Z",
        "schemaVersion": "2.0"
    },
    "characters": {
        "coriolanus-snow": {"name": "Coriolanus Snow", "aliases": ["Coryo"], "appearances": list(range(1, 31)), "knowledge": {"1": {"revealedIn": 1, "description": "18-year-old Capitol student struggling to maintain his family's status.", "role": "Mentor", "relationships": {"Lucy Gray Baird": "Mentors", "Tigris": "Cousin"}}}},
        "lucy-gray-baird": {"name": "Lucy Gray Baird", "aliases": [], "appearances": list(range(2, 31)), "knowledge": {"2": {"revealedIn": 2, "description": "Tribute from District 12, member of the Covey band.", "role": "Tribute", "relationships": {"Coriolanus Snow": "Mentored by"}}}},
        "sejanus-plinth": {"name": "Sejanus Plinth", "aliases": [], "appearances": list(range(1, 25)), "knowledge": {"1": {"revealedIn": 1, "description": "District 2 native at the Capitol Academy, Snow's friend.", "role": "Student", "relationships": {"Coriolanus Snow": "Friend"}}}},
        "dr-gaul": {"name": "Dr. Volumnia Gaul", "aliases": [], "appearances": list(range(5, 28)), "knowledge": {"5": {"revealedIn": 5, "description": "Head Gamemaker and mad scientist.", "role": "Head Gamemaker", "relationships": {"Coriolanus Snow": "Mentors"}}}},
        "tigris": {"name": "Tigris", "aliases": [], "appearances": list(range(1, 30)), "knowledge": {"1": {"revealedIn": 1, "description": "Snow's cousin who works to support their family.", "role": "Cousin", "relationships": {"Coriolanus Snow": "Cousin"}}}},
        "dean-highbottom": {"name": "Dean Casca Highbottom", "aliases": [], "appearances": list(range(1, 28)), "knowledge": {"1": {"revealedIn": 1, "description": "Dean of the Academy, creator of the Hunger Games concept.", "role": "Dean", "relationships": {"Coriolanus Snow": "Dislikes"}}}},
    },
    "recaps": {}
}

# Add more characters
for i in range(145):
    songbirds["characters"][f"character-{i+1}"] = {
        "name": f"10th Games Participant {i+1}",
        "aliases": [],
        "appearances": [i % 30 + 1],
        "knowledge": {
            "1": {"revealedIn": 1, "description": "Participant in the 10th Hunger Games.", "role": "Participant", "relationships": {}}
        }
    }

for i in range(1, 31):
    songbirds["recaps"][str(i)] = f"Chapter {i} of The Ballad of Songbirds and Snakes explores young Snow's transformation into a villain."

with open('data/hunger-games/songbirds-snakes.json', 'w') as f:
    json.dump(songbirds, f, indent=2)

print(f"Created The Ballad of Songbirds and Snakes with {len(songbirds['characters'])} characters")

print("\nAll 4 Hunger Games books created successfully!")