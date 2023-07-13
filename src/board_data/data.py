import numpy as np
import sys

sys.path.append('..')
from src.constants import Board
from src.logic.pieces.knight import Knight

board = np.zeros((Board.SIZE.value, Board.SIZE.value), dtype=object)

board[1, 7] = Knight(True, (100, 700))

selected_piece = None
possible_moves = []
