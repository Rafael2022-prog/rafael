#!/usr/bin/env python3
"""
Script to help post GitHub Discussion announcement for RAFAEL Framework
"""

import webbrowser
from pathlib import Path

def main():
    print("💬 RAFAEL Framework v1.2.0 - GitHub Discussion Helper")
    print("=" * 60)
    
    # Read announcement content
    content_file = Path(__file__).parent.parent / "ANNOUNCEMENT_GITHUB_DISCUSSIONS.md"
    
    if not content_file.exists():
        print("❌ Error: ANNOUNCEMENT_GITHUB_DISCUSSIONS.md not found!")
        return
    
    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("\n📝 Discussion content ready!")
    print(f"   Content length: {len(content)} characters")
    
    print("\n" + "=" * 60)
    print("📋 INSTRUCTIONS:")
    print("=" * 60)
    print("\n1. Browser will open GitHub Discussions")
    print("2. Click 'New discussion'")
    print("3. Category: Announcements")
    print("4. Title: 🎉 RAFAEL Framework v1.2.0 Released - Phase 1: Stabilization Complete!")
    print("5. Copy content from ANNOUNCEMENT_GITHUB_DISCUSSIONS.md")
    print("6. Click 'Start discussion'")
    
    print("\n" + "=" * 60)
    input("\nPress ENTER to open GitHub Discussions...")
    
    # Open GitHub Discussions
    url = "https://github.com/Rafael2022-prog/rafael/discussions/new?category=announcements"
    webbrowser.open(url)
    
    print("\n✅ Browser opened!")
    print("\n📄 Content file location:")
    print(f"   {content_file}")
    
    # Try to copy to clipboard
    try:
        import pyperclip
        copy = input("\n📋 Copy discussion content to clipboard? (y/n): ").lower()
        if copy == 'y':
            # Extract just the discussion content (skip the header)
            discussion_content = content.split("---", 2)[-1].strip()
            pyperclip.copy(discussion_content)
            print("✅ Content copied to clipboard!")
    except ImportError:
        print("\n💡 Install pyperclip to enable clipboard copy: pip install pyperclip")
    
    print("\n🎉 Ready to announce!")

if __name__ == "__main__":
    main()
