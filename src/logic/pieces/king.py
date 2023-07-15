from .piece import Piece
import sys
import numpy as np
sys.path.append("..")

class King(Piece):
    def get_valid_moves(self, board):
        possible_moves = []
        position = np.where(board == self)
        row, col = position[0][0], position[1][0]
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue  # Skip the current position
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8:
                    if board[r, c] == 0 or (isinstance(board[r, c], King) and board[r, c].white != self.white):
                        possible_moves.append((r, c))

        return possible_moves
