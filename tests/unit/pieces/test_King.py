import unittest
from src.pieces.Color import Color
from src.pieces.King import King

class TestKing(unittest.TestCase):
    def setUp(self) -> None:
        self.king = King(Color.WHITE)

    def test_blocks_moves_to_non_adjacent_cells(self):
        # (column, line) -> (column, line)
        for position, target in [
            ((4, 4), (4, 4)), # does not move
            
            # moves too far (from middle to end of table)
            ((4, 4), (4, 0)), # top
            ((4, 4), (7, 0)), # top right
            ((4, 4), (7, 4)), # right
            ((4, 4), (7, 7)), # bottom right
            ((4, 4), (4, 7)), # bottom
            ((4, 4), (0, 7)), # bottom left
            ((4, 4), (0, 4)), # left
            ((4, 4), (0, 0)), # top left
        ]:
            with self.subTest(position=position, target=target):
                self.assertFalse(self.king.is_valid_move(position, target))

    def test_allows_moves_to_adjacent_cells(self):
        # (column, line) -> (column, line)
        for position, target in [
            ((4, 4), (4, 3)), # top
            ((4, 4), (5, 3)), # top right
            ((4, 4), (5, 4)), # right
            ((4, 4), (5, 5)), # bottom right
            ((4, 4), (4, 5)), # bottom
            ((4, 4), (3, 5)), # bottom left
            ((4, 4), (3, 4)), # left
            ((4, 4), (3, 3)), # top left
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(self.king.is_valid_move(position, target))

    def test_route_is_move_target(self):
        position, target = (3, 3), (4, 4)
        actual_route = self.king.get_route(position, target)
        expected_route = [target]

        self.assertEqual(actual_route, expected_route)