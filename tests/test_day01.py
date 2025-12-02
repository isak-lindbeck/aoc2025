import pathlib
from unittest import TestCase

from aoc2025 import day01


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day01.run(pathlib.Path("example/day01.txt").read_text().strip())
        self.assertEqual(3, out_1)
        self.assertEqual(6, out_2)
