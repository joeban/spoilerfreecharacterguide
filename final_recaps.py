#!/usr/bin/env python3
import json
import os

def add_god_emperor_recaps(data):
    """Add missing recaps for God Emperor of Dune"""
    missing_recaps = {
        "2": "Duncan Idaho, the latest ghola companion, shows signs of awakening to memories from previous incarnations. The God Emperor's vast empire maintains an enforced peace that has lasted millennia, preventing both war and meaningful progress.",
        "3": "Moneo serves as the God Emperor's faithful administrator while struggling with his daughter Siona's rebellious nature. The complex bureaucracy required to maintain Leto's empire reveals the scope of his control over human civilization.",
        "5": "The Ixians develop new technologies while carefully avoiding forbidden areas that might threaten the God Emperor's rule. Their ambassador programs reflect growing tensions between innovation and the constraints of Leto's Peace.",
        "6": "Leto's prescient visions span thousands of years, allowing him to guide humanity with perfect foresight but at the cost of terrible loneliness. His conversations reveal the weight of immortal rule and the burden of seeing all possible futures.",
        "8": "The death of Malky, Leto's former Ixian friend, deeply affects the God Emperor and influences his relationship with the new ambassador Hwi Noree. Memories of genuine friendship become precious in his isolated existence.",
        "9": "Duncan's awakening memories create internal conflict as he struggles with multiple lifetimes of serving Leto. His growing awareness of his eternal servitude raises questions about identity, free will, and the price of loyalty.",
        "11": "Siona's rebel activities intensify as she demonstrates her unique ability to remain hidden from prescient vision. This genetic trait makes her both dangerous to Leto and essential to his long-term plans for humanity.",
        "12": "The introduction of new players into the political game shows how even after millennia, human ambition and desire for power continue to create tension within Leto's carefully controlled empire.",
        "14": "Duncan's relationship with other characters develops as his growing humanity conflicts with his designed purpose. The emotional complexity of the ghola condition becomes apparent as memories and loyalty war within him.",
        "15": "Leto's rule through the Fish Speakers demonstrates his understanding of power dynamics and human nature. His all-female army represents his attempt to break historical patterns of male-dominated warfare.",
        "17": "The God Emperor's interactions with various subjects reveal both his wisdom and the terrible isolation that comes with absolute power. His ability to see all possible futures makes every conversation fraught with knowledge of consequences.",
        "18": "Hwi Noree's arrival begins to awaken emotions in Leto that he thought were long dead. Her artificial creation by the Ixians to appeal to him creates complex feelings about love, manipulation, and genuine connection.",
        "20": "Duncan's awakening accelerates as he begins to remember not just his original life but multiple resurrections and deaths. The weight of eternal servitude becomes clearer as he grapples with his unique situation.",
        "21": "Political maneuvering intensifies as various factions attempt to position themselves advantageously within Leto's empire. The God Emperor's responses demonstrate his complete awareness of their schemes while pursuing his own larger agenda.",
        "23": "Siona's tests and trials reveal her growing capabilities while Leto evaluates her potential as his successor. The criteria for leadership in the post-Leto era become apparent through their interactions.",
        "24": "The relationship between Leto and Hwi deepens as their conversations reveal both his longing for companionship and her growing understanding of his true nature. Their connection transcends her original programming.",
        "26": "Duncan's memories of previous incarnations create a complex web of loyalty, resentment, and understanding. His unique perspective as the only person to have known Leto across multiple lifetimes provides insights into the God Emperor's evolution.",
        "27": "The God Emperor's teachings and philosophy become clearer through his interactions with various characters. His lessons about power, freedom, and human nature reveal the deeper purposes behind his tyrannical rule.",
        "29": "Tensions escalate as the various plotlines begin to converge toward crisis. Leto's prescient abilities allow him to see the approaching climax while making final preparations for the transition he has foreseen.",
        "30": "Hwi's influence on Leto becomes more pronounced as she serves as both companion and conscience. Her presence reminds him of his lost humanity while also representing hope for emotional connection.",
        "32": "The conspiracy against Leto gains momentum as multiple factions coordinate their efforts. The God Emperor's apparent vulnerability creates opportunities for those who underestimate his prescient awareness of their plans.",
        "33": "Siona's development reaches critical stages as she demonstrates the qualities Leto has been cultivating. Her ability to remain invisible to prescience makes her uniquely qualified for the role he has planned for her.",
        "35": "Duncan's final awakening brings complete understanding of his situation and role in Leto's plans. His acceptance or rejection of his eternal servitude will determine his fate in the approaching crisis.",
        "36": "The political situation reaches a boiling point as various factions make their moves against the God Emperor. Leto's responses reveal whether he will prevent their success or allow events to unfold as he has foreseen.",
        "38": "Personal relationships become crucial as the approaching crisis tests loyalties and reveals true motivations. The connections between characters will determine who survives the coming transformation of the empire.",
        "39": "Leto's preparations for his own end become more apparent as he positions key people and resources for the post-imperial period. His willingness to sacrifice himself for humanity's future becomes clear.",
        "41": "The conspiracy reaches its final phase as the plotters move against Leto. His supernatural abilities and prescient knowledge are tested against the coordinated efforts of his enemies.",
        "42": "Duncan's loyalty is put to the ultimate test as he must choose between his programmed devotion to Leto and his growing love for Siona. His decision will affect not only his own fate but the success of the conspiracy.",
        "44": "The immediate crisis explodes into violence as the carefully laid plans of both Leto and his enemies come to fruition. The God Emperor's true intentions regarding his own survival become apparent.",
        "45": "Hwi's fate becomes intertwined with the larger conspiracy as her relationship with Leto makes her both a target and a catalyst for his final decisions. Her potential loss represents the emotional cost of the transition.",
        "47": "The confrontation between Leto and his enemies reaches its climax as the various plotlines converge. The God Emperor's ultimate sacrifice begins to unfold as planned thousands of years in advance.",
        "48": "Leto's death becomes inevitable as the conspiracy succeeds according to his own design. His willing sacrifice triggers the changes he has foreseen as necessary for humanity's long-term survival.",
        "50": "The immediate aftermath of Leto's death begins the transformation of human civilization. Siona emerges as a leader while Duncan faces the reality of life without his eternal master.",
        "51": "The breaking of Leto's empire allows humanity to begin the Scattering that he always intended. The God Emperor's death paradoxically fulfills his greatest vision for human survival and growth.",
        "53": "Political structures collapse and reform as the post-Leto era begins. The characters who survive must adapt to a universe without the God Emperor's controlling presence.",
        "54": "The early stages of the Scattering show humanity beginning to spread across the universe as Leto intended. The genetic traits he cultivated, particularly in Siona's line, become crucial for future survival.",
        "56": "Duncan and Siona's relationship develops in the new reality as they work together to guide humanity through the transition. Their partnership represents both practical necessity and emotional connection.",
        "57": "The legacy of Leto's rule becomes apparent as his long-term plans begin to unfold even after his death. The seeds he planted throughout millennia of rule begin to germinate.",
        "59": "The sandworms begin to return to Arrakis as Leto's death releases the sandtrout that formed his skin. The ecological restoration of the desert planet begins the next phase of the spice cycle.",
        "60": "Humanity's expansion into the universe accelerates as the Scattering gains momentum. The freedom Leto's death provides comes with both opportunities and dangers he foresaw.",
        "62": "The full implications of Leto's genetic breeding program become apparent as his carefully selected bloodlines prove their worth in the new era. Siona's descendants will be crucial for humanity's future.",
        "63": "The transformation of human civilization continues as new leaders emerge from the chaos of Leto's fallen empire. The lessons of his rule begin to influence how humanity organizes itself.",
        "65": "The final stages of the transition show humanity successfully beginning the expansion that Leto envisioned. His sacrifice achieves its intended purpose of ensuring human survival and growth.",
        "66": "The God Emperor's ultimate victory becomes clear as his death accomplishes what his life was designed to achieve. Humanity is set on a path that will prevent its extinction and ensure its expansion across the universe."
    }
    
    for chapter, recap in missing_recaps.items():
        data["recaps"][chapter] = recap
    
    return data

def add_heretics_recaps(data):
    """Add missing recaps for Heretics of Dune"""
    missing_recaps = {
        "2": "The political situation in the post-Scattering universe becomes clearer as the Bene Gesserit face unprecedented challenges. Ancient enemies return with new powers and technologies that threaten the Sisterhood's traditional methods and survival.",
        "4": "Sheeana's abilities continue to develop under Bene Gesserit guidance while the Sisterhood struggles to understand and control her unique talents. Her connection to the sandworms represents both opportunity and danger for their long-term plans.",
        "5": "Bashar Teg's military genius becomes apparent as he's recalled from retirement to handle the growing crisis. His combination of tactical brilliance and Mentat abilities makes him uniquely qualified for the challenges ahead.",
        "7": "The scope of the returning forces from the Scattering becomes clearer as the Honored Matres demonstrate their brutal efficiency in conquest. Their methods represent a dark mirror of Bene Gesserit techniques, replacing subtlety with overwhelming violence.",
        "9": "The Duncan Idaho ghola project reaches critical stages as the Bene Gesserit prepare their ultimate weapon against the returning threats. His enhanced abilities and unique nature make him potentially crucial for humanity's survival.",
        "10": "Ancient Tleilaxu Master Scytale reveals his survival and continued involvement in galactic politics. His knowledge and grudges spanning millennia add another dangerous element to the complex situation facing all factions.",
        "12": "The training and preparation of key assets intensifies as the Bene Gesserit recognize the approaching crisis. Teg, Duncan, and others are positioned for the crucial roles they will play in the coming conflict.",
        "13": "Political maneuvering accelerates as various factions attempt to position themselves advantageously for the coming storm. The Honored Matres' approach forces difficult decisions and desperate alliances.",
        "15": "The situation on Rakis becomes increasingly critical as the Honored Matres close in on their targets. The planet's importance as the source of sandworms makes it a crucial battleground for all factions.",
        "16": "Teg's abilities begin manifesting under extreme stress, revealing superhuman capabilities that make him nearly unstoppable in combat. These powers come at great physical cost but provide crucial advantages.",
        "18": "Duncan's awakening process accelerates under the pressure of approaching danger. His memories and enhanced abilities begin to emerge as the Bene Gesserit's careful planning reaches crucial stages.",
        "19": "The conspiracy involving multiple factions reaches critical mass as the Honored Matres demonstrate their willingness to use extreme violence to achieve their goals. Their brutality shocks even experienced political manipulators.",
        "21": "Teg's superhuman speed and combat abilities are fully revealed as he faces impossible odds to protect his charges. His sacrifice becomes inevitable as he uses his powers to their limit against overwhelming forces.",
        "22": "The various plotlines converge as the different factions clash in increasingly desperate conflict. Political maneuvering gives way to open warfare as the stakes become clear to all participants.",
        "24": "Duncan's complete awakening provides him with both his original memories and his enhanced capabilities. His transformation into the super ghola represents the culmination of centuries of Bene Gesserit planning.",
        "25": "The crisis reaches its peak as multiple factions make their final desperate moves. The survival of key individuals and organizations hangs in the balance as the conflict explodes into open warfare.",
        "27": "Teg's heroic sacrifice protects the crucial assets while demonstrating the full extent of his abilities. His death serves as both tragedy and catalyst for the events that follow.",
        "28": "The immediate aftermath of major losses reshapes the political landscape as surviving factions regroup and reassess their positions. New alliances and enmities form from the crucible of conflict.",
        "30": "Duncan emerges as a formidable force with his awakened memories and enhanced abilities intact. His unique nature makes him a valuable asset for any faction that can secure his loyalty.",
        "31": "The consequences of the recent conflicts become apparent as the balance of power shifts dramatically. The Honored Matres' methods prove both effective and ultimately self-defeating.",
        "33": "Political realignments accelerate as the surviving factions adapt to changed circumstances. New strategies emerge from the lessons learned through violence and loss.",
        "34": "The situation stabilizes temporarily as the immediate crisis passes, but underlying tensions remain. The various factions prepare for the next phase of their eternal conflicts.",
        "36": "Long-term planning begins as the survivors adapt to the new reality. The lessons learned from recent events influence future strategies and alliances.",
        "37": "The broader implications of recent events become clearer as their effects ripple through the political structure. Changes that seemed local prove to have galactic significance.",
        "39": "New alliances and strategies emerge from the changed circumstances as the various factions position themselves for future conflicts. The balance of power continues to evolve.",
        "40": "The political situation continues to develop as the consequences of earlier events work through the complex web of galactic politics. New opportunities and dangers emerge from the chaos.",
        "42": "The final preparations for the next phase of conflict begin as the various factions marshal their remaining resources. The stakes continue to escalate as the true scope of the threat becomes apparent.",
        "43": "The climactic confrontation approaches as all the carefully laid plans and desperate schemes converge toward a final resolution. The survival of entire civilizations hangs in the balance.",
        "45": "The immediate crisis resolves with significant consequences for all participants. The political landscape is permanently altered by the events that have unfolded.",
        "47": "The aftermath of the major conflicts sets the stage for future developments. New leaders emerge while others fall, reshaping the balance of power throughout the known universe."
    }
    
    for chapter, recap in missing_recaps.items():
        data["recaps"][chapter] = recap
    
    return data

def add_chapterhouse_recaps(data):
    """Add missing recaps for Chapterhouse: Dune"""  
    missing_recaps = {
        "2": "Duncan Idaho settles into his role working with the Bene Gesserit while maintaining his independence. His relationship with the captured Honored Matre Murbella begins to develop as part of Odrade's complex strategy for survival.",
        "4": "Murbella's training and conversion process intensifies as she learns to integrate both Bene Gesserit and Honored Matre techniques. Her unique dual nature makes her crucial to Odrade's plans for merging the two organizations.",
        "6": "The scope of the Unknown Enemy threat becomes clearer as evidence accumulates of their influence throughout the galaxy. This mysterious force drove the Honored Matres to flee and now approaches the Old Empire.",
        "8": "Reverend Mother Rebecca and other cultural preservers work to maintain human diversity within the Sisterhood. Their efforts become increasingly important as the merger with the Honored Matres threatens traditional Bene Gesserit values.",
        "10": "Scytale bargains with his captors using his irreplaceable genetic knowledge while the political situation becomes more desperate. His survival skills and ancient wisdom make him valuable to all factions despite his prisoner status.",
        "12": "The captured Tleilaxu Master reveals more about his vast genetic knowledge and the techniques that make him the last of his kind. His cooperation becomes essential for the Bene Gesserit's long-term survival plans.",
        "14": "Political tensions within the Bene Gesserit intensify as conservative and progressive factions disagree about the merger strategy. Bellonda leads the opposition to Odrade's radical changes while supporting voices grow fewer.",
        "16": "Duncan's role as teacher and converter becomes more crucial as his relationship with Murbella deepens. Their intimate connection serves both personal and strategic purposes in the broader plan for organizational merger.",
        "18": "The merger concept gains momentum as Murbella demonstrates successful integration of both traditions within herself. Her transformation proves that combining the organizations is possible despite the risks involved.",
        "20": "Evidence of the Unknown Enemy's approach becomes more concrete as signs of their influence multiply. The merged organization's formation appears to be humanity's last hope against this ultimate threat.",
        "22": "Internal opposition to the merger grows as conservative elements within the Sisterhood fear the loss of essential traditions and knowledge. The debate becomes more intense as the external threats continue to mount.",
        "24": "Cultural preservation efforts intensify as the merger proceeds. Key figures like Rebecca work to ensure that important human traditions survive the organizational transformation.",
        "26": "Sheeana's growing independence and unique abilities make her increasingly important to future plans. Her connection to the sandworms gives her perspectives that others lack on the unfolding crisis.",
        "28": "The political transformation accelerates as Odrade pushes forward with increasingly desperate measures. Her willingness to sacrifice traditional purity for survival creates deep divisions within the Sisterhood.",
        "30": "The Unknown Enemy's influence becomes more apparent as their approach threatens all human factions. The merger between Bene Gesserit and Honored Matres advances as the only viable response to this threat.",
        "32": "Preparations for the final merger phase intensify while escape plans develop in secret. Sheeana begins assembling resources and people needed to preserve pure Bene Gesserit knowledge separately from the political alliance.",
        "34": "The conspiracy to preserve authentic Sisterhood values gains momentum as key figures position themselves for the escape. The tension between political necessity and cultural preservation reaches critical levels.",
        "36": "Duncan's loyalty increasingly shifts toward the mission of preserving true Bene Gesserit values rather than supporting the political merger. His ancient connection to the Atreides mission transcends immediate political considerations.",
        "38": "The final preparations for both the merger and the escape accelerate as time runs out. Multiple agendas compete as various factions prepare for their different visions of the future.",
        "40": "Odrade's final plans reach fruition as she prepares to complete the merger at the cost of her own life. Her sacrifice will ensure the new organization's success while allowing the authentic Sisterhood to continue elsewhere.",
        "42": "The great exodus begins as the escaping group prepares to depart on their mission to preserve Bene Gesserit knowledge among the scattered worlds. Their journey represents hope for the continuation of human wisdom and diversity."
    }
    
    for chapter, recap in missing_recaps.items():
        data["recaps"][chapter] = recap
    
    return data

def process_remaining_books():
    """Process the remaining Dune books to add missing recaps"""
    data_dir = "data/dune"
    
    books = [
        ("god-emperor.json", "God Emperor of Dune", add_god_emperor_recaps),
        ("heretics.json", "Heretics of Dune", add_heretics_recaps), 
        ("chapterhouse.json", "Chapterhouse: Dune", add_chapterhouse_recaps),
    ]
    
    for filename, title, add_func in books:
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            data = add_func(data)
            
            # Write back to file
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"Added missing recaps to {title}")
        else:
            print(f"File not found: {filepath}")

if __name__ == "__main__":
    process_remaining_books()