import sys
sys.path.append('..')
from src.ui.images import ChessBoard, White, Black
import src.board_data.data as BoardData

WHITE_PIECES = [White.PAWN, White.KNIGHT, White.BISHOP, White.ROOK, White.QUEEN, White.KING]
BLACK_PIECES = [Black.PAWN, Black.KNIGHT, Black.BISHOP, Black.ROOK, Black.QUEEN, Black.KING]

def render_board(win, x, y):
    win.blit(ChessBoard.BOARD_IMG.value, (x, y))


def render_pieces(win):
    for row in range(len(BoardData.board)):
        for col in range(len(BoardData.board[0])):
            if BoardData.board[row, col] != 0:
                if BoardData.board[row, col].white:
                    win.blit(WHITE_PIECES[BoardData.board[row, col].type].value, BoardData.board[row, col].pos)
                else:
                    win.blit(BLACK_PIECES[BoardData.board[row, col].type].value, BoardData.board[row, col].pos)


