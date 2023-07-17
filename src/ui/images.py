import pygame
import sys
from enum import Enum

sys.path.append('..')
from src.constants import Board
import io

def load_and_scale_svg(filename, scale):
    svg_string = open(filename, "rt").read()
    start = svg_string.find('<svg')
    if start > 0:
        svg_string = svg_string[:start + 4] + f' transform="scale({scale})"' + svg_string[start + 4:]
    return pygame.image.load(io.BytesIO(svg_string.encode()))



class ChessBoard(Enum):
    BOARD_IMG = pygame.transform.scale(pygame.image.load("../images/chessboard.svg"),
                                       (Board.WIDTH.value, Board.HEIGHT.value))


class White(Enum):
    KNIGHT = load_and_scale_svg("../images/white/wkn.svg", 100/45)
    PAWN = load_and_scale_svg("../images/white/wp.svg", 100/45)
    BISHOP = load_and_scale_svg("../images/white/wb.svg", 100/45)
    ROOK = load_and_scale_svg("../images/white/wr.svg", 100/45)
    QUEEN = load_and_scale_svg("../images/white/wq.svg", 100/45)
    KING = load_and_scale_svg("../images/white/wk.svg", 100/45)


class Black(Enum):
    KNIGHT = load_and_scale_svg("../images/black/bkn.svg", 100/45)
    PAWN = load_and_scale_svg("../images/black/bp.svg", 100/45)
    BISHOP = load_and_scale_svg("../images/black/bb.svg", 100/45)
    ROOK = load_and_scale_svg("../images/black/br.svg", 100/45)
    QUEEN = load_and_scale_svg("../images/black/bq.svg", 100/45)
    KING = load_and_scale_svg("../images/black/bk.svg", 100/45)
