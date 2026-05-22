# Edukamu AI Developer — Learning Diary & NotebookLM

Study notes, cheat sheets, and Google NotebookLM notebooks for the **Microsoft Skills for Jobs — AI Developer** program (10 ECTS) via [Edukamu](https://skill.edukamu.fi/aideveloper/).

## Live Site

The learning diary is hosted as a Jekyll site on GitHub Pages:

**[View the Learning Diary &rarr;](https://sanjaykhatichhetri.github.io/edukamu-ai-developer/)**
<!-- Replace # with your GitHub Pages URL after deployment -->

## What's Inside

### Learning Diary (Jekyll Site)

A searchable reference covering all 7 courses (100 sections):

| # | Course | Sections |
|---|--------|----------|
| 1 | Exploring Microsoft Azure | 15 |
| 2 | Exploring Artificial Intelligence | 21 |
| 3 | Exploring Data and Analytics | 12 |
| 4 | Accelerating Development Workflow | 11 |
| 5 | Getting Started with Cloud Native Data Storage | 12 |
| 6 | Getting Started with Azure Development | 14 |
| 7 | Getting Started with AI Development | 15 |

Each course page includes:
- **TL;DR** summaries per section
- **Key Terms** tables with definitions
- **Key Points** extracted from course material
- **My Notes** expandable sections for personal annotations
- **Cross-course Cheat Sheet** for quick lookups

### NotebookLM Notebooks

7 Google NotebookLM notebooks with all course content uploaded as text sources. Use them for:
- AI-powered Q&A about course material
- Audio overview generation (podcast-style summaries)
- Auto-generated study guides and FAQs

### Tooling

| Script | Purpose |
|--------|---------|
| `scrape_courses.py` | Fetch course markdown from Firebase |
| `create_notebooks.py` | Create NotebookLM notebooks with scraped content |
| `generate_diary.py` | Generate learning diary from scraped content |
| `note_single_course.py` | Generate notes/flashcards/quiz for a single course |

## Project Structure

```
.
├── docs/                    # Jekyll site (GitHub Pages)
│   ├── _config.yml
│   ├── index.md             # Home page
│   ├── cheatsheet.md        # Cross-course cheat sheet
│   └── courses/             # Individual course pages
├── learning_diary/          # Source markdown files
├── scraped_content/         # Raw course content (100 .md files)
├── notes/                   # NotebookLM-generated notes
├── courses.py               # Course metadata
├── scrape_courses.py        # Content scraper
├── create_notebooks.py      # NotebookLM notebook creator
└── generate_diary.py        # Diary generator
```

## Setup

```bash
# 1. Scrape course content
pip install httpx
python scrape_courses.py

# 2. Generate learning diary
python generate_diary.py

# 3. Create NotebookLM notebooks (requires Google auth)
pip install 'notebooklm-py[browser]'
notebooklm login
python create_notebooks.py
```

## Tech Stack

- **Content source:** Firebase-hosted markdown (Edukamu SPA)
- **Scraping:** httpx (direct HTTP fetch, no browser needed)
- **NotebookLM:** notebooklm-py (unofficial async API wrapper)
- **Site:** Jekyll + just-the-docs theme on GitHub Pages
- **Auth:** Playwright-based Google login for NotebookLM

## License

Personal study notes. Course content belongs to Edukamu / Microsoft.
