from src.Board import Board
from src.Tile import Tile
from src.pieces.Bishop import Bishop
from src.pieces.Color import Color
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.pieces.Pawn import Pawn
from src.pieces.Queen import Queen
from src.pieces.Rook import Rook


class Controller:
    def __init__(self) -> None:
        self._board = Board()
        self._spawn_pieces()
        pass

    def show_valid_moves(self, position) -> None:
        temp_board = self._board
        tile = temp_board.get(position)
        if tile.piece == None:
            print(f"No piece found for position {position}")
            return
        for i in range(8):
            for j in range(8):
                if tile.piece.is_valid_move(position, (i,j)):
                    temp_board.set((i,j), Tile('◎'))
        temp_board.show()

    def _spawn_pieces(self) -> None:
        # Pawns
        for i in range(8):
            self._board.set((i, 1), Pawn(Color.BLACK))
            self._board.set((i, 6), Pawn(Color.WHITE))

        # Rooks
        for i in [0, 7]:
            self._board.set((i, 0), Rook(Color.BLACK))
            self._board.set((i, 7), Rook(Color.WHITE))

        # Knights
        for i in [1, 6]:
            self._board.set((i, 0), Knight(Color.BLACK))
            self._board.set((i, 7), Knight(Color.WHITE))
        
        # Bishops
        for i in [2, 5]:
            self._board.set((i, 0), Bishop(Color.BLACK))
            self._board.set((i, 7), Bishop(Color.WHITE))

        # Queens
        self._board.set((3, 0), Queen(Color.BLACK))
        self._board.set((3, 7), Queen(Color.WHITE))

        # Queens
        self._board.set((4, 0), King(Color.BLACK))
        self._board.set((4, 7), King(Color.WHITE))