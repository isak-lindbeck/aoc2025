import pathlib
from unittest import TestCase

from aoc2025 import day03


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day03.run(pathlib.Path("example/day03.txt").read_text().strip())
        self.assertEqual(357, out_1)
        self.assertEqual(3121910778619, out_2)
