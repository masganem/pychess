from enum import Enum

class Color(Enum):
    WHITE = 0
    BLACK = 1

def get_opposite_color(color: Color) -> str:
    if color == Color.BLACK:
        return Color.WHITE
    else:
        return Color.BLACK