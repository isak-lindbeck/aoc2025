import pathlib
from unittest import TestCase

from aoc2025 import day02


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day02.run(pathlib.Path("examples/day02.txt").read_text().strip())
        self.assertEqual(1227775554, out_1)
        self.assertEqual(4174379265, out_2)
