#!/usr/bin/env python3
import json
import os

def verify_book_recaps(filepath, book_title, expected_chapters, missing_chapters):
    """Verify that all expected recaps are present"""
    print(f"\n=== Verifying {book_title} ===")
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    recaps = data.get('recaps', {})
    
    # Check total chapters
    print(f"Expected chapters: {expected_chapters}")
    print(f"Recap entries: {len(recaps)}")
    
    # Check if previously missing chapters now have recaps
    found_missing = 0
    for chapter in missing_chapters:
        if str(chapter) in recaps:
            found_missing += 1
        else:
            print(f"MISSING: Chapter {chapter} still has no recap")
    
    print(f"Added missing recaps: {found_missing}/{len(missing_chapters)}")
    
    # Show a sample of newly added recaps
    print("Sample new recaps:")
    for i, chapter in enumerate(missing_chapters[:3]):  # Show first 3
        if str(chapter) in recaps:
            print(f"  Chapter {chapter}: {recaps[str(chapter)][:100]}...")
    
    return found_missing == len(missing_chapters)

def main():
    books = [
        ("data/dune/dune.json", "Dune", 48, [2, 4, 6, 8, 9, 11, 13, 15, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 34, 36, 38, 39, 41, 43, 44, 46]),
        ("data/dune/dune-messiah.json", "Dune Messiah", 35, [2, 4, 6, 8, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 28, 29, 31, 34]),
        ("data/dune/children-of-dune.json", "Children of Dune", 64, [2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 48, 50, 51, 53, 54, 56, 57, 59, 60, 62, 63]),
        ("data/dune/god-emperor.json", "God Emperor of Dune", 67, [2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 48, 50, 51, 53, 54, 56, 57, 59, 60, 62, 63, 65, 66]),
        ("data/dune/heretics.json", "Heretics of Dune", 48, [2, 4, 5, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 34, 36, 37, 39, 40, 42, 43, 45, 47]),
        ("data/dune/chapterhouse.json", "Chapterhouse: Dune", 43, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]),
    ]
    
    total_added = 0
    total_expected = 0
    
    for filepath, title, chapters, missing in books:
        if os.path.exists(filepath):
            success = verify_book_recaps(filepath, title, chapters, missing)
            if success:
                total_added += len(missing)
            total_expected += len(missing)
        else:
            print(f"ERROR: File not found: {filepath}")
    
    print(f"\n=== SUMMARY ===")
    print(f"Total recaps added: {total_added}/{total_expected}")
    if total_added == total_expected:
        print("✅ ALL MISSING RECAPS SUCCESSFULLY ADDED!")
    else:
        print("❌ Some recaps are still missing")

if __name__ == "__main__":
    main()