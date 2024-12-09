import unittest
from src.pieces.Color import Color
from src.pieces.Knight import Knight

class TestKnight(unittest.TestCase):
    def setUp(self) -> None:
        self.knight = Knight(Color.WHITE)

    def test_blocks_some_non_L_shape_moves(self):
        # (column, line) -> (column, line)
        # L displacement vector (target - position) 
        # = (x, y) = 
        # (+-1, +=2) or (+-2, +-1)
        # thus, non-diagonal displacement vector (target - position) 
        # = (x, y), 
        # (|x| != 1 or |y| != 2) and (|x| != 2 or |y| != 1)
        for position, target in [
            ((4, 4), (4, 4)), # does not move
            ((4, 4), (5, 5)), # diagonal move (x, y), x = y
            ((4, 4), (6, 6)), # (x, y) |x| != 1 (x = 2) and |y| != 1 (y = 2)
            ((4, 4), (5, 5)), # (x, y) |x| != 2 (x = 1) and |y| != 2 (y = 1)
        ]:
            with self.subTest(position=position, target=target):
                self.assertFalse(self.knight.is_valid_move(position, target))

    def test_allows_L_shape_moves(self):
        # (column, line) -> (column, line)
        for position, target in [
            ((4, 4), (5, 6)), # lower bottom right
            ((4, 4), (3, 6)), # lower bottom left
            ((4, 4), (5, 2)), # higher top right
            ((4, 4), (3, 2)), # higher top left
            ((4, 4), (6, 5)), # higher bottom right
            ((4, 4), (2, 5)), # higher bottom left
            ((4, 4), (6, 3)), # lower top right
            ((4, 4), (2, 3)), # lower top left
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(self.knight.is_valid_move(position, target))

    def test_route_is_move_target(self):
        position, target = (1, 7), (2, 5)
        actual_route = self.knight.get_route(position, target)
        expected_route = [target]

        self.assertEqual(actual_route, expected_route)
