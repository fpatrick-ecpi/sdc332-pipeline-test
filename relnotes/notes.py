"""Read CHANGELOG.md into (version, [notes]) pairs."""
from pathlib import Path

CHANGELOG = Path(__file__).resolve().parent.parent / "CHANGELOG.md"


def read_notes(path=CHANGELOG):
    releases = []
    for line in Path(path).read_text().splitlines():
        if line.startswith("## "):
            releases.append((line[3:].strip(), []))
        elif line.startswith("- ") and releases:
            releases[-1][1].append(line[2:].strip())
    return releases
