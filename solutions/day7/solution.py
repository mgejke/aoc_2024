from pathlib import Path
from enum import Enum, auto
from itertools import product

from solutions.common import get_clean_data, get_rows

test_data = """
292: 11 6 16 20
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
"""


class Operators(Enum):
    Add = auto()
    Mul = auto()
    Concatenate = auto()


def test_combo(values, result, operators):
    for combo in product(
        operators,
        repeat=len(values) - 1,
    ):
        acc = values[0]
        for v, o in zip(values[1:], combo):
            match o:
                case Operators.Add:
                    acc += v
                case Operators.Mul:
                    acc *= v
                case Operators.Concatenate:
                    acc = int(f"{acc}{v}")

        if acc == result:
            return acc

    return 0


def solve1(data: str) -> int:
    s = 0
    for row in get_rows(data):
        r_str, v_str = row.split(":")
        values = list(map(int, v_str.split()))
        result = int(r_str)
        s += test_combo(values, result, [Operators.Add, Operators.Mul])
    return s


def solve2(data: str) -> int:
    s = 0
    for row in get_rows(data):
        r_str, v_str = row.split(":")
        values = list(map(int, v_str.split()))
        result = int(r_str)
        s += test_combo(
            values, result, [Operators.Add, Operators.Mul, Operators.Concatenate]
        )
    return s


def main(path: Path, example=False) -> tuple[int, int]:
    r1 = solve1(test_data if example else get_clean_data(path))
    r2 = solve2(test_data if example else get_clean_data(path))

    return r1, r2
