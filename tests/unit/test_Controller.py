import unittest
from copy import deepcopy
from src.Controller import Controller
from src.pieces.Color import Color
from src.pieces.Pawn import Pawn
from src.pieces.King import King
from src.pieces.Rook import Rook


class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()

    def test_initial_turn(self):
        black_pawn_position = (6, 0)
        with self.assertRaises(Exception):
            self.controller.move(black_pawn_position, (5, 0))

    def test_valid_pawn_move(self):
        white_pawn_position = (6, 6)
        target_position = (6, 5)
        result = self.controller.move(white_pawn_position, target_position)
        self.assertTrue(result)

    def test_out_of_bounds_move(self):
        white_pawn_position = (0, 1)
        invalid_position = (-1, 10)
        with self.assertRaises(Exception):
            self.controller.move(white_pawn_position, invalid_position)

    def test_no_piece_at_origin(self):
        empty_position = (4, 4)
        with self.assertRaises(Exception):
            self.controller.move(empty_position, (4, 5))

    def test_invalid_move_for_piece(self):
        white_rook_position = (0, 0)
        invalid_target = (1, 1)
        with self.assertRaises(Exception):
            self.controller.move(white_rook_position, invalid_target)

    def test_blocked_move(self):
        white_rook_position = (0, 0)
        blocked_target = (0, 3)
        with self.assertRaises(Exception):
            self.controller.move(white_rook_position, blocked_target)

    def test_check_scenario(self):
        temp_board = deepcopy(self.controller.board)
        for x in range(8):
            for y in range(8):
                temp_board.get((x, y)).clear()
        white_rook = Rook(Color.WHITE)
        black_king = King(Color.BLACK)
        temp_board.set((0,0), white_rook)
        temp_board.set((0,7), black_king)
        self.controller.board = temp_board
        self.controller._turn = Color.BLACK
        with self.assertRaises(Exception):
            self.controller.move((0,7), (0,6))

    def test_promotion_detection(self):
        temp_board = deepcopy(self.controller.board)
        for x in range(8):
            for y in range(8):
                temp_board.get((x,y)).clear()
        white_pawn = Pawn(Color.WHITE)
        temp_board.set((0,1), white_pawn)
        self.controller.board = temp_board
        self.controller.move((0,1), (0,0))
        promo_position = self.controller.is_promotion()
        self.assertEqual(promo_position, (0,0))

    def test_promotion_action(self):
        from src.pieces.Queen import Queen
        temp_board = deepcopy(self.controller.board)
        for x in range(8):
            for y in range(8):
                temp_board.get((x,y)).clear()
        white_pawn = Pawn(Color.WHITE)
        temp_board.set((0,1), white_pawn)
        self.controller.board = temp_board
        self.controller.move((0,1), (0,0))
        self.controller.promote((0,0), Queen)
        piece_at_promotion = self.controller.board.get((0,0)).piece
        self.assertTrue(isinstance(piece_at_promotion, Queen))

    def test_checkmate_detection(self):
        # f2-f3
        self.controller.move((5,6),(5,5))
        # e7-e5
        self.controller.move((4,1),(4,3))
        # g2-g4
        self.controller.move((6,6),(6,4))
        # Qd8-h4
        self.controller.move((3,0),(7,4))
        self.assertTrue(self.controller.is_checkmate())

