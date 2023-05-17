import sys
from src.ReplayInterface import ReplayInterface
from src.PlayerInterface import PlayerInterface

if len(sys.argv) == 2:
    ReplayInterface().replay(sys.argv[1])
else:
    PlayerInterface().start()