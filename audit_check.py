#!/usr/bin/env python3
import json
import os
import re
from collections import defaultdict

def check_character_consistency(data, filename):
    """Check if characters have knowledge entries for chapters not in appearances"""
    issues = []
    
    if 'characters' not in data:
        return issues
        
    for char_id, char_data in data['characters'].items():
        char_name = char_data.get('name', char_id)
        appearances = char_data.get('appearances', [])
        knowledge = char_data.get('knowledge', {})
        
        # Check if knowledge chapters are in appearances
        for chapter, knowledge_data in knowledge.items():
            try:
                chapter_num = int(chapter)
                revealed_in = knowledge_data.get('revealedIn', chapter_num)
                
                if chapter_num not in appearances:
                    issues.append(f"CHARACTER CONSISTENCY: {filename} - {char_name}: Knowledge for chapter {chapter_num} but not in appearances")
                    
                if revealed_in not in appearances:
                    issues.append(f"CHARACTER CONSISTENCY: {filename} - {char_name}: revealedIn {revealed_in} but not in appearances")
                    
            except ValueError:
                continue
                
    return issues

def check_spoiler_keywords(data, filename):
    """Check for potential spoiler keywords in descriptions"""
    issues = []
    spoiler_patterns = [
        r'\bdies?\b',
        r'\bdeath\b', 
        r'\bkilled?\b',
        r'\bmurders?\b',
        r'\bbetray[s|ed]\b',
        r'\bactually\b',
        r'\bturns out\b',
        r'\bsecretly\b',
        r'\breveals?\b.*\b(true|real|actual)\b',
        r'\bis really\b',
        r'\bwho is\b.*\b(actually|really|truly)\b'
    ]
    
    def check_text(text, context):
        for pattern in spoiler_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                issues.append(f"POTENTIAL SPOILER: {filename} - {context}: '{text[:100]}...'")
    
    # Check character descriptions and relationships
    if 'characters' in data:
        for char_id, char_data in data['characters'].items():
            char_name = char_data.get('name', char_id)
            
            # Check aliases for spoilers
            aliases = char_data.get('aliases', [])
            for alias in aliases:
                check_text(alias, f"{char_name} alias")
                
            # Check knowledge descriptions
            knowledge = char_data.get('knowledge', {})
            for chapter, knowledge_data in knowledge.items():
                desc = knowledge_data.get('description', '')
                check_text(desc, f"{char_name} ch{chapter}")
                
                # Check relationships
                relationships = knowledge_data.get('relationships', {})
                for rel_type, rel_desc in relationships.items():
                    check_text(f"{rel_type}: {rel_desc}", f"{char_name} ch{chapter} relationship")
    
    # Check chapter recaps
    if 'recaps' in data:
        for chapter, recap in data['recaps'].items():
            check_text(recap, f"Chapter {chapter} recap")
            
    return issues

def check_missing_recaps(data, filename):
    """Check for missing chapter recaps"""
    issues = []
    
    meta = data.get('meta', {})
    total_chapters = meta.get('chapters', 0)
    recaps = data.get('recaps', {})
    
    missing_recaps = []
    for i in range(1, total_chapters + 1):
        if str(i) not in recaps:
            missing_recaps.append(str(i))
            
    if missing_recaps:
        issues.append(f"MISSING RECAPS: {filename} - Missing recaps for chapters: {', '.join(missing_recaps)}")
        
    return issues

def audit_file(filepath):
    """Audit a single JSON file"""
    filename = os.path.basename(filepath)
    issues = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Run all checks
        issues.extend(check_character_consistency(data, filename))
        issues.extend(check_spoiler_keywords(data, filename))
        issues.extend(check_missing_recaps(data, filename))
        
    except json.JSONDecodeError as e:
        issues.append(f"JSON ERROR: {filename} - Invalid JSON: {str(e)}")
    except Exception as e:
        issues.append(f"ERROR: {filename} - {str(e)}")
        
    return issues

def main():
    data_dir = "data"
    all_issues = []
    
    # Priority series for focused checking
    priority_series = [
        'harry-potter', 'fourth-wing', 'percy-jackson', 
        'court-thorns-roses', 'throne-of-glass', 'song-ice-fire'
    ]
    
    # Check priority series first
    print("=== PRIORITY SERIES AUDIT ===")
    for series in priority_series:
        series_dir = os.path.join(data_dir, series)
        if os.path.exists(series_dir):
            for filename in os.listdir(series_dir):
                if filename.endswith('.json') and not filename.endswith('-backup.json'):
                    filepath = os.path.join(series_dir, filename)
                    issues = audit_file(filepath)
                    all_issues.extend(issues)
                    
                    if issues:
                        print(f"\n--- {series}/{filename} ---")
                        for issue in issues:
                            print(issue)
    
    # Quick check of all other series
    print(f"\n=== ALL SERIES SUMMARY ===")
    total_files = 0
    files_with_issues = 0
    
    for series_dir in os.listdir(data_dir):
        series_path = os.path.join(data_dir, series_dir)
        if os.path.isdir(series_path):
            for filename in os.listdir(series_path):
                if filename.endswith('.json') and not filename.endswith('-backup.json'):
                    total_files += 1
                    filepath = os.path.join(series_path, filename)
                    issues = audit_file(filepath)
                    if issues:
                        files_with_issues += 1
                        all_issues.extend(issues)
    
    print(f"Total files checked: {total_files}")
    print(f"Files with issues: {files_with_issues}")
    print(f"Total issues found: {len(all_issues)}")
    
    # Categorize issues
    issue_types = defaultdict(int)
    for issue in all_issues:
        issue_type = issue.split(':')[0]
        issue_types[issue_type] += 1
        
    print("\n=== ISSUE BREAKDOWN ===")
    for issue_type, count in sorted(issue_types.items()):
        print(f"{issue_type}: {count} issues")

if __name__ == "__main__":
    main()