from pathlib import Path
from collections import defaultdict
import itertools

from solutions.common import get_clean_data, get_rows, timing

test_data = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def check_bounds(x: int, y: int, w: int, h: int) -> bool:
    return 0 <= x < w and 0 <= y < h


@timing
def solve1(data: str) -> int:
    rows = get_rows(data)
    h = len(rows)
    w = len(rows[0])

    map_ = defaultdict(list)
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c != ".":
                map_[c].append((x, y))

    antinodes = set()
    for _, v in map_.items():
        for c1, c2 in itertools.combinations(v, 2):
            f1 = c1[0] - c2[0], c1[1] - c2[1]
            f2 = c2[0] - c1[0], c2[1] - c1[1]

            c3 = c1[0] + f1[0], c1[1] + f1[1]
            c4 = c2[0] + f2[0], c2[1] + f2[1]

            if check_bounds(c3[0], c3[1], w, h):
                antinodes.add(c3)

            if check_bounds(c4[0], c4[1], w, h):
                antinodes.add(c4)

    return len(antinodes)


@timing
def solve2(data: str) -> int:
    rows = get_rows(data)
    h = len(rows)
    w = len(rows[0])

    map_ = defaultdict(list)
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c != ".":
                map_[c].append((x, y))

    antinodes = set()
    for _, v in map_.items():
        for c1, c2 in itertools.combinations(v, 2):
            antinodes.add(c1)
            antinodes.add(c2)
            f1 = c1[0] - c2[0], c1[1] - c2[1]
            f2 = c2[0] - c1[0], c2[1] - c1[1]

            inside = True
            while inside:
                inside = False

                c3 = c1[0] + f1[0], c1[1] + f1[1]
                c4 = c2[0] + f2[0], c2[1] + f2[1]

                if check_bounds(c3[0], c3[1], w, h):
                    antinodes.add(c3)
                    inside = True

                if check_bounds(c4[0], c4[1], w, h):
                    antinodes.add(c4)
                    inside = True

                c1, c2 = c3, c4

    return len(antinodes)


def main(path: Path, example=False) -> tuple[int, int]:
    r1 = solve1(test_data if example else get_clean_data(path))
    r2 = solve2(test_data if example else get_clean_data(path))

    return r1, r2
