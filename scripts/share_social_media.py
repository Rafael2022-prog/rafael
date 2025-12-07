#!/usr/bin/env python3
"""
Script to help share RAFAEL Framework v1.2.0 on social media
"""

import webbrowser
from pathlib import Path

def read_announcement_content():
    content_file = Path(__file__).parent.parent / "ANNOUNCEMENT_SOCIAL_MEDIA.md"
    
    if not content_file.exists():
        print("❌ Error: ANNOUNCEMENT_SOCIAL_MEDIA.md not found!")
        return None
    
    with open(content_file, 'r', encoding='utf-8') as f:
        return f.read()

def extract_section(content, platform):
    """Extract content for specific platform"""
    sections = {
        'twitter': ('## Twitter/X Post', '---'),
        'linkedin': ('## LinkedIn Post', '---'),
        'reddit': ('## Reddit Post', '---'),
        'devto': ('## Dev.to / Medium Article', '---'),
        'hackernews': ('## Hacker News Post', '---'),
        'email': ('## Email Template', '---')
    }
    
    if platform not in sections:
        return None
    
    start_marker, end_marker = sections[platform]
    
    try:
        start = content.find(start_marker)
        if start == -1:
            return None
        
        # Find next section or end
        next_section = content.find('\n## ', start + len(start_marker))
        if next_section == -1:
            section_content = content[start:]
        else:
            section_content = content[start:next_section]
        
        # Clean up the content
        lines = section_content.split('\n')
        # Skip the header and separator
        content_lines = []
        skip_next = False
        for line in lines[1:]:
            if line.strip() == '```' or line.strip().startswith('```'):
                skip_next = not skip_next
                continue
            if not skip_next and line.strip() and not line.strip() == '---':
                content_lines.append(line)
        
        return '\n'.join(content_lines).strip()
    except Exception as e:
        print(f"Error extracting {platform}: {e}")
        return None

def main():
    print("📱 RAFAEL Framework v1.2.0 - Social Media Helper")
    print("=" * 60)
    
    content = read_announcement_content()
    if not content:
        return
    
    platforms = {
        '1': ('Twitter/X', 'twitter', 'https://twitter.com/intent/tweet'),
        '2': ('LinkedIn', 'linkedin', 'https://www.linkedin.com/feed/'),
        '3': ('Reddit (r/Python)', 'reddit', 'https://www.reddit.com/r/Python/submit'),
        '4': ('Reddit (r/devops)', 'reddit', 'https://www.reddit.com/r/devops/submit'),
        '5': ('Dev.to', 'devto', 'https://dev.to/new'),
        '6': ('Hacker News', 'hackernews', 'https://news.ycombinator.com/submit'),
        '7': ('Email', 'email', None)
    }
    
    print("\n📋 Available platforms:")
    for key, (name, _, _) in platforms.items():
        print(f"   {key}. {name}")
    print("   0. Exit")
    
    while True:
        print("\n" + "=" * 60)
        choice = input("\nSelect platform (0-7): ").strip()
        
        if choice == '0':
            print("\n👋 Goodbye!")
            break
        
        if choice not in platforms:
            print("❌ Invalid choice!")
            continue
        
        name, platform_key, url = platforms[choice]
        
        print(f"\n📱 {name}")
        print("=" * 60)
        
        # Extract and show content
        platform_content = extract_section(content, platform_key)
        
        if platform_content:
            print("\n📝 Content preview:")
            print("-" * 60)
            preview = platform_content[:500]
            print(preview)
            if len(platform_content) > 500:
                print(f"\n... ({len(platform_content) - 500} more characters)")
            print("-" * 60)
            
            # Copy to clipboard
            try:
                import pyperclip
                pyperclip.copy(platform_content)
                print("\n✅ Content copied to clipboard!")
            except ImportError:
                print("\n💡 Install pyperclip for clipboard support: pip install pyperclip")
            
            # Open URL
            if url:
                open_browser = input(f"\n🌐 Open {name}? (y/n): ").lower()
                if open_browser == 'y':
                    webbrowser.open(url)
                    print(f"✅ {name} opened in browser!")
            
            print(f"\n📄 Full content in: ANNOUNCEMENT_SOCIAL_MEDIA.md")
            print(f"   Section: {name}")
        else:
            print(f"❌ Could not extract content for {name}")
        
        continue_choice = input("\n📱 Share on another platform? (y/n): ").lower()
        if continue_choice != 'y':
            break
    
    print("\n🎉 Thank you for sharing RAFAEL Framework!")

if __name__ == "__main__":
    main()
