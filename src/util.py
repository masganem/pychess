import os
import re

from src.Position import Position

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def parse_move(move: str) -> bool:
        matches = re.findall(r"[a-h][1-8]", move)
        if len(matches) == 1:
            position = parse_position(matches[0])
            return position, None
        elif len(matches) != 2:
            raise Exception("Invalid move format.\n")
        
        position = parse_position(matches[0])
        target = parse_position(matches[1])

        return position, target

def parse_position(coordinate: str) -> Position:
    x = ord(coordinate[0]) - 97
    y = (8 - int(coordinate[1])) % 8
    return (x, y)