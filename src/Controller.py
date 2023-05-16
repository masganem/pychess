from copy import deepcopy
from src.pieces.Pawn import Pawn
from src.Board import Board
from src.Tile import Tile


class Controller:
    def __init__(self) -> None:
        self._board = Board()

    def is_valid_move(self, position, target) -> bool:
        piece = self._board.get(position).piece
        if not piece.is_valid_move(position, target):
            return False
        
        route = piece.get_route(position, target)
        for coordinate in route:
            tile = self._board.get(coordinate)
            if isinstance(piece, Pawn):
                if abs(position[0] - target[0]) != 0:
                    if tile.piece != None:
                        if tile.piece.color != piece.color:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    if tile.piece != None:
                        return False
                    else:
                        return True

            if tile.piece != None:
                if coordinate == route[-1] and tile.piece.color != piece.color:
                    return True
                else:
                    return False

        return True
        
    def show_valid_moves(self, position) -> None:
        temp_board = deepcopy(self._board)
        tile = temp_board.get(position)
        if tile.piece == None:
            print(f"No piece found for position {position}")
            return
        for i in range(8):
            for j in range(8):
                if self.is_valid_move(position, (i,j)):
                    temp_board._board[j][i] = Tile('◎')
        temp_board.show()