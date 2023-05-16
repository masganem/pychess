from abc import ABC, abstractmethod
from src.pieces.Route import Route

from src.pieces.Color import Color

class Piece(ABC):
    @abstractmethod
    def __init__(self, color: Color) -> None:
        pass

    @abstractmethod
    def is_valid_move(self, position, target) -> bool:
        pass

    @abstractmethod
    def get_route(self, position, target) -> Route:
        pass