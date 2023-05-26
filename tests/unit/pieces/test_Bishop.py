import unittest
from src.pieces.Color import Color
from src.pieces.Bishop import Bishop

class TestBishop(unittest.TestCase):
    def setUp(self) -> None:
        self.bishop = Bishop(Color.WHITE)

    def test_allows_diagonal_moves(self):
        for position, target in [
            ((1, 7), (3, 5)),
            ((3, 5), (5, 7)),
            ((3, 5), (5, 3)),
            ((5, 7), (1, 3)),
            ((1, 3), (5, 7)),
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(self.bishop.is_valid_move(position, target))

    def test_builds_diagonal_route(self):
        position, target = (1, 3), (5, 7)
        actual_route = self.bishop.get_route(position, target)
        expected_route = [(2, 4), (3, 5), (4, 6), (5, 7)]

        self.assertEqual(actual_route, expected_route)
        