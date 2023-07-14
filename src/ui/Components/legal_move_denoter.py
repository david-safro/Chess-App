import pygame
import sys

sys.path.append("..")
from src.constants import Board, Color


def render(win, positions):
    for pos in positions:
        pygame.draw.circle(win, Color.SHADER_GRAY.value,
                           (pos[0] * 100 + Board.CELL.value // 2, pos[1] * 100 + Board.CELL.value // 2),
                           Board.CELL.value * 0.24)
