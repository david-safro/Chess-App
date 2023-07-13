import sys
sys.path.append('..')
from src.ui.images import ChessBoard, White
import src.board_data.data as BoardData


def render_board(win, x, y):
    win.blit(ChessBoard.BOARD_IMG.value, (x, y))


def render_white_pieces(win):
    win.blit(White.KNIGHT.value, BoardData.board[1, 7].pos)


def render_black_pieces(win):
    pass
