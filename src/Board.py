from src.Tile import Tile


class Board:
    def __init__(self):
        self.board = self._build()

    def _build(self):
        board = [[None]*8 for i in range(8)]
        for i in range(8):
            for j in range(8):
                if (i+j)%2:
                    board[i][j] = Tile('□')
                else:
                    board[i][j] = Tile('■')
        return board
    
    def set(self, position, piece):
        # Flipped because access is [line][column] but position is (x, y), i.e., (column, line)
        self.board[position[1]][position[0]].set(piece)
    
    def get(self, position) -> Tile:
        # Flipped because access is [line][column] but position is (x, y), i.e., (column, line)
        return self.board[position[1]][position[0]]
    
    def show(self):
        for line in self.board:
            line_tokens = [tile.get_token() for tile in line]
            print(' '.join(line_tokens))