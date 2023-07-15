from .piece import Piece
import numpy as np
import sys

sys.path.append("..")

class Rook(Piece):
    def get_valid_moves(self, board):
        possible_moves = []
        position = np.where(board == self)
        row, col = position[0][0], position[1][0]

        # Check vertical and horizontal moves
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r, c] == 0:
                    possible_moves.append((r, c))
                elif isinstance(board[r, c], Rook) and board[r, c].white != self.white:
                    possible_moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc

        return possible_moves