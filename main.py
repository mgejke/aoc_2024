import click
import importlib
from pathlib import Path


@click.command
@click.argument("day", type=int)
@click.argument("example", type=bool, default=False)
def main(day: str, example: bool):
    day_solution = importlib.import_module(f"solutions.day{day}.solution")

    r1, r2 = day_solution.main(Path(f"solutions/day{day}"), example)

    print(r1)
    print(r2)


if __name__ == "__main__":
    main()
