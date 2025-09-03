#!/usr/bin/env python3

import json

def fix_cos_appearances():
    file_path = '/Users/josephban/Downloads/spoilerfreecharacterguide-main/data/harry-potter/chamber-of-secrets.json'
    
    # Load the current data
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Fix Harry Potter - he should appear in virtually every chapter
    if 'harry-potter' in data['characters']:
        # Harry appears in all chapters 1-18 except maybe a few specific ones
        data['characters']['harry-potter']['appearances'] = list(range(1, 19))
        print("Fixed Harry Potter appearances: chapters 1-18")
    
    # Fix Ron Weasley - appears from chapter 3 onwards (after Harry is rescued)  
    if 'ron-weasley' in data['characters']:
        # Ron appears from chapter 3 to 18 (after Harry rescue through end)
        data['characters']['ron-weasley']['appearances'] = list(range(3, 19))
        print("Fixed Ron Weasley appearances: chapters 3-18")
    
    # Fix Hermione Granger - appears from chapter 5 onwards (when school starts)
    if 'hermione-granger' in data['characters']:
        # Hermione appears from chapter 5 to 18 (school start through end)
        data['characters']['hermione-granger']['appearances'] = list(range(5, 19))
        print("Fixed Hermione Granger appearances: chapters 5-18")
    
    # Save the updated data
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Successfully updated Chamber of Secrets character appearances")

if __name__ == "__main__":
    fix_cos_appearances()