from pathlib import Path

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed


class Point:
    def __init__(self, xy: tuple[int, int]):
        self.x = xy[0]
        self.y = xy[1]


class Rectangle:
    def __init__(self, p_1: Point, p_2: Point):
        self.p_1 = p_1
        self.p_2 = p_2

        self.left = min(self.p_1.x, self.p_2.x)
        self.right = max(self.p_1.x, self.p_2.x)
        self.top = min(self.p_1.y, self.p_2.y)
        self.bottom = max(self.p_1.y, self.p_2.y)

    def area(self) -> int:
        # Edges adds 1 thickness
        width = self.right - self.left + 1
        height = self.bottom - self.top + 1
        return width * height

    def overlaps(self, r: Rectangle) -> bool:
        # No overlap if only edges are "touching" 
        return self.left < r.right and self.right > r.left and self.top < r.bottom and self.bottom > r.top


def is_corner_subtractive(a: Point, b: Point, c: Point) -> bool:
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) < 0


def run(input_str: str) -> tuple[int, int]:
    out_1, out_2 = 0, 0

    points: list[Point] = list(map(Point, map(eval, input_str.splitlines())))
    num_points = len(points)

    negative_boxes: list[Rectangle] = []
    for i in range(num_points):
        a = points[i]
        b = points[(i + 1) % num_points]
        c = points[(i + 2) % num_points]
        if is_corner_subtractive(a, b, c):
            negative_boxes.append(Rectangle(a, c))

    negative_boxes.sort(key=lambda box: box.area(), reverse=True)

    for i in range(num_points):
        for j in range(i + 1, num_points):
            box = Rectangle(points[i], points[j])

            out_1 = max(box.area(), out_1)

            if out_2 < box.area():
                for cb in negative_boxes:
                    if box.overlaps(cb):
                        break
                else:
                    out_2 = max(box.area(), out_2)

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day09.txt").read_text().strip())
        check_output(output, Path("answers/day09.txt").resolve())
