#!/usr/bin/env python3
"""
Git Graph Painter - Draw text on your GitHub contribution graph
"""

import subprocess
import os
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

FONT = {
    'A': [
        "  #  ",
        " # # ",
        "#   #",
        "#####",
        "#   #",
        "#   #",
        "#   #",
    ],
    'B': [
        "#### ",
        "#   #",
        "#   #",
        "#### ",
        "#   #",
        "#   #",
        "#### ",
    ],
    'C': [
        " ### ",
        "#   #",
        "#    ",
        "#    ",
        "#    ",
        "#   #",
        " ### ",
    ],
    'D': [
        "#### ",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#### ",
    ],
    'E': [
        "#####",
        "#    ",
        "#    ",
        "#### ",
        "#    ",
        "#    ",
        "#####",
    ],
    'F': [
        "#####",
        "#    ",
        "#    ",
        "#### ",
        "#    ",
        "#    ",
        "#    ",
    ],
    'G': [
        " ### ",
        "#   #",
        "#    ",
        "# ###",
        "#   #",
        "#   #",
        " ### ",
    ],
    'H': [
        "#   #",
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #",
        "#   #",
    ],
    'I': [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "#####",
    ],
    'J': [
        "#####",
        "    #",
        "    #",
        "    #",
        "#   #",
        "#   #",
        " ### ",
    ],
    'K': [
        "#   #",
        "#  # ",
        "# #  ",
        "##   ",
        "# #  ",
        "#  # ",
        "#   #",
    ],
    'L': [
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#####",
    ],
    'M': [
        "#   #",
        "## ##",
        "# # #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
    ],
    'N': [
        "#   #",
        "##  #",
        "# # #",
        "#  ##",
        "#   #",
        "#   #",
        "#   #",
    ],
    'O': [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " ### ",
    ],
    'P': [
        "#### ",
        "#   #",
        "#   #",
        "#### ",
        "#    ",
        "#    ",
        "#    ",
    ],
    'Q': [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        "# # #",
        "#  # ",
        " ## #",
    ],
    'R': [
        "#### ",
        "#   #",
        "#   #",
        "#### ",
        "# #  ",
        "#  # ",
        "#   #",
    ],
    'S': [
        " ####",
        "#    ",
        "#    ",
        " ### ",
        "    #",
        "    #",
        "#### ",
    ],
    'T': [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
    ],
    'U': [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " ### ",
    ],
    'V': [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " # # ",
        " # # ",
        "  #  ",
    ],
    'W': [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "# # #",
        "## ##",
        "#   #",
    ],
    'X': [
        "#   #",
        "#   #",
        " # # ",
        "  #  ",
        " # # ",
        "#   #",
        "#   #",
    ],
    'Y': [
        "#   #",
        "#   #",
        " # # ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
    ],
    'Z': [
        "#####",
        "    #",
        "   # ",
        "  #  ",
        " #   ",
        "#    ",
        "#####",
    ],
    '0': [
        " ### ",
        "#   #",
        "#  ##",
        "# # #",
        "##  #",
        "#   #",
        " ### ",
    ],
    '1': [
        "  #  ",
        " ##  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "#####",
    ],
    '2': [
        " ### ",
        "#   #",
        "    #",
        "  ## ",
        " #   ",
        "#    ",
        "#####",
    ],
    '3': [
        "#####",
        "    #",
        "   # ",
        "  ## ",
        "    #",
        "#   #",
        " ### ",
    ],
    '4': [
        "   # ",
        "  ## ",
        " # # ",
        "#  # ",
        "#####",
        "   # ",
        "   # ",
    ],
    '5': [
        "#####",
        "#    ",
        "#### ",
        "    #",
        "    #",
        "#   #",
        " ### ",
    ],
    '6': [
        " ### ",
        "#    ",
        "#    ",
        "#### ",
        "#   #",
        "#   #",
        " ### ",
    ],
    '7': [
        "#####",
        "    #",
        "   # ",
        "  #  ",
        " #   ",
        " #   ",
        " #   ",
    ],
    '8': [
        " ### ",
        "#   #",
        "#   #",
        " ### ",
        "#   #",
        "#   #",
        " ### ",
    ],
    '9': [
        " ### ",
        "#   #",
        "#   #",
        " ####",
        "    #",
        "    #",
        " ### ",
    ],
    ' ': [
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
    ],
    '!': [
        " # ",
        " # ",
        " # ",
        " # ",
        " # ",
        "   ",
        " # ",
    ],
    '.': [
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "# ",
    ],
    '-': [
        "     ",
        "     ",
        "     ",
        "#####",
        "     ",
        "     ",
        "     ",
    ],
    '_': [
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
        "#####",
    ],
    '<': [
        "   #",
        "  # ",
        " #  ",
        "#   ",
        " #  ",
        "  # ",
        "   #",
    ],
    '>': [
        "#   ",
        " #  ",
        "  # ",
        "   #",
        "  # ",
        " #  ",
        "#   ",
    ],
    '3': [
        "#####",
        "    #",
        "   # ",
        "  ## ",
        "    #",
        "#   #",
        " ### ",
    ],
    ':': [
        "  ",
        "# ",
        "# ",
        "  ",
        "# ",
        "# ",
        "  ",
    ],
    '/': [
        "    #",
        "   # ",
        "   # ",
        "  #  ",
        " #   ",
        " #   ",
        "#    ",
    ],
    '?': [
        " ### ",
        "#   #",
        "    #",
        "   # ",
        "  #  ",
        "     ",
        "  #  ",
    ],
    '*': [
        "     ",
        "# # #",
        " ### ",
        "#####",
        " ### ",
        "# # #",
        "     ",
    ],
    '+': [
        "     ",
        "  #  ",
        "  #  ",
        "#####",
        "  #  ",
        "  #  ",
        "     ",
    ],
    '=': [
        "     ",
        "     ",
        "#####",
        "     ",
        "#####",
        "     ",
        "     ",
    ],
}

def text_to_grid(text: str) -> List[List[bool]]:
    """Convert text to a 7-row pixel grid."""
    text = text.upper()
    grid = [[] for _ in range(7)]

    for i, char in enumerate(text):
        if char not in FONT:
            char = ' '

        char_pattern = FONT[char]
        for row in range(7):
            for pixel in char_pattern[row]:
                grid[row].append(pixel == '#')
            if i < len(text) - 1:
                grid[row].append(False)

    return grid


def get_start_date(year: int = None) -> datetime:
    """Get the start date for the contribution graph (first Sunday)."""
    if year is None:
        year = datetime.now().year

    start = datetime(year - 1, datetime.now().month, datetime.now().day)
    start = start + timedelta(days=7)

    while start.weekday() != 6:
        start = start - timedelta(days=1)

    return start


def grid_to_dates(grid: List[List[bool]], start_date: datetime, offset_weeks: int = 0) -> List[datetime]:
    """Convert pixel grid to list of dates that need commits."""
    dates = []

    for col in range(len(grid[0])):
        for row in range(7):
            if grid[row][col]:
                date = start_date + timedelta(weeks=col + offset_weeks, days=row)
                if date <= datetime.now():
                    dates.append(date)

    return dates


def preview_grid(grid: List[List[bool]]) -> str:
    """Generate ASCII preview of the grid."""
    result = []
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    for row in range(7):
        line = f"{days[row]} "
        for col in range(len(grid[0])):
            line += '#' if grid[row][col] else '.'
        result.append(line)

    return '\n'.join(result)


def create_commits(dates: List[datetime], commits_per_day: int = 1, dry_run: bool = False):
    """Create git commits for each date."""
    data_file = "contributions.txt"

    if not os.path.exists(data_file):
        with open(data_file, 'w') as f:
            f.write("Git Graph Painter\n")
        subprocess.run(['git', 'add', data_file], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)

    total = len(dates) * commits_per_day
    count = 0

    for date in sorted(dates):
        for i in range(commits_per_day):
            count += 1
            date_str = date.strftime("%Y-%m-%dT12:00:00")

            with open(data_file, 'a') as f:
                f.write(f"Commit {count}: {date_str}\n")

            if dry_run:
                print(f"[DRY RUN] Would commit for {date_str}")
            else:
                env = os.environ.copy()
                env['GIT_AUTHOR_DATE'] = date_str
                env['GIT_COMMITTER_DATE'] = date_str

                subprocess.run(['git', 'add', data_file], check=True)
                subprocess.run(
                    ['git', 'commit', '-m', f'Contribution {count}'],
                    env=env,
                    check=True
                )
                print(f"[{count}/{total}] Committed for {date.strftime('%Y-%m-%d')}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Draw text on your GitHub contribution graph')
    parser.add_argument('text', nargs='?', default='HI', help='Text to display (default: HI)')
    parser.add_argument('--preview', '-p', action='store_true', help='Preview the pattern without creating commits')
    parser.add_argument('--offset', '-o', type=int, default=1, help='Week offset from start (default: 1)')
    parser.add_argument('--intensity', '-i', type=int, default=1, choices=[1, 2, 3, 4], help='Commits per day for intensity (1-4)')
    parser.add_argument('--year', '-y', type=int, help='Target year (default: current)')
    parser.add_argument('--dry-run', '-d', action='store_true', help='Show what would be done without doing it')

    args = parser.parse_args()

    grid = text_to_grid(args.text)

    print(f"\n=== Git Graph Painter ===")
    print(f"Text: {args.text.upper()}")
    print(f"Grid size: {len(grid[0])} weeks x 7 days")
    print(f"\nPreview:")
    print(preview_grid(grid))

    if len(grid[0]) + args.offset > 52:
        print(f"\n[WARNING] Text is too long! Max ~52 weeks available, you need {len(grid[0]) + args.offset}")

    if args.preview:
        return

    start_date = get_start_date(args.year)
    dates = grid_to_dates(grid, start_date, args.offset)

    print(f"\nStart date: {start_date.strftime('%Y-%m-%d')} (Sunday)")
    print(f"Commits needed: {len(dates) * args.intensity}")
    print(f"Date range: {min(dates).strftime('%Y-%m-%d')} to {max(dates).strftime('%Y-%m-%d')}")

    if not args.dry_run:
        confirm = input("\nProceed with commit creation? [y/N] ")
        if confirm.lower() != 'y':
            print("Aborted.")
            return

    create_commits(dates, args.intensity, args.dry_run)

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Done! Push to GitHub with: git push origin main")


if __name__ == '__main__':
    main()
