import sys
from pathlib import Path

import z3

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed

sys.setrecursionlimit(1500)

translation = str.maketrans("(){}.# ", "[][]01,", "[]")

INF = sys.maxsize


def run(input_str: str) -> tuple[int, int]:
    out_1, out_2 = 0, 0
    for line in input_str.splitlines():
        split = line.split(" ")
        section_1 = split[0]
        section_2 = " ".join(split[1:-1])
        section_3 = split[-1]

        current_state: int = int(section_1.translate(translation)[::-1], 2)
        buttons: tuple[list[int], ...] = eval(section_2.translate(translation))
        required_sums: list[int] = eval(section_3.translate(translation))

        state_changes: list[int] = []
        for button in buttons:
            bit_field = 0
            for value in button:
                bit_field |= (2 ** value)
            state_changes.append(bit_field)

        out_1 += solve_1(state_changes, current_state, [], {})

        optimizer = z3.Optimize()
        x_i = []
        for i in range(len(buttons)):
            x_i.append(z3.Int(f"x{i}"))
            optimizer.add(x_i[-1] >= 0)

        for idx, required_sum in enumerate(required_sums):
            xs_for_idx = [x_i[i] for i, button in enumerate(buttons) if idx in button]
            expression = sum(xs_for_idx) == required_sum
            # print(expression)
            optimizer.add(expression)
        # print()

        optimizer.minimize(sum(x_i))
        optimizer.check()
        model = optimizer.model()
        out_2 += sum([model[x].as_long() for x in model])

    return out_1, out_2


def solve_1(state_changes: list[int], current_state: int, seen: list[int], cache: dict[int, int]) -> int:
    if current_state == 0:
        return 0
    if result := cache.get(current_state):
        return result
    if current_state in seen:
        cache[current_state] = INF
        return INF
    seen = seen + [current_state]

    result = INF
    for state_change in state_changes:
        result = min(solve_1(state_changes, current_state ^ state_change, seen, cache), result)
    cache[current_state] = result + 1
    return cache[current_state]


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day10.txt").read_text().strip())
        check_output(output, Path("answers/day10.txt").resolve())
