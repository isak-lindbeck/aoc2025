import operator
from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0

    lines = input_str.splitlines()

    out_1 += part_1(lines)
    out_2 += part_2(lines)

    return out_1, out_2


def part_1(lines: list[str]) -> int:
    out_1 = 0
    operators = lines[-1].split()
    numbers: list[list[int]] = []
    for line in lines[:len(lines) - 1]:
        row = [int(x) for x in line.split()]
        numbers.append(row)

    for i, char in enumerate(operators):
        if char == "*":
            value, op = 1, operator.mul
        else:
            value, op = 0, operator.add
        
        for num in numbers:
            value = op(value, num[i])
        out_1 += value
    return out_1


def part_2(num_lines: list[str]) -> int:
    out_1 = 0
    op_line = num_lines[-1]
    num_lines = num_lines[:len(num_lines) - 1]

    value, op = 0, operator.add
    for idx, op_char in enumerate(op_line):
        if op_char != " ":
            out_1 += value
            if op_char == "*":
                value, op = 1, operator.mul
            else:
                value, op = 0, operator.add
        
        num = ""
        for line in num_lines:
            if line[idx] != " ":
                num += line[idx]
        if num != "":
            value = op(value, int(num))
    out_1 += value

    return out_1


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day06.txt").read_text())
        check_output(output, Path("answers/day06.txt").resolve())
