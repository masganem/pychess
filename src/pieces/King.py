from src.pieces.Color import Color
from src.pieces.Piece import Piece

class King(Piece):
    def __init__(self, color: Color):
        self.color = color
        if color == Color.BLACK:
            self.token = '♔'
        else:
            self.token = '♚'

    def is_valid_move(self, position, target):
        dist_x = abs(position[0] - target[0])
        dist_y = abs(position[1] - target[1])
        return (dist_x != 0 or dist_y != 0) and (dist_x <= 1 and dist_y <= 1)
    
    def get_route(self, position, target):
        return [target]
    
    def validate_special_move(self, inspected_piece: Piece):
        if isinstance(inspected_piece, King) and inspected_piece.color != self.color:
                raise Exception('Kings are afraid of each other!')
                