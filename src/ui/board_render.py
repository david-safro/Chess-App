from src.ui.images import ChessBoard, White, Black
import src.board_data.data as board_data

WHITE_PIECES = [White.PAWN, White.KNIGHT, White.BISHOP, White.ROOK, White.QUEEN, White.KING]
BLACK_PIECES = [Black.PAWN, Black.KNIGHT, Black.BISHOP, Black.ROOK, Black.QUEEN, Black.KING]


def render_board(win, x, y):
    win.blit(ChessBoard.BOARD_IMG.value, (x, y))


def render_pieces(win):
    for row in range(len(board_data.board)):
        for col in range(len(board_data.board[0])):
            if board_data.board[row, col] != 0:
                if board_data.board[row, col].white:
                    win.blit(WHITE_PIECES[board_data.board[row, col].type].value, board_data.board[row, col].pos)
                else:
                    win.blit(BLACK_PIECES[board_data.board[row, col].type].value, board_data.board[row, col].pos)
