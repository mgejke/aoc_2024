from pathlib import Path
from collections import defaultdict

from solutions.common import get_clean_data, get_rows

test_data = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def parse_map(rows, h, w):
    map_ = set()
    for y in range(h):
        for x in range(w):
            if rows[y][x] == "#":
                map_.add((x, y))
            if rows[y][x] == "^":
                start = (x, y)
    return map_, start


def find_path(
    map_: set[tuple[int, int]], start: tuple[int, int], w: int, h: int
) -> tuple[dict[tuple[int, int], set[int]], bool]:
    facing = 0
    visited = defaultdict(set)
    visited[start].add(facing)
    current = start
    while True:
        next_position = current[0] + DIRS[facing][0], current[1] + DIRS[facing][1]

        if not 0 <= next_position[0] < w:
            break

        if not 0 <= next_position[1] < h:
            break

        if next_position in map_:
            facing = (facing + 1) % 4
            continue

        current = next_position
        if facing in visited[current]:
            return (visited, True)

        visited[current].add(facing)

    return (visited, False)


def solve1(data: str) -> int:
    rows = get_rows(data)
    h = len(rows)
    w = len(rows[0])

    map_, start = parse_map(rows, h, w)
    (visited, _) = find_path(map_, start, w, h)

    s = len(visited)
    return s


def solve2(data: str) -> int:
    rows = get_rows(data)
    h = len(rows)
    w = len(rows[0])

    map_, start = parse_map(rows, h, w)
    (path, _) = find_path(map_, start, w, h)

    loops = 0
    for y in range(h):
        for x in range(w):
            added = (x, y)
            if added not in path:
                continue

            if added in map_:
                continue

            new_map = map_.copy()
            new_map.add(added)

            (_, loop) = find_path(new_map, start, w, h)
            loops += loop

    return loops


def main(path: Path, example=False) -> tuple[int, int]:
    r1 = solve1(test_data if example else get_clean_data(path))
    r2 = solve2(test_data if example else get_clean_data(path))

    return r1, r2
