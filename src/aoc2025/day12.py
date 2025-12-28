from pathlib import Path

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed

def run(input_str: str) -> tuple[int, int]:
    out_1, out_2 = 0, 0

    split = input_str.split("\n\n")

    piece_areas = []
    for s in split[:-1]:
        area = s.count("#")
        piece_areas.append(area)

    for s in split[-1].splitlines():
        split_2 = s.split(": ")
        height, width = eval(split_2[0].replace("x", ", "))
        idx_count : tuple[int, ...] = eval(split_2[1].replace(" ", ", "))
        
        region_area = height * width
        total_required_area = sum([piece_areas[idx] * count for idx, count in enumerate(idx_count)])
        if total_required_area <= region_area:
            out_1 += 1

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day12.txt").read_text().strip())
        check_output(output, Path("answers/day12.txt").resolve())
