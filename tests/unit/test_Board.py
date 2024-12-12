import unittest
from src.Board import Board
from src.pieces.Color import Color
from src.pieces.Knight import Knight

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_setup_paws(self):
        for i in range(8):
            self.assertEqual(self.board.get((i, 1)).get_token(), '♙')
            self.assertEqual(self.board.get((i, 6)).get_token(), '♟︎')

    def test_initial_board_setup_rook(self):
        self.assertEqual(self.board.get((0, 0)).get_token(), '♖')
        self.assertEqual(self.board.get((7, 0)).get_token(), '♖')
        self.assertEqual(self.board.get((0, 7)).get_token(), '♜')
        self.assertEqual(self.board.get((7, 7)).get_token(), '♜')

    def test_initial_board_setup_knight(self):
        self.assertEqual(self.board.get((1, 0)).get_token(), '♘')
        self.assertEqual(self.board.get((6, 0)).get_token(), '♘')
        self.assertEqual(self.board.get((1, 7)).get_token(), '♞')
        self.assertEqual(self.board.get((6, 7)).get_token(), '♞')

    def test_initial_board_setup_bishop(self):
        self.assertEqual(self.board.get((2, 0)).get_token(), '♗')
        self.assertEqual(self.board.get((5, 0)).get_token(), '♗')
        self.assertEqual(self.board.get((2, 7)).get_token(), '♝')
        self.assertEqual(self.board.get((5, 7)).get_token(), '♝')

    def test_initial_board_setup_queen(self):
        self.assertEqual(self.board.get((3, 0)).get_token(), '♕')
        self.assertEqual(self.board.get((3, 7)).get_token(), '♛')
    
    def test_initial_board_setup_king(self):
        self.assertEqual(self.board.get((4, 0)).get_token(), '♔')
        self.assertEqual(self.board.get((4, 7)).get_token(), '♚')

    def test_set_and_get_piece(self):
        knight = Knight(Color.BLACK)
        position = (2, 2)
        self.board.set(position, knight)
        tile = self.board.get(position)
        self.assertEqual(tile.get_token(), '♘')

    def test_get_display(self):
        display = self.board.get_display()
        self.assertIn('a b c d e f g h', display)
        self.assertIn('8', display)
        self.assertIn('1', display)
        self.assertIn('♔', display)
        self.assertIn('♚', display)

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

    def test_in_bound_positions(self):
        for position, target in [
            ((3, 4), (2, 2)),
            ((0, 0), (0, 0)),
            ((7, 7), (7, 7)),
            ((7, 7), (5, 4)),
            ((6, 0), (7, 7)),
        ]:
            with self.subTest(position=position, target=target):
                self.assertTrue(Board.in_bounds(position, target))
