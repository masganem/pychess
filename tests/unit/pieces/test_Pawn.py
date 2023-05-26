import unittest
from src.pieces.Color import Color
from src.pieces.Pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_blocks_invalid_moves(self):
        pawn = Pawn(Color.BLACK)

        for position, target in [
            ((3, 1), (3, 4)),
            ((3, 1), (2, 1)),
            ((3, 1), (3, 1)),
            ((3, 1), (3, 0)),
            ((3, 1), (4, 4)),
        ]:
            with self.subTest(position=position, target=target):
                self.assertFalse(pawn.is_valid_move(position, target))

    def test_allows_cross_capturing(self):
        pawn = Pawn(Color.BLACK)

        for position, target in [
            ((3, 1), (4, 2)),
            ((3, 1), (2, 2)),
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(pawn.is_valid_move(position, target))
    
    def test_allows_double_forward(self):
        pawn = Pawn(Color.BLACK)

        for position, target in [
            ((3, 1), (3, 3)),
            ((1, 1), (1, 3)),
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(pawn.is_valid_move(position, target))

    def test_blocks_backwards_moves(self):
        pawn = Pawn(Color.WHITE)

        for position, target in [
            ((3, 1), (3, 2)),
            ((3, 1), (3, 3)),
            ((4, 3), (4, 4)),
        ]:
            with self.subTest(position=position, target=target):
                self.assertFalse(pawn.is_valid_move(position, target))

    def test_is_blocked_by_obstacle(self):
        pawn = Pawn(Color.WHITE)
        target = Pawn(Color.BLACK)

        with self.assertRaises(Exception):
            pawn.validate_special_move((2,4),(2,3), target)