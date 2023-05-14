from src.pieces.Color import Color
from src.pieces.Piece import Piece

class Knight(Piece):
    def __init__(self, color: Color):
        self.color = color
        if color == Color.BLACK:
            self.token = '♘'
        else:
            self.token = '♞'

    def is_valid_move(self, position, target):
        dist_x = abs(position[0] - target[0])
        dist_y = abs(position[1] - target[1])
        return (dist_x == 1 and dist_y == 2) or (dist_x == 2 and dist_y == 1)