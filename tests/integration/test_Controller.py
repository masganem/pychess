# Integration tests for the interactions of Controller with other classes
import unittest
from src.pieces.Color import Color
from src.Controller import Controller


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_displays_board(self): # Interaction with the Board class
        controller_display = self.controller.get_display()
        board_display = self.controller.board.get_display()
        self.assertTrue(controller_display == board_display)

    def test_validates_board_bounds(self): # Interaction with the Board class
        with self.assertRaises(Exception):
            self.controller._pre_validate((8, 8), (8, 8), None, None)
    
    def test_switch_turn(self): # Interaction with the Color module
        self.controller._switch_turn()
        self.assertTrue(self.controller._turn == Color.BLACK)
