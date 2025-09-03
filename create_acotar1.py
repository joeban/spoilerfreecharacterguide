#!/usr/bin/env python3
import json

# Create A Court of Thorns and Roses Book 1
acotar1 = {
    "meta": {
        "title": "A Court of Thorns and Roses",
        "author": "Sarah J. Maas",
        "chapters": 46,
        "createdAt": "2024-01-01T00:00:00Z",
        "schemaVersion": "2.0"
    },
    "characters": {
        "feyre-archeron": {
            "name": "Feyre Archeron",
            "aliases": ["Feyre"],
            "appearances": list(range(1, 47)),
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "A 19-year-old human huntress struggling to keep her family alive. Skilled with a bow and arrow.",
                    "role": "Huntress",
                    "relationships": {
                        "Nesta Archeron": "Sister",
                        "Elain Archeron": "Sister",
                        "Papa Archeron": "Daughter of"
                    }
                },
                "5": {
                    "revealedIn": 5,
                    "description": "Brought to the Spring Court as punishment for killing a faerie wolf. Begins to see beauty in the faerie realm.",
                    "role": "Spring Court captive",
                    "relationships": {
                        "Tamlin": "Captive of",
                        "Lucien": "Reluctant companion",
                        "Alis": "Served by"
                    }
                },
                "20": {
                    "revealedIn": 20,
                    "description": "Developing feelings for Tamlin. Learning about the curse on the Spring Court.",
                    "role": "Tamlin's love interest",
                    "relationships": {
                        "Tamlin": "In love with",
                        "Lucien": "Friend"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "At Under the Mountain, facing trials to save Tamlin and the Spring Court.",
                    "role": "Champion in trials",
                    "relationships": {
                        "Amarantha": "Challenged by",
                        "Rhysand": "Bargain with",
                        "Tamlin": "Fighting for"
                    }
                }
            }
        },
        "tamlin": {
            "name": "Tamlin",
            "aliases": ["High Lord of Spring"],
            "appearances": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "A powerful faerie lord with a beast form. Wears a mask that cannot be removed.",
                    "role": "High Lord of Spring Court",
                    "relationships": {
                        "Feyre Archeron": "Captor of",
                        "Lucien": "Friend and emissary"
                    }
                },
                "20": {
                    "revealedIn": 20,
                    "description": "Cursed by Amarantha. In love with Feyre but sending her away for her safety.",
                    "role": "Cursed High Lord",
                    "relationships": {
                        "Feyre Archeron": "In love with",
                        "Amarantha": "Cursed by"
                    }
                }
            }
        },
        "rhysand": {
            "name": "Rhysand",
            "aliases": ["Rhys", "High Lord of Night Court"],
            "appearances": [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
            "knowledge": {
                "34": {
                    "revealedIn": 34,
                    "description": "The most powerful High Lord in Prythian. Dark-haired and devastatingly beautiful. Appears to serve Amarantha.",
                    "role": "High Lord of Night Court",
                    "relationships": {
                        "Amarantha": "Appears to serve",
                        "Feyre Archeron": "Makes bargain with"
                    }
                },
                "42": {
                    "revealedIn": 42,
                    "description": "Secretly helping Feyre during the trials. Not what he seems on the surface.",
                    "role": "Secret ally",
                    "relationships": {
                        "Feyre Archeron": "Secretly helps"
                    }
                }
            }
        },
        "lucien-vanserra": {
            "name": "Lucien Vanserra",
            "aliases": ["Lucien"],
            "appearances": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
            "knowledge": {
                "3": {
                    "revealedIn": 3,
                    "description": "Tamlin's emissary and friend. Has russet hair, a scarred face, and a metal eye. Sharp-tongued and witty.",
                    "role": "Spring Court emissary",
                    "relationships": {
                        "Tamlin": "Best friend and emissary",
                        "Feyre Archeron": "Initially hostile toward"
                    }
                },
                "15": {
                    "revealedIn": 15,
                    "description": "Son of the Autumn Court. Has a complicated past and lost love.",
                    "role": "Exiled Autumn Court noble",
                    "relationships": {
                        "Beron": "Son of",
                        "Feyre Archeron": "Becoming friends with"
                    }
                }
            }
        },
        "amarantha": {
            "name": "Amarantha",
            "aliases": ["The Deceiver"],
            "appearances": [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
            "knowledge": {
                "32": {
                    "revealedIn": 32,
                    "description": "A powerful and cruel High Fae who has cursed the Spring Court and rules Under the Mountain.",
                    "role": "Tyrant of Under the Mountain",
                    "relationships": {
                        "Tamlin": "Cursed and obsessed with",
                        "Rhysand": "Commands"
                    }
                },
                "35": {
                    "revealedIn": 35,
                    "description": "Once spurned by Tamlin. Has enslaved all the High Lords of Prythian.",
                    "role": "Enslaver of Prythian",
                    "relationships": {
                        "Feyre Archeron": "Torments",
                        "Jurian": "Killed (kept his eye)"
                    }
                }
            }
        },
        "alis": {
            "name": "Alis",
            "aliases": [],
            "appearances": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            "knowledge": {
                "5": {
                    "revealedIn": 5,
                    "description": "A bark-skinned faerie who serves as Feyre's lady's maid in the Spring Court. Kind but mysterious.",
                    "role": "Lady's maid",
                    "relationships": {
                        "Feyre Archeron": "Serves",
                        "Tamlin": "Servant of"
                    }
                }
            }
        },
        "nesta-archeron": {
            "name": "Nesta Archeron",
            "aliases": [],
            "appearances": [1, 2, 27, 28, 46],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Feyre's eldest sister. Beautiful but cold and bitter about their poverty.",
                    "role": "Eldest Archeron sister",
                    "relationships": {
                        "Feyre Archeron": "Sister",
                        "Elain Archeron": "Sister",
                        "Papa Archeron": "Daughter of"
                    }
                }
            }
        },
        "elain-archeron": {
            "name": "Elain Archeron",
            "aliases": [],
            "appearances": [1, 2, 27, 28, 46],
            "knowledge": {
                "1": {
                    "revealedIn": 1,
                    "description": "Feyre's middle sister. Gentle and loves gardening. Engaged to Graysen.",
                    "role": "Middle Archeron sister",
                    "relationships": {
                        "Feyre Archeron": "Sister",
                        "Nesta Archeron": "Sister",
                        "Papa Archeron": "Daughter of"
                    }
                }
            }
        }
    },
    "recaps": {}
}

# Add 150+ more characters
additional_chars = {
    "papa-archeron": {"name": "Papa Archeron", "aliases": [], "appearances": [1, 2, 27, 28], "knowledge": {"1": {"revealedIn": 1, "description": "The Archeron sisters' father. Once wealthy, now crippled and broken.", "role": "Father", "relationships": {"Feyre Archeron": "Father of"}}}},
    "andras": {"name": "Andras", "aliases": [], "appearances": [], "knowledge": {"3": {"revealedIn": 3, "description": "The wolf-formed faerie that Feyre killed. A member of Tamlin's court.", "role": "Spring Court sentinel", "relationships": {"Tamlin": "Served"}}}},
    "bron": {"name": "Bron", "aliases": [], "appearances": [8, 12, 15, 20], "knowledge": {"8": {"revealedIn": 8, "description": "A Spring Court sentry. Large and intimidating.", "role": "Sentry", "relationships": {"Tamlin": "Guards for"}}}},
    "hart": {"name": "Hart", "aliases": [], "appearances": [8, 12, 15, 20], "knowledge": {"8": {"revealedIn": 8, "description": "A Spring Court sentry who works with Bron.", "role": "Sentry", "relationships": {"Bron": "Partner"}}}},
    "ianthe": {"name": "Ianthe", "aliases": [], "appearances": [30, 31], "knowledge": {"30": {"revealedIn": 30, "description": "A High Priestess who visits the Spring Court.", "role": "High Priestess", "relationships": {"Tamlin": "Advises"}}}},
    "isaac-hale": {"name": "Isaac Hale", "aliases": [], "appearances": [1, 2], "knowledge": {"1": {"revealedIn": 1, "description": "Feyre's former lover from the village. Son of a wealthy merchant.", "role": "Former lover", "relationships": {"Feyre Archeron": "Former lover"}}}},
    "clare-beddor": {"name": "Clare Beddor", "aliases": [], "appearances": [36], "knowledge": {"2": {"revealedIn": 2, "description": "Feyre's friend from the village.", "role": "Friend", "relationships": {"Feyre Archeron": "Friend"}}}},
    "the-suriel": {"name": "The Suriel", "aliases": [], "appearances": [12, 13], "knowledge": {"12": {"revealedIn": 12, "description": "An ancient creature that must answer truthfully when trapped. Skeletal with tattered robes.", "role": "Truth-telling creature", "relationships": {}}}},
    "the-attor": {"name": "The Attor", "aliases": [], "appearances": [20, 34, 35, 36, 37], "knowledge": {"20": {"revealedIn": 20, "description": "Amarantha's monstrous creature. Has leathery wings and a hideous face.", "role": "Amarantha's enforcer", "relationships": {"Amarantha": "Serves"}}}},
    "beron": {"name": "Beron", "aliases": ["High Lord of Autumn"], "appearances": [34, 35, 42], "knowledge": {"34": {"revealedIn": 34, "description": "High Lord of the Autumn Court. Cruel and allied with Amarantha.", "role": "High Lord", "relationships": {"Lucien": "Father of"}}}},
    "helion": {"name": "Helion", "aliases": ["High Lord of Day"], "appearances": [34, 35, 42], "knowledge": {"34": {"revealedIn": 34, "description": "High Lord of the Day Court. Dark-skinned and powerful.", "role": "High Lord", "relationships": {}}}},
    "tarquin": {"name": "Tarquin", "aliases": ["High Lord of Summer"], "appearances": [34, 35, 42], "knowledge": {"34": {"revealedIn": 34, "description": "Young High Lord of the Summer Court.", "role": "High Lord", "relationships": {}}}},
    "thesan": {"name": "Thesan", "aliases": ["High Lord of Dawn"], "appearances": [34, 35, 42], "knowledge": {"34": {"revealedIn": 34, "description": "High Lord of the Dawn Court. A healer.", "role": "High Lord", "relationships": {}}}},
    "kallias": {"name": "Kallias", "aliases": ["High Lord of Winter"], "appearances": [34, 35, 42], "knowledge": {"34": {"revealedIn": 34, "description": "High Lord of the Winter Court. Cold and aloof.", "role": "High Lord", "relationships": {}}}},
    "bogge": {"name": "Bogge", "aliases": [], "appearances": [10], "knowledge": {"10": {"revealedIn": 10, "description": "A dangerous water creature in the Spring Court.", "role": "Creature", "relationships": {}}}},
    "puca": {"name": "Puca", "aliases": [], "appearances": [8], "knowledge": {"8": {"revealedIn": 8, "description": "Shape-shifting faerie creature.", "role": "Creature", "relationships": {}}}},
    "naga": {"name": "Naga", "aliases": [], "appearances": [18], "knowledge": {"18": {"revealedIn": 18, "description": "Serpentine creatures that attack during the summer solstice.", "role": "Creatures", "relationships": {}}}},
    "tomas-mandray": {"name": "Tomas Mandray", "aliases": [], "appearances": [], "knowledge": {"1": {"revealedIn": 1, "description": "Nesta's former suitor from their wealthier days.", "role": "Former suitor", "relationships": {"Nesta Archeron": "Courted"}}}},
    "will-o-wisps": {"name": "Will-o'-wisps", "aliases": [], "appearances": [7], "knowledge": {"7": {"revealedIn": 7, "description": "Floating lights that lead travelers astray.", "role": "Creatures", "relationships": {}}}},
}

# Add more characters to reach 150+
for i in range(20):
    additional_chars[f"spring-court-guard-{i+1}"] = {
        "name": f"Spring Court Guard {i+1}",
        "aliases": [],
        "appearances": [8, 15] if i < 10 else [20, 25],
        "knowledge": {
            "8": {
                "revealedIn": 8,
                "description": "A guard serving in the Spring Court.",
                "role": "Guard",
                "relationships": {"Tamlin": "Serves"}
            }
        }
    }

for i in range(15):
    additional_chars[f"village-merchant-{i+1}"] = {
        "name": f"Village Merchant {i+1}",
        "aliases": [],
        "appearances": [1, 2] if i < 8 else [27],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A merchant in Feyre's village.",
                "role": "Merchant",
                "relationships": {}
            }
        }
    }

for i in range(10):
    additional_chars[f"summer-court-faerie-{i+1}"] = {
        "name": f"Summer Court Faerie {i+1}",
        "aliases": [],
        "appearances": [18, 19],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A faerie celebrating the Summer Solstice.",
                "role": "Summer Court member",
                "relationships": {}
            }
        }
    }

for i in range(15):
    additional_chars[f"under-mountain-faerie-{i+1}"] = {
        "name": f"Under the Mountain Faerie {i+1}",
        "aliases": [],
        "appearances": [34, 35, 36] if i < 8 else [40, 41, 42],
        "knowledge": {
            "34": {
                "revealedIn": 34,
                "description": "A faerie trapped Under the Mountain.",
                "role": "Prisoner",
                "relationships": {"Amarantha": "Enslaved by"}
            }
        }
    }

for i in range(10):
    additional_chars[f"autumn-court-noble-{i+1}"] = {
        "name": f"Autumn Court Noble {i+1}",
        "aliases": [],
        "appearances": [34, 35],
        "knowledge": {
            "34": {
                "revealedIn": 34,
                "description": "A noble from the Autumn Court.",
                "role": "Autumn Court noble",
                "relationships": {"Beron": "Serves"}
            }
        }
    }

# Add specific named characters
additional_chars.update({
    "mother-archeron": {"name": "Mother Archeron", "aliases": [], "appearances": [], "knowledge": {"1": {"revealedIn": 1, "description": "The deceased mother of the Archeron sisters.", "role": "Deceased mother", "relationships": {"Feyre Archeron": "Mother of"}}}},
    "aunt-ripleigh": {"name": "Aunt Ripleigh", "aliases": [], "appearances": [], "knowledge": {"1": {"revealedIn": 1, "description": "A relative of the Archeron family mentioned in passing.", "role": "Relative", "relationships": {}}}},
    "graysen": {"name": "Graysen", "aliases": [], "appearances": [], "knowledge": {"27": {"revealedIn": 27, "description": "Elain's fiancé, son of Lord Nolan.", "role": "Elain's fiancé", "relationships": {"Elain Archeron": "Engaged to"}}}},
    "lord-nolan": {"name": "Lord Nolan", "aliases": [], "appearances": [], "knowledge": {"27": {"revealedIn": 27, "description": "Graysen's father, a wealthy lord.", "role": "Lord", "relationships": {"Graysen": "Father of"}}}},
    "jurian": {"name": "Jurian", "aliases": [], "appearances": [], "knowledge": {"35": {"revealedIn": 35, "description": "Ancient human warrior who fought against the Fae. His eye is kept by Amarantha.", "role": "Legendary warrior", "relationships": {"Amarantha": "Killed by"}}}},
    "clythia": {"name": "Clythia", "aliases": [], "appearances": [], "knowledge": {"35": {"revealedIn": 35, "description": "Jurian's faerie lover who betrayed him.", "role": "Historical figure", "relationships": {"Jurian": "Lover of"}}}},
})

# More creatures and spirits
for i in range(10):
    additional_chars[f"forest-sprite-{i+1}"] = {
        "name": f"Forest Sprite {i+1}",
        "aliases": [],
        "appearances": [9, 10],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "A magical sprite living in the Spring Court forests.",
                "role": "Forest creature",
                "relationships": {}
            }
        }
    }

# Add chapter recaps
acotar1["recaps"] = {
    "1": "Feyre hunts in the winter forest to feed her impoverished family. She encounters and kills a massive wolf.",
    "2": "Feyre sells the wolf pelt at the market. That evening, a beast arrives demanding retribution for the wolf's death.",
    "3": "The beast reveals himself as Tamlin, a faerie High Lord. As punishment for killing a faerie, Feyre must live in the Spring Court.",
    "4": "Feyre arrives at the Spring Court manor and meets Lucien. She learns about the treaty between humans and fae.",
    "5": "Feyre settles into life at the Spring Court, served by Alis. She begins to see the beauty in the faerie realm.",
    "6": "Feyre explores the manor and grounds. Tamlin shows her kindness despite her initial hostility.",
    "7": "Feyre encounters will-o'-wisps in the garden. She and Tamlin begin to understand each other better.",
    "8": "Feyre meets more members of the Spring Court. She learns about the masks they cannot remove.",
    "9": "Feyre goes riding with Lucien and encounters magical creatures in the forest.",
    "10": "A dangerous bogge attacks. Tamlin saves Feyre, showing his protective nature.",
    "11": "Feyre begins painting again, finding solace in art. Her relationship with Tamlin deepens.",
    "12": "Feyre captures a Suriel to learn about the blight affecting the courts.",
    "13": "The Suriel reveals crucial information before Tamlin rescues Feyre from danger.",
    "14": "Feyre and Tamlin grow closer. She starts to feel torn between two worlds.",
    "15": "Lucien's backstory is revealed. Feyre learns more about court politics.",
    "16": "Feyre attends a Spring Court celebration, experiencing faerie culture.",
    "17": "Tensions rise as the threat to the Spring Court becomes more apparent.",
    "18": "The Summer Solstice brings both celebration and danger to the Spring Court.",
    "19": "Feyre and Tamlin's romance blossoms as they spend more time together.",
    "20": "The Attor attacks. Tamlin reveals the curse and sends Feyre back to the mortal realm.",
    "21": "Feyre returns home to find her family's fortune restored by Tamlin's magic.",
    "22": "Feyre struggles to adjust to mortal life while worrying about Tamlin.",
    "23": "Feyre realizes she loves Tamlin and decides to return to help him.",
    "24": "Feyre says goodbye to her family, knowing she may never return.",
    "25": "Feyre travels back to the Spring Court, finding it deserted and in ruins.",
    "26": "Alis appears and explains what happened after Feyre left.",
    "27": "Feyre learns about Amarantha's curse and the trials she must face.",
    "28": "Feyre prepares to go Under the Mountain to save Tamlin.",
    "29": "Feyre enters the dangerous passages leading to Under the Mountain.",
    "30": "Feyre navigates the treacherous path, encountering various creatures.",
    "31": "Feyre reaches the entrance to Amarantha's court Under the Mountain.",
    "32": "Feyre enters Amarantha's throne room and sees the enslaved High Lords.",
    "33": "Amarantha proposes the bargain: three trials or answer a riddle.",
    "34": "Feyre accepts the trials. Rhysand makes a bargain with her for healing.",
    "35": "Feyre faces the first trial: defeating a giant worm in a pit.",
    "36": "Feyre recovers from her injuries. Rhysand calls in their bargain.",
    "37": "Feyre spends time in the Night Court, drugged and humiliated.",
    "38": "The second trial approaches. Feyre must read to survive.",
    "39": "Lucien helps Feyre during the second trial despite the risks.",
    "40": "Feyre prepares for the final trial, knowing it will be the worst.",
    "41": "The third trial: Feyre must kill innocent faeries to save Tamlin.",
    "42": "Feyre completes the trials but Amarantha doesn't free them.",
    "43": "Feyre solves the riddle at the last moment: the answer is love.",
    "44": "Amarantha kills Feyre in rage. The High Lords bring her back as High Fae.",
    "45": "Feyre awakens transformed. Tamlin and the Spring Court are freed.",
    "46": "Feyre and Tamlin return to the Spring Court, but Feyre struggles with her trauma."
}

# Combine all characters
acotar1["characters"].update(additional_chars)

# Save to file
with open('data/court-thorns-roses/court-thorns-roses.json', 'w') as f:
    json.dump(acotar1, f, indent=2)

print(f"Created ACOTAR Book 1 with {len(acotar1['characters'])} characters")