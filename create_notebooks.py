"""
Create NotebookLM notebooks for each Edukamu AI Developer course.

Uploads scraped markdown content directly as text sources (URLs are
access-restricted so NotebookLM can't crawl them).

Usage:
  1. Run `python scrape_courses.py` first (already done)
  2. Run `notebooklm login` to authenticate (already done)
  3. Run `python create_notebooks.py`
"""

import asyncio
import json
import time
from pathlib import Path
from courses import COURSES

try:
    from notebooklm import NotebookLMClient
except ImportError:
    print("notebooklm-py not installed. Run: pip install 'notebooklm-py[browser]'")
    raise SystemExit(1)

SCRAPED_DIR = Path("scraped_content")
NOTES_DIR = Path("notes")
PROGRESS_FILE = Path("progress.json")

COURSE_SLUGS = [
    "exploring-azure",
    "exploring-ai",
    "exploring-data-and-analytics",
    "accelerating-development-workflow",
    "cloud-native-data-storage",
    "azure-development",
    "ai-development",
]


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {}


def save_progress(progress: dict):
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2), encoding="utf-8")


def get_scraped_sections(course_idx: int) -> list[tuple[str, str]]:
    """Return list of (title, content) tuples for a course's sections, in order."""
    slug = COURSE_SLUGS[course_idx]
    course_dir = SCRAPED_DIR / slug
    if not course_dir.exists():
        return []

    sections = []
    for fpath in sorted(course_dir.glob("*.md")):
        title = fpath.stem.split("_", 1)[-1].replace("-", " ").title()
        content = fpath.read_text(encoding="utf-8")
        if content.strip():
            sections.append((title, content))
    return sections


async def delete_course_notebooks(client, course_names: set[str]):
    """Delete existing course notebooks so we can recreate them cleanly."""
    notebooks = await client.notebooks.list()
    for nb in notebooks:
        if nb.title in course_names:
            print(f"  Deleting old notebook: {nb.title}")
            try:
                await client.notebooks.delete(nb.id)
                await asyncio.sleep(1)
            except Exception as e:
                print(f"    [WARN] Could not delete {nb.title}: {e}")


async def create_course_notebook(client, course_idx: int, course: dict, progress: dict):
    name = course["name"]

    if progress.get(name, {}).get("sources_uploaded") and progress.get(name, {}).get("notebook_id"):
        print(f"  [SKIP] {name} — already done")
        return

    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")

    if name not in progress:
        progress[name] = {}

    # Create notebook
    print(f"  Creating notebook...")
    nb = await client.notebooks.create(name)
    progress[name]["notebook_id"] = nb.id
    save_progress(progress)
    print(f"  Notebook ID: {nb.id}")

    # Get scraped content
    sections = get_scraped_sections(course_idx)
    if not sections:
        print(f"  [ERROR] No scraped content found. Run: python scrape_courses.py {course_idx + 1}")
        return

    print(f"  Uploading {len(sections)} sections as text sources...")

    uploaded = []
    for i, (title, content) in enumerate(sections):
        try:
            source = await client.sources.add_text(nb.id, title, content)
            uploaded.append(title)
            print(f"    [{i+1}/{len(sections)}] ✓ {title}")
            await asyncio.sleep(1.5)  # avoid rate limiting
        except Exception as e:
            print(f"    [{i+1}/{len(sections)}] ✗ {title}: {e}")
            await asyncio.sleep(2)

    progress[name]["sources_uploaded"] = True
    progress[name]["sections_count"] = len(uploaded)
    save_progress(progress)

    print(f"  ✓ {len(uploaded)}/{len(sections)} sources uploaded")
    print(f"  Done! Open at: https://notebooklm.google.com")


async def main():
    NOTES_DIR.mkdir(exist_ok=True)
    progress = load_progress()

    print("Edukamu AI Developer — NotebookLM Notebook Creator")
    print("=" * 60)
    print(f"Courses: {len(COURSES)}")
    print(f"Source: scraped markdown files from {SCRAPED_DIR}/")
    print()

    # Check scraped content exists
    total_files = sum(1 for _ in SCRAPED_DIR.rglob("*.md"))
    if total_files == 0:
        print("ERROR: No scraped content found. Run: python scrape_courses.py")
        return
    print(f"Scraped files available: {total_files}")
    print()

    async with await NotebookLMClient.from_storage() as client:
        # Delete old broken notebooks first
        course_names = {c["name"] for c in COURSES}
        print("Cleaning up old notebooks with broken URL sources...")
        await delete_course_notebooks(client, course_names)
        print()

        # Create fresh notebooks with text content
        for i, course in enumerate(COURSES):
            await create_course_notebook(client, i, course, progress)

        print("\n" + "=" * 60)
        print("ALL DONE!")
        print("=" * 60)
        print("Open NotebookLM: https://notebooklm.google.com")
        print()
        for name, data in progress.items():
            if "notebook_id" in data:
                count = data.get("sections_count", "?")
                print(f"  ✓ {name} ({count} sources)")


if __name__ == "__main__":
    asyncio.run(main())
