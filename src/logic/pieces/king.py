from .piece import Piece


class King(Piece):
    def get_valid_moves(self, board):
        row, col = self.pos[0]//100, self.pos[1]//100
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        valid_moves = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board[r, c]
                if piece == 0:
                    valid_moves.append((r, c))
                elif (self.white and not piece.white) or (not self.white and piece.white):
                    valid_moves.append((r, c))

        return valid_moves
