from src.Position import Position
from src.pieces.Color import Color
from src.pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, color: Color):
        self.color = color
        if color == Color.BLACK:
            self.token = '♙'
        else:
            self.token = '♟︎'

    def is_valid_move(self, position, target):
        dist_x = position[0] - target[0]
        dist_y = position[1] - target[1]
        
        is_starting_position = self.color == Color.BLACK and position[1] == 1 or self.color == Color.WHITE and position[1] == 6
        direction = -1 if self.color == Color.BLACK else 1
        double_move = direction * 2

        is_common_valid_move = dist_y == direction and (-1 <= dist_x <= 1)
        
        return (is_starting_position and dist_y == double_move) or is_common_valid_move
    
    def get_route(self, position, target):
        dist_x = abs(position[0] - target[0])
        if dist_x == 1:
            return [target]
        else:
            route = []
            step = -1 if position[1] > target[1] else 1
            # Range bounds are incremented to exclude starting position and include ending position
            for i in range(position[1] + step, target[1] + step, step):
                route.append((position[0], i))
            return route
        
    def validate_special_move(self, position: Position, target: Position, target_piece: Piece):
        if abs(position[0] - target[0]) != 0:
            if target_piece != None:
                if target_piece.color == self.color:
                    raise Exception('You can\'t capture your own piece.')
                else:
                    pass
            else:
                raise Exception('Pawns only do that when capturing.')
        else:
            if target_piece != None:
                raise Exception('Can\'t get past that.')
            else:
                pass