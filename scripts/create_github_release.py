#!/usr/bin/env python3
"""
Script to help create GitHub Release for RAFAEL Framework
This script prepares the release content and opens the browser
"""

import webbrowser
import os
from pathlib import Path

def main():
    print("🚀 RAFAEL Framework v1.2.0 - GitHub Release Helper")
    print("=" * 60)
    
    # Read release content
    content_file = Path(__file__).parent.parent / "GITHUB_RELEASE_CONTENT.md"
    
    if not content_file.exists():
        print("❌ Error: GITHUB_RELEASE_CONTENT.md not found!")
        return
    
    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check distribution files
    dist_dir = Path(__file__).parent.parent / "dist"
    wheel_file = dist_dir / "rafael_framework-1.2.0-py3-none-any.whl"
    tar_file = dist_dir / "rafael_framework-1.2.0.tar.gz"
    
    print("\n📦 Checking distribution files...")
    if wheel_file.exists():
        print(f"  ✅ {wheel_file.name} - {wheel_file.stat().st_size / 1024:.1f} KB")
    else:
        print(f"  ❌ {wheel_file.name} - NOT FOUND")
    
    if tar_file.exists():
        print(f"  ✅ {tar_file.name} - {tar_file.stat().st_size / 1024:.1f} KB")
    else:
        print(f"  ❌ {tar_file.name} - NOT FOUND")
    
    print("\n📝 Release content ready!")
    print(f"   Content length: {len(content)} characters")
    
    print("\n" + "=" * 60)
    print("📋 INSTRUCTIONS:")
    print("=" * 60)
    print("\n1. Browser will open GitHub Release page")
    print("2. Select tag: v1.2.0")
    print("3. Title: v1.2.0 - Phase 1: Stabilization")
    print("4. Copy content from GITHUB_RELEASE_CONTENT.md")
    print("5. Attach files:")
    print(f"   - {wheel_file}")
    print(f"   - {tar_file}")
    print("6. Check 'Set as the latest release'")
    print("7. Click 'Publish release'")
    
    print("\n" + "=" * 60)
    input("\nPress ENTER to open GitHub Release page...")
    
    # Open GitHub Release page
    url = "https://github.com/Rafael2022-prog/rafael/releases/new?tag=v1.2.0&title=v1.2.0%20-%20Phase%201:%20Stabilization"
    webbrowser.open(url)
    
    print("\n✅ Browser opened!")
    print("\n💡 TIP: Keep this window open to reference the instructions")
    print("\n📄 Content file location:")
    print(f"   {content_file}")
    
    # Ask if user wants to copy content to clipboard
    try:
        import pyperclip
        copy = input("\n📋 Copy release content to clipboard? (y/n): ").lower()
        if copy == 'y':
            # Extract just the release content (skip the header)
            release_content = content.split("---", 2)[-1].strip()
            pyperclip.copy(release_content)
            print("✅ Content copied to clipboard!")
    except ImportError:
        print("\n💡 Install pyperclip to enable clipboard copy: pip install pyperclip")
    
    print("\n🎉 Good luck with the release!")

if __name__ == "__main__":
    main()
