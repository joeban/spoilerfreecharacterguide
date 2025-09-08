#!/usr/bin/env python3
"""
Script to identify and report character appearance/knowledge mismatches
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
                mismatches.append({
                    'type': 'missing_appearance',
                    'chapter': revealed_in,
                    'description': f'Knowledge revealed in chapter {revealed_in} but not in appearances {appearances}'
                })
                
        except (ValueError, TypeError):
            continue
    
    return mismatches

def analyze_book(book_path):
    """Analyze a single book file for mismatches."""
    try:
        with open(book_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return {'error': f'Failed to load {book_path}: {e}'}
    
    characters = data.get('characters', {})
    book_mismatches = {}
    
    for char_id, char_data in characters.items():
        mismatches = analyze_character(char_id, char_data)
        if mismatches:
            book_mismatches[char_id] = {
                'name': char_data.get('name', char_id),
                'mismatches': mismatches,
                'current_appearances': char_data.get('appearances', [])
            }
    
    return book_mismatches

def main():
    data_dir = Path('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data')
    
    # Priority series order
    priority_series = [
        'harry-potter',
        'song-ice-fire', 
        'wheel-of-time',
        'fourth-wing',
        'percy-jackson',
        'lord-of-rings'
    ]
    
    all_results = {}
    total_books_with_issues = 0
    total_character_issues = 0
    
    for series in priority_series:
        series_dir = data_dir / series
        if not series_dir.exists():
            print(f"Warning: {series} directory not found")
            continue
            
        series_results = {}
        json_files = list(series_dir.glob('*.json'))
        # Filter out backup files
        json_files = [f for f in json_files if 'backup' not in f.name]
        
        for book_file in sorted(json_files):
            book_results = analyze_book(book_file)
            if book_results and not book_results.get('error'):
                if book_results:  # Has mismatches
                    series_results[book_file.stem] = book_results
                    total_books_with_issues += 1
                    total_character_issues += len(book_results)
        
        if series_results:
            all_results[series] = series_results
    
    # Print results
    print(f"\n=== CHARACTER APPEARANCE/KNOWLEDGE MISMATCH REPORT ===")
    print(f"Total books with issues: {total_books_with_issues}")
    print(f"Total characters with issues: {total_character_issues}\n")
    
    for series, series_data in all_results.items():
        print(f"📚 {series.upper().replace('-', ' ')}")
        for book, book_data in series_data.items():
            print(f"  📖 {book}: {len(book_data)} characters with mismatches")
            for char_id, char_info in book_data.items():
                print(f"    - {char_info['name']} ({char_id})")
                print(f"      Current appearances: {char_info['current_appearances']}")
                for mismatch in char_info['mismatches']:
                    print(f"      ❌ {mismatch['description']}")
        print()
    
    # Generate fix suggestions
    if all_results:
        print("\n=== SUGGESTED FIXES ===")
        for series, series_data in all_results.items():
            for book, book_data in series_data.items():
                missing_chapters = set()
                for char_id, char_info in book_data.items():
                    for mismatch in char_info['mismatches']:
                        if mismatch['type'] == 'missing_appearance':
                            missing_chapters.add(mismatch['chapter'])
                
                if missing_chapters:
                    print(f"{series}/{book}.json needs appearance fixes:")
                    print(f"  Chapters to add to various characters: {sorted(missing_chapters)}")

if __name__ == '__main__':
    main()