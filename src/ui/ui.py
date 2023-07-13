from .board_render import *
import pygame
from .Components.legal_move_denoter import render
from .move_reader import get_rounded_position
import sys

sys.path.append("..")
from src.board_data.data import board


class UI:
    def __init__(self):
        pass

    def legal_move_display(self, win):
        rounded_pos = get_rounded_position()
        print(board[rounded_pos].get_valid_moves(board))
        render(win, board[rounded_pos].get_valid_moves(board))

    def ui_render(self, win: pygame.surface.Surface, board_x: int, board_y: int):
        render_board(win, board_x, board_y)
        render_white_pieces(win)
        render_black_pieces(win)
