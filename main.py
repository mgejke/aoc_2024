import click
import importlib
from pathlib import Path
from timeit import default_timer as timer


@click.command
@click.argument("day", type=int)
@click.argument("example", type=bool, default=False)
def main(day: str, example: bool):
    day_solution = importlib.import_module(f"solutions.day{day}.solution")

    start = timer()
    r1, r2 = day_solution.main(Path(f"solutions/day{day}"), example)
    elapsed = timer() - start
    print(f"Elapsed: {elapsed:.6f}s")

    print(f"1: {r1}")
    print(f"2: {r2}")


if __name__ == "__main__":
    main()
