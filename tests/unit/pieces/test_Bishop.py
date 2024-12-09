import unittest
from src.pieces.Color import Color
from src.pieces.Bishop import Bishop

class TestBishop(unittest.TestCase):
    def setUp(self) -> None:
        self.bishop = Bishop(Color.WHITE)

    def test_block_non_diagonal_moves_1_tile(self):
        # (column, line) -> (column, line)
        # diagonal displacement vector (target - position) 
        # = (x, x), x == y and x != 0
        # thus, non-diagonal displacement vector (target - position) 
        # = (x, y), x != y or x == 0
        for position, target in [
            # x == 0 and x == y
            ((4, 4), (4, 4)), # does not move

            # x == 0 and x != y
            ((4, 4), (4, 3)), # top
            ((4, 4), (4, 5)), # down

            # x != 0 and x != y
            ((4, 4), (3, 4)), # left
            ((4, 4), (5, 4)), # right
        ]:
            with self.subTest(position=position, target=target):
                self.assertFalse(self.bishop.is_valid_move(position, target))

    def test_allows_diagonal_moves_1_tile(self):
        # (column, line) -> (column, line)
        for position, target in [
            ((4, 4), (5, 3)), # top right
            ((4, 4), (5, 5)), # bottom right
            ((4, 4), (3, 5)), # bottom left
            ((4, 4), (3, 3)), # top left
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(self.bishop.is_valid_move(position, target))

    def test_allows_diagonal_moves_max_tiles(self):
        # (column, line) -> (column, line)
        for position, target in [
            ((0, 7), (7, 0)), # top right
            ((0, 0), (7, 7)), # bottom right
            ((7, 0), (0, 7)), # bottom left
            ((7, 7), (0, 0)), # top left
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(self.bishop.is_valid_move(position, target))

    def test_route_for_some_correct_moves_is_diagonal(self):
        # (column, line) -> (column, line)
        for position, target, expected_route in [
            # board primary diagonal
            # to top-left
            ((7, 7), (0, 0), [(6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)]),
            # to bottom-right
            ((0, 0), (7, 7), [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]),

            # board secondary diagonal
            # to top-right
            ((0, 7), (7, 0), [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]),
            # to bottom-left
            ((7, 0), (0, 7), [(6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)]),
        ]:
            with self.subTest(position=position, target=target, expected_route=expected_route):
                actual_route = self.bishop.get_route(position, target)
                self.assertEqual(actual_route, expected_route)