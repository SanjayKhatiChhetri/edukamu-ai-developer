"""
Create a NotebookLM notebook for a single course.

Usage:
  python note_single_course.py <course_number>

Example:
  python note_single_course.py 1    # Course 1: Exploring Microsoft Azure
  python note_single_course.py 7    # Course 7: Getting Started with AI Development
"""

import asyncio
import sys
import time
from pathlib import Path
from courses import COURSES

try:
    from notebooklm import NotebookLMClient
except ImportError:
    print("notebooklm-py not installed. Run: pip install 'notebooklm-py[browser]'")
    raise SystemExit(1)

NOTES_DIR = Path("notes")

PROMPTS = {
    "summary": (
        "Create comprehensive study notes for this course. Include:\n"
        "1. Course overview and learning objectives\n"
        "2. Key concepts and definitions for each unit\n"
        "3. Important Azure services, tools, and features mentioned\n"
        "4. Practical takeaways and things to remember\n"
        "Format with clear headings and bullet points."
    ),
    "flashcards": (
        "Create a set of flashcards (question and answer pairs) covering "
        "the most important concepts from this course. Include at least "
        "20 flashcards covering key terms, services, and concepts."
    ),
    "quiz": (
        "Create a practice quiz with 15 multiple-choice questions based on "
        "the course content. Include the correct answer and a brief explanation "
        "for each question."
    ),
}


async def main():
    if len(sys.argv) < 2:
        print("Usage: python note_single_course.py <course_number> [note_type]")
        print("  course_number: 1-7")
        print("  note_type: summary (default), flashcards, quiz")
        print("\nAvailable courses:")
        for i, c in enumerate(COURSES, 1):
            print(f"  {i}. {c['name']}")
        return

    course_num = int(sys.argv[1])
    if course_num < 1 or course_num > len(COURSES):
        print(f"Invalid course number. Choose 1-{len(COURSES)}")
        return

    note_type = sys.argv[2] if len(sys.argv) > 2 else "summary"
    if note_type not in PROMPTS:
        print(f"Invalid note type. Choose: {', '.join(PROMPTS.keys())}")
        return

    course = COURSES[course_num - 1]
    NOTES_DIR.mkdir(exist_ok=True)

    print(f"Processing: {course['name']}")
    print(f"Note type: {note_type}")
    print(f"Sections to add: {len(course['sections'])}")
    print()

    async with await NotebookLMClient.from_storage() as client:
        print("Creating notebook...")
        nb = await client.notebooks.create(f"{course['name']} - {note_type.title()}")
        print(f"Notebook ID: {nb.id}")

        print(f"\nAdding main course URL...")
        try:
            await client.sources.add_url(nb.id, course["url"])
            time.sleep(2)
        except Exception as e:
            print(f"  [WARN] {e}")

        for i, url in enumerate(course["sections"]):
            name = url.split("/")[-1].replace("-", " ").title()
            print(f"  Adding [{i+1}/{len(course['sections'])}]: {name}")
            try:
                await client.sources.add_url(nb.id, url)
                time.sleep(2)
            except Exception as e:
                print(f"    [WARN] {e}")

        print(f"\nGenerating {note_type}...")
        result = await client.chat.ask(nb.id, PROMPTS[note_type])

        filename = f"Course_{course_num}_{note_type}.md"
        output = NOTES_DIR / filename
        output.write_text(f"# {course['name']} - {note_type.title()}\n\n{result.answer}")
        print(f"\nSaved to: {output}")


if __name__ == "__main__":
    asyncio.run(main())
