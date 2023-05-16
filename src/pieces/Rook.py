from src.pieces.Color import Color
from src.pieces.Piece import Piece

class Rook(Piece):
    def __init__(self, color: Color):
        self.color = color
        if color == Color.BLACK:
            self.token = '♖'
        else:
            self.token = '♜'

    def is_valid_move(self, position, target):
        dist_x = abs(position[0] - target[0])
        dist_y = abs(position[1] - target[1])
        return (dist_x == 0 and dist_y != 0) or (dist_y == 0 and dist_x != 0)
    
    def get_route(self, position, target):
        dist_x = abs(position[0] - target[0])
        dist_y = abs(position[1] - target[1])
        if dist_x:
            step = -1 if position[0] > target[0] else 1
            return list(zip(range(position[0] + step, target[0] + step, step), [position[1]] * dist_x))
        else:
            step = -1 if position[1] > target[1] else 1
            return list(zip([position[0]] * dist_y, range(position[1] + step, target[1] + step, step)))