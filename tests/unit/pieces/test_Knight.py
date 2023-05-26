import unittest
from src.pieces.Color import Color
from src.pieces.Knight import Knight

class TestKnight(unittest.TestCase):
    def setUp(self) -> None:
        self.knight = Knight(Color.WHITE)

    def test_allows_L_shape_moves(self):
        for position, target in [
            ((1, 7), (2, 5)),
            ((2, 5), (1, 7)),
            ((1, 7), (0, 5)),
            ((2, 5), (3, 3)),
            ((3, 3), (5, 4)),
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(self.knight.is_valid_move(position, target))

    def test_skips_obstacles(self):
        position, target = (1, 7), (2, 5)
        actual_route = self.knight.get_route(position, target)
        expected_route = [target]

        self.assertEqual(actual_route, expected_route)
        