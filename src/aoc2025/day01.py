from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0
    pos = 50
    for line in input_str.splitlines():
        direction = line[0]
        steps = int(line.removeprefix(direction))
        step = 1 if direction == 'L' else -1

        for _ in range(steps):
            pos = (pos + step) % 100
            if pos == 0:
                out_2 += 1
        if pos == 0:
            out_1 += 1

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day01.txt").read_text())
        check_output(output, Path("answers/day01.txt"))
