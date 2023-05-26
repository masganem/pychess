import unittest

from src.Board import Board

class TestBoard(unittest.TestCase):
    def test_blocks_out_of_bound_positions(self):
        for position, target in [
            ((-1, 0), (2, 2)),  # invalid position
            ((0, 0), (8, 2)),  # invalid target
            ((8, 8), (6, 7)),  # invalid position
            ((6, 6), (-1, 4)), # invalid target
            ((-1, -1), (1, 0)), # both position and target are invalid
            ((0, 0), (9, 9)),  # both position and target are invalid
        ]:
            with self.subTest(position=position, target=target):
                self.assertFalse(Board.in_bounds(position, target))