import sys
sys.path.append('..')
from src.ui.images import ChessBoard, White
import src.board_data.data as BoardData


def render_board(win, x, y):
    win.blit(ChessBoard.BOARD_IMG.value, (x, y))


def render_white_pieces(win):
    for row in range(len(BoardData.board)):
        for col in range(len(BoardData.board[0])):
            if BoardData.board[row, col] != 0:
                win.blit(White.KNIGHT.value, BoardData.board[row, col].pos)
                print("rendered", (row, col))


def render_black_pieces(win):
    pass
