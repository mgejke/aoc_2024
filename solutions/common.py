from pathlib import Path
from typing import Sequence


def get_clean_data(path) -> str:
    with Path(path / "input.txt").open("r") as f:
        return f.read()


def get_rows(data: str) -> Sequence[str]:
    return data.strip().splitlines()


# def get_rows_data_int() -> Sequence[int]:
#     return get_clean_data().strip().splitlines()
