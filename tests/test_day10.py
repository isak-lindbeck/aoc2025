import pathlib
from unittest import TestCase

from aoc2025 import day10


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day10.run(pathlib.Path("examples/day10.txt").read_text())
        self.assertEqual(7, out_1)
        self.assertEqual(33, out_2)