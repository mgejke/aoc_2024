from pathlib import Path
from dataclasses import dataclass
from collections import deque

from solutions.common import get_clean_data, timing

test_data = """2333133121414131402"""


@dataclass
class Block:
    index: int
    count: int
    id_: int = -1


@timing
def solve1(data: str) -> int:
    empty: deque[int] = deque()
    blocks: deque[int] = deque()

    _id = 0
    for i, c in enumerate(data):
        if i % 2 != 0:
            length = len(blocks) + len(empty)
            empty.extend(range(length, length + int(c)))
        else:
            blocks.extend([_id] * int(c))
            _id += 1

    while empty:
        blocks.insert(empty.popleft(), blocks.pop())

    return sum((v * i for (i, v) in enumerate(blocks)))


@timing
def solve2(data: str) -> int:
    empty: list[Block] = []
    blocks: list[Block] = []

    _id = 0
    position = 0
    for i, c_s in enumerate(data):
        c = int(c_s)
        if i % 2 != 0:
            empty.append(Block(position, c))
        else:
            blocks.append(Block(position, c, _id))
            _id += 1
        position += c

    defraged = []
    while blocks:
        b = blocks.pop()
        moved = False
        for i, e in enumerate(empty):
            if b.index < e.index:
                break

            if b.count <= e.count:
                b.index = e.index
                defraged.append(b)
                moved = True

                new_size = e.count - b.count
                if new_size > 0:
                    e.index = e.index + b.count
                    e.count = new_size
                else:
                    del empty[i]

                break
        if not moved:
            defraged.append(b)

    return sum((b.id_ * i) for b in defraged for i in range(b.index, b.index + b.count))


def main(path: Path, example=False) -> tuple[int, int]:
    r1 = solve1(test_data if example else get_clean_data(path))
    r2 = solve2(test_data if example else get_clean_data(path))

    return r1, r2
