import unittest
from src.util import parse_move

class TestUtil(unittest.TestCase):
    def test_parse_valid_move(self):
        move_text = "a2a4"
        expected_move = ((0, 6), (0, 4))

        self.assertEqual(expected_move, parse_move(move_text))
    
    def test_parse_partial_move(self):
        move_text = "a2"
        expected_move = ((0, 6), None)

        self.assertEqual(expected_move, parse_move(move_text))

    def test_parse_invalid_move(self):
        move_text = "x9x0"
        with self.assertRaises(Exception):
            parse_move(move_text)
