import pathlib
from unittest import TestCase

from aoc2025 import day06


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day06.run(pathlib.Path("examples/day06.txt").read_text())
        self.assertEqual(4277556, out_1)
        self.assertEqual(3263827, out_2)
