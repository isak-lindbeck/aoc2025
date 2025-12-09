import pathlib
from unittest import TestCase

from aoc2025 import day09


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day09.run(pathlib.Path("examples/day09.txt").read_text())
        self.assertEqual(50, out_1)
        self.assertEqual(24, out_2)
