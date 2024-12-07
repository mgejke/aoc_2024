from pathlib import Path
import re

from solutions.common import get_clean_data


test_data = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

test_data2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


def solve1(data: str) -> int:
    s = 0
    for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data):
        s += int(a) * int(b)
    return s


def solve2(data: str) -> int:
    s = 0
    mul = True
    for n in re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))", data):
        match n:
            case ("do()", _, _):
                mul = True
            case ("don't()", _, _):
                mul = False
            case (_, a, b) if mul:
                s += int(a) * int(b)
    return s


def main(path: Path, example=False) -> tuple[int, int]:
    r1 = solve1(test_data if example else get_clean_data(path))
    r2 = solve2(test_data2 if example else get_clean_data(path))

    return r1, r2
