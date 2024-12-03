from pathlib import Path
from collections import Counter

from solutions.common import get_clean_data, get_rows

test_data = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def solve1(data: str) -> int:
    pairs = [tuple(map(int, line.split())) for line in get_rows(data)]
    t1, t2 = zip(*pairs)

    return sum(abs(a - b) for a, b in zip(sorted(t1), sorted(t2)))


def solve2(data: str) -> int:
    pairs = [tuple(map(int, line.split())) for line in get_rows(data)]
    t1, t2 = zip(*pairs)
    c = Counter(t2)
    return sum((v * c[v] for v in t1))


def main(path: Path, example=False) -> tuple[int, int]:
    data = test_data if example else get_clean_data(path)
    r1 = solve1(data)
    r2 = solve2(data)

    return r1, r2
