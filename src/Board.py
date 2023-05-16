from src.pieces.Piece import Piece
from src.pieces.Color import Color
from src.pieces.Pawn import Pawn
from src.pieces.Bishop import Bishop
from src.pieces.Color import Color
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.pieces.Queen import Queen
from src.pieces.Rook import Rook
from src.Tile import Tile


class Board:
    def __init__(self):
        self._board = self._build()
        self._spawn_pieces()

    def _build(self):
        board = [[None]*8 for i in range(8)]
        for i in range(8):
            for j in range(8):
                if (i+j)%2:
                    board[i][j] = Tile('□')
                else:
                    board[i][j] = Tile('■')
        return board
    
    def set(self, position, piece: Piece) -> None:
        # Flipped because access is [line][column] but position is (x, y), i.e., (column, line)
        self._board[position[1]][position[0]].set(piece)
    
    def get(self, position) -> Tile:
        # Flipped because access is [line][column] but position is (x, y), i.e., (column, line)
        return self._board[position[1]][position[0]]
    
    def get_display(self) -> None:
        x_axis = '  a b c d e f g h'
        y_axis = range(8, 0, -1)
        display = [x_axis]
        for line, y_index in zip(self._board, y_axis):
            line_tokens = [tile.get_token() for tile in line]
            line_tokens = [str(y_index)] + line_tokens
            display.append(' '.join(line_tokens))
        return '\n'.join(display)

    def _spawn_pieces(self) -> None:
        # Pawns
        for i in range(8):
            self.set((i, 1), Pawn(Color.BLACK))
            self.set((i, 6), Pawn(Color.WHITE))

        # Rooks
        for i in [0, 7]:
            self.set((i, 0), Rook(Color.BLACK))
            self.set((i, 7), Rook(Color.WHITE))

        # Knights
        for i in [1, 6]:
            self.set((i, 0), Knight(Color.BLACK))
            self.set((i, 7), Knight(Color.WHITE))
        
        # Bishops
        for i in [2, 5]:
            self.set((i, 0), Bishop(Color.BLACK))
            self.set((i, 7), Bishop(Color.WHITE))

        # Queens
        self.set((3, 0), Queen(Color.BLACK))
        self.set((3, 7), Queen(Color.WHITE))

        # Kings
        self.set((4, 0), King(Color.BLACK))
        self.set((4, 7), King(Color.WHITE))

    def in_bounds(self, position, target) -> bool:
        pos_x_valid = 0 <= position[0] <= 7
        pos_y_valid = 0 <= position[1] <= 7
        target_x_valid = 0 <= target[0] <= 7
        target_y_valid = 0 <= target[1] <= 7
        return pos_x_valid and pos_y_valid and target_x_valid and target_y_valid