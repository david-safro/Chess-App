import numpy as np
import sys

sys.path.append('..')
from src.constants import Board
from src.logic.pieces.knight import Knight

board = np.empty((Board.SIZE.value, Board.SIZE.value), dtype=object)

board[1, 7] = Knight(True, (100, 700))
board[6, 7] = Knight(True, (600, 700))
