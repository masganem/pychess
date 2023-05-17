from copy import deepcopy
from typing import Optional, Type
from src.pieces.Piece import Piece
from src.Position import Position
from src.pieces.King import King
from src.pieces.Color import Color, get_opposite_color
from src.pieces.Pawn import Pawn
from src.Board import Board
from src.Tile import Tile


class Controller:
    def __init__(self) -> None:
        self.board = Board()
        self._turn = Color.WHITE

    def move(self, position, target) -> bool:
        if not self._is_valid_move(position, target):
            return False
        else:
            origin_tile = self.board.get(position)
            origin_piece = origin_tile.piece

            target_tile = self.board.get(target)
            target_tile.set(origin_piece)

            origin_tile.clear()

            self._switch_turn()
            return True
        
    def promote(self, position, DesiredPiece: Type[Piece]) -> None:
        promoted_piece = self.board.get(position).piece
        if promoted_piece == None:
            raise Exception('There is no piece to be promoted in that position.')
        color = promoted_piece.color
        self.board.set(position, DesiredPiece(color))
    
    def get_display(self) -> bool:
        return self.board.get_display()

    def _is_valid_move(self, position, target, check_check=True, board=None, turn=None) -> bool:
        if board == None:
            board = self.board

        if turn == None:
            turn = self._turn

        if not (board.in_bounds(position, target)):
            raise Exception('Move is out of bounds.')

        origin_tile = board.get(position)
        origin_piece = origin_tile.piece
        if origin_piece == None:
            raise Exception('No piece at origin position.')

        if not origin_piece.color == turn:
            attempted_color = str(origin_piece.color.name).lower()
            raise Exception(f'It\'s not {attempted_color}\'s turn yet.')

        if not origin_piece.is_valid_move(position, target):
            piece_name = origin_piece.__class__.__name__.lower()
            raise Exception(f'The {piece_name} does not move like that.')
        
        route = origin_piece.get_route(position, target)
        for coordinate in route:
            tile = board.get(coordinate)
            # Special cases for Pawn: enabling cross-capturing; blocking forward capturing.
            if isinstance(origin_piece, Pawn):
                if abs(position[0] - target[0]) != 0:
                    if tile.piece != None:
                        if tile.piece.color == origin_piece.color:
                            raise Exception('You can\'t capture your own piece.')
                        else:
                            pass
                    else:
                        raise Exception('Pawns only do that when capturing.')
                else:
                    if tile.piece != None:
                        raise Exception('Can\'t get past that.')
                    else:
                        pass

            if isinstance(origin_piece, King):
                for x in range(-1,2):
                    for y in range(-1,2):
                        shifted_target = (target[0] + x, target[1] + y)
                        inspected_piece = self.board.get(shifted_target).piece
                        if isinstance(inspected_piece, King) and inspected_piece.color != origin_piece.color:
                            raise Exception('Kings are afraid of each other!')
            
            if tile.piece != None and not isinstance(origin_piece, Pawn):
                if coordinate == route[-1] and tile.piece.color != origin_piece.color:
                    pass
                else:
                    raise Exception('There\'s something in your way.')
        
        if check_check and self._blocked_by_check(position, target):
            raise Exception('You\'re in check!')

        return True
        
    def get_valid_moves(self, position) -> str:
        moves = []
        for x in range(8):
            for y in range(8):
                try:
                    self._is_valid_move(position, (x,y))
                    moves.append((position, (x, y)))
                except:
                    pass
        return moves
    
    # Checks if a move is blocked by check
    def _blocked_by_check(self, position, target) -> bool:
        temp_board = deepcopy(self.board)

        # Simulate movement
        origin_tile = temp_board.get(position)
        origin_piece = origin_tile.piece
        temp_board.set(target, origin_piece)
        origin_tile.clear()

        # Find King
        king_position = ()
        for x in range(8):
            for y in range(8):
                target_piece = temp_board.get((x, y)).piece
                if isinstance(target_piece, King) and target_piece.color == origin_piece.color:
                    king_position = (x, y)
        
        # Check if King can be captured after move
        for x in range(8):
            for y in range(8):
                try:
                    mock_turn = get_opposite_color(self._turn)
                    self._is_valid_move((x, y), king_position, False, temp_board, mock_turn)
                    return True
                except:
                    pass
        
        return False

    def is_checkmate(self) -> bool:
        # If every move is invalid, then checkmate!
        for x in range(8):
            for y in range(8):
                tile = self.board.get((x,y))
                if tile.piece == None:
                    pass
                elif tile.piece.color != self._turn:
                    pass
                
                valid_moves = self.get_valid_moves((x,y))
                if len(valid_moves) > 0:
                    return False

        return True
    
    def is_promotion(self) -> Optional[Position]:
        for x in range(8):
            for y in [0, 7]:
                tile = self.board.get((x,y))
                if tile.piece == None:
                    pass
                elif isinstance(tile.piece, Pawn):
                    if tile.piece.color == Color.BLACK and y == 7:
                        return (x, y)
                    elif tile.piece.color == Color.WHITE and y == 0:
                        return (x, y)
                    else:
                        pass

    def _switch_turn(self) -> str:
        self._turn = get_opposite_color(self._turn)
