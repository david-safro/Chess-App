import pygame

def get_rounded_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rounded_x = (mouse_x // 100) * 100
    rounded_y = (mouse_y // 100) * 100
    return (rounded_x//100, rounded_y//100)