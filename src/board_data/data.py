import numpy as np
import sys

sys.path.append('..')
from src.constants import Board
from src.logic.pieces.knight import Knight
from src.logic.pieces.pawn import Pawn
from src.logic.pieces.bishop import Bishop
from src.logic.pieces.rook import Rook
from src.logic.pieces.queen import Queen
from src.logic.pieces.king import King

board = np.zeros((Board.SIZE.value, Board.SIZE.value), dtype=object)
board[0, 7] = Rook(True, (0, 700), 3, False)
board[1, 7] = Knight(True, (100, 700), 1, False)
board[2, 7] = Bishop(True, (200, 700), 2, False)
board[3, 7] = Queen(True, (300, 700), 4, False)
board[4, 7] = King(True, (400, 700), 5, False)
board[5, 7] = Bishop(True, (500, 700), 2, False)
board[6, 7] = Knight(True, (600, 700), 1, False)
board[7, 7] = Rook(True, (700, 700), 3, False)
board[0, 6] = Pawn(True, (0, 600), 0, False)
board[1, 6] = Pawn(True, (100, 600), 0, False)
board[2, 6] = Pawn(True, (200, 600), 0, False)
board[3, 6] = Pawn(True, (300, 600), 0, False)
board[4, 6] = Pawn(True, (400, 600), 0, False)
board[5, 6] = Pawn(True, (500, 600), 0, False)
board[6, 6] = Pawn(True, (600, 600), 0, False)
board[7, 6] = Pawn(True, (700, 600), 0, False)

board[0, 0] = Rook(False, (0, 0), 3, False)
board[1, 0] = Knight(False, (100, 0), 1, False)
board[2, 0] = Bishop(False, (200, 0), 2, False)
board[3, 0] = Queen(False, (300, 0), 4, False)
board[4, 0] = King(False, (400, 0), 5, False)
board[5, 0] = Bishop(False, (500, 0), 2, False)
board[6, 0] = Knight(False, (600, 0), 1, False)
board[7, 0] = Rook(False, (700, 0), 3, False)
board[0, 1] = Pawn(False, (0, 100), 0, False)
board[1, 1] = Pawn(False, (100, 100), 0, False)
board[2, 1] = Pawn(False, (200, 100), 0, False)
board[3, 1] = Pawn(False, (300, 100), 0, False)
board[4, 1] = Pawn(False, (400, 100), 0, False)
board[5, 1] = Pawn(False, (500, 100), 0, False)
board[6, 1] = Pawn(False, (600, 100), 0, False)
board[7, 1] = Pawn(False, (700, 100), 0, False)
selected_piece = None
possible_moves = []
