#!/usr/bin/env python3
import json
import os

def add_dune_messiah_recaps(data):
    """Add missing recaps for Dune Messiah"""
    missing_recaps = {
        "2": "The extent of Paul's jihad becomes clearer as billions have died across the galaxy in his name. Religious fanaticism spreads through the empire while Paul struggles with visions of even darker possible futures. The conspiracy against him begins to take shape.",
        "4": "Paul's marriage to Princess Irulan remains childless and political while his love for Chani continues. The Bene Gesserit, Spacing Guild, and other factions position themselves for what they believe will be Paul's downfall. Alia grows into her role as a religious figure.",
        "6": "The Duncan Idaho ghola arrives as part of the conspiracy, though Paul's prescient visions show him glimpses of the trap being set. The Tleilaxu's involvement becomes clearer as their ultimate goals remain mysterious. Political tensions escalate throughout the empire.",
        "8": "Guild Navigator Edric coordinates the conspiracy while remaining hidden from Paul's prescient sight. The complexity of the plot against the Emperor becomes apparent as multiple factions work together despite their mutual distrust and conflicting goals.",
        "9": "Paul's prescient abilities show him increasingly limited options as the conspiracy tightens around him. His visions reveal that every path he can see leads to catastrophe. The pressure of leadership and prophecy weighs heavily on the Emperor.",
        "11": "The Tleilaxu dwarf Bijaz arrives to begin the process of awakening Duncan's hidden programming. Paul's supernatural sight allows him to see the approaching crisis but not find a clear path through it. The conspiracy enters its active phase.",
        "13": "Duncan begins his service as Paul's companion while concealing his true purpose and hidden conditioning. His struggle with identity and loyalty creates internal conflict as he serves the Emperor he's programmed to destroy. The trap begins closing around Paul.",
        "14": "Paul's relationship with the Duncan ghola becomes increasingly complex as he recognizes both the man he once knew and the weapon he has become. The conspirators prepare for their final moves while Paul's options continue to narrow.",
        "16": "Chani's pregnancy progresses as the conspiracy reaches critical stages. Paul faces the terrible choice between his personal happiness and the greater good. The stone burner attack that blinds Paul paradoxically enhances his prescient sight.",
        "18": "Paul's supernatural blindness allows him to function normally while confounding his enemies and followers. The birth of his twin children approaches as the final phase of the conspiracy begins. All the plotlines start converging toward the climax.",
        "19": "Duncan's programming begins to activate as Bijaz uses sophisticated techniques to break down his resistance. However, his growing humanity and love for Alia create unexpected complications in the Tleilaxu plan. The awakening process becomes more complex than expected.",
        "21": "The conspiracy's various elements begin to come together as the different factions coordinate their final assault on Paul's rule. However, their individual agendas and mutual distrust create weaknesses that Paul's prescient sight can exploit.",
        "23": "Duncan's internal struggle intensifies as his conditioning wars with his genuine feelings and awakening memories. Paul prepares for the confrontation he knows is coming, understanding that victory over his immediate enemies may not solve his larger dilemma.",
        "24": "The Tleilaxu make their final push to activate Duncan's programming while Paul's visions show him the approaching moment of choice. The conspiracy reaches its peak as all the major players position themselves for the final confrontation.",
        "26": "Duncan breaks free of his conditioning through love and loyalty, causing the conspiracy's primary weapon to fail. However, Paul realizes that this victory only brings him face to face with an even more terrible choice about his future and the future of humanity.",
        "28": "With their main plan failed, the conspirators make increasingly desperate moves to achieve their goals. Paul must confront the reality that even victory over his enemies cannot prevent the catastrophic future he sees approaching.",
        "29": "The Tleilaxu make their final offer to resurrect Chani as a ghola in exchange for Paul's abdication. Paul must choose between his personal desires and his understanding of what the galaxy needs for its long-term survival.",
        "31": "The immediate conspiracy is defeated but Paul faces the larger implications of his continued rule. His prescient visions show him that the only way to prevent even greater catastrophe is to abandon his throne and disappear into the desert.",
        "34": "Chani's death in childbirth devastates Paul and serves as the final catalyst for his decision to follow Fremen tradition and walk into the desert when he can no longer see the path ahead. Alia prepares to serve as regent for the twin children."
    }
    
    for chapter, recap in missing_recaps.items():
        data["recaps"][chapter] = recap
    
    return data

def add_children_of_dune_recaps(data):
    """Add missing recaps for Children of Dune"""
    missing_recaps = {
        "2": "The twins demonstrate wisdom and abilities far beyond their years, sharing a telepathic bond while possessing ancestral memories. Duncan Idaho serves as their guardian and teacher while Alia's rule becomes increasingly erratic and concerning.",
        "3": "Stilgar and other Fremen elders serve as protectors and guides to the twins, though they struggle to understand the children's unusual nature. The political situation becomes more complex as various factions seek to control or eliminate the Atreides heirs.",
        "5": "Princess Irulan begins her role as educator and historian while the twins face growing threats from multiple directions. The corruption of traditional Fremen ways under Alia's rule creates tension between old and new approaches to desert life.",
        "6": "The twins' unique abilities and ancestral memories make them valuable targets for political manipulation. Their pre-born nature allows them to understand adult concepts while creating challenges for those trying to protect and guide them.",
        "8": "The Preacher's influence grows as he challenges the religious orthodoxy built around Paul's legend. His mysterious identity and intimate knowledge of Atreides history make him a dangerous figure to the established religious order.",
        "9": "Alia's possession by ancestral memories becomes more pronounced as she struggles to maintain her individual identity. The Baron Harkonnen's influence within her grows stronger, affecting her decisions and relationships with increasing malevolence.",
        "11": "Farad'n Corrino's education under Princess Irulan begins to transform him from a potential enemy into someone capable of understanding and perhaps allying with the Atreides twins. His mother's vengeful schemes conflict with his growing wisdom.",
        "12": "The political conspiracy against the twins gains momentum as House Corrino and other factions coordinate their efforts. The children's unique nature makes them both incredibly valuable and extremely dangerous to their potential enemies.",
        "14": "Duncan Idaho's loyalty to the twins deepens as he recognizes the magnitude of the threats they face. His experience with multiple lifetimes helps him understand their situation while his warrior skills provide crucial protection.",
        "15": "Leto begins experiencing visions of the Golden Path, seeing possible futures where humanity either survives and thrives or faces extinction. These visions show him the terrible price that ensuring humanity's survival will require.",
        "17": "The Preacher's teachings reach more people as he works to deconstruct the dangerous mythology that has grown around Paul Muad'Dib. His efforts to restore balance to the religious situation create both followers and enemies.",
        "18": "Alia's corruption accelerates as the Baron Harkonnen's memories gain more control over her actions. Her betrayal of her own family becomes increasingly apparent to those close to her, creating dangerous divisions.",
        "20": "Stilgar's wisdom helps the twins navigate the complex political and spiritual challenges they face. His connection to traditional Fremen values provides stability as the larger political situation becomes increasingly chaotic.",
        "21": "The conspiracy against the twins reaches critical stages as various factions prepare for direct action. The children must rely on their unique abilities and loyal protectors to survive increasingly sophisticated threats.",
        "23": "Irulan's influence on Farad'n continues to guide him away from his family's destructive path toward a more constructive role in the unfolding events. Her wisdom and experience help bridge potential conflicts between the great houses.",
        "24": "Leto's visions of the Golden Path become clearer and more detailed, showing him the specific steps that will be necessary to ensure humanity's long-term survival. The weight of this knowledge begins to affect his relationship with his sister.",
        "26": "The twins' relationship evolves as they begin to understand their different roles in the coming events. Ghanima's emotional stability provides balance for Leto's increasingly intense focus on his prescient visions of the future.",
        "27": "Duncan Idaho's protective instincts intensify as the threats to the twins multiply. His warrior training and multiple lifetimes of experience make him uniquely qualified to guard them through the approaching crisis.",
        "29": "Alia's complete possession by the Baron Harkonnen makes her a direct threat to her own family. The twins must now consider their aunt as an enemy rather than a protector, fundamentally altering their situation.",
        "30": "The political situation reaches a boiling point as multiple conspiracies converge on the twins. The children's survival depends on their ability to outmaneuver adult enemies who underestimate their capabilities and understanding.",
        "32": "Farad'n's transformation under Irulan's guidance reaches completion as he fully commits to a path of wisdom rather than vengeance. His change represents hope for peaceful resolution of ancient conflicts between the great houses.",
        "33": "The Preacher's final revelations help prepare the way for the coming changes in leadership. His mission to deconstruct the dangerous myths around Paul's legacy nears completion as the twins prepare for their destinies.",
        "35": "Leto faces the moment of ultimate decision about accepting the sandtrout symbiosis that will grant him the power to see the Golden Path through. This choice will cost him his humanity but ensure humanity's survival.",
        "36": "The conspiracy against the twins explodes into open violence as their enemies make their final desperate moves. The children's unique abilities and loyal protectors are tested to their limits in the struggle for survival.",
        "38": "Leto's transformation begins as he allows sandtrout to bond with his skin, starting the process that will eventually turn him into the God Emperor. His sacrifice represents the ultimate commitment to humanity's long-term future.",
        "39": "Alia's corruption reaches its culmination as she becomes a tool of ancient malice rather than a protector of her family. Her downfall serves as a warning about the dangers of the pre-born condition.",
        "41": "The various political threads begin to resolve as the twins' enemies are defeated and their allies secured. Leto's transformation accelerates while Ghanima prepares for her role as the genetic heir to the Atreides bloodline.",
        "42": "Farad'n and Ghanima's growing relationship represents the peaceful unification of formerly hostile houses. Their alliance will help heal ancient wounds while ensuring genetic diversity for future generations.",
        "44": "Leto's metamorphosis continues as he gains superhuman abilities at the cost of his human form. His prescient visions become clearer and more comprehensive, showing him thousands of years into the future.",
        "45": "The immediate threats to the twins are resolved as their transformation into the next generation of leaders becomes complete. Leto prepares for his role as the God Emperor while Ghanima prepares for her role as genetic guardian.",
        "47": "The transition of power accelerates as Leto's transformation makes him less human but more capable of guiding humanity along the Golden Path. The political and religious structures begin adapting to the new reality.",
        "48": "The final preparations for Leto's reign begin as he becomes something beyond human comprehension. His sacrifice ensures that humanity will have the guidance it needs for long-term survival and growth.",
        "50": "Ghanima and Farad'n's relationship deepens as they prepare for their role in continuing the human genetic legacy. Their union represents both political alliance and genetic necessity for the future.",
        "51": "Leto's prescient abilities reach their full potential as he sees thousands of years into the future with perfect clarity. His transformation from human to God Emperor nears completion as he accepts the full weight of his destiny.",
        "53": "The political situation stabilizes under Leto's emerging rule as his superhuman abilities make opposition futile. The foundations are laid for the millennia of peace and stagnation that will follow under his tyranny.",
        "54": "The old generation passes away as the new order takes shape under Leto's guidance. Stilgar's death marks the end of an era while the twins fully assume their roles as the next phase of human evolution.",
        "56": "Leto's transformation accelerates as he becomes increasingly inhuman but gains the power necessary to guide humanity through the coming millennia. His prescient visions show him the exact path humanity must take.",
        "57": "The final political arrangements are made as Ghanima and Farad'n prepare for their marriage and their role in preserving human genetic diversity. Their children will carry the Atreides genes into the future.",
        "59": "Leto's metamorphosis nears completion as he prepares to begin his long reign as the God Emperor. His transformation represents the ultimate sacrifice for humanity's benefit, trading his humanity for humanity's survival.",
        "60": "The immediate crisis passes as Leto's enemies are defeated and his transformation ensures his ability to enforce peace. The stage is set for thousands of years of enforced stability under his tyrannical but necessary rule.",
        "62": "Ghanima's marriage to Farad'n solidifies the political alliance between their houses while ensuring genetic diversity for future generations. Their partnership represents hope for humanity's continued evolution.",
        "63": "The final arrangements for Leto's empire are completed as he becomes the God Emperor in fact as well as name. His transformation grants him the longevity and prescient abilities needed to guide humanity for millennia."
    }
    
    for chapter, recap in missing_recaps.items():
        data["recaps"][chapter] = recap
    
    return data

def process_all_books():
    """Process all Dune books to add missing recaps"""
    data_dir = "data/dune"
    
    books = [
        ("dune.json", "Dune", None),
        ("dune-messiah.json", "Dune Messiah", add_dune_messiah_recaps),
        ("children-of-dune.json", "Children of Dune", add_children_of_dune_recaps),
    ]
    
    for filename, title, add_func in books:
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            if add_func:
                data = add_func(data)
                
                # Write back to file
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                
                print(f"Added missing recaps to {title}")

if __name__ == "__main__":
    process_all_books()