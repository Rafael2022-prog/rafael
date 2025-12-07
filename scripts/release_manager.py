#!/usr/bin/env python3
"""
RAFAEL Framework v1.2.0 - Release Manager
Main script to manage all post-release activities
"""

import sys
from pathlib import Path

def print_header():
    print("=" * 70)
    print("🔱 RAFAEL Framework v1.2.0 - Release Manager")
    print("=" * 70)
    print("\nManage all post-release activities from one place!")

def print_menu():
    print("\n" + "=" * 70)
    print("📋 MAIN MENU:")
    print("=" * 70)
    print("\n1. 🚀 Create GitHub Release")
    print("2. 💬 Post GitHub Discussion")
    print("3. 📱 Share on Social Media")
    print("4. 📊 Start Monitoring")
    print("5. 📚 View All Documentation")
    print("6. ✅ View Implementation Status")
    print("0. 🚪 Exit")

def view_documentation():
    print("\n" + "=" * 70)
    print("📚 DOCUMENTATION FILES:")
    print("=" * 70)
    
    docs = {
        '1': 'RELEASE_NOTES_v1.2.0.md',
        '2': 'PHASE1_IMPLEMENTATION_SUMMARY.md',
        '3': 'ROADMAP_PENGEMBANGAN.md',
        '4': 'GITHUB_RELEASE_CONTENT.md',
        '5': 'ANNOUNCEMENT_GITHUB_DISCUSSIONS.md',
        '6': 'ANNOUNCEMENT_SOCIAL_MEDIA.md',
        '7': 'MONITORING_CHECKLIST_v1.2.0.md',
        '8': 'DEPLOYMENT_COMPLETE_v1.2.0.md',
        '9': 'IMPLEMENTATION_COMPLETE_v1.2.0.md',
    }
    
    base_path = Path(__file__).parent.parent
    
    print("\nAvailable documentation:")
    for key, filename in docs.items():
        filepath = base_path / filename
        if filepath.exists():
            size = filepath.stat().st_size / 1024
            print(f"   {key}. ✅ {filename} ({size:.1f} KB)")
        else:
            print(f"   {key}. ❌ {filename} (NOT FOUND)")
    
    print("\n💡 All documentation is in the project root directory")
    print(f"📁 Location: {base_path}")

def view_status():
    print("\n" + "=" * 70)
    print("✅ IMPLEMENTATION STATUS:")
    print("=" * 70)
    
    status = {
        'Phase 1 Implementation': '✅ COMPLETE',
        'PyPI Deployment': '✅ LIVE',
        'GitHub Repository': '✅ UPDATED',
        'Documentation': '✅ COMPLETE',
        'Release Content': '✅ READY',
        'Announcements': '✅ READY',
        'Monitoring Plan': '✅ READY',
    }
    
    print("\n📊 Current Status:")
    for task, state in status.items():
        print(f"   {task:.<40} {state}")
    
    print("\n🎯 Next Steps:")
    print("   1. Create GitHub Release")
    print("   2. Post announcements")
    print("   3. Start monitoring")
    
    print("\n🔗 Important Links:")
    print("   PyPI: https://pypi.org/project/rafael-framework/1.2.0/")
    print("   GitHub: https://github.com/Rafael2022-prog/rafael")
    print("   Commit: cf1658f")
    print("   Tag: v1.2.0")

def main():
    print_header()
    
    scripts_dir = Path(__file__).parent
    
    while True:
        print_menu()
        choice = input("\n👉 Select option (0-6): ").strip()
        
        if choice == '0':
            print("\n" + "=" * 70)
            print("👋 Thank you for using RAFAEL Release Manager!")
            print("=" * 70)
            print("\n🎉 RAFAEL Framework v1.2.0 is ready for the world!")
            print("🚀 Good luck with your release!")
            break
        
        elif choice == '1':
            print("\n🚀 Launching GitHub Release helper...")
            try:
                import create_github_release
                create_github_release.main()
            except Exception as e:
                print(f"❌ Error: {e}")
                print("💡 Try running: python scripts/create_github_release.py")
        
        elif choice == '2':
            print("\n💬 Launching GitHub Discussion helper...")
            try:
                import post_github_discussion
                post_github_discussion.main()
            except Exception as e:
                print(f"❌ Error: {e}")
                print("💡 Try running: python scripts/post_github_discussion.py")
        
        elif choice == '3':
            print("\n📱 Launching Social Media helper...")
            try:
                import share_social_media
                share_social_media.main()
            except Exception as e:
                print(f"❌ Error: {e}")
                print("💡 Try running: python scripts/share_social_media.py")
        
        elif choice == '4':
            print("\n📊 Launching Monitoring helper...")
            try:
                import start_monitoring
                start_monitoring.main()
            except Exception as e:
                print(f"❌ Error: {e}")
                print("💡 Try running: python scripts/start_monitoring.py")
        
        elif choice == '5':
            view_documentation()
        
        elif choice == '6':
            view_status()
        
        else:
            print("\n❌ Invalid choice! Please select 0-6")
        
        if choice in ['1', '2', '3', '4']:
            input("\n⏸️  Press ENTER to return to main menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
        sys.exit(0)
