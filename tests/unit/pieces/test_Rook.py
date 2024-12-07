import unittest
from src.pieces.Color import Color
from src.pieces.Rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self) -> None:
        self.rook = Rook(Color.WHITE)

    def test_blocks_static_move_and_knight_like_moves(self):
        # (column, line) -> (column, line)
        for position, target in [
            ((4, 4), (4, 4)), # does not move

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
                self.assertFalse(self.rook.is_valid_move(position, target))

    def test_blocks_some_bishop_like_moves(self):
        # (column, line) -> (column, line)
        for position, target in [
            # short moves
            ((4, 4), (5, 3)), # top right
            ((4, 4), (5, 5)), # bottom right
            ((4, 4), (3, 5)), # bottom left
            ((4, 4), (3, 3)), # top left

            # longest moves
            ((0, 7), (7, 0)), # top right
            ((0, 0), (7, 7)), # bottom right
            ((7, 0), (0, 7)), # bottom left
            ((7, 7), (0, 0)), # top left
        ]:
            with self.subTest(position=position, target=target):
                self.assertFalse(self.rook.is_valid_move(position, target))

    def test_allows_some_horizontal_and_vertical_moves(self):
        # (column, line) -> (column, line)
        for position, target in [
            # short moves
            ((4, 4), (4, 3)), # top
            ((4, 4), (5, 4)), # right
            ((4, 4), (4, 5)), # bottom
            ((4, 4), (3, 4)), # left

            # longest moves
            ((0, 7), (0, 0)), # top
            ((0, 0), (7, 0)), # right
            ((0, 0), (0, 7)), # bottom
            ((7, 0), (0, 0)), # left
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(self.rook.is_valid_move(position, target))

    def test_route_for_some_correct_moves_is_a_horizontal_or_vertical_line(self):
        # (column, line) -> (column, line)
        for position, target, expected_route in [
            # entire first board line
            # <- left
            ((7, 0), (0, 0), [(6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)]),
            # -> right
            ((0, 0), (7, 0), [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]),

            # entire first board column
            # ^ top
            ((0, 7), (0, 0), [(0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)]),
            # v bottom
            ((0, 0), (0, 7), [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]),
        ]:
            with self.subTest(position=position, target=target, expected_route=expected_route):
                actual_route = self.rook.get_route(position, target)
                self.assertEqual(actual_route, expected_route)