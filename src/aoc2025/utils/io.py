from pathlib import Path
from typing import Tuple, Any

from termcolor import colored


def red(s: str) -> str:
    return colored(s, 'red')


def green(s: str) -> str:
    return colored(s, 'green')


def blue(s: str) -> str:
    return colored(s, 'blue')


def check_value(answer: str, value: Any, part: int):
    if value is None or value == "0":
        return blue(f"part {part}: pass")
    if answer is None:
        return blue(f"part {part}: {value}")
    if str(value) != answer:
        return red(f"part {part}: {value} is wrong")
    else:
        return green(f"part {part}: {value} is correct")


def check_output(out: Tuple, path: Path):
    answers = path.read_text().strip().splitlines()
    print(out)
    print()
    print(check_value(answers[0], str(out[0]), 1))
    print(check_value(answers[1], str(out[1]), 2))
