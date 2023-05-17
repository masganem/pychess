import os
import re

from src.Position import Position

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def parse_move(move: str) -> bool:
        matches = re.findall(r"\w\d", move)
        if len(matches) != 2:
            print("Invalid move format.\n")
            return False
        
        position = parse_position(matches[0])
        target = parse_position(matches[1])

        return position, target

def parse_position(coordinate: str) -> Position:
    x = ord(coordinate[0]) - 97
    y = (8 - int(coordinate[1])) % 8
    return (x, y)