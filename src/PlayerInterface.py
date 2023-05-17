from time import sleep
from typing import Tuple
from src.Controller import Controller
from src.Position import Position
from src.util import cls, parse_move


class PlayerInterface:
    def __init__(self) -> None:
        self._controller = Controller()
        self._is_checkmate = False

    def start(self) -> None:
        cls()
        print(self._controller.get_display(), '\n')
        while not self._is_checkmate:
            move = input(f"{str(self._controller._turn.name).title()} plays: ")
            position, target = parse_move(move)
            self._move(position, target)
            self._is_checkmate = self._controller.is_checkmate()
        self._checkmate()

    def _move(self, position, target) -> bool:
        try:
            self._controller.move(position, target)
            cls()
            print(self._controller.get_display(), '\n')
            return True
        except Exception as e:
            print(e, '\n')
            return False

    def _checkmate(self):
        cls()
        print(self._controller.get_display(), '\n')
        print("CHECKMATE!")
        sleep(5)
        exit()
