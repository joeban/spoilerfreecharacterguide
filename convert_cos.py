#!/usr/bin/env python3
"""
Converts Chamber of Secrets from v1.0 format to v2.0 format
"""

import json
import sys

def convert_character(char_data):
    """Convert a single character from v1.0 to v2.0 format"""
    new_char = {
        "name": char_data["name"],
        "appearances": [],
        "knowledge": {}
    }
    
    # Add aliases if present
    if "aliases" in char_data:
        new_char["aliases"] = char_data["aliases"]
    
    # Extract appearances and convert tiers to knowledge
    appearances = set()
    if "tiers" in char_data:
        for tier_key, tier_data in char_data["tiers"].items():
            chapter_num = int(tier_key)
            appearances.add(chapter_num)
            
            # Convert tier to knowledge entry
            new_char["knowledge"][tier_key] = {
                "revealedIn": chapter_num,
                "description": tier_data["description"],
                "role": tier_data["role"]
            }
            
            if "relationships" in tier_data:
                new_char["knowledge"][tier_key]["relationships"] = tier_data["relationships"]
    
    # Sort appearances
    new_char["appearances"] = sorted(list(appearances))
    
    return new_char

def main():
    # Read the file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/chamber-of-secrets.json', 'r') as f:
        data = json.load(f)
    
    # Update schema version
    data["meta"]["schemaVersion"] = "2.0"
    
    # Convert all characters
    new_characters = {}
    for char_key, char_data in data["characters"].items():
        new_characters[char_key] = convert_character(char_data)
    
    data["characters"] = new_characters
    
    # Write back to file
    with open('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/chamber-of-secrets.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Successfully converted Chamber of Secrets to v2.0 format")
    print(f"Converted {len(new_characters)} characters")

if __name__ == "__main__":
    main()