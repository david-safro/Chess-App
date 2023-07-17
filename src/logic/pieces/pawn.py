from .piece import Piece
import numpy as np


class Pawn(Piece):
    def get_valid_moves(self, board):
        possible_moves = []
        direction = -1 if self.white else 1  # Adjusted direction
        position = np.where(board == self)
        row, col = position[0][0], position[1][0]

        # Check forward move
        if board[row, col + direction] == 0:
            possible_moves.append((row, col + direction))

        # Check diagonal captures
        if row > 0 and col > 0 and isinstance(board[row - 1, col - 1], Pawn) and board[
            row - 1, col - 1].white != self.white:
            possible_moves.append((row - 1, col - 1))
        if row < 7 and col > 0 and isinstance(board[row + 1, col - 1], Pawn) and board[
            row + 1, col - 1].white != self.white:
            possible_moves.append((row + 1, col - 1))
        if col == 6 and self.white:
            possible_moves.append((row, col - 2))
        elif col == 1 and not self.white:
            possible_moves.append((row, col + 2))
        return possible_moves
