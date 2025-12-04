from typing import Callable, Generator


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

    def neighbour_values(self, x: int, y: int, default: str) -> list[str]:
        n = self.get(x=x, y=y - 1, default=default)
        ne = self.get(x=x + 1, y=y - 1, default=default)
        e = self.get(x=x + 1, y=y, default=default)
        se = self.get(x=x + 1, y=y + 1, default=default)
        s = self.get(x=x, y=y + 1, default=default)
        sw = self.get(x=x - 1, y=y + 1, default=default)
        w = self.get(x=x - 1, y=y, default=default)
        nw = self.get(x=x - 1, y=y - 1, default=default)
        return [n, ne, e, se, s, sw, w, nw]

    def for_each(self, callable: Callable[[str], bool]) -> Generator[tuple[int, int, str]]:
        for y in range(0, self.height):
            for x in range(0, self.width):
                if callable(self.data[x][y]):
                    yield x, y, self.data[x][y]

    def __str__(self):
        s = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                s += self.data[x][y]
            s += "\n"
        return s
