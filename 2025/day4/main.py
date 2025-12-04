import itertools
from pathlib import Path


def main(part: str):
    input_text = Path("input.txt").read_text()
    diagram = [list(l) for l in input_text.splitlines()]
    accessible_rolls = 0
    for y, row in enumerate(diagram):
        for x, cell in enumerate(row):
            if cell != "@":
                # Not a roll, no need to worry about it
                continue
            adjacent_cells = list(get_adjacent_cells(diagram, x, y))
            if len([cell for cell in adjacent_cells if cell == "@"]) < 4:
                accessible_rolls += 1
    print(accessible_rolls)
    # 1580 -> too high
    # 1393 -> OK


def get_adjacent_cells(diagram: list[list[str]], x: int, y: int):
    for (ox, oy) in itertools.product(range(-1, 2), repeat=2):
        if (ox, oy) == (0, 0):
            continue
        ax, ay = x + ox, y + oy
        if 0 <= ax < len(diagram[0]) and 0 <= ay < len(diagram):
            yield diagram[ay][ax]


if __name__ == '__main__':
    main("1")
