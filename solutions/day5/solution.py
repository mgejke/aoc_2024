from pathlib import Path
from dataclasses import dataclass
from collections import defaultdict
from collections import deque

from solutions.common import get_clean_data, get_rows

test_data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def check_order(values: list[int], order: dict[int, set[int]]) -> bool:
    d = deque(values)
    while d:
        f = d.popleft()
        if not all(v in order[f] for v in d):
            return False
    return True


def solve1(data: str) -> int:
    rules, updates = data.split("\n\n")

    order: dict[int, set[int]] = defaultdict(set)
    for rule in rules.strip().splitlines():
        b, a = tuple(map(int, rule.split("|")))
        order[b].add(a)

    s = 0
    for update in updates.strip().splitlines():
        values = list(map(int, update.split(",")))

        if check_order(values, order):
            s += values[len(values) // 2]

    return s


def solve2(data: str) -> int:
    rules, updates = data.split("\n\n")

    order: dict[int, set[int]] = defaultdict(set)
    for rule in rules.strip().splitlines():
        b, a = tuple(map(int, rule.split("|")))
        order[b].add(a)

    s = 0
    for update in updates.strip().splitlines():
        values = list(map(int, update.split(",")))

        i = len(values) - 2
        while not check_order(values, order):
            if not check_order(values[i:], order):
                values[i], values[i + 1] = values[i + 1], values[i]

            i -= 1
            if i < 0:
                i = len(values) - 2

        s += values[len(values) // 2]

    return s


def main(path: Path, example=False) -> tuple[int, int]:
    r1 = solve1(test_data if example else get_clean_data(path))
    r2 = solve2(test_data if example else get_clean_data(path))

    return r1, r2
