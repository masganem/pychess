import unittest
from src.pieces.Color import Color
from src.pieces.Queen import Queen
from src.pieces.King import King
from src.pieces.Bishop import Bishop
from src.pieces.Rook import Rook

class TestQueen(unittest.TestCase):
    def setUp(self) -> None:
        self.queen = Queen(Color.WHITE)

    def test_blocks_static_move_and_knight_like_moves(self):
        # (column, line) -> (column, line)
        for position, target in [
            ((4, 4), (4, 4)), # does not move

            # moves like a knight
            ((4, 4), (5, 6)), # knight lower bottom right
            ((4, 4), (3, 6)), # knight lower bottom left
            ((4, 4), (5, 2)), # knight higher top right
            ((4, 4), (3, 2)), # knight higher top left
            ((4, 4), (6, 5)), # knight higher bottom right
            ((4, 4), (2, 5)), # knight higher bottom left
            ((4, 4), (6, 3)), # knight lower top right
            ((4, 4), (2, 3)), # knight lower top left
        ]:
            with self.subTest(position=position, target=target):
                self.assertFalse(self.queen.is_valid_move(position, target))

    def test_allows_king_like_moves(self):
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
                self.assertTrue(self.queen.is_valid_move(position, target))

    def test_allows_some_bishop_like_moves(self):
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
                self.assertTrue(self.queen.is_valid_move(position, target))

    def test_allows_some_rook_like_moves(self):
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
                self.assertTrue(self.queen.is_valid_move(position, target))

    def test_route_for_king_like_move_is_king_route(self):
        
        king = King(Color.WHITE)
        position, target = (3, 3), (4, 4)
        king_route = king.get_route(position, target)
        self.assertEqual(self.queen.get_route(position, target), king_route)

    def test_route_for_some_bishop_like_moves_is_bishop_route(self):
        
        bishop = Bishop(Color.WHITE)
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
                bishop_route = bishop.get_route(position, target)
                self.assertTrue(self.queen.get_route(position, target), bishop_route)

    def test_route_for_some_rook_like_moves_is_rook_route(self):

        rook = Rook(Color.WHITE)
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
                rook_route = rook.get_route(position, target)
                self.assertTrue(self.queen.get_route(position, target), rook_route)