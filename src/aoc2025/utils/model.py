from typing import Callable, Generator

ORTHOGONALS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
DIAGONALS = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
SURROUNDING = ORTHOGONALS + DIAGONALS


class Matrix:
    def __init__(self, input_str: str):
        self.data: list[list[str]] = []
        for line in input_str.splitlines():
            self.data.append([''] * len(line))

        for y, line in enumerate(input_str.splitlines()):
            for x, c in enumerate(line):
                self.data[x][y] = c

        self.width = len(self.data[0])
        self.height = len(self.data)

    def get(self, x: int, y: int, default: str | None = None) -> str:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.data[x][y]
        return default

    def set(self, x: int, y: int, value: str):
        self.data[x][y] = value

    def surrounding(self, x: int, y: int, default: str | None = None) -> list[str]:
        return [self.get(x + xy[0], y + xy[1], default) for xy in SURROUNDING]

    def all(self, elem_filter: Callable[[str], bool] = lambda x: True) -> Generator[tuple[int, int, str]]:
        for y in range(0, self.height):
            for x in range(0, self.width):
                if elem_filter(self.data[x][y]):
                    yield x, y, self.data[x][y]

    def __str__(self):
        s = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                s += self.data[x][y]
            s += "\n"
        return s
