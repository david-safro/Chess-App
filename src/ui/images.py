import pygame
import sys
from enum import Enum

sys.path.append('..')
from src.constants import Board


class ChessBoard(Enum):
    BOARD_IMG = pygame.transform.scale(pygame.image.load("../images/chessboard.svg"),
                                       (Board.WIDTH.value, Board.HEIGHT.value))


class White(Enum):
    KNIGHT = pygame.transform.smoothscale(pygame.image.load("../images/white/wkn.svg"),
                                    (Board.CELL.value, Board.CELL.value))
