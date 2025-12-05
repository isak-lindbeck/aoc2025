from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed


class Range:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __lt__(self, other) -> bool:
        return self.start < other.start

    def __repr__(self) -> str:
        return f"({self.start} -> {self.end})"


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0

    split = input_str.split("\n\n")

    ranges: list[Range] = []
    for line in split[0].splitlines():
        line_split = line.split("-")
        ranges.append(Range(int(line_split[0]), int(line_split[1])))
    ranges.sort()

    for line in split[1].splitlines():
        for r in ranges:
            if r.start <= int(line) <= r.end:
                out_1 += 1
                break

    idx = 0
    while idx < len(ranges) - 1:
        cur = ranges[idx]
        nxt = ranges[idx + 1]
        if cur.end >= nxt.start:
            ranges.remove(nxt)
            cur.end = max(cur.end, nxt.end)
        else:
            idx += 1

    for r in ranges:
        out_2 += r.end - r.start + 1

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day05.txt").read_text())
        check_output(output, Path("answers/day05.txt").resolve())
