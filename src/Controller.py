from copy import deepcopy
from src.pieces.King import King
from src.pieces.Color import Color
from src.pieces.Pawn import Pawn
from src.Board import Board
from src.Tile import Tile


class Controller:
    def __init__(self) -> None:
        self._board = Board()
        self._turn = Color.WHITE

    def move(self, position, target) -> bool:
        if not self._is_valid_move(position, target):
            return False
        else:
            origin_tile = self._board.get(position)
            target_tile = self._board.get(target)
            target_tile.set(origin_tile.piece)
            origin_tile.clear()
            self._switch_turn()
            return True
    
    def get_display(self) -> bool:
        return self._board.get_display()

    def _is_valid_move(self, position, target, check_check=True, board=None, turn=None) -> bool:
        if board == None:
            board = self._board

        if turn == None:
            turn = self._turn

        if not (board.in_bounds(position, target)):
            raise Exception('Move is out of bounds.')

        origin_tile = board.get(position)
        origin_piece = origin_tile.piece
        if origin_piece == None:
            raise Exception('No piece at origin position.')

        if not origin_piece.color == turn:
            raise Exception('Invalid turn.')

        if not origin_piece.is_valid_move(position, target):
            raise Exception('Invalid move for chosen piece.')
        
        route = origin_piece.get_route(position, target)
        for coordinate in route:
            tile = board.get(coordinate)
            # Special cases for Pawn: enabling cross-capturing; blocking forward capturing.
            if isinstance(origin_piece, Pawn):
                if abs(position[0] - target[0]) != 0:
                    if tile.piece != None:
                        if tile.piece.color == origin_piece.color:
                            raise Exception('Invalid move for chosen piece.')
                        else:
                            pass
                    else:
                        raise Exception('Invalid move for chosen piece.')
                else:
                    if tile.piece != None:
                        raise Exception('Invalid move for chosen piece.')
                    else:
                        pass

            elif tile.piece != None:
                if coordinate == route[-1] and tile.piece.color != origin_piece.color:
                    pass
                else:
                    raise Exception('Invalid move for chosen piece.')
        
        if check_check and self._is_in_check(position, target):
            raise Exception('You\'re in check!')

        return True
        
    def get_valid_moves_display(self, position) -> str:
        temp_board = deepcopy(self._board)
        tile = temp_board.get(position)
        if tile.piece == None:
            print(f"No piece found for position {position}")
            return
        for i in range(8):
            for j in range(8):
                if self._is_valid_move(position, (i,j)):
                    temp_board._board[j][i] = Tile('◎')
        return temp_board.get_display()
    
    def _is_in_check(self, position, target) -> bool:
        temp_board = deepcopy(self._board)

        # Simulate movement
        origin_tile = temp_board.get(position)
        origin_piece = origin_tile.piece
        temp_board.set(target, origin_piece)
        origin_tile.clear()

        # Find King
        king_position = ()
        for i in range(8):
            for j in range(8):
                target_piece = temp_board.get((i, j)).piece
                if isinstance(target_piece, King) and target_piece.color == origin_piece.color:
                    king_position = (i, j)
        
        # Check if King can be captured after move
        for i in range(8):
            for j in range(8):
                try:
                    mock_turn = self._get_opposite_turn(self._turn)
                    self._is_valid_move((i, j), king_position, False, temp_board, mock_turn)
                    return True
                except:
                    pass
        
        return False
    
    def _switch_turn(self) -> str:
        self._turn = self._get_opposite_turn(self._turn)
    
    def _get_opposite_turn(self, turn: Color) -> str:
        if turn == Color.BLACK:
            return Color.WHITE
        else:
            return Color.BLACK
