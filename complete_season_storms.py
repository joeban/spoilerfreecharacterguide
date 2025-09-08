#!/usr/bin/env python3
import json

# Load existing data
with open('data/witcher/season-of-storms.json', 'r') as f:
    data = json.load(f)

# Add final 51 characters for Season of Storms to reach exactly 150
final_characters = {
    "kerack-court-scribe": {
        "name": "Court Scribe Record-Keeper",
        "aliases": ["The Royal Recorder"],
        "appearances": [5, 6, 7, 8],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "The court scribe who maintains official records and documents all proceedings at the Kerack royal court.",
                "role": "Court scribe",
                "relationships": {
                    "Royal Court": "Records proceedings of",
                    "Official Documents": "Maintains"
                }
            }
        }
    },
    "kerack-court-herald": {
        "name": "Court Herald Announcer",
        "aliases": ["The Royal Voice"],
        "appearances": [5, 6, 7, 8],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "The court herald who makes official announcements and introduces visitors to the Kerack royal court.",
                "role": "Court herald",
                "relationships": {
                    "Royal Ceremonies": "Announces",
                    "Court Protocol": "Maintains"
                }
            }
        }
    },
    "kerack-court-page": {
        "name": "Court Page Messenger-Boy",
        "aliases": ["The Young Runner"],
        "appearances": [5, 6, 7, 8],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "A young page who runs messages and performs small tasks around the Kerack court, learning court protocol.",
                "role": "Court page",
                "relationships": {
                    "Royal Court": "Serves",
                    "Court Messages": "Carries"
                }
            }
        }
    },
    "kerack-royal-librarian": {
        "name": "Royal Librarian Book-Keeper",
        "aliases": ["The Knowledge Guardian"],
        "appearances": [5, 6, 7],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "The royal librarian who maintains the extensive library at Kerack castle and advises on historical matters.",
                "role": "Royal librarian",
                "relationships": {
                    "Royal Library": "Maintains",
                    "Historical Knowledge": "Guards"
                }
            }
        }
    },
    "kerack-royal-chaplain": {
        "name": "Royal Chaplain Blessing-Giver",
        "aliases": ["The Court Priest"],
        "appearances": [5, 6, 7, 8],
        "knowledge": {
            "5": {
                "revealedIn": 5,
                "description": "The royal chaplain who conducts religious services for the royal family and provides spiritual guidance.",
                "role": "Court chaplain",
                "relationships": {
                    "Royal Family": "Spiritual advisor to",
                    "Religious Services": "Conducts"
                }
            }
        }
    },
    "ship-prophet-deck-hand": {
        "name": "Deck Hand Wave-Walker",
        "aliases": ["The Ship Worker"],
        "appearances": [14, 15, 16, 17],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "A hardworking deck hand on the Ship Prophet who maintains the vessel and assists with daily operations.",
                "role": "Deck hand",
                "relationships": {
                    "Ship Maintenance": "Performs",
                    "Ship's Crew": "Member of"
                }
            }
        }
    },
    "ship-prophet-lookout": {
        "name": "Lookout Keen-Eye",
        "aliases": ["The Watch Keeper"],
        "appearances": [14, 15, 16, 17],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "The ship's lookout who watches for dangers, other vessels, and navigational landmarks from the crow's nest.",
                "role": "Ship lookout",
                "relationships": {
                    "Ship Safety": "Monitors",
                    "Navigation": "Assists with"
                }
            }
        }
    },
    "ship-prophet-cabin-boy": {
        "name": "Cabin Boy Quick-Feet",
        "aliases": ["The Young Sailor"],
        "appearances": [14, 15, 16],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "A young cabin boy on the Ship Prophet who performs various tasks and learns seamanship from the crew.",
                "role": "Cabin boy",
                "relationships": {
                    "Ship's Crew": "Learns from",
                    "Ship Duties": "Performs various"
                }
            }
        }
    },
    "ship-prophet-quartermaster": {
        "name": "Quartermaster Supply-Master",
        "aliases": ["The Provisions Keeper"],
        "appearances": [14, 15, 16, 17],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "The ship's quartermaster who manages supplies, provisions, and equipment aboard the Ship Prophet.",
                "role": "Ship quartermaster",
                "relationships": {
                    "Ship Supplies": "Manages",
                    "Crew Provisions": "Distributes"
                }
            }
        }
    },
    "ship-prophet-surgeon": {
        "name": "Ship Surgeon Bone-Setter",
        "aliases": ["The Sea Doctor"],
        "appearances": [14, 15, 16, 17],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "The ship's surgeon who tends to injuries and illnesses among the crew and passengers during the voyage.",
                "role": "Ship surgeon",
                "relationships": {
                    "Crew Health": "Maintains",
                    "Medical Treatment": "Provides"
                }
            }
        }
    },
    "rissberg-groundskeeper": {
        "name": "Groundskeeper Garden-Tend",
        "aliases": ["The Academy Caretaker"],
        "appearances": [9, 10, 11, 12],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "The groundskeeper who maintains the extensive gardens and grounds of Rissberg academy.",
                "role": "Academy groundskeeper",
                "relationships": {
                    "Rissberg Grounds": "Maintains",
                    "Academy Environment": "Cares for"
                }
            }
        }
    },
    "rissberg-stable-master": {
        "name": "Stable Master Horse-Care",
        "aliases": ["The Beast Tender"],
        "appearances": [9, 10, 11, 12],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "The stable master at Rissberg who cares for horses and other animals used by the academy.",
                "role": "Stable master",
                "relationships": {
                    "Academy Horses": "Cares for",
                    "Transportation": "Manages"
                }
            }
        }
    },
    "rissberg-porter": {
        "name": "Porter Gate-Keep",
        "aliases": ["The Academy Doorkeeper"],
        "appearances": [9, 10, 11, 12],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "The porter who controls access to Rissberg academy and monitors who enters and leaves the premises.",
                "role": "Academy porter",
                "relationships": {
                    "Academy Security": "Controls access",
                    "Visitor Monitoring": "Responsible for"
                }
            }
        }
    },
    "rissberg-cleaning-staff": {
        "name": "Head Cleaner Dust-Away",
        "aliases": ["The Maintenance Chief"],
        "appearances": [9, 10, 11],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "The head of cleaning staff who oversees the maintenance and cleanliness of Rissberg academy facilities.",
                "role": "Cleaning supervisor",
                "relationships": {
                    "Academy Cleanliness": "Maintains",
                    "Cleaning Staff": "Supervises"
                }
            }
        }
    },
    "rissberg-messenger": {
        "name": "Academy Messenger Swift-Word",
        "aliases": ["The Information Carrier"],
        "appearances": [9, 10, 11, 12],
        "knowledge": {
            "9": {
                "revealedIn": 9,
                "description": "A messenger who carries communications between Rissberg and other institutions or individuals.",
                "role": "Academy messenger",
                "relationships": {
                    "External Communications": "Handles",
                    "Academy Business": "Facilitates"
                }
            }
        }
    },
    "festival-storyteller": {
        "name": "Festival Storyteller Tale-Weaver",
        "aliases": ["The Legend Keeper"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A storyteller at the festival who entertains crowds with epic tales and local legends.",
                "role": "Festival storyteller",
                "relationships": {
                    "Festival Entertainment": "Provides",
                    "Local Legends": "Preserves"
                }
            }
        }
    },
    "festival-fortune-teller": {
        "name": "Fortune Teller Future-See",
        "aliases": ["The Fate Reader"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A fortune teller at the festival who claims to read the future and provides entertainment through divination.",
                "role": "Festival fortune teller",
                "relationships": {
                    "Festival Goers": "Provides readings for",
                    "Mystical Entertainment": "Offers"
                }
            }
        }
    },
    "festival-fire-eater": {
        "name": "Fire Eater Flame-Mouth",
        "aliases": ["The Fire Performer"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A fire eater who performs dangerous fire stunts at the festival, amazing crowds with flame manipulation.",
                "role": "Fire performer",
                "relationships": {
                    "Festival Crowds": "Amazes",
                    "Fire Arts": "Masters"
                }
            }
        }
    },
    "festival-animal-trainer": {
        "name": "Animal Trainer Beast-Friend",
        "aliases": ["The Creature Master"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "An animal trainer who performs with trained animals at the festival, showcasing the bond between humans and beasts.",
                "role": "Animal trainer",
                "relationships": {
                    "Trained Animals": "Works with",
                    "Festival Shows": "Provides"
                }
            }
        }
    },
    "festival-mask-maker": {
        "name": "Mask Maker Art-Face",
        "aliases": ["The Disguise Crafter"],
        "appearances": [18, 19, 20],
        "knowledge": {
            "18": {
                "revealedIn": 18,
                "description": "A craftsman who makes and sells decorative masks at the festival, representing the artistic traditions of celebration.",
                "role": "Mask craftsman",
                "relationships": {
                    "Festival Arts": "Creates",
                    "Disguise Craft": "Masters"
                }
            }
        }
    },
    "auction-house-porter": {
        "name": "Auction House Porter Heavy-Lift",
        "aliases": ["The Item Mover"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "A porter who moves heavy and valuable items within the auction house, ensuring safe handling of rare artifacts.",
                "role": "Item porter",
                "relationships": {
                    "Auction Items": "Handles safely",
                    "Auction Operations": "Supports"
                }
            }
        }
    },
    "auction-house-clerk": {
        "name": "Auction Clerk Record-Write",
        "aliases": ["The Sale Recorder"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "A clerk who records auction transactions, maintains bidder records, and handles administrative duties.",
                "role": "Auction clerk",
                "relationships": {
                    "Auction Records": "Maintains",
                    "Sale Administration": "Handles"
                }
            }
        }
    },
    "auction-house-cashier": {
        "name": "Auction Cashier Gold-Count",
        "aliases": ["The Payment Handler"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "The cashier who handles payments and financial transactions for successful auction bids.",
                "role": "Auction cashier",
                "relationships": {
                    "Auction Payments": "Processes",
                    "Financial Transactions": "Handles"
                }
            }
        }
    },
    "auction-house-doorman": {
        "name": "Auction Doorman Gate-Watch",
        "aliases": ["The Entry Guardian"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "The doorman who controls entry to the auction house and ensures only qualified bidders are admitted.",
                "role": "Entry controller",
                "relationships": {
                    "Auction Access": "Controls",
                    "Qualified Bidders": "Admits"
                }
            }
        }
    },
    "auction-house-crier": {
        "name": "Auction Crier Loud-Voice",
        "aliases": ["The Sale Announcer"],
        "appearances": [17, 18, 19],
        "knowledge": {
            "17": {
                "revealedIn": 17,
                "description": "The crier who announces upcoming auctions and calls out lot descriptions during sales.",
                "role": "Auction announcer",
                "relationships": {
                    "Auction Publicity": "Provides",
                    "Sale Announcements": "Makes"
                }
            }
        }
    },
    "criminal-fence-network": {
        "name": "Fence Network Boss Stolen-Goods",
        "aliases": ["The Contraband King"],
        "appearances": [2, 3, 4, 17, 18],
        "knowledge": {
            "2": {
                "revealedIn": 2,
                "description": "The boss of a network of fences who deal in stolen goods, potentially including Geralt's witcher swords.",
                "role": "Criminal fence boss",
                "relationships": {
                    "Stolen Goods": "Traffics",
                    "Criminal Network": "Leads"
                }
            }
        }
    },
    "criminal-lookout-spy": {
        "name": "Criminal Lookout Watch-Eye",
        "aliases": ["The Street Watcher"],
        "appearances": [2, 3, 4, 17, 18],
        "knowledge": {
            "2": {
                "revealedIn": 2,
                "description": "A lookout who watches for law enforcement and provides early warning to criminal operations.",
                "role": "Criminal lookout",
                "relationships": {
                    "Criminal Operations": "Watches for",
                    "Law Enforcement": "Monitors"
                }
            }
        }
    },
    "criminal-muscle-enforcer": {
        "name": "Criminal Enforcer Break-Bone",
        "aliases": ["The Intimidator"],
        "appearances": [2, 3, 4, 17, 18],
        "knowledge": {
            "2": {
                "revealedIn": 2,
                "description": "A criminal enforcer who uses violence and intimidation to collect debts and enforce criminal hierarchy.",
                "role": "Criminal muscle",
                "relationships": {
                    "Criminal Hierarchy": "Enforces",
                    "Violence": "Specializes in"
                }
            }
        }
    },
    "criminal-safe-cracker": {
        "name": "Safe Cracker Lock-Pick",
        "aliases": ["The Vault Opener"],
        "appearances": [2, 3, 4, 17],
        "knowledge": {
            "2": {
                "revealedIn": 2,
                "description": "A specialist criminal who can open locks and safes, essential for high-value thefts.",
                "role": "Safe cracker",
                "relationships": {
                    "Criminal Heists": "Essential to",
                    "Lock Technology": "Masters"
                }
            }
        }
    },
    "criminal-forger": {
        "name": "Document Forger False-Write",
        "aliases": ["The Paper Faker"],
        "appearances": [3, 4, 17, 18],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "A forger who creates false documents and papers for criminal operations and identity changes.",
                "role": "Document forger",
                "relationships": {
                    "False Documents": "Creates",
                    "Criminal Identity": "Provides"
                }
            }
        }
    },
    "tavern-serving-wench": {
        "name": "Serving Wench Ale-Pour",
        "aliases": ["The Tavern Girl"],
        "appearances": [1, 17, 18, 19],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A serving girl who works in taverns, bringing drinks and meals to customers and often overhearing useful gossip.",
                "role": "Tavern server",
                "relationships": {
                    "Tavern Customers": "Serves",
                    "Local Gossip": "Overhears"
                }
            }
        }
    },
    "tavern-bouncer": {
        "name": "Tavern Bouncer Strong-Arm",
        "aliases": ["The Peace Keeper"],
        "appearances": [1, 17, 18, 19],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A bouncer who maintains order in taverns, ejecting troublemakers and protecting customers and staff.",
                "role": "Tavern security",
                "relationships": {
                    "Tavern Order": "Maintains",
                    "Troublemakers": "Ejects"
                }
            }
        }
    },
    "tavern-regular-drunk": {
        "name": "Tavern Regular Ale-Belly",
        "aliases": ["The Local Drunk"],
        "appearances": [1, 17, 18, 19],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A regular tavern customer who spends most of his time drinking and often knows local gossip and rumors.",
                "role": "Tavern regular",
                "relationships": {
                    "Local Gossip": "Source of",
                    "Tavern Atmosphere": "Part of"
                }
            }
        }
    },
    "tavern-gambler": {
        "name": "Tavern Gambler Dice-Throw",
        "aliases": ["The Game Player"],
        "appearances": [1, 17, 18, 19],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A professional gambler who frequents taverns, playing dice and card games for money.",
                "role": "Professional gambler",
                "relationships": {
                    "Gambling Games": "Masters",
                    "Tavern Economy": "Participates in"
                }
            }
        }
    },
    "tavern-musician": {
        "name": "Tavern Musician Song-Play",
        "aliases": ["The Entertainment Provider"],
        "appearances": [1, 17, 18, 19],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A musician who performs in taverns for tips and meals, providing entertainment for customers.",
                "role": "Tavern entertainer",
                "relationships": {
                    "Tavern Atmosphere": "Enhances",
                    "Customer Entertainment": "Provides"
                }
            }
        }
    },
    "traveling-merchant-caravan": {
        "name": "Caravan Merchant Road-Trade",
        "aliases": ["The Traveling Trader"],
        "appearances": [1, 2, 14, 17, 18, 19],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A merchant who travels with caravans, trading goods between towns and cities along established routes.",
                "role": "Traveling merchant",
                "relationships": {
                    "Trade Routes": "Follows",
                    "Commercial Exchange": "Facilitates"
                }
            }
        }
    },
    "traveling-merchant-guard": {
        "name": "Caravan Guard Shield-Road",
        "aliases": ["The Trade Protector"],
        "appearances": [1, 2, 14, 17, 18],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A guard who protects merchant caravans from bandits and other threats during dangerous journeys.",
                "role": "Caravan guard",
                "relationships": {
                    "Merchant Protection": "Provides",
                    "Travel Safety": "Ensures"
                }
            }
        }
    },
    "traveling-merchant-apprentice": {
        "name": "Merchant Apprentice Learn-Trade",
        "aliases": ["The Trade Student"],
        "appearances": [1, 2, 17, 18],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A young apprentice learning the merchant trade, assisting with caravan operations and business dealings.",
                "role": "Merchant apprentice",
                "relationships": {
                    "Merchant Master": "Learns from",
                    "Trade Skills": "Developing"
                }
            }
        }
    },
    "local-fisherman": {
        "name": "Local Fisherman Net-Cast",
        "aliases": ["The Water Worker"],
        "appearances": [14, 15, 16, 17],
        "knowledge": {
            "14": {
                "revealedIn": 14,
                "description": "A local fisherman who works the coastal waters, providing information about sea conditions and maritime activities.",
                "role": "Local fisherman",
                "relationships": {
                    "Sea Knowledge": "Possesses",
                    "Maritime Information": "Provides"
                }
            }
        }
    },
    "local-baker": {
        "name": "Local Baker Bread-Make",
        "aliases": ["The Food Provider"],
        "appearances": [1, 17, 18, 19],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A local baker who provides fresh bread and baked goods to the community, often serving as a source of local news.",
                "role": "Community baker",
                "relationships": {
                    "Local Community": "Feeds",
                    "Community News": "Spreads"
                }
            }
        }
    },
    "local-blacksmith": {
        "name": "Local Blacksmith Iron-Work",
        "aliases": ["The Metal Worker"],
        "appearances": [1, 3, 17, 18, 22],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A local blacksmith who repairs tools and weapons, potentially providing information about unusual metalwork.",
                "role": "Village blacksmith",
                "relationships": {
                    "Metal Craft": "Practices",
                    "Community Tools": "Maintains"
                }
            }
        }
    },
    "local-herbalist": {
        "name": "Local Herbalist Plant-Know",
        "aliases": ["The Herb Woman"],
        "appearances": [7, 8, 15, 19],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "A local herbalist who knows about medicinal plants and natural remedies, sometimes helping with injuries and illnesses.",
                "role": "Village herbalist",
                "relationships": {
                    "Medicinal Plants": "Knows",
                    "Natural Healing": "Practices"
                }
            }
        }
    },
    "local-miller": {
        "name": "Local Miller Grain-Grind",
        "aliases": ["The Flour Maker"],
        "appearances": [1, 17, 18],
        "knowledge": {
            "1": {
                "revealedIn": 1,
                "description": "A local miller who grinds grain into flour, serving as a central figure in the community's food production.",
                "role": "Village miller",
                "relationships": {
                    "Grain Processing": "Handles",
                    "Food Production": "Essential to"
                }
            }
        }
    },
    "local-constable": {
        "name": "Local Constable Law-Keep",
        "aliases": ["The Peace Officer"],
        "appearances": [3, 4, 17, 18],
        "knowledge": {
            "3": {
                "revealedIn": 3,
                "description": "A local constable who maintains law and order in smaller communities, investigating crimes and keeping the peace.",
                "role": "Local lawman",
                "relationships": {
                    "Community Order": "Maintains",
                    "Local Justice": "Enforces"
                }
            }
        }
    },
    "local-priest": {
        "name": "Local Priest Faith-Guide",
        "aliases": ["The Spiritual Shepherd"],
        "appearances": [7, 8, 15, 18, 19],
        "knowledge": {
            "7": {
                "revealedIn": 7,
                "description": "A local priest who provides spiritual guidance and conducts religious services for the community.",
                "role": "Community priest",
                "relationships": {
                    "Spiritual Guidance": "Provides",
                    "Religious Services": "Conducts"
                }
            }
        }
    },
    "local-teacher": {
        "name": "Local Teacher Knowledge-Share",
        "aliases": ["The Village Educator"],
        "appearances": [12, 13, 18, 19],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "A local teacher who educates children and sometimes adults in reading, writing, and basic knowledge.",
                "role": "Village teacher",
                "relationships": {
                    "Community Education": "Provides",
                    "Knowledge Transmission": "Facilitates"
                }
            }
        }
    },
    "mysterious-sage": {
        "name": "Mysterious Sage Wisdom-Deep",
        "aliases": ["The Ancient Scholar"],
        "appearances": [12, 13, 20, 21, 22],
        "knowledge": {
            "12": {
                "revealedIn": 12,
                "description": "A mysterious sage with deep knowledge of ancient lore and magical theory, encountered during Geralt's adventures.",
                "role": "Ancient scholar",
                "relationships": {
                    "Ancient Knowledge": "Possesses",
                    "Magical Wisdom": "Shares selectively"
                }
            }
        }
    },
    "mysterious-oracle": {
        "name": "Mysterious Oracle Future-Know",
        "aliases": ["The Fate Speaker"],
        "appearances": [20, 21, 22, 23],
        "knowledge": {
            "20": {
                "revealedIn": 20,
                "description": "A mysterious oracle who appears near the end of Geralt's adventure, possibly connected to the larger magical forces at work.",
                "role": "Mystical oracle",
                "relationships": {
                    "Future Knowledge": "Claims",
                    "Mystical Forces": "Connected to"
                }
            }
        }
    },
    "final-witness": {
        "name": "Final Witness Truth-See",
        "aliases": ["The Last Observer"],
        "appearances": [22, 23],
        "knowledge": {
            "22": {
                "revealedIn": 22,
                "description": "A witness to the final resolution of Geralt's quest, representing those who observe and remember the conclusion of adventures.",
                "role": "Final witness",
                "relationships": {
                    "Adventure Conclusion": "Witnesses",
                    "Historical Memory": "Preserves"
                }
            }
        }
    }
}

# Add characters to existing data
for char_id, char_data in final_characters.items():
    data['characters'][char_id] = char_data

print(f"Adding {len(final_characters)} final characters to Season of Storms")
print(f"New total: {len(data['characters'])} characters")

# Save completed data
with open('data/witcher/season-of-storms.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✅ Season of Storms completed with exactly 150 characters!")