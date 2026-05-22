"""
Generate a structured Learning Diary from scraped course markdown content.

Usage:
  1. First run: python scrape_courses.py
  2. Then run:  python generate_diary.py

Produces learning_diary/ with:
  - README.md                  (master index)
  - course_1_azure.md          (per-course reference)
  - ...
  - cheatsheet.md              (quick-reference across all courses)
"""

import re
from pathlib import Path
from courses import COURSES

SCRAPED_DIR = Path("scraped_content")
DIARY_DIR = Path("learning_diary")

COURSE_SLUGS = [
    "exploring-azure",
    "exploring-ai",
    "exploring-data-and-analytics",
    "accelerating-development-workflow",
    "cloud-native-data-storage",
    "azure-development",
    "ai-development",
]

COURSE_SHORT = [
    "azure", "ai", "data_analytics", "dev_workflow",
    "cloud_storage", "azure_dev", "ai_dev",
]


# ── helpers ────────────────────────────────────────────────────────────

def extract_headings(md: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r'^#{1,3}\s+(.+)', md, re.M)]


def extract_definitions(md: str) -> list[tuple[str, str]]:
    """Pull out bold-term + description patterns from markdown."""
    defs = []
    # Pattern: **Term**: description  or  **Term** - description
    for m in re.finditer(r'\*\*([^*]{3,60})\*\*[:\s\-–]+(.+?)(?:\n|$)', md):
        term = m.group(1).strip()
        desc = m.group(2).strip()
        if len(desc) > 15:
            defs.append((term, desc))
    return defs


def extract_bullet_points(md: str) -> list[str]:
    """Extract meaningful bullet points."""
    points = []
    for m in re.finditer(r'^[-*]\s+(.{30,250})', md, re.M):
        points.append(m.group(1).strip())
    return points


def first_paragraph(md: str) -> str:
    """Return the first non-heading paragraph."""
    blocks = re.split(r'\n{2,}', md.strip())
    for b in blocks:
        b = b.strip()
        if b.startswith('#') or len(b) < 40:
            continue
        clean = re.sub(r'\*\*|__|\[([^\]]+)\]\([^)]+\)', r'\1', b)
        return clean[:350] + ('...' if len(clean) > 350 else '')
    return ''


def section_title(slug: str) -> str:
    return slug.replace('-', ' ').title()


# ── per-course diary ──────────────────────────────────────────────────

def generate_course_diary(idx: int) -> str:
    course = COURSES[idx]
    slug = COURSE_SLUGS[idx]
    course_dir = SCRAPED_DIR / slug

    if not course_dir.exists():
        return f"# {course['name']}\n\n> Not scraped yet.  Run `python scrape_courses.py {idx+1}`\n"

    L = []  # output lines
    L.append(f"# {course['name']}")
    L.append(f"")
    L.append(f"**URL:** [{course['url']}]({course['url']})  ")
    L.append(f"**Sections:** {len(course['sections'])}  ")
    L.append(f"")
    L.append(f"---")
    L.append(f"")

    # Group files by unit
    files = sorted(course_dir.glob("*.md"))
    units: dict[str, list[Path]] = {}
    for f in files:
        unit = f.stem.split('_')[0]
        units.setdefault(unit, []).append(f)

    # TOC
    L.append("## Table of Contents\n")
    for unit_num in sorted(units):
        titles = [section_title(f.stem.split('_', 1)[1]) for f in units[unit_num]]
        L.append(f"- **Unit {unit_num}:** " + " | ".join(titles[:3]) + (" ..." if len(titles) > 3 else ""))
    L.append("")
    L.append("---\n")

    # Process each unit
    all_terms: list[tuple[str, str, str]] = []  # (term, def, section)

    for unit_num in sorted(units):
        L.append(f"## Unit {unit_num}\n")

        for fpath in units[unit_num]:
            sec_slug = fpath.stem.split('_', 1)[1]
            title = section_title(sec_slug)
            md = fpath.read_text(encoding='utf-8')

            L.append(f"### {title}\n")

            # TL;DR
            intro = first_paragraph(md)
            if intro:
                L.append(f"**TL;DR:** {intro}\n")

            # Key headings / topics covered
            headings = extract_headings(md)
            sub_headings = [h for h in headings if h != headings[0]] if headings else []
            if sub_headings:
                L.append("**Topics covered:**")
                for h in sub_headings[:10]:
                    L.append(f"- {h}")
                L.append("")

            # Definitions / key terms
            defs = extract_definitions(md)
            if defs:
                L.append("**Key Terms:**\n")
                L.append("| Term | Definition |")
                L.append("|------|-----------|")
                for term, defn in defs[:10]:
                    defn_short = defn[:180].replace('|', '\\|')
                    if len(defn) > 180:
                        defn_short = defn_short.rsplit(' ', 1)[0] + '...'
                    L.append(f"| {term} | {defn_short} |")
                    all_terms.append((term, defn_short, title))
                L.append("")

            # Key bullet points
            bullets = extract_bullet_points(md)
            if bullets:
                L.append("**Key Points:**")
                for bp in bullets[:8]:
                    bp_clean = re.sub(r'\*\*|__|\[([^\]]+)\]\([^)]+\)', r'\1', bp)
                    bp_short = bp_clean[:200]
                    if len(bp_clean) > 200:
                        bp_short = bp_short.rsplit(' ', 1)[0] + '...'
                    L.append(f"- {bp_short}")
                L.append("")

            # Personal notes placeholder
            L.append("<details><summary>📝 My Notes</summary>\n")
            L.append("_Write your own observations, questions, or mnemonics here._\n")
            L.append("</details>\n")
            L.append("---\n")

    # Quick-reference glossary at the end
    if all_terms:
        L.append("## Quick-Reference Glossary\n")
        L.append("| Term | Definition | Section |")
        L.append("|------|-----------|---------|")
        seen = set()
        for term, defn, sec in all_terms:
            key = term.lower()
            if key not in seen:
                seen.add(key)
                L.append(f"| {term} | {defn} | {sec} |")
        L.append("")

    L.append("---\n")
    L.append("*Auto-generated by `generate_diary.py` — re-run to refresh after re-scraping.*\n")

    return '\n'.join(L)


# ── master index ──────────────────────────────────────────────────────

def generate_master_index() -> str:
    L = []
    L.append("# Learning Diary — AI Developer Program")
    L.append("")
    L.append("**Program:** Microsoft Skills for Jobs — AI Developer (10 ECTS)  ")
    L.append("**Platform:** [Edukamu](https://skill.edukamu.fi/aideveloper/)  ")
    L.append("**Purpose:** Quick-reference memory refresher for everything learned.")
    L.append("")
    L.append("---\n")
    L.append("## Courses\n")

    for i, course in enumerate(COURSES):
        fn = f"course_{i+1}_{COURSE_SHORT[i]}.md"
        L.append(f"{i+1}. [{course['name']}]({fn})  ")
        L.append(f"   {len(course['sections'])} sections — {course['url']}")
        L.append("")

    L.append("**Cross-course cheat sheet:** [cheatsheet.md](cheatsheet.md)\n")
    L.append("---\n")
    L.append("## How to Use\n")
    L.append("- **Forgot a concept?** `Ctrl+F` in the course file or cheatsheet")
    L.append("- **Quick refresher?** Read the **TL;DR** and **Key Terms** tables")
    L.append("- **Deeper review?** Expand each section's topics and key points")
    L.append("- **Personal notes?** Click the _My Notes_ dropdowns to add your insights")
    L.append("")
    L.append("## Regenerate\n")
    L.append("```bash")
    L.append("python scrape_courses.py   # fetch latest content")
    L.append("python generate_diary.py   # rebuild this diary")
    L.append("```\n")

    return '\n'.join(L)


# ── cheatsheet ────────────────────────────────────────────────────────

def generate_cheatsheet() -> str:
    L = []
    L.append("# Cheat Sheet — AI Developer Program\n")
    L.append("One-page quick reference across all 7 courses. `Ctrl+F` is your friend.\n")
    L.append("---\n")

    for i, course in enumerate(COURSES):
        slug = COURSE_SLUGS[i]
        course_dir = SCRAPED_DIR / slug
        L.append(f"## {course['name']}\n")

        if not course_dir.exists():
            L.append(f"> Not scraped. Run `python scrape_courses.py {i+1}`\n")
            continue

        all_defs = []
        all_bullets = []
        for fpath in sorted(course_dir.glob("*.md")):
            md = fpath.read_text(encoding='utf-8')
            all_defs.extend(extract_definitions(md)[:3])
            all_bullets.extend(extract_bullet_points(md)[:2])

        if all_defs:
            L.append("**Key Terms:**")
            seen = set()
            for term, defn in all_defs:
                if term.lower() not in seen:
                    seen.add(term.lower())
                    short = defn[:120]
                    if len(defn) > 120:
                        short = short.rsplit(' ', 1)[0] + '...'
                    L.append(f"- **{term}:** {short}")
            L.append("")

        if all_bullets:
            L.append("**Key Facts:**")
            seen = set()
            for bp in all_bullets:
                clean = re.sub(r'\*\*|__|\[([^\]]+)\]\([^)]+\)', r'\1', bp)[:150]
                if clean not in seen:
                    seen.add(clean)
                    L.append(f"- {clean}")
            L.append("")

        L.append("---\n")

    return '\n'.join(L)


# ── main ──────────────────────────────────────────────────────────────

def main():
    DIARY_DIR.mkdir(exist_ok=True)
    print("Generating Learning Diary")
    print("=" * 60)

    idx = generate_master_index()
    (DIARY_DIR / "README.md").write_text(idx, encoding='utf-8')
    print("  [OK] README.md")

    for i in range(len(COURSES)):
        fn = f"course_{i+1}_{COURSE_SHORT[i]}.md"
        diary = generate_course_diary(i)
        (DIARY_DIR / fn).write_text(diary, encoding='utf-8')
        print(f"  [OK] {fn}")

    cs = generate_cheatsheet()
    (DIARY_DIR / "cheatsheet.md").write_text(cs, encoding='utf-8')
    print("  [OK] cheatsheet.md")

    total = sum(1 for _ in DIARY_DIR.glob('*.md'))
    size = sum(f.stat().st_size for f in DIARY_DIR.glob('*.md'))
    print(f"\nDiary generated in: {DIARY_DIR.absolute()}")
    print(f"Files: {total}, Size: {size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
