import pathlib
from unittest import TestCase

from aoc2025 import day10


class Test(TestCase):

    def test_run(self):
        out_1, out_2 = day10.run(pathlib.Path("examples/day10.txt").read_text())
        self.assertEqual(7, out_1)
        self.assertEqual(33, out_2)

"""
 1 3 0 3 1 2
 2 5 1 0 3 0
 

0 0 0 0 1 1 3
0 1 0 0 0 1 5
0 0 1 1 1 0 4
1 1 0 1 0 0 7
 
 x5 + x6 = 3
 x2 + x6 = 5
 x3 + x4 + x5 = 4
 x1 + x2 + x4 = 7
 
 
 x2 - x5 = 2
 
 mat = [
 [1, 1, 0, 1, 0, 0, 7],
 [0, 1, 0, 0, 0, 1, 5],
 [0, 0, 1, 1, 1, 0, 4],
 [0, 0, 0, 0, 1, 1, 3]
    ]
"""