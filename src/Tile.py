from src.pieces.Piece import Piece


class Tile:
    def __init__(self, token: str) -> None:
        self.token: str = token
        self.piece: Piece = None
    
    def set(self, piece: Piece) -> None:
        self.piece = piece

    def get_token(self):
        if self.piece != None:
            return self.piece.token
        else:
            return self.token
    
    def clear(self):
        self.piece = None
    