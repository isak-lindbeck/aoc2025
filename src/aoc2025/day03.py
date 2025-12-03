from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0

    for line in input_str.splitlines():
        first = max(line[:len(line) - 1])
        idx = line.index(first)
        second = max(line[idx + 1:])
        i = int(f"{first}{second}")
        out_1 += i

        nums = ""
        for i in range(0, 12):
            remaining = 11 - i
            length = len(line)
            selection = line[:length - remaining]
            m = max(selection)
            line = line[line.index(m) + 1:]
            nums += m
        out_2 += int(nums)

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day03.txt").read_text())
        check_output(output, Path("answers/day03.txt").resolve())
