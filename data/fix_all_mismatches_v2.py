#!/usr/bin/env python3
"""
Automated script to fix ALL character appearance/knowledge mismatches
in the Spoiler-Free Character Guide data files.
FIXED VERSION: Handles mixed string/integer chapter numbers
"""

import json
import os
import sys
from pathlib import Path
from collections import defaultdict

def safe_sort_chapters(chapters):
    """Safely sort chapter numbers handling mixed string/int types."""
    def sort_key(chapter):
        # Handle special chapter names
        if isinstance(chapter, str):
            if chapter.lower() == 'prologue':
                return (0, chapter)
            elif chapter.lower() == 'epilogue':
                return (9999, chapter)
            else:
                # Try to convert to int, otherwise use string value
                try:
                    return (int(chapter), chapter)
                except ValueError:
                    return (9998, chapter)
        else:
            return (chapter, str(chapter))
    
    return sorted(chapters, key=sort_key)

def fix_character_appearances(char_data):
    """Fix a character's appearances array by adding missing chapters from knowledge."""
    if not isinstance(char_data, dict):
        return char_data, []
        
    appearances = list(char_data.get('appearances', []))  # Convert to list to handle both types
    knowledge = char_data.get('knowledge', {})
    
    missing_chapters = []
    
    # Check each knowledge entry
    for chapter_str, know_data in knowledge.items():
        if not isinstance(know_data, dict):
            continue
            
        try:
            # Handle both string and int chapter numbers
            revealed_in = know_data.get('revealedIn', chapter_str)
            
            # Convert chapter_str to appropriate type
            if isinstance(chapter_str, str):
                try:
                    chapter_int = int(chapter_str)
                    chapter_key = chapter_int
                except ValueError:
                    chapter_key = chapter_str
            else:
                chapter_key = chapter_str
            
            # Check if revealedIn matches the chapter or is explicitly set
            if revealed_in != chapter_key and revealed_in != chapter_str:
                # This is a mismatch - revealed_in should be in appearances
                if revealed_in not in appearances:
                    appearances.append(revealed_in)
                    missing_chapters.append(revealed_in)
            elif revealed_in not in appearances:
                # The revealed_in chapter should be in appearances
                appearances.append(revealed_in)
                missing_chapters.append(revealed_in)
                
        except Exception as e:
            print(f"    Warning: Error processing chapter {chapter_str}: {e}")
            continue
    
    # Sort appearances safely and update character data
    char_data['appearances'] = safe_sort_chapters(set(appearances))
    
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
        try:
            fixed_data, missing_chapters = fix_character_appearances(char_data)
            if missing_chapters:
                fixed_characters += 1
                total_missing_chapters += len(missing_chapters)
                characters[char_id] = fixed_data
                print(f"  ✅ Fixed {char_data.get('name', char_id)}: added chapters {missing_chapters}")
        except Exception as e:
            print(f"  ⚠️  Error fixing {char_id}: {e}")
            continue
    
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
    
    print("🔧 Starting automated fix of ALL character appearance/knowledge mismatches (v2)...")
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
                try:
                    if fix_book_file(book_file):
                        total_files_fixed += 1
                except Exception as e:
                    print(f"  ❌ Critical error processing {book_file}: {e}")
            print()
    
    print(f"🎉 Batch fix completed!")
    print(f"   Files processed: {total_files_processed}")
    print(f"   Files successfully processed: {total_files_fixed}")
    
    if total_files_fixed < total_files_processed:
        print(f"   Files with errors: {total_files_processed - total_files_fixed}")

if __name__ == '__main__':
    main()