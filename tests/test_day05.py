import pathlib
from unittest import TestCase

from aoc2025 import day05


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day05.run(pathlib.Path("examples/day05.txt").read_text().strip())
        self.assertEqual(3, out_1)
        self.assertEqual(14, out_2)
