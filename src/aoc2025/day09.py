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
        # Edges are 1 thick
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

    node_list: list[Point] = []
    for line in input_str.splitlines():
        split = line.split(",")
        current = Point(int(split[0]), int(split[1]))
        node_list.append(current)

    negative_boxes: list[Rectangle] = []
    for i in range(len(node_list)):
        a = node_list[i]
        b = node_list[(i + 1) % len(node_list)]
        c = node_list[(i + 2) % len(node_list)]
        if is_corner_subtractive(a, b, c):
            negative_boxes.append(Rectangle(a, c))

    for i in range(len(node_list)):
        for j in range(i + 1, len(node_list)):
            current = node_list[i]
            other = node_list[j]
            box = Rectangle(current, other)

            area = box.area()
            out_1 = max(box.area(), out_1)

            if out_2 < area:
                for cb in negative_boxes:
                    if box.overlaps(cb):
                        break
                else:
                    out_2 = max(area, out_2)

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day09.txt").read_text().strip())
        check_output(output, Path("answers/day09.txt").resolve())
