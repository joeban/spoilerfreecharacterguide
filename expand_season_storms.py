#!/usr/bin/env python3
import json

# Load existing data
with open('data/witcher/season-of-storms.json', 'r') as f:
    data = json.load(f)

# Add new characters for Season of Storms - focusing on the standalone adventure's unique cast
new_characters = {
    "kerack-court-noble-lady": {
        "name": "Lady Adelina of Kerack",
        "aliases": ["The Court Beauty"],
        "appearances": [5, 6, 7, 8],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "A beautiful noble lady at the Kerack court who becomes involved in the political intrigue surrounding the royal succession.",
                "role": "Court beauty",
                "relationships": {
                    "Royal Court": "Ornament of",
                    "Political Intrigue": "Unwittingly part of"
                }
            }
        }
    },
    "kerack-court-noble-lord": {
        "name": "Lord Chamberlain Eustace",
        "aliases": ["The Royal Chamberlain"],
        "appearances": [5, 6, 7, 8],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "The royal chamberlain who manages the daily affairs of the Kerack court and serves as a key advisor to the king.",
                "role": "Royal chamberlain",
                "relationships": {
                    "King Belohun": "Chief advisor to",
                    "Court Administration": "Manages"
                }
            }
        }
    },
    "kerack-royal-physician": {
        "name": "Royal Physician Cornelius",
        "aliases": ["The Court Healer"],
        "appearances": [7, 8, 15],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "The royal physician who tends to the health of the royal family and becomes involved in treating those affected by the dangerous mission.",
                "role": "Royal physician",
                "relationships": {
                    "King Belohun": "Personal physician to",
                    "Royal Family": "Medical care for"
                }
            }
        }
    },
    "kerack-royal-treasurer": {
        "name": "Royal Treasurer Moneybags",
        "aliases": ["The Gold Counter"],
        "appearances": [5, 6, 7],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "The royal treasurer who manages the kingdom's finances and often worries about the cost of royal ventures.",
                "role": "Royal treasurer",
                "relationships": {
                    "Kingdom Finances": "Manages",
                    "Royal Spending": "Oversees"
                }
            }
        }
    },
    "kerack-royal-armorer": {
        "name": "Royal Armorer Ironwright",
        "aliases": ["The Weapon Master"],
        "appearances": [5, 6, 7, 8],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "The royal armorer who maintains the weapons and armor of the royal guard and assists in military preparations.",
                "role": "Royal armorer",
                "relationships": {
                    "Royal Guards": "Arms and equips",
                    "Military Preparations": "Supports"
                }
            }
        }
    },
    "ship-prophet-first-mate": {
        "name": "First Mate Seasalt",
        "aliases": ["The Sea Dog"],
        "appearances": [14, 15, 16, 17],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "The experienced first mate of the Ship Prophet who knows the dangerous waters and helps navigate treacherous passages.",
                "role": "Ship's first mate",
                "relationships": {
                    "Captain Wolverstone": "Second-in-command to",
                    "Ship Navigation": "Expert in"
                }
            }
        }
    },
    "ship-prophet-navigator": {
        "name": "Navigator Starwatch",
        "aliases": ["The Star Reader"],
        "appearances": [14, 15, 16, 17],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "The ship's navigator who uses stars and magical instruments to chart courses across dangerous seas.",
                "role": "Ship navigator",
                "relationships": {
                    "Sea Navigation": "Master of",
                    "Star Charts": "Reads and interprets"
                }
            }
        }
    },
    "ship-prophet-passenger-noble": {
        "name": "Noble Passenger Lord Tidecrest",
        "aliases": ["The Traveling Lord"],
        "appearances": [14, 15, 16],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "A traveling noble who becomes a passenger on the Ship Prophet and witnesses Geralt's sea adventures.",
                "role": "Noble passenger",
                "relationships": {
                    "Ship Travel": "Experiences",
                    "High Society": "Represents"
                }
            }
        }
    },
    "ship-prophet-passenger-merchant": {
        "name": "Merchant Passenger Goldcount",
        "aliases": ["The Sea Trader"],
        "appearances": [14, 15, 16],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "A wealthy merchant who travels on the Ship Prophet for business purposes and gets caught up in the adventure.",
                "role": "Merchant passenger",
                "relationships": {
                    "Sea Trade": "Engaged in",
                    "Commercial Interests": "Represents"
                }
            }
        }
    },
    "ship-prophet-crew-rigger": {
        "name": "Ship Rigger Ropemaster",
        "aliases": ["The Line Handler"],
        "appearances": [14, 15, 16],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "A skilled rigger who maintains the ship's rigging and sails, essential for navigating dangerous waters.",
                "role": "Ship rigger",
                "relationships": {
                    "Ship Maintenance": "Responsible for",
                    "Sail Management": "Expert in"
                }
            }
        }
    },
    "rissberg-sorcerer-enchanter": {
        "name": "Enchanter Spellweave",
        "aliases": ["The Item Enchanter"],
        "appearances": [9, 10, 11, 12],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "A sorcerer at Rissberg who specializes in enchanting items and creating magical artifacts for the academy.",
                "role": "Item enchanter",
                "relationships": {
                    "Rissberg Academy": "Enchanter for",
                    "Magical Items": "Creates"
                }
            }
        }
    },
    "rissberg-sorcerer-alchemist": {
        "name": "Alchemist Potionbrew",
        "aliases": ["The Potion Master"],
        "appearances": [9, 10, 11, 12],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "An alchemist at Rissberg who creates potions and conducts dangerous experiments with magical substances.",
                "role": "Academy alchemist",
                "relationships": {
                    "Magical Alchemy": "Practices",
                    "Dangerous Experiments": "Conducts"
                }
            }
        }
    },
    "rissberg-guard-captain": {
        "name": "Guard Captain Ironward",
        "aliases": ["The Academy Guard"],
        "appearances": [9, 10, 11, 12],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "The captain of guards at Rissberg who protects the academy and its dangerous magical research.",
                "role": "Academy guard captain",
                "relationships": {
                    "Rissberg Security": "Commands",
                    "Magical Research": "Protects"
                }
            }
        }
    },
    "rissberg-librarian-keeper": {
        "name": "Librarian Bookward",
        "aliases": ["The Knowledge Keeper"],
        "appearances": [9, 10, 11],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "The librarian at Rissberg who maintains the academy's vast collection of magical tomes and research.",
                "role": "Academy librarian",
                "relationships": {
                    "Magical Knowledge": "Guards",
                    "Research Archives": "Maintains"
                }
            }
        }
    },
    "rissberg-cook-head": {
        "name": "Head Cook Heartymeals",
        "aliases": ["The Academy Cook"],
        "appearances": [9, 10, 11],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "The head cook at Rissberg who prepares meals for the sorcerers and students at the academy.",
                "role": "Academy cook",
                "relationships": {
                    "Academy Life": "Supports",
                    "Daily Meals": "Provides"
                }
            }
        }
    },
    "auction-house-auctioneer": {
        "name": "Master Auctioneer Hammer-Fall",
        "aliases": ["The Sale Master"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "The master auctioneer who conducts the sale of rare and magical items, including items connected to Geralt's stolen swords.",
                "role": "Master auctioneer",
                "relationships": {
                    "Rare Items": "Auctions",
                    "Wealthy Bidders": "Serves"
                }
            }
        }
    },
    "auction-house-appraiser": {
        "name": "Item Appraiser Value-Eye",
        "aliases": ["The Assessor"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "An expert appraiser who evaluates rare items for auction, including magical weapons and artifacts.",
                "role": "Item appraiser",
                "relationships": {
                    "Magical Items": "Evaluates",
                    "Auction Values": "Determines"
                }
            }
        }
    },
    "auction-house-security": {
        "name": "Security Chief Guardwatch",
        "aliases": ["The Vault Guardian"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "The security chief who protects valuable items at the auction house and ensures safe transactions.",
                "role": "Auction security",
                "relationships": {
                    "Valuable Items": "Protects",
                    "Auction Safety": "Ensures"
                }
            }
        }
    },
    "auction-house-bidder-wealthy": {
        "name": "Wealthy Bidder Goldpurse",
        "aliases": ["The High Bidder"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "A wealthy bidder who competes for rare magical items at the auction, representing the elite collectors.",
                "role": "Wealthy collector",
                "relationships": {
                    "Rare Collecting": "Passionate about",
                    "Auction Competition": "Participates in"
                }
            }
        }
    },
    "auction-house-bidder-noble": {
        "name": "Noble Bidder Lord Rarecollect",
        "aliases": ["The Collector Lord"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "A noble collector who seeks rare items for his private collection and becomes involved in bidding wars.",
                "role": "Noble collector",
                "relationships": {
                    "Private Collection": "Builds",
                    "Noble Society": "Represents"
                }
            }
        }
    },
    "borsodi-brother-elder": {
        "name": "Elder Borsodi Brother Firstborn",
        "aliases": ["The Senior Brother"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "The elder of the Borsodi brothers who manages their business operations and criminal connections.",
                "role": "Criminal businessman",
                "relationships": {
                    "Borsodi Operations": "Leads",
                    "Criminal Network": "Manages"
                }
            }
        }
    },
    "borsodi-brother-younger": {
        "name": "Younger Borsodi Brother Secondborn",
        "aliases": ["The Junior Brother"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "The younger Borsodi brother who handles the more dangerous aspects of their criminal enterprises.",
                "role": "Criminal enforcer",
                "relationships": {
                    "Elder Brother": "Works with",
                    "Criminal Violence": "Handles"
                }
            }
        }
    },
    "borsodi-employee-accountant": {
        "name": "Borsodi Accountant Coincount",
        "aliases": ["The Money Counter"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "An accountant who manages the financial records of the Borsodi brothers' legitimate and illegitimate businesses.",
                "role": "Criminal accountant",
                "relationships": {
                    "Borsodi Finances": "Manages",
                    "Criminal Profits": "Tracks"
                }
            }
        }
    },
    "borsodi-security-chief": {
        "name": "Security Chief Musclearm",
        "aliases": ["The Enforcer"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "The security chief who protects Borsodi operations and enforces their will through intimidation and violence.",
                "role": "Criminal enforcer",
                "relationships": {
                    "Borsodi Protection": "Provides",
                    "Criminal Intimidation": "Specializes in"
                }
            }
        }
    },
    "borsodi-warehouse-manager": {
        "name": "Warehouse Manager Storekeeper",
        "aliases": ["The Storage Master"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "The manager of Borsodi warehouses where stolen and smuggled goods are stored before distribution.",
                "role": "Warehouse manager",
                "relationships": {
                    "Stolen Goods": "Stores",
                    "Criminal Logistics": "Manages"
                }
            }
        }
    },
    "festival-performer-acrobat": {
        "name": "Festival Acrobat Flipjump",
        "aliases": ["The High Flyer"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A skilled acrobat who performs amazing feats at the festival, entertaining crowds with death-defying stunts.",
                "role": "Festival acrobat",
                "relationships": {
                    "Festival Crowds": "Entertains",
                    "Acrobatic Arts": "Masters"
                }
            }
        }
    },
    "festival-performer-juggler": {
        "name": "Festival Juggler Manyhands",
        "aliases": ["The Dexterous"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A talented juggler who amazes festival-goers with complex juggling routines using various objects.",
                "role": "Festival juggler",
                "relationships": {
                    "Festival Entertainment": "Provides",
                    "Juggling Arts": "Masters"
                }
            }
        }
    },
    "festival-performer-dancer": {
        "name": "Festival Dancer Gracestep",
        "aliases": ["The Elegant Mover"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A graceful dancer who performs traditional and exotic dances at the festival, captivating audiences.",
                "role": "Festival dancer",
                "relationships": {
                    "Dance Arts": "Masters",
                    "Cultural Traditions": "Preserves"
                }
            }
        }
    },
    "festival-merchant-food": {
        "name": "Food Merchant Tastygood",
        "aliases": ["The Feast Provider"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A food merchant who sells delicious meals and treats to festival-goers, representing the commercial side of celebrations.",
                "role": "Food vendor",
                "relationships": {
                    "Festival Goers": "Feeds",
                    "Food Commerce": "Engaged in"
                }
            }
        }
    },
    "festival-merchant-trinkets": {
        "name": "Trinket Merchant Prettyshine",
        "aliases": ["The Bauble Seller"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A merchant who sells small trinkets, jewelry, and souvenirs to festival visitors as mementos of the celebration.",
                "role": "Trinket vendor",
                "relationships": {
                    "Festival Commerce": "Participates in",
                    "Souvenir Trade": "Specializes in"
                }
            }
        }
    },
    "festival-guard-peace": {
        "name": "Festival Peacekeeper Orderkeep",
        "aliases": ["The Crowd Controller"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A guard who maintains order during the festival, ensuring celebrations remain peaceful and safe for all participants.",
                "role": "Festival security",
                "relationships": {
                    "Festival Order": "Maintains",
                    "Crowd Safety": "Ensures"
                }
            }
        }
    },
    "insurance-investigator": {
        "name": "Insurance Investigator Clueseek",
        "aliases": ["The Claim Hunter"],
        "appearances": [19, 20, 21],
        "knowledge": {
            "19": {
                "revealedIn": 19,
                "description": "An insurance investigator who looks into claims related to Geralt's stolen swords and becomes involved in the case.",
                "role": "Insurance investigator",
                "relationships": {
                    "Insurance Claims": "Investigates",
                    "Theft Cases": "Specializes in"
                }
            }
        }
    },
    "insurance-clerk": {
        "name": "Insurance Clerk Paperwork",
        "aliases": ["The Record Keeper"],
        "appearances": [19, 20, 21],
        "knowledge": {
            "19": {
                "revealedIn": 19,
                "description": "A clerk who handles insurance paperwork and documentation related to valuable item theft and recovery.",
                "role": "Insurance clerk",
                "relationships": {
                    "Insurance Records": "Maintains",
                    "Claim Processing": "Handles"
                }
            }
        }
    },
    "insurance-assessor": {
        "name": "Insurance Assessor Value-Judge",
        "aliases": ["The Damage Evaluator"],
        "appearances": [19, 20, 21],
        "knowledge": {
            "19": {
                "revealedIn": 19,
                "description": "An assessor who evaluates the value of stolen items for insurance purposes, including magical weapons.",
                "role": "Insurance assessor",
                "relationships": {
                    "Item Valuation": "Specializes in",
                    "Damage Assessment": "Conducts"
                }
            }
        }
    },
    "pirate-captain-smuggler": {
        "name": "Pirate Captain Blacksail",
        "aliases": ["The Sea Raider"],
        "appearances": [14, 15, 16, 17],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "A pirate captain who operates in the waters where Geralt travels, representing the lawless elements of the seas.",
                "role": "Pirate captain",
                "relationships": {
                    "Sea Lawlessness": "Represents",
                    "Maritime Crime": "Leads"
                }
            }
        }
    },
    "pirate-first-mate": {
        "name": "Pirate First Mate Cutlass",
        "aliases": ["The Blade Master"],
        "appearances": [14, 15, 16, 17],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "The first mate of the pirate crew who serves as the captain's right hand in raids and nautical operations.",
                "role": "Pirate first mate",
                "relationships": {
                    "Pirate Captain": "Right hand of",
                    "Pirate Crew": "Leads in action"
                }
            }
        }
    },
    "smuggler-ring-leader": {
        "name": "Smuggling Leader Contraband",
        "aliases": ["The Shadow Trader"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "The leader of a smuggling ring who deals in illegal goods and potentially stolen magical items.",
                "role": "Smuggling leader",
                "relationships": {
                    "Illegal Trade": "Controls",
                    "Contraband Network": "Manages"
                }
            }
        }
    },
    "smuggler-courier": {
        "name": "Smuggling Courier Fastrun",
        "aliases": ["The Message Runner"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "A courier who carries messages and small contraband items for the smuggling network, operating in secret.",
                "role": "Smuggling courier",
                "relationships": {
                    "Smuggling Network": "Serves",
                    "Secret Messages": "Carries"
                }
            }
        }
    },
    "assassin-guild-master": {
        "name": "Guild Master Shadowstrike",
        "aliases": ["The Silent Death"],
        "appearances": [20, 21, 22],
        "knowledge": {
            "20": {
                "revealedIn": 20,
                "description": "The master of an assassin's guild who becomes involved in the complex web surrounding Geralt's stolen swords.",
                "role": "Assassin guild master",
                "relationships": {
                    "Professional Killers": "Leads",
                    "Shadow Operations": "Controls"
                }
            }
        }
    },
    "assassin-guild-trainer": {
        "name": "Assassin Trainer Blade-Teach",
        "aliases": ["The Skill Master"],
        "appearances": [20, 21, 22],
        "knowledge": {
            "20": {
                "revealedIn": 20,
                "description": "A trainer who teaches assassination skills to guild members, representing the professional development of killers.",
                "role": "Assassin trainer",
                "relationships": {
                    "Guild Assassins": "Trains",
                    "Killing Arts": "Masters"
                }
            }
        }
    },
    "assassin-guild-informant": {
        "name": "Guild Informant Whisper-Ear",
        "aliases": ["The Information Broker"],
        "appearances": [20, 21, 22],
        "knowledge": {
            "20": {
                "revealedIn": 20,
                "description": "An informant who gathers intelligence for the assassin's guild, providing information on targets and opportunities.",
                "role": "Guild informant",
                "relationships": {
                    "Information Network": "Maintains",
                    "Target Intelligence": "Gathers"
                }
            }
        }
    },
    "lytta-servant-maid": {
        "name": "Coral's Maid Tidyneat",
        "aliases": ["The Faithful Servant"],
        "appearances": [3, 4, 5, 6, 7, 8, 9],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "Lytta Neyd's personal maid who serves the sorceress and witnesses her relationship with Geralt develop.",
                "role": "Personal maid",
                "relationships": {
                    "Lytta Neyd": "Personal servant of",
                    "Household Management": "Responsible for"
                }
            }
        }
    },
    "lytta-butler-steward": {
        "name": "Coral's Steward Housekeep",
        "aliases": ["The Manor Manager"],
        "appearances": [3, 4, 5, 6, 7, 8, 9],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "The steward who manages Lytta Neyd's household and property, ensuring everything runs smoothly for the sorceress.",
                "role": "Household steward",
                "relationships": {
                    "Lytta Neyd": "Manages household for",
                    "Estate Management": "Oversees"
                }
            }
        }
    },
    "lytta-guard-bodyguard": {
        "name": "Coral's Bodyguard Strongarm",
        "aliases": ["The Protector"],
        "appearances": [3, 4, 5, 6, 7, 8, 9],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "A bodyguard who protects Lytta Neyd from physical threats, representing the mundane security even powerful sorceresses need.",
                "role": "Sorceress bodyguard",
                "relationships": {
                    "Lytta Neyd": "Protects",
                    "Physical Security": "Provides"
                }
            }
        }
    }
}

# Add characters to existing data
for char_id, char_data in new_characters.items():
    data['characters'][char_id] = char_data

print(f"Adding {len(new_characters)} characters to Season of Storms")
print(f"New total: {len(data['characters'])} characters")

# Save updated data
with open('data/witcher/season-of-storms.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✅ Season of Storms expanded with first batch of characters!")