from pathlib import Path
import copy

from solutions.common import get_clean_data, get_rows


test_data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def safe_list(lst: list[int]) -> bool:
    d = [a - b for a, b in zip(lst, lst[1:])]

    inc = all((x > 0 for x in d))
    dec = all((x < 0 for x in d))
    dist = all((abs(x) < 4 for x in d))

    if (inc or dec) and dist:
        return True

    return False


def solve1(data: str) -> int:
    lines = get_rows(data)
    return sum(safe_list(list(map(int, line.split()))) for line in lines)


def solve2(data: str) -> int:
    lines = get_rows(data)

    s = 0
    for line in lines:
        int_line = list(map(int, line.split()))

        if safe_list(int_line):
            s += 1
            continue

        for k in range(len(int_line)):
            lst = copy.copy(int_line)
            del lst[k]
            if safe_list(lst):
                s += 1
                break

    return s


def main(path: Path, example=False) -> tuple[int, int]:
    data = test_data if example else get_clean_data(path)
    r1 = solve1(data)
    r2 = solve2(data)

    return r1, r2
