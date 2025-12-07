# RAFAEL Framework - Release Management Scripts

**Version**: 1.2.0  
**Purpose**: Automate post-release activities

---

## 📋 Available Scripts

### 1. Release Manager (Main Script)
**File**: `release_manager.py`

Main script to manage all post-release activities from one place.

```bash
python scripts/release_manager.py
```

**Features**:
- Interactive menu
- All scripts in one place
- Status overview
- Documentation viewer

---

### 2. Create GitHub Release
**File**: `create_github_release.py`

Helper to create GitHub Release with proper content.

```bash
python scripts/create_github_release.py
```

**What it does**:
- Opens GitHub Release page
- Checks distribution files
- Provides instructions
- Copies content to clipboard (if pyperclip installed)

**Requirements**:
- Distribution files in `dist/` folder
- `GITHUB_RELEASE_CONTENT.md` file

---

### 3. Post GitHub Discussion
**File**: `post_github_discussion.py`

Helper to post announcement in GitHub Discussions.

```bash
python scripts/post_github_discussion.py
```

**What it does**:
- Opens GitHub Discussions
- Provides instructions
- Copies content to clipboard

**Requirements**:
- `ANNOUNCEMENT_GITHUB_DISCUSSIONS.md` file

---

### 4. Share on Social Media
**File**: `share_social_media.py`

Interactive helper for sharing on multiple platforms.

```bash
python scripts/share_social_media.py
```

**Supported Platforms**:
- Twitter/X
- LinkedIn
- Reddit (r/Python, r/devops)
- Dev.to
- Hacker News
- Email

**What it does**:
- Extracts platform-specific content
- Copies to clipboard
- Opens platform URL
- Interactive selection

**Requirements**:
- `ANNOUNCEMENT_SOCIAL_MEDIA.md` file

---

### 5. Start Monitoring
**File**: `start_monitoring.py`

Helper to start monitoring release metrics.

```bash
python scripts/start_monitoring.py
```

**What it does**:
- Opens monitoring links
- Creates monitoring log
- Provides checklist
- Quick access to metrics

**Monitoring Links**:
- PyPI Stats
- GitHub Issues
- GitHub Discussions
- GitHub Actions
- GitHub Insights
- GitHub Traffic

**Requirements**:
- `MONITORING_CHECKLIST_v1.2.0.md` file

---

## 🚀 Quick Start

### Option 1: Use Release Manager (Recommended)

```bash
cd r:\RAFAEL
python scripts\release_manager.py
```

Then select from menu:
1. Create GitHub Release
2. Post GitHub Discussion
3. Share on Social Media
4. Start Monitoring

### Option 2: Run Individual Scripts

```bash
# Create GitHub Release
python scripts\create_github_release.py

# Post Discussion
python scripts\post_github_discussion.py

# Share on Social Media
python scripts\share_social_media.py

# Start Monitoring
python scripts\start_monitoring.py
```

---

## 📦 Optional Dependencies

### For Clipboard Support

```bash
pip install pyperclip
```

**Benefits**:
- Auto-copy content to clipboard
- Easier pasting into web forms
- Faster workflow

---

## 📝 Usage Examples

### Example 1: Create GitHub Release

```bash
$ python scripts/create_github_release.py

🚀 RAFAEL Framework v1.2.0 - GitHub Release Helper
============================================================

📦 Checking distribution files...
  ✅ rafael_framework-1.2.0-py3-none-any.whl - 59.2 KB
  ✅ rafael_framework-1.2.0.tar.gz - 233.0 KB

📝 Release content ready!
   Content length: 15234 characters

============================================================
📋 INSTRUCTIONS:
============================================================

1. Browser will open GitHub Release page
2. Select tag: v1.2.0
3. Title: v1.2.0 - Phase 1: Stabilization
...

Press ENTER to open GitHub Release page...
```

### Example 2: Share on Social Media

```bash
$ python scripts/share_social_media.py

📱 RAFAEL Framework v1.2.0 - Social Media Helper
============================================================

📋 Available platforms:
   1. Twitter/X
   2. LinkedIn
   3. Reddit (r/Python)
   4. Reddit (r/devops)
   5. Dev.to
   6. Hacker News
   7. Email
   0. Exit

============================================================

Select platform (0-7): 1

📱 Twitter/X
============================================================

📝 Content preview:
------------------------------------------------------------
🎉 RAFAEL Framework v1.2.0 is LIVE!

✅ Persistence layer for genome state
✅ Enhanced error handling & recovery
...

✅ Content copied to clipboard!

🌐 Open Twitter/X? (y/n): y
✅ Twitter/X opened in browser!
```

### Example 3: Start Monitoring

```bash
$ python scripts/start_monitoring.py

📊 RAFAEL Framework v1.2.0 - Monitoring Helper
============================================================

📋 Monitoring checklist loaded!

🎯 MONITORING TASKS:
============================================================

📅 DAILY TASKS (First Week):
   1. Check PyPI downloads
   2. Review new GitHub issues
   3. Monitor CI/CD pipeline
   4. Read user feedback

🔗 MONITORING LINKS:
============================================================

📊 Quick access:
   1. PyPI Stats
   2. GitHub Issues
   3. GitHub Discussions
   ...

Open monitoring link (0-7, or 'all' for all): all

🌐 Opening all monitoring links...
   Opening PyPI Stats...
   Opening GitHub Issues...
   ...

✅ All links opened!
```

---

## 🔧 Troubleshooting

### Script Won't Run

**Problem**: `python: command not found`

**Solution**:
```bash
# Use python3
python3 scripts/release_manager.py

# Or use full path
C:\Python311\python.exe scripts\release_manager.py
```

### Import Error

**Problem**: `ModuleNotFoundError: No module named 'pyperclip'`

**Solution**:
```bash
# Install optional dependency
pip install pyperclip

# Or continue without clipboard support
# (scripts will still work)
```

### File Not Found

**Problem**: `Error: GITHUB_RELEASE_CONTENT.md not found!`

**Solution**:
```bash
# Make sure you're in the project root
cd r:\RAFAEL

# Then run the script
python scripts/release_manager.py
```

### Browser Doesn't Open

**Problem**: Browser doesn't open automatically

**Solution**:
- Copy the URL from terminal
- Open manually in browser
- Check if default browser is set

---

## 📚 Related Documentation

- **Release Notes**: `RELEASE_NOTES_v1.2.0.md`
- **Implementation Summary**: `PHASE1_IMPLEMENTATION_SUMMARY.md`
- **Roadmap**: `ROADMAP_PENGEMBANGAN.md`
- **Monitoring Checklist**: `MONITORING_CHECKLIST_v1.2.0.md`

---

## 🎯 Workflow

### Recommended Order

1. **Create GitHub Release** (Most important)
   - Run `create_github_release.py`
   - Follow instructions
   - Publish release

2. **Post GitHub Discussion**
   - Run `post_github_discussion.py`
   - Announce to community

3. **Share on Social Media**
   - Run `share_social_media.py`
   - Share on preferred platforms

4. **Start Monitoring**
   - Run `start_monitoring.py`
   - Track metrics daily

---

## 💡 Tips

### For Best Results

1. **Install pyperclip** for clipboard support
2. **Use Release Manager** for guided workflow
3. **Follow the order** above for maximum impact
4. **Monitor daily** in the first week
5. **Respond quickly** to issues

### Time Estimates

- GitHub Release: 5-10 minutes
- GitHub Discussion: 2-3 minutes
- Social Media (all): 15-20 minutes
- Monitoring setup: 5 minutes

**Total**: ~30-40 minutes for complete release announcement

---

## 🆘 Support

### Need Help?

- **Documentation**: Check the main docs folder
- **Issues**: Open a GitHub issue
- **Email**: info@rafaelabs.xyz

### Script Issues

If scripts don't work:
1. Check Python version (3.8+)
2. Check file locations
3. Check internet connection
4. Try manual process (see documentation files)

---

## 📄 License

These scripts are part of RAFAEL Framework and follow the same license.

---

**🔱 RAFAEL Framework v1.2.0**  
*Release Management Made Easy*

**Happy Releasing!** 🚀
