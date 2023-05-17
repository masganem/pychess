import sys
from time import sleep
from src.Controller import Controller
from src.util import cls, parse_move


class ReplayInterface:
    def __init__(self) -> None:
        self._controller = Controller()
    
    def replay(self, filename: str) -> None:
        move_log = self._parse_move_log(filename)
        cls()
        print(self._controller.get_display(), '\n')
        for move in move_log:
            sys.stdout.write(f"{str(self._controller._turn.name).title()} plays: ")
            sys.stdout.flush()
            sleep(1)
            for i in move:
                sleep(0.1)
                sys.stdout.write(i)
                sys.stdout.flush()
            print('\n')
            position, target = parse_move(move)
            self._controller.move(position, target)
            sleep(1)
            cls()
            print(self._controller.get_display(), '\n')
            sleep(1)
        print('Replay over.')
            
    def _parse_move_log(self, filename: str) -> None:
        with open(f'games/{filename}.pcg', 'r') as file:
            text_log = file.read()
            return text_log.split(', ')