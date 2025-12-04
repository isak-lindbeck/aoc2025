import pathlib
from unittest import TestCase

from aoc2025 import day04


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day04.run(pathlib.Path("example/day04.txt").read_text().strip())
        self.assertEqual(13, out_1)
        self.assertEqual(43, out_2)
