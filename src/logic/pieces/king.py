from .piece import Piece
import sys
import numpy as np
sys.path.append("..")

class King(Piece):
    def get_valid_moves(self, board):
        possible_moves = []

        row, col = self.pos

        # Define the eight possible directions the king can move
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new position is within the board boundaries
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                # Check if the new position is empty or occupied by a white piece
                if board[new_row][new_col] == 0 or board[new_row][new_col].white:
                    possible_moves.append((new_row, new_col))

        # Check if castling is possible
        if not self.has_moved:
            # Check if castling to the right is possible
            if board[row][7] and not board[row][7].has_moved:
                if all(board[row][col + 1:col + 3] == 0):
                    possible_moves.append((row, col + 2))

            # Check if castling to the left is possible
            if board[row][0] and not board[row][0].has_moved:
                if all(board[row][col - 3:col] == 0):
                    possible_moves.append((row, col - 2))

        return possible_moves
