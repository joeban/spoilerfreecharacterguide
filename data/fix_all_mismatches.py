#!/usr/bin/env python3
"""
Automated script to fix ALL character appearance/knowledge mismatches
in the Spoiler-Free Character Guide data files.
"""

import json
import os
import sys
from pathlib import Path
from collections import defaultdict

def analyze_character(char_id, char_data):
    """Analyze a character for appearance/knowledge mismatches."""
    mismatches = []
    
    if not isinstance(char_data, dict):
        return mismatches
        
    appearances = char_data.get('appearances', [])
    knowledge = char_data.get('knowledge', {})
    
    if not appearances or not knowledge:
        return mismatches
    
    # Check each knowledge entry
    for chapter_str, know_data in knowledge.items():
        if not isinstance(know_data, dict):
            continue
            
        try:
            chapter = int(chapter_str)
            revealed_in = know_data.get('revealedIn', chapter)
            
            # Check if revealedIn is in appearances
            if revealed_in not in appearances:
                mismatches.append(revealed_in)
                
        except (ValueError, TypeError):
            continue
    
    return mismatches

def fix_character_appearances(char_data):
    """Fix a character's appearances array by adding missing chapters from knowledge."""
    if not isinstance(char_data, dict):
        return char_data, []
        
    appearances = set(char_data.get('appearances', []))
    knowledge = char_data.get('knowledge', {})
    
    missing_chapters = []
    
    # Check each knowledge entry
    for chapter_str, know_data in knowledge.items():
        if not isinstance(know_data, dict):
            continue
            
        try:
            chapter = int(chapter_str)
            revealed_in = know_data.get('revealedIn', chapter)
            
            # Add missing chapters to appearances
            if revealed_in not in appearances:
                appearances.add(revealed_in)
                missing_chapters.append(revealed_in)
                
        except (ValueError, TypeError):
            continue
    
    # Sort appearances and update character data
    char_data['appearances'] = sorted(appearances)
    
    return char_data, missing_chapters

def fix_book_file(book_path):
    """Fix all characters in a single book file."""
    print(f"Processing: {book_path}")
    
    try:
        with open(book_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"  ❌ Failed to load: {e}")
        return False
    
    characters = data.get('characters', {})
    fixed_characters = 0
    total_missing_chapters = 0
    
    # Fix each character
    for char_id, char_data in characters.items():
        fixed_data, missing_chapters = fix_character_appearances(char_data)
        if missing_chapters:
            fixed_characters += 1
            total_missing_chapters += len(missing_chapters)
            characters[char_id] = fixed_data
            print(f"  ✅ Fixed {char_data.get('name', char_id)}: added chapters {missing_chapters}")
    
    if fixed_characters > 0:
        # Write back the fixed data
        try:
            with open(book_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"  📝 Fixed {fixed_characters} characters ({total_missing_chapters} missing chapters)")
            return True
        except Exception as e:
            print(f"  ❌ Failed to write: {e}")
            return False
    else:
        print(f"  ✨ No fixes needed")
        return True

def main():
    data_dir = Path('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data')
    
    print("🔧 Starting automated fix of ALL character appearance/knowledge mismatches...")
    print()
    
    # Get all series directories
    series_dirs = [d for d in data_dir.iterdir() if d.is_dir()]
    
    total_files_processed = 0
    total_files_fixed = 0
    
    for series_dir in sorted(series_dirs):
        series_name = series_dir.name
        json_files = list(series_dir.glob('*.json'))
        # Filter out backup files
        json_files = [f for f in json_files if 'backup' not in f.name]
        
        if json_files:
            print(f"📚 {series_name.upper().replace('-', ' ')}")
            
            for book_file in sorted(json_files):
                total_files_processed += 1
                if fix_book_file(book_file):
                    total_files_fixed += 1
            print()
    
    print(f"🎉 Batch fix completed!")
    print(f"   Files processed: {total_files_processed}")
    print(f"   Files successfully fixed: {total_files_fixed}")
    
    if total_files_fixed < total_files_processed:
        print(f"   Files with errors: {total_files_processed - total_files_fixed}")

if __name__ == '__main__':
    main()