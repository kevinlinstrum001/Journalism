#!/usr/bin/env python3
"""Generate repository-tree.txt for the Journalism repository.

Run from the repository root:
    python build_repository_tree.py

The generated tree is physical structure evidence for navigation. It is not
semantic authority for record identity, ownership, relationships, or status.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "repository-tree.txt"

EXCLUDED_DIRS = {".git", ".github", "__pycache__", ".venv", "venv", "node_modules"}
EXCLUDED_FILES = {OUTPUT.name}


def visible_entries(directory: Path) -> list[Path]:
    entries = []
    for path in directory.iterdir():
        if path.is_dir() and path.name in EXCLUDED_DIRS:
            continue
        if path.is_file() and path.name in EXCLUDED_FILES:
            continue
        entries.append(path)
    return sorted(entries, key=lambda p: (p.is_file(), p.name.lower()))


def walk(directory: Path, prefix: str = "") -> list[str]:
    lines: list[str] = []
    entries = visible_entries(directory)

    for index, path in enumerate(entries):
        last = index == len(entries) - 1
        connector = "└── " if last else "├── "
        suffix = "/" if path.is_dir() else ""
        lines.append(f"{prefix}{connector}{path.name}{suffix}")

        if path.is_dir():
            extension = "    " if last else "│   "
            lines.extend(walk(path, prefix + extension))

    return lines


def main() -> None:
    lines = [f"{ROOT.name}/"] + walk(ROOT)
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(lines)} lines.")


if __name__ == "__main__":
    main()
