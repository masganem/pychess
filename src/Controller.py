from src.Board import Board
from src.Tile import Tile


class Controller:
    def __init__(self) -> None:
        self._board = Board()

    def show_valid_moves(self, position) -> None:
        temp_board = self._board
        tile = temp_board.get(position)
        if tile.piece == None:
            print(f"No piece found for position {position}")
            return
        for i in range(8):
            for j in range(8):
                if tile.piece.is_valid_move(position, (i,j)):
                    temp_board.set((i,j), Tile('◎'))
        temp_board.show()