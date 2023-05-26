import unittest
import subprocess

class TestPlay(unittest.TestCase):
    def setUp(self) -> None:
        cmd = ["python", "main.py"]
        self.process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def test_foolsmate(self):
        foolsmate = ["f2f3", "e7e6", "g2g4", "d8h4"]

        for move in foolsmate:
            self.process.stdin.write(move + "\n")
            self.process.stdin.flush()

        out, _ = self.process.communicate()

        self.assertTrue("Checkmate!" in out)
    
    def test_basic_capture(self):
        basic_capture = ["b2b4", "a7a5", "b4a5"]

        for move in basic_capture:
            self.process.stdin.write(move + "\n")
            self.process.stdin.flush()

        out, _ = self.process.communicate()

        # Represents the expected state of the board in this case
        self.assertTrue("5 ♟︎ ■ □ ■ □ ■ □ ■" in out)

    def test_blocks_invalid_move(self):
        invalid_move = "b2b5"

        self.process.stdin.write(invalid_move + "\n")
        self.process.stdin.flush()

        out, _ = self.process.communicate()

        self.assertTrue("The pawn does not move like that" in out)
    
    def test_enforces_check(self):
        king_exposure = ["e2e4", "g7g5", "d1h5", "f7f6"]

        for move in king_exposure:
            self.process.stdin.write(move + "\n")
            self.process.stdin.flush()

        out, _ = self.process.communicate()

        self.assertTrue("You're in check" in out)