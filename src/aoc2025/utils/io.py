from pathlib import Path

from typing import Tuple

HERE = Path(__file__).parent


def check_output(out: Tuple, path: Path):
    answers = path.read_text().strip().splitlines()
    print(out)
    if str(out[0]) != answers[0]:
        print(f"{out[0]} is not correct for part 1")
    else:
        print(f"{out[0]} is correct for part 1")

    if out[1] is None:
        print("pass")
    else:
        if str(out[1]) != answers[1]:
            print(f"{out[1]} is not correct for part 2")
        else:
            print(f"{out[1]} is correct for part 2")
