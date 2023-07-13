from .piece import Piece
import numpy as np
import sys

sys.path.append("..")


class Knight(Piece):
    def get_valid_moves(self, matrix):
        valid_moves = []
        x, y = (self.pos[0] // 100, self.pos[1] // 100)

        offsets = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                   (1, -2), (2, -1), (-1, -2), (-2, -1)]

        for offset in offsets:
            new_x = x + offset[0]
            new_y = y + offset[1]

            if 0 <= new_x < 8 and 0 <= new_y < 8 and matrix[new_x, new_y] != 1:
                valid_moves.append((new_x, new_y))

        return valid_moves
