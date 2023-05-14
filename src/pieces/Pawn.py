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
        if (self.color == Color.BLACK):
            return (position[1] == 1 and dist_y == -2 and dist_x == 0) or (dist_y == -1 and (-1 <= dist_x <= 1))
        else:
            return (position[1] == 6 and dist_y == 2 and dist_x == 0) or (dist_y == 1 and (-1 <= dist_x <= 1))
