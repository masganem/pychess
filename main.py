from src.pieces.Queen import Queen
from src.pieces.Color import Color
from src.pieces.Pawn import Pawn
from src.Controller import Controller

game = Controller()
game._board.get((2,5)).set(Queen(Color.WHITE))
game.show_valid_moves((2,5))
# print(game.is_valid_move((0,0),(0,1)))
# game._board.show()