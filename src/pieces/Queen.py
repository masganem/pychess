from src.pieces.Color import Color
from src.pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, color: Color):
        self.color = color
        if color == Color.BLACK:
            self.token = '♕'
        else:
            self.token = '♛'

    def is_valid_move(self, position, target):
        dist_x = abs(position[0] - target[0])
        dist_y = abs(position[1] - target[1])
        return (dist_x == 0 and dist_y != 0) or (dist_y == 0 and dist_x != 0) or (dist_x != 0 and dist_x == dist_y)
    
    def get_route(self, position, target):
        dist_x = abs(position[0] - target[0])
        dist_y = abs(position[1] - target[1])

        x_step = -1 if position[0] > target[0] else 1
        y_step = -1 if position[1] > target[1] else 1

        if dist_y == 0:
            return list(zip(range(position[0] + x_step, target[0] + x_step, x_step), [position[1]] * dist_x))
        elif dist_x == 0:
            return list(zip([position[0]] * dist_y, range(position[1] + y_step, target[1] + y_step, y_step)))
        else:
            return list(zip(range(position[0] + x_step, target[0] + x_step, x_step), range(position[1] + y_step, target[1] + y_step, y_step)))