import unittest
from unittest.mock import patch, MagicMock, mock_open
from io import StringIO
from copy import deepcopy

from src.PlayerInterface import PlayerInterface
from src.pieces.Queen import Queen

class TestPlayerInterface(unittest.TestCase):
    def setUp(self):
        self.interface = PlayerInterface()
        self.interface._controller.get_display = MagicMock(return_value="Mocked Board Display")

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_valid_moves(self, mock_stdout):
        self.interface._controller.get_valid_moves = MagicMock(return_value=[((0,1),(0,2)), ((0,1),(0,3))])
        temp_board = deepcopy(self.interface._controller.board)
        # Mock board for display
        temp_board.get_display = MagicMock(return_value="Mocked Display with Markers")
        with patch.object(self.interface._controller, 'board', temp_board):
            self.interface._display_valid_moves((0,1))
        
        output = mock_stdout.getvalue()
        self.assertIn("Mocked Display with Markers", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_move_successful(self, mock_stdout):
        # Mock a successful move
        self.interface._controller.move = MagicMock(return_value=True)
        self.interface._move((0,1),(0,2))
        output = mock_stdout.getvalue()
        self.assertIn("Mocked Board Display", output)
        self.interface._controller.move.assert_called_once_with((0,1),(0,2))

    @patch('sys.stdout', new_callable=StringIO)
    def test_move_failure(self, mock_stdout):
        # Mock a failed move due to exception
        self.interface._controller.move = MagicMock(side_effect=Exception("Invalid move"))
        self.interface._move((0,1),(0,2))
        output = mock_stdout.getvalue()
        self.assertIn("Invalid move", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['queen'])
    def test_promote(self, mock_input, mock_stdout):
        # Mock a promotion scenario
        self.interface._controller.promote = MagicMock()
        self.interface._promote((0,0))
        output = mock_stdout.getvalue()
        self.assertIn("Promotion time!", output)
        self.interface._controller.promote.assert_called_once_with((0,0), Queen)

    @patch('builtins.input', side_effect=['y', 'testgame'])
    @patch('builtins.open', new_callable=mock_open)
    def test_log_moves_yes(self, mock_file, mock_input):
        self.interface._move_log = ["e2e4", "e7e5"]
        self.interface._log_moves()
        mock_file.assert_called_once_with('games/testgame.pcg', 'w')
        handle = mock_file()
        handle.write.assert_called_once_with("e2e4, e7e5")

    @patch('builtins.input', return_value='n')
    @patch('builtins.open', new_callable=mock_open)
    def test_log_moves_no(self, mock_file, mock_input):
        self.interface._move_log = ["e2e4", "e7e5"]
        self.interface._log_moves()
        mock_file.assert_not_called()

    @patch('builtins.input', side_effect=['a2a4', 'a2']) # mock invalid input
    @patch('sys.stdout', new_callable=StringIO)
    def test_start_simplified(self, mock_stdout, mock_input):
        # Mock controller for game steps
        self.interface._controller.is_checkmate = MagicMock(return_value=False)
        self.interface._controller.is_promotion = MagicMock(return_value=None)
        self.interface._controller.move = MagicMock(side_effect=Exception("No piece at origin"))
        self.interface._controller.get_valid_moves = MagicMock(return_value=[((0,1),(0,2))])
        
        def side_effect_checkmate():
            # should be checkmate on second call
            if not hasattr(side_effect_checkmate, 'called'):
                side_effect_checkmate.called = True
                return False
            return True

        # spy on is_checkmate's side effects
        self.interface._controller.is_checkmate.side_effect = side_effect_checkmate

        try:
            self.interface.start()
        except StopIteration:
            pass
        
        output = mock_stdout.getvalue()
        self.assertIn("No piece at origin", output)
        self.assertIn("◎", output)