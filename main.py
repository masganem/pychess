import sys
import codecs
from src.ReplayInterface import ReplayInterface
from src.PlayerInterface import PlayerInterface

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer, 'strict')
sys.stderr = codecs.getwriter('utf8')(sys.stderr.buffer, 'strict')

if len(sys.argv) == 2:
    ReplayInterface().replay(sys.argv[1])
else:
    PlayerInterface().start()