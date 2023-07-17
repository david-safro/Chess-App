import pygame
from .board_render import render_board, render_pieces
from .Components.legal_move_denoter import render
from .move_reader import get_rounded_position
from src.board_data import data


class UI:
    def __init__(self):
        pass

    def legal_move_display(self, win):
        rounded_pos = get_rounded_position()
        board = data.board
        selected_piece = data.selected_piece
        possible_moves = data.possible_moves

        if board[rounded_pos] != 0 and rounded_pos != selected_piece:
            data.selected_piece = rounded_pos
            data.possible_moves = board[rounded_pos].get_valid_moves(board)
            render(win, data.possible_moves)
        elif rounded_pos in possible_moves:
            board[selected_piece].pos = (rounded_pos[0] * 100, rounded_pos[1] * 100)
            board[rounded_pos], board[selected_piece] = board[selected_piece], board[rounded_pos]
            data.selected_piece = None
            data.possible_moves = []
        else:
            data.selected_piece = None
            data.possible_moves = []


    def ui_render(self, win: pygame.surface.Surface, board_x: int, board_y: int):
        render_board(win, board_x, board_y)
        self.legal_move_display(win)
        render_pieces(win)
