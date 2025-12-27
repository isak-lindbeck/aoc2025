import pathlib
from unittest import TestCase

from aoc2025 import day11


class Test(TestCase):

    def test_run_1(self):
        out_1 = day11.run_1(pathlib.Path("examples/day11_1.txt").read_text())
        self.assertEqual(5, out_1)

    def test_run_2(self):
        out_2 = day11.run_2(pathlib.Path("examples/day11_2.txt").read_text())
        self.assertEqual(2, out_2)
