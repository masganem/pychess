import unittest
import subprocess

class TestReplay(unittest.TestCase):
    def test_replay_foolsmate(self):
        cmd = ["python", "main.py", "foolsmate"]
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        out, _ = process.communicate()

        self.assertTrue("Replay over" in out)