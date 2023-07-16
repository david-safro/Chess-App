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
    PAWN = pygame.transform.smoothscale(pygame.image.load("../images/white/wp.svg"),
                                          (Board.CELL.value, Board.CELL.value))
    BISHOP = pygame.transform.smoothscale(pygame.image.load("../images/white/wb.svg"),
                                        (Board.CELL.value, Board.CELL.value))
    ROOK = pygame.transform.smoothscale(pygame.image.load("../images/white/wr.svg"),
                                        (Board.CELL.value, Board.CELL.value))
    QUEEN = pygame.transform.smoothscale(pygame.image.load("../images/white/wq.svg"),
                                        (Board.CELL.value, Board.CELL.value))
    KING = pygame.transform.smoothscale(pygame.image.load("../images/white/wk.svg"),
                                        (Board.CELL.value, Board.CELL.value))

class Black(Enum):

    KNIGHT = pygame.transform.smoothscale(pygame.image.load("../images/black/bkn.svg"),
                                    (Board.CELL.value, Board.CELL.value))
    PAWN = pygame.transform.smoothscale(pygame.image.load("../images/black/bp.svg"),
                                          (Board.CELL.value, Board.CELL.value))
    BISHOP = pygame.transform.smoothscale(pygame.image.load("../images/black/bb.svg"),
                                        (Board.CELL.value, Board.CELL.value))
    ROOK = pygame.transform.smoothscale(pygame.image.load("../images/black/br.svg"),
                                        (Board.CELL.value, Board.CELL.value))
    QUEEN = pygame.transform.smoothscale(pygame.image.load("../images/black/bq.svg"),
                                        (Board.CELL.value, Board.CELL.value))
    KING = pygame.transform.smoothscale(pygame.image.load("../images/black/bk.svg"),
                                        (Board.CELL.value, Board.CELL.value))
