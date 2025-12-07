from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.model import Matrix
from aoc2025.utils.timed import Timed


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0

    matrix = Matrix(input_str)

    for y in range(1, matrix.height):
        for x in range(matrix.width):
            current = matrix.get(x, y)
            above = matrix.get(x, y - 1, default=".")
            if above == "|" or above == "S":
                if current == ".":
                    matrix.set(x, y, "|")
                if current == "^":
                    out_1 += 1
                    left = matrix.get(x - 1, y, "")
                    right = matrix.get(x + 1, y, "")
                    if left == ".":
                        matrix.set(x - 1, y, "|")
                    if right == ".":
                        matrix.set(x + 1, y, "|")

    for x in range(matrix.width):
        if matrix.get(x, matrix.height - 1) == "|":
            matrix.set(x, matrix.height - 1, "1")

    for y in range(matrix.height - 2, -1, -1):
        for x in range(matrix.width):
            current = matrix.get(x, y)
            below = matrix.get(x, y + 1, "")
            if current == "|" and below.isnumeric():
                matrix.set(x, y, below)
            if current == "^":
                value = 0
                left_below = matrix.get(x - 1, y + 1, "")
                right_below = matrix.get(x + 1, y + 1, "")
                if left_below.isnumeric():
                    value += int(left_below)
                if right_below.isnumeric():
                    value += int(right_below)
                matrix.set(x, y, str(value))
            if current == "S":
                out_2 = int(below)

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day07.txt").read_text().strip())
        check_output(output, Path("answers/day07.txt").resolve())
