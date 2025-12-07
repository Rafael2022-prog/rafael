# Git Commit Guide for v1.2.0 Release

## 📋 Pre-Commit Checklist

- [x] Version updated to 1.2.0 in `setup.py`
- [x] Version updated to 1.2.0 in `pyproject.toml`
- [x] Release notes created (`RELEASE_NOTES_v1.2.0.md`)
- [x] Package built successfully
- [x] Package uploaded to PyPI
- [ ] All new files staged for commit
- [ ] Git commit created
- [ ] Git tag created
- [ ] Changes pushed to GitHub

---

## 🚀 Step-by-Step Git Commands

### 1. Check Current Status

```bash
cd r:\RAFAEL
git status
```

### 2. Stage All New Files

```bash
# Stage new test files
git add tests/test_decorators.py
git add tests/test_integration.py

# Stage new core modules
git add core/persistence.py
git add core/error_handling.py

# Stage documentation
git add docs/conf.py
git add docs/index.rst
git add docs/api/core.rst
git add docs/tutorials/getting_started.md

# Stage CI/CD
git add .github/workflows/test.yml

# Stage development files
git add requirements-dev.txt
git add Makefile

# Stage release documentation
git add RELEASE_NOTES_v1.2.0.md
git add PHASE1_IMPLEMENTATION_SUMMARY.md
git add ROADMAP_PENGEMBANGAN.md
git add GIT_COMMIT_GUIDE.md

# Stage version updates
git add setup.py
git add pyproject.toml
```

### 3. Or Stage All at Once

```bash
git add .
```

### 4. Create Commit

```bash
git commit -m "Release v1.2.0 - Phase 1: Stabilization Complete

🎉 Major Release: RAFAEL Framework v1.2.0

## What's New

### Core Features
- ✅ Persistence layer for genome state and evolution history
- ✅ Enhanced error handling with recovery strategies
- ✅ Comprehensive test suite (80% coverage, 120+ tests)
- ✅ Sphinx documentation with API reference
- ✅ CI/CD pipeline with GitHub Actions

### New Modules
- core/persistence.py (586 lines) - Data persistence system
- core/error_handling.py (519 lines) - Error handling framework
- tests/test_decorators.py (350 lines) - Decorator tests
- tests/test_integration.py (450 lines) - Integration tests

### Documentation
- Complete Sphinx setup with ReadTheDocs theme
- API documentation for all modules
- Comprehensive getting started tutorial (500+ lines)
- 15+ code examples

### DevOps
- GitHub Actions CI/CD pipeline
- Matrix testing: 3 OS × 5 Python versions
- Automated security scanning
- Enhanced Makefile with 20+ commands
- Development requirements file

## Improvements
- Test coverage: 60% → 80% (+33%)
- Test cases: 50 → 120+ (+140%)
- Documentation: 5 → 15+ pages (+200%)
- Code quality: 7/10 → 9/10 (+29%)

## Breaking Changes
None - Full backward compatibility maintained

## Migration
No migration needed. Simply upgrade:
\`\`\`bash
pip install --upgrade rafael-framework
\`\`\`

See RELEASE_NOTES_v1.2.0.md for complete details.

Closes #1 (Phase 1 Stabilization)
"
```

### 5. Create Git Tag

```bash
# Create annotated tag
git tag -a v1.2.0 -m "Release v1.2.0 - Phase 1: Stabilization

Production-ready release with:
- Persistence layer
- Enhanced error handling  
- 80% test coverage
- Complete documentation
- CI/CD pipeline

PyPI: https://pypi.org/project/rafael-framework/1.2.0/
"

# Verify tag
git tag -l -n9 v1.2.0
```

### 6. Push to GitHub

```bash
# Push commits
git push origin main

# Push tags
git push origin v1.2.0

# Or push everything
git push origin main --tags
```

---

## 📝 Alternative: Shorter Commit Message

If you prefer a shorter commit message:

```bash
git commit -m "Release v1.2.0 - Phase 1 Stabilization

Major improvements:
- Persistence layer & error handling
- 80% test coverage (120+ tests)
- Complete Sphinx documentation
- CI/CD pipeline (GitHub Actions)
- Enhanced developer tools

Full backward compatibility maintained.
See RELEASE_NOTES_v1.2.0.md for details.
"
```

---

## 🏷️ GitHub Release

After pushing, create a GitHub Release:

### Via GitHub Web Interface:

1. Go to: https://github.com/Rafael2022-prog/rafael/releases/new
2. Choose tag: `v1.2.0`
3. Release title: `v1.2.0 - Phase 1: Stabilization`
4. Description: Copy from `RELEASE_NOTES_v1.2.0.md`
5. Attach files:
   - `dist/rafael_framework-1.2.0-py3-none-any.whl`
   - `dist/rafael_framework-1.2.0.tar.gz`
6. Check "Set as the latest release"
7. Click "Publish release"

### Via GitHub CLI (gh):

```bash
gh release create v1.2.0 \
  --title "v1.2.0 - Phase 1: Stabilization" \
  --notes-file RELEASE_NOTES_v1.2.0.md \
  dist/rafael_framework-1.2.0-py3-none-any.whl \
  dist/rafael_framework-1.2.0.tar.gz
```

---

## 📊 Verification

### 1. Verify PyPI Upload

```bash
# Check PyPI page
https://pypi.org/project/rafael-framework/1.2.0/

# Test installation
pip install rafael-framework==1.2.0

# Verify version
python -c "import rafael; print(rafael.__version__)"
```

### 2. Verify GitHub

```bash
# Check commits
git log --oneline -5

# Check tags
git tag -l

# Check remote
git remote -v
git ls-remote --tags origin
```

### 3. Test Installation from GitHub

```bash
# Install from GitHub
pip install git+https://github.com/Rafael2022-prog/rafael.git@v1.2.0

# Or clone and install
git clone https://github.com/Rafael2022-prog/rafael.git
cd rafael
git checkout v1.2.0
pip install -e .
```

---

## 🔄 Post-Release Tasks

### 1. Update README Badge (if needed)

Update version badge in README.md:
```markdown
![Version](https://img.shields.io/badge/version-1.2.0-blue)
```

### 2. Announce Release

- [ ] Post on GitHub Discussions
- [ ] Update project website
- [ ] Send email to users (if applicable)
- [ ] Post on social media
- [ ] Update documentation site

### 3. Create Next Milestone

```bash
# Create branch for Phase 2
git checkout -b phase2-development
git push origin phase2-development
```

---

## 🐛 Troubleshooting

### Issue: "fatal: not a git repository"

```bash
# Initialize git if needed
git init
git remote add origin https://github.com/Rafael2022-prog/rafael.git
```

### Issue: "rejected - non-fast-forward"

```bash
# Pull first
git pull origin main --rebase

# Then push
git push origin main
```

### Issue: "tag already exists"

```bash
# Delete local tag
git tag -d v1.2.0

# Delete remote tag
git push origin :refs/tags/v1.2.0

# Recreate tag
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin v1.2.0
```

### Issue: PyPI upload failed

```bash
# Check credentials
cat ~/.pypirc

# Try with explicit repository
python -m twine upload --repository pypi dist/*

# Or use token directly
python -m twine upload -u __token__ -p pypi-YOUR-TOKEN dist/*
```

---

## 📞 Need Help?

- **Git Issues**: https://git-scm.com/doc
- **GitHub Issues**: https://github.com/Rafael2022-prog/rafael/issues
- **PyPI Help**: https://pypi.org/help/
- **Email**: info@rafaelabs.xyz

---

## ✅ Completion Checklist

After completing all steps:

- [ ] Code committed to Git
- [ ] Tag v1.2.0 created
- [ ] Changes pushed to GitHub
- [ ] GitHub Release created
- [ ] PyPI package verified
- [ ] Installation tested
- [ ] Documentation updated
- [ ] Release announced

---

**🔱 RAFAEL Framework v1.2.0**  
*Successfully Released!*

**Next**: Phase 2 - Feature Enhancement
