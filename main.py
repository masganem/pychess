from src.Board import Board
from src.Controller import Controller
from src.Tile import Tile
from src.pieces.Color import Color
from src.pieces.Bishop import Bishop

# bishop = Bishop(Color.BLACK)
# board = Board()
# board.set((1,1), bishop)
# for i in range(8):
#     for j in range(8):
#         if bishop.is_valid_move((1,1), (i,j)):
#             board.set((i,j), Tile('x'))
# board.show()

game = Controller()
# game.show_valid_moves((4,0))
# game._board.show()