import pygame
import sys

sys.path.append('..')
from src.constants import Screen, Color
from src.ui.ui import UI
from src.ui.move_reader import get_rounded_position
from src.board_data.data import board

pygame.init()
win = pygame.display.set_mode((Screen.WIDTH.value, Screen.HEIGHT.value), pygame.SRCALPHA)
pygame.display.set_caption(Screen.TITLE.value)
UI = UI()


def main():
    clock = pygame.time.Clock()
    run = True
    win.fill(Color.BLACK.value)
    UI.ui_render(win, 0, 0)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                UI.ui_render(win, 0, 0)
                UI.legal_move_display(win)

        clock.tick(Screen.FPS.value)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
