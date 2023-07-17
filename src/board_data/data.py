import numpy as np
from src.constants import Board
from src.logic.pieces import rook, king, knight, pawn, bishop, queen

board = np.zeros((Board.SIZE.value, Board.SIZE.value), dtype=object)
board[0, 7] = rook.Rook(True, (0, 700), 3)
board[1, 7] = knight.Knight(True, (100, 700), 1)
board[2, 7] = bishop.Bishop(True, (200, 700), 2)
board[3, 7] = queen.Queen(True, (300, 700), 4)
board[4, 7] = king.King(True, (400, 700), 5)
board[5, 7] = bishop.Bishop(True, (500, 700), 2)
board[6, 7] = knight.Knight(True, (600, 700), 1)
board[7, 7] = rook.Rook(True, (700, 700), 3)
for x in range(0, 8):
    board[x, 6] = pawn.Pawn(True, (x*100, 600), 0)

board[0, 0] = rook.Rook(False, (0, 0), 3)
board[1, 0] = knight.Knight(False, (100, 0), 1)
board[2, 0] = bishop.Bishop(False, (200, 0), 2)
board[3, 0] = queen.Queen(False, (300, 0), 4)
board[4, 0] = king.King(False, (400, 0), 5)
board[5, 0] = bishop.Bishop(False, (500, 0), 2)
board[6, 0] = knight.Knight(False, (600, 0), 1)
board[7, 0] = rook.Rook(False, (700, 0), 3)
for x in range(0, 8):
    board[x, 1] = pawn.Pawn(False, (x*100, 100), 0)
white_turn = True
selected_piece = None
possible_moves = []
