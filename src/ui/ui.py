from .board_render import *
import pygame
from .Components.legal_move_denoter import render
from .move_reader import get_rounded_position
import sys

sys.path.append("..")
import src.board_data.data
class UI:
    def __init__(self):
        pass

    def legal_move_display(self, win):
        rounded_pos = get_rounded_position()
        if src.board_data.data.board[rounded_pos] != 0 and rounded_pos != src.board_data.data.selected_piece:
            src.board_data.data.selected_piece = rounded_pos
            src.board_data.data.possible_moves = src.board_data.data.board[rounded_pos].get_valid_moves(src.board_data.data.board)
            render(win, src.board_data.data.possible_moves)
        elif rounded_pos in src.board_data.data.possible_moves:
            src.board_data.data.board[src.board_data.data.selected_piece].pos = rounded_pos
            print(src.board_data.data.board[src.board_data.data.selected_piece].pos)
            src.board_data.data.selected_piece = None
            src.board_data.data.possible_moves = []


        else:
            src.board_data.data.selected_piece = None
            src.board_data.data.possible_moves = []
        print(src.board_data.data.possible_moves, src.board_data.data.selected_piece)

    def ui_render(self, win: pygame.surface.Surface, board_x: int, board_y: int):
        render_board(win, board_x, board_y)
        render_white_pieces(win)
        render_black_pieces(win)
