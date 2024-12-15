import unittest
from unittest.mock import patch, mock_open, MagicMock
from io import StringIO

from src.ReplayInterface import ReplayInterface

class TestReplayInterface(unittest.TestCase):
    def setUp(self):
        self.interface = ReplayInterface()
        self.interface._controller.get_display = MagicMock(return_value="Mocked Display")

    # mock IO functions to not mess up test log
    @patch('builtins.open', new_callable=mock_open, read_data="e2e4, e7e5") # mock game record file
    @patch('sys.stdout', new_callable=StringIO)
    @patch('time.sleep', return_value=None)
    @patch('src.util.cls', return_value=None)
    def test_replay(self, mock_cls, mock_sleep, mock_stdout, mock_file):
        self.interface._controller.move = MagicMock()
        self.interface.replay("testgame")

        output = mock_stdout.getvalue()
        self.assertIn("Mocked Display", output)
        self.assertIn("White plays: e2e4", output)
        self.assertIn("Replay over.", output)

        # Check that the moves were executed
        self.assertEqual(self.interface._controller.move.call_count, 2)
        self.interface._controller.move.assert_any_call((4,6),(4,4))
        self.interface._controller.move.assert_any_call((4,1),(4,3))