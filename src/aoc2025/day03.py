from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0

    for line in input_str.splitlines():
        out_1 += calculate(line, 2)
        out_2 += calculate(line, 12)

    return out_1, out_2


def calculate(line: str, num_digits: int) -> int:
    result = ""
    for i in range(0, num_digits):
        remaining = num_digits - 1 - i
        m = max(line[:len(line) - remaining])
        line = line[line.index(m) + 1:]
        result += m
    return int(result)


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day03.txt").read_text())
        check_output(output, Path("answers/day03.txt").resolve())
