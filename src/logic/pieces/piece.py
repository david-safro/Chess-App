class Piece:
    def __init__(self, white: bool, pos: tuple, type: int, has_moved: bool):
        self.white = white
        self.pos = pos
        self.type = type
        self.has_moved = has_moved


