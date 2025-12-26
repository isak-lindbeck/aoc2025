import sys
from pathlib import Path

import z3
from z3 import Int

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed

sys.setrecursionlimit(1500)

translation = str.maketrans("(){}.# ", "[][]01,", "[]")

INF = sys.maxsize
cache: dict[tuple[int, int], int] = {}

def solve_1(desired_state: int, state_changes: list[int], current_state: int, change: int,
            seen: list[int]) -> int | None:
    key = (current_state, change)
    if r := cache.get(key):
        return r
    next_state = current_state ^ change
    if next_state == desired_state:
        return 0
    if next_state in seen:
        cache[key] = INF
        return cache[key]
    seen = seen + [next_state]

    result = INF
    for state_change in state_changes:
        if state_change == change:
            continue
        result = min(solve_1(desired_state, state_changes, next_state, state_change, seen), result)
    cache[key] = result + 1
    return cache[key]


def run(input_str: str) -> tuple[int, int]:
    out_1, out_2 = 0, 0
    for line in input_str.splitlines():
        split = line.split(" ")
        section_1 = split[0]
        section_2 = " ".join(split[1:-1])
        section_3 = split[-1]

        desired_state: int = int(section_1.translate(translation)[::-1], 2)
        buttons: tuple[list[int], ...] = eval(section_2.translate(translation))
        required_sums: list[int] = eval(section_3.translate(translation))

        state_changes: list[int] = []
        for button in buttons:
            bit_field = 0
            for value in button:
                bit_field |= (2 ** value)
            state_changes.append(bit_field)

        global cache
        cache = {}
        out_1 += solve_1(desired_state, state_changes, 0, 0, [])

        optimizer = z3.Optimize()
        x_i = []
        for i in range(len(buttons)):
            new_x = Int(f"x{i}")
            x_i.append(new_x)
            optimizer.add(new_x >= 0)

        optimizer.minimize(sum(x_i))

        for idx, required_sum in enumerate(required_sums):
            xs_for_sum = [x_i[i] for i, button in enumerate(buttons) if idx in button]
            expression = sum(xs_for_sum) == required_sum
            # print(expression)
            optimizer.add(expression)
        # print()

        optimizer.check()
        model = optimizer.model()
        res = sum([model[x].as_long() for x in model])
        out_2 += res

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day10.txt").read_text().strip())
        check_output(output, Path("answers/day10.txt").resolve())
