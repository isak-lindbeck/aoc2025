import pathlib
from unittest import TestCase

from aoc2025 import day08


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day08.run(pathlib.Path("examples/day08.txt").read_text(), 10)
        self.assertEqual(40, out_1)
        self.assertEqual(25272, out_2)
