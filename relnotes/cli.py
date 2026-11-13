"""Command line: print the release notes."""
from relnotes.notes import read_notes


def main():
    for version, notes in read_notes():
        print(version)
        for note in notes:
            print(f"  - {note}")


if __name__ == "__main__":
    main()
