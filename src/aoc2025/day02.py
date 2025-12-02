import re
from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0
    for r in input_str.split(","):
        split = r.strip().split("-")
        start = int(split[0])
        stop = int(split[1]) + 1
        for i in range(start, stop):
            string = str(i)
            if re.match(r"^(.+)(\1)$", string):
                out_1 += i
            if re.match(r"^(.+)(\1)+$", string):
                out_2 += i
    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day02.txt").read_text())
        check_output(output, Path("answers/day02.txt").resolve())