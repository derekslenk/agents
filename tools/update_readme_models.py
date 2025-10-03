#!/usr/bin/env python3
"""Synchronize README model tables with agent frontmatter definitions."""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
EXCLUDED_FILES = {"README.md", "WARP.md"}
AGENT_LINK_RE = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<path>[^)]+)\)")
SEPARATOR_CHARS = set("-: ")


class TableFormatError(RuntimeError):
    """Raised when a README table row cannot be parsed safely."""


def load_model_mapping() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in sorted(REPO_ROOT.glob("*.md")):
        if path.name in EXCLUDED_FILES:
            continue
        for line in path.read_text().splitlines():
            if line.startswith("model:"):
                mapping[path.stem] = line.split(":", 1)[1].strip()
                break
    return mapping


def parse_table_row(line: str) -> tuple[str, list[str]] | None:
    """Return agent filename and raw table segments for data rows."""

    stripped = line.strip()
    if not stripped.startswith("|"):
        return None

    segments = stripped.split("|")
    if len(segments) != 5:
        return None

    agent_cell = segments[1].strip()
    if not agent_cell or "[" not in agent_cell or "]" not in agent_cell:
        return None

    match = AGENT_LINK_RE.fullmatch(agent_cell)
    if not match:
        raise TableFormatError(f"Unrecognized agent cell format: {agent_cell!r}")

    path = match.group("path")
    if not path.endswith(".md"):
        raise TableFormatError(f"Agent link does not reference a markdown file: {path!r}")

    return path, segments


def update_readme(mapping: dict[str, str]) -> bool:
    original_lines = README_PATH.read_text().splitlines(keepends=True)
    updated_lines: list[str] = []
    changes = 0
    skipped = Counter()

    for raw_line in original_lines:
        line = raw_line.rstrip("\r\n")
        parsed = parse_table_row(line)
        if not parsed:
            updated_lines.append(raw_line)
            continue

        path, segments = parsed
        key = Path(path).stem
        desired_model = mapping.get(key)

        if desired_model is None:
            skipped["missing_agent"] += 1
            updated_lines.append(raw_line)
            continue

        desired_segment = f" {desired_model} "
        if segments[2] != desired_segment:
            segments[2] = desired_segment
            changes += 1

        updated_line = "|".join(segments)
        newline = ""
        if raw_line.endswith("\r\n"):
            newline = "\r\n"
        elif raw_line.endswith("\n"):
            newline = "\n"
        updated_lines.append(updated_line + newline)

    if changes:
        README_PATH.write_text("".join(updated_lines))

    if skipped:
        print("Warning: skipped rows ->", dict(skipped))

    return bool(changes)


def main() -> None:
    mapping = load_model_mapping()
    if not mapping:
        raise SystemExit("No agent model mappings found")

    try:
        updated = update_readme(mapping)
    except TableFormatError as exc:
        raise SystemExit(f"ERROR: {exc}") from exc

    if updated:
        print("README.md model assignments updated.")
    else:
        print("README.md already matches agent model assignments.")


if __name__ == "__main__":
    main()
