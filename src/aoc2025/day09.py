from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p_1: Point, p_2: Point):
        self.x_1, self.y_1, self.x_2, self.y_2 = p_1.x, p_1.y, p_2.x, p_2.y

        # Ensure the lower number is in the _1 var
        if self.x_2 < self.x_1:
            self.x_1, self.x_2 = self.x_2, self.x_1
        if self.y_2 < self.y_1:
            self.y_1, self.y_2 = self.y_2, self.y_1

    def area(self) -> int:
        # Edges adds 1 thickness
        dx = self.x_2 - self.x_1 + 1
        dy = self.y_2 - self.y_1 + 1
        return dx * dy

    def overlaps(self, b: Rectangle) -> bool:
        # No overlap if only edges are "touching" 
        return self.x_1 < b.x_2 and self.x_2 > b.x_1 and self.y_1 < b.y_2 and self.y_2 > b.y_1


def is_corner_subtractive(a: Point, b: Point, c: Point) -> bool:
    return ((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)) < 0


def run(input_str: str) -> Tuple[int, int]:
    out_1, out_2 = 0, 0

    points: list[Point] = []
    for line in input_str.splitlines():
        split = line.split(",")
        points.append(Point(int(split[0]), int(split[1])))

    negative_boxes: list[Rectangle] = []
    for i in range(len(points)):
        a = points[i]
        b = points[(i + 1) % len(points)]
        c = points[(i + 2) % len(points)]
        if is_corner_subtractive(a, b, c):
            negative_boxes.append(Rectangle(a, c))

    negative_boxes = sorted(negative_boxes, key=lambda box: box.area(), reverse=True)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
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
