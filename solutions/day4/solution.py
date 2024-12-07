from pathlib import Path
from typing import Sequence

from solutions.common import get_clean_data, get_rows

test_data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

DIRS = [(1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, -1)]


def find(
    word: str, x: int, y: int, d: tuple[int, int], w: int, h: int, rows: Sequence[str]
) -> int:
    for c in word:
        if not (0 <= x < w):
            return 0
        if not (0 <= y < h):
            return 0

        if rows[y][x] != c:
            return 0

        x += d[0]
        y += d[1]

    return 1


def find_xmas(x: int, y: int, w: int, h: int, rows: Sequence[str]):
    if not rows[y][x] == "A":
        return 0

    f = ""
    for d in [(1, 1), (-1, -1)]:
        x1 = x + d[0]
        y1 = y + d[1]

        if not (0 <= x1 < w):
            return 0
        if not (0 <= y1 < h):
            return 0

        f += rows[y1][x1]

    if f != "MS" and f != "SM":
        return 0

    f = ""
    for d in [(-1, 1), (1, -1)]:
        x1 = x + d[0]
        y1 = y + d[1]

        if not (0 <= x1 < w):
            return 0
        if not (0 <= y1 < h):
            return 0

        f += rows[y1][x1]

    if f != "MS" and f != "SM":
        return 0

    return 1


def solve1(data: str) -> int:
    rows = get_rows(data)
    h = len(rows)
    w = len(rows[0])

    s = 0
    for y in range(h):
        for x in range(w):
            for d in DIRS:
                s += find("XMAS", x, y, d, w, h, rows)

    return s


def solve2(data: str) -> int:
    rows = get_rows(data)
    h = len(rows)
    w = len(rows[0])

    s = 0
    for y in range(h):
        for x in range(w):
            s += find_xmas(y, x, w, h, rows)
    return s


def main(path: Path, example=False) -> tuple[int, int]:
    r1 = solve1(test_data if example else get_clean_data(path))
    r2 = solve2(test_data if example else get_clean_data(path))

    return r1, r2
