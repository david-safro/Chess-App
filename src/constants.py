from enum import Enum


class Screen(Enum):
    WIDTH = 800
    HEIGHT = 800
    FPS = 60
    TITLE = "CHESS"


class Board(Enum):
    SIZE = 8
    WIDTH = SIZE * 100
    HEIGHT = SIZE * 100
    CELL = WIDTH / SIZE


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    GRAY = (128, 128, 128)
    SHADER_GRAY = (128, 128, 128, 50)
