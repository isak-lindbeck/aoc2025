from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.model import Matrix
from aoc2025.utils.timed import Timed


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0

    matrix = Matrix(input_str)
    for x, y, value in matrix.for_each(lambda v: v == "@"):
        if matrix.neighbour_values(x, y).count("@") < 4:
            out_1 += 1

    while True:
        prev_count = out_2
        for x, y, value in matrix.for_each(lambda v: v == "@"):
            if matrix.neighbour_values(x, y).count("@") < 4:
                matrix.set(x, y, "x")
                out_2 += 1
        if prev_count == out_2:
            break

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day04.txt").read_text())
        check_output(output, Path("answers/day04.txt").resolve())
