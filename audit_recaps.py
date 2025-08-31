#!/usr/bin/env python3

import json
import os
from pathlib import Path

def audit_book_recaps(file_path):
    """Check if a book has recaps for all chapters."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        meta = data.get('meta', {})
        title = meta.get('title', 'Unknown')
        total_chapters = meta.get('chapters', 0)
        recaps = data.get('recaps', {})
        
        missing_recaps = []
        for chapter in range(1, total_chapters + 1):
            if str(chapter) not in recaps:
                missing_recaps.append(chapter)
        
        return {
            'file': file_path,
            'title': title,
            'total_chapters': total_chapters,
            'recaps_count': len(recaps),
            'missing_recaps': missing_recaps,
            'complete': len(missing_recaps) == 0
        }
    except Exception as e:
        return {
            'file': file_path,
            'error': str(e)
        }

def main():
    data_dir = Path('/Users/josephban/Downloads/spoilerfreecharacterguide-main/data')
    books = []
    
    # Find all book JSON files
    for json_file in data_dir.rglob('*.json'):
        if json_file.name != 'index.json':
            books.append(json_file)
    
    print("CHAPTER RECAP AUDIT REPORT")
    print("=" * 50)
    print()
    
    complete_books = 0
    incomplete_books = 0
    total_missing = 0
    
    for book_file in sorted(books):
        result = audit_book_recaps(book_file)
        
        if 'error' in result:
            print(f"❌ ERROR: {result['file']} - {result['error']}")
            continue
            
        status = "✅ COMPLETE" if result['complete'] else "❌ INCOMPLETE"
        print(f"{status} - {result['title']}")
        print(f"   File: {result['file']}")
        print(f"   Chapters: {result['total_chapters']}")
        print(f"   Recaps: {result['recaps_count']}/{result['total_chapters']}")
        
        if not result['complete']:
            print(f"   Missing: {len(result['missing_recaps'])} chapters - {result['missing_recaps']}")
            incomplete_books += 1
            total_missing += len(result['missing_recaps'])
        else:
            complete_books += 1
        print()
    
    print("SUMMARY")
    print("=" * 20)
    print(f"Total books: {complete_books + incomplete_books}")
    print(f"Complete: {complete_books}")
    print(f"Incomplete: {incomplete_books}")
    print(f"Total missing recaps: {total_missing}")

if __name__ == "__main__":
    main()