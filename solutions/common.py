from pathlib import Path
from typing import Sequence
from functools import wraps
from timeit import default_timer as timer


def get_clean_data(path) -> str:
    with Path(path / "input.txt").open("r") as f:
        return f.read().strip()


def get_rows(data: str) -> Sequence[str]:
    return data.strip().splitlines()


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        start = timer()
        result = f(*args, **kw)
        elapsed = timer() - start
        print(f"{f.__name__}: {elapsed:.6f}s")
        return result

    return wrap
