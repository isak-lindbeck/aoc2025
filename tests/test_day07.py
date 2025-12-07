import pathlib
from unittest import TestCase

from aoc2025 import day07


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day07.run(pathlib.Path("examples/day07.txt").read_text())
        self.assertEqual(21, out_1)
        self.assertEqual(40, out_2)
