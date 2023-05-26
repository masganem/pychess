import unittest
from src.pieces.Color import Color
from src.pieces.Pawn import Pawn
from src.Controller import Controller

class TestController(unittest.TestCase):
    def test_detects_checkmate(self):
        controller = Controller()

        controller.move((5, 6), (5, 5))
        controller.move((4, 1), (4, 2))
        controller.move((6, 6), (6, 4))
        controller.move((3, 0), (7, 4))

        self.assertTrue(controller.is_checkmate())
    
    def test_detects_promotion(self):
        controller = Controller()

        controller.board.set((0,0), Pawn(Color.WHITE))

        self.assertTrue(controller.is_promotion())

    def test_blocks_wrong_turn_movement(self):
        controller = Controller()

        with self.assertRaises(Exception):
            controller.move((1,1), (1, 3))