from typing import Callable, Generator, TypeVar, Generic

ORTHOGONALS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
DIAGONALS = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
SURROUNDING = ORTHOGONALS + DIAGONALS

T = TypeVar('T')


class Matrix(Generic[T]):

    def __init__(self, data: list[list[T]]):
        self.height = len(data[0])
        self.width = len(data)
        self.data = data

    def get(self, x: int, y: int, default: T | None = None) -> T:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.data[x][y]
        return default

    def set(self, x: int, y: int, value: T):
        self.data[x][y] = value

    def replace(self, x: int, y: int, old_value: T, new_value: T):
        if self.data[x][y] == old_value:
            self.data[x][y] = new_value

    def surrounding(self, x: int, y: int, default: T | None = None) -> list[T]:
        return [self.get(x + xy[0], y + xy[1], default) for xy in SURROUNDING]

    def all(self, elem_filter: Callable[[T], bool] = lambda x: True) -> Generator[tuple[int, int, T]]:
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


def matrix_from_str(input_str: str) -> Matrix[str]:
    lines = input_str.splitlines()
    height = len(lines)
    width = len(lines[0])

    data: list[list[str]] = []

    for x in range(width):
        data.append([''] * height)

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            data[x][y] = c

    return Matrix(data)
