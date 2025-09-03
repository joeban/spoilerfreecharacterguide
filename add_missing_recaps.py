#!/usr/bin/env python3
import json
import sys

def add_dune_recaps(data):
    """Add missing recaps for Dune"""
    missing_recaps = {
        "11": "The Atreides establish their base of operations in Arrakeen while learning about spice harvesting and the constant threat of sandworms. Paul's first direct encounter with the desert's dangers gives him a deeper appreciation for the planet's harsh beauty and deadly nature.",
        "13": "Dr. Yueh's internal torment grows as the Harkonnens tighten their psychological grip on him through his captured wife. His loyalty to the Atreides wars with his desperate love for Wanna, setting the stage for the tragedy to come. Paul's abilities continue to develop at an alarming rate.",
        "15": "Paul and Jessica use their survival training and a few precious supplies to stay alive in the hostile desert. Their Bene Gesserit and Mentat training proves crucial as they navigate the dangers while being hunted by Harkonnen forces. Paul's prescient abilities become more pronounced under the stress of survival.",
        "17": "Paul and Jessica make their way deeper into the desert, learning to conserve water and move like the Fremen to avoid detection. Paul's visions guide them toward potential safety while showing him darker possibilities ahead. Their mother-son dynamic evolves as they face life-or-death situations together.",
        "19": "The fugitives encounter their first Fremen, leading to tense negotiations for survival. Paul must prove their worth while Jessica demonstrates her Bene Gesserit abilities. The meeting sets in motion events that will determine whether they find sanctuary or death in the deep desert.",
        "21": "Paul's integration into Fremen society begins as he learns their customs and harsh desert law. His combat victory earns him respect, but also the responsibility of caring for Jamis's family. Jessica faces her own challenges as the Fremen evaluate her potential as a Reverend Mother.",
        "23": "Paul's training with the Fremen intensifies as he learns to fight with crysknives and move like a true desert warrior. His natural abilities combined with Fremen techniques make him formidable. Jessica's pregnancy progresses, and the Fremen begin to see religious significance in her condition.",
        "24": "The political situation shifts as the Baron consolidates his control over Arrakis. Paul's growing legend among the Fremen begins to worry the Harkonnen forces. Jessica prepares for a crucial test that will determine her role in Fremen society and the fate of her unborn child.",
        "26": "The transformation of Jessica affects the entire sietch as she becomes a bridge between Fremen traditions and the ancient Bene Gesserit teachings. Paul's abilities continue to evolve as he spends more time in the desert. The unborn Alia's presence becomes increasingly apparent to those with sensitivity.",
        "28": "Paul's first major military action against the Harkonnens demonstrates his tactical genius and the effectiveness of Fremen fighting methods. His success begins to attract attention from other sietches. The legend of Muad'Dib starts to spread across the desert.",
        "29": "Gurney Halleck's survival is revealed as he joins Paul's cause, though initially suspicious of Jessica's role in the Duke's death. His reunion with Paul provides both emotional closure and military expertise. The Fremen rebellion gains a crucial ally with intimate knowledge of Atreides tactics.",
        "31": "The Fremen rebellion gains momentum as more sietches join Muad'Dib's cause. Paul's strategic brilliance combined with Fremen desert warfare creates devastating losses for the occupying forces. His prescient visions show him the approaching climax and the terrible cost of victory.",
        "33": "Paul's forces begin to seriously disrupt spice production, affecting the galactic economy and drawing Imperial attention. His transformation into a messianic figure accelerates as religious fervor spreads among the Fremen. The Baron realizes that conventional military tactics cannot defeat the desert fighters.",
        "34": "The rebellion reaches a tipping point as Harkonnen control of Arrakis begins to crumble. Paul faces the terrible knowledge that his success is leading exactly toward the bloody jihad he hoped to prevent. Alia's birth approaches, bringing with it questions about what the pre-born child will become.",
        "36": "Alia's strange nature becomes apparent as she demonstrates adult knowledge and lethal capabilities despite her infant body. Paul's inner circle must grapple with the reality of a pre-born child who possesses the memories of countless generations. The rebellion enters its final phase.",
        "38": "The spice flow disruption forces the Emperor's hand as the galactic economy teeters on the brink. Paul's prescient visions confirm the approaching climax with perfect clarity. The Fremen prepare for their ultimate test against the Emperor's elite Sardaukar troops.",
        "39": "News of the Emperor's decision to personally intervene reaches the desert as massive Imperial forces prepare to assault Arrakis. Paul sees in his visions that this confrontation will determine not just his fate, but the future of the entire galaxy. The final preparations begin.",
        "41": "The Emperor's arrival on Arrakis with his Sardaukar forces sets the stage for the ultimate battle. Paul must balance his prescient knowledge of victory with the terrible cost he knows it will bring. The Fremen steel themselves for their greatest challenge.",
        "43": "The final battle begins as Fremen forces engage the Emperor's elite Sardaukar. Paul's tactical genius and the Fremen's superior desert fighting skills begin to tell as the Imperial forces find themselves outmatched. The political ramifications of a potential Imperial defeat become clear.",
        "44": "The tide of battle turns decisively in favor of the Fremen as their superior numbers and fighting ability overcome the Sardaukar. Paul's moment of ultimate choice approaches as victory brings him face to face with the Emperor and the weight of imperial power.",
        "46": "Paul consolidates his victory and begins the transition from rebel leader to Emperor. The political marriages and alliances necessary to secure his rule require painful compromises with his personal desires. The machinery of the jihad that will spread across the galaxy begins to take shape."
    }
    
    for chapter, recap in missing_recaps.items():
        data["recaps"][chapter] = recap
    
    return data

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 add_missing_recaps.py <json_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        data = json.load(f)
    
    # Add missing recaps based on the book
    if "Dune" in data["meta"]["title"] and "Messiah" not in data["meta"]["title"]:
        data = add_dune_recaps(data)
    
    # Write back to file with pretty formatting
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Added missing recaps to {filename}")

if __name__ == "__main__":
    main()