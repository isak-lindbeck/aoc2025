import typing
from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.model import matrix_from_str, Matrix
from aoc2025.utils.timed import Timed


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0

    matrix = matrix_from_str(input_str)

    for y in range(1, matrix.height):
        for x in range(matrix.width):
            current = matrix.get(x,y)
            above = matrix.get(x, y - 1)
            if above == "|" or above == "S":
                if current == ".":
                    matrix.set(x, y, "|")
                if current == "^":
                    out_1 += 1
                    matrix.replace(x - 1, y, old_value=".", new_value="|")
                    matrix.replace(x + 1, y, old_value=".", new_value="|")

    matrix = typing.cast(Matrix[str | int], matrix)
    for x in range(matrix.width):
        matrix.replace(x, matrix.height - 1, "|", 1)

    for y in reversed(range(matrix.height - 1)):
        for x in range(matrix.width):
            current = matrix.get(x, y)
            below = matrix.get(x, y + 1)
            if current == "|":
                matrix.set(x, y, below)
            elif current == "^":
                value = left_below if isinstance(left_below := matrix.get(x - 1, y + 1), int) else 0
                value += right_below if isinstance(right_below := matrix.get(x + 1, y + 1), int) else 0
                matrix.set(x, y, value)
            elif current == "S":
                out_2 = below

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day07.txt").read_text().strip())
        check_output(output, Path("answers/day07.txt").resolve())
