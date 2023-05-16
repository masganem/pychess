import re
from typing import Tuple
from src.Controller import Controller
from src.Position import Position
from src.util import cls


class PlayerInterface:
    def __init__(self) -> None:
        self._controller = Controller()

    def start(self) -> None:
        print(self._controller.get_display(), '\n')
        while True:
            move = input(f"{str(self._controller._turn.name).title()} plays: ")
            self.parse_move(move)
        

    def parse_move(self, move: str) -> bool:
        matches = re.findall(r"\w\d", move)
        if len(matches) != 2:
            print("Invalid move format.\n")
            return False
        
        position = self._parse_position(matches[0])
        target = self._parse_position(matches[1])

        try:
            self._controller.move(position, target)
            cls()
            print(self._controller.get_display(), '\n')
            return True
        except Exception as e:
            print(e, '\n')
            return False

    def _parse_position(self, coordinate: str) -> Position:
        x = ord(coordinate[0]) - 97
        y = (8 - int(coordinate[1])) % 8
        return (x, y)
