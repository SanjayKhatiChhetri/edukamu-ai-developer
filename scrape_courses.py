"""
Scrape all Edukamu course content by fetching raw markdown files from Firebase.

Usage:
  python scrape_courses.py           # Scrape all courses
  python scrape_courses.py 1         # Scrape only course 1
  python scrape_courses.py 1 3 7     # Scrape courses 1, 3, and 7
"""

import asyncio
import sys
from pathlib import Path
import httpx
from courses import COURSES

OUTPUT_DIR = Path("scraped_content")

FIREBASE_HOSTS = {
    "exploring-azure": "ek-msc2-dev-ai-azure-funda.web.app",
    "exploring-ai": "ek-msc2-da-azure-ai-fund.web.app",
    "exploring-data-and-analytics": "ek-msc2-azure-data-fund.web.app",
    "accelerating-development-workflow": "ek-msc2-da-github-copilot.web.app",
    "cloud-native-data-storage": "ek-msc2-da-azure-cosmos.web.app",
    "azure-development": "ek-msc2-da-azure-dev-assoc.web.app",
    "ai-development": "ek-msc2-azure-ai-dev.web.app",
}

# Courses 5-7 use a numbered prefix in the markdown filename: {N}-{slug}.md
NUMBERED_PREFIX_COURSES = {
    "cloud-native-data-storage",
    "azure-development",
    "ai-development",
}


def parse_section_url(url: str) -> tuple[str, str, str]:
    """Return (course_slug, unit_number, section_slug) from a section URL."""
    parts = url.rstrip("/").split("/")
    return parts[3], parts[4], parts[5]


def compute_section_index(course: dict, section_url: str) -> int:
    """Return the 1-indexed position of a section within its unit."""
    _, target_unit, _ = parse_section_url(section_url)
    idx = 1
    for url in course["sections"]:
        _, unit, slug = parse_section_url(url)
        if url == section_url:
            return idx
        if unit == target_unit:
            idx += 1
    return idx


def build_md_url(course_slug: str, unit_num: str, section_slug: str, section_idx: int = 0) -> str:
    host = FIREBASE_HOSTS[course_slug]
    if course_slug in NUMBERED_PREFIX_COURSES:
        return f"https://{host}/chapters/module{unit_num}/{section_idx}-{section_slug}.md"
    return f"https://{host}/chapters/module{unit_num}/{section_slug}.md"


async def fetch_section(client: httpx.AsyncClient, course_slug: str, section_url: str, section_idx: int) -> tuple[str, str]:
    """Fetch a single section markdown file. Returns (filename, content)."""
    _, unit_num, section_slug = parse_section_url(section_url)
    md_url = build_md_url(course_slug, unit_num, section_slug, section_idx)
    filename = f"{unit_num}_{section_slug}.md"

    try:
        resp = await client.get(md_url)
        if resp.status_code == 200:
            return filename, resp.text
        else:
            print(f"    [WARN] {filename}: HTTP {resp.status_code} ({md_url})")
            return filename, ""
    except Exception as e:
        print(f"    [ERROR] {filename}: {e}")
        return filename, ""


async def scrape_course(course_idx: int):
    course = COURSES[course_idx]
    course_slug = course["url"].rstrip("/").split("/")[-1]
    out_dir = OUTPUT_DIR / course_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"  {course['name']} ({len(course['sections'])} sections)")
    print(f"  Firebase: {FIREBASE_HOSTS.get(course_slug, 'UNKNOWN')}")
    print(f"{'='*60}")

    if course_slug not in FIREBASE_HOSTS:
        print(f"  [ERROR] No Firebase host mapping for {course_slug}")
        return

    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        # Fetch all sections concurrently
        tasks = []
        cached = 0
        to_fetch = []

        for section_url in course["sections"]:
            _, unit_num, section_slug = parse_section_url(section_url)
            filename = f"{unit_num}_{section_slug}.md"
            out_file = out_dir / filename

            if out_file.exists() and out_file.stat().st_size > 50:
                cached += 1
                continue
            to_fetch.append(section_url)

        if cached > 0:
            print(f"  [CACHED] {cached} sections already scraped")

        if not to_fetch:
            print(f"  All sections already scraped!")
            return

        print(f"  Fetching {len(to_fetch)} sections...")
        results = await asyncio.gather(
            *[
                fetch_section(client, course_slug, url, compute_section_index(course, url))
                for url in to_fetch
            ]
        )

        ok = 0
        for filename, content in results:
            if content:
                (out_dir / filename).write_text(content, encoding="utf-8")
                ok += 1

        print(f"  Result: {ok} OK, {len(to_fetch) - ok} failed")


async def main():
    if len(sys.argv) > 1:
        course_nums = [int(x) for x in sys.argv[1:]]
    else:
        course_nums = list(range(1, len(COURSES) + 1))

    print("Edukamu Course Scraper (Direct Markdown Fetch)")
    print("=" * 60)
    print(f"Courses: {course_nums}")

    for num in course_nums:
        if num < 1 or num > len(COURSES):
            print(f"  [SKIP] Invalid course number: {num}")
            continue
        await scrape_course(num - 1)

    print(f"\nAll content saved to: {OUTPUT_DIR.absolute()}")
    total_files = sum(1 for _ in OUTPUT_DIR.rglob("*.md"))
    total_size = sum(f.stat().st_size for f in OUTPUT_DIR.rglob("*.md"))
    print(f"Total files: {total_files}, Total size: {total_size / 1024:.1f} KB")


if __name__ == "__main__":
    asyncio.run(main())
