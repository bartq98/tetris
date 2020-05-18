import pygame
import config
import Tetromino


class Gameboard:
    """Implementing board when tetrominos falls and whole game happend"""
    fields = [[]]

    def __init__(self):
        self.initialize_board()

    def initialize_board(self):
        # When start all fields are set to 0 (except boundaries set which are set to -1)
        self.fields = [[0 for i in range(0, config.BOARD_COLUMNS)] for j in range(0, config.BOARD_ROWS)]

        # Setting bounds to -1
        for i in range(0, config.BOARD_ROWS-1):
            for j in range(0, config.BOARD_COLUMNS):
                if j in (0, config.BOARD_COLUMNS-1):
                    self.fields[i][j] = -1

        for i in range(0, config.BOARD_COLUMNS):
            self.fields[config.BOARD_ROWS-1][i] = -1

    def draw_gameboard(self, screen):
        """Drawing gameboard within screen"""

        # used colors can be simply changed
        color_bound = config.COLORS["black"]
        color_empty = config.COLORS["red"]
        color_block = config.COLORS["orange"]

        for i, row in enumerate(self.fields):
            for j, board_elem in enumerate(row):
                if board_elem == 0: # for empty cells
                    pygame.draw.rect(
                        screen,
                        color_empty,
                        (config.GAME_BOARD_COORDS["left"] + j * config.BLOCK_SIZE,
                         config.GAME_BOARD_COORDS["top"] + i * config.BLOCK_SIZE,
                         config.BLOCK_SIZE, config.BLOCK_SIZE)
                    )
                elif board_elem == -1: #for boundaries
                    pygame.draw.rect(
                        screen,
                        color_bound,
                        (config.GAME_BOARD_COORDS["left"] + j * config.BLOCK_SIZE,
                         config.GAME_BOARD_COORDS["top"] + i * config.BLOCK_SIZE,
                         config.BLOCK_SIZE, config.BLOCK_SIZE)
                    )
                elif board_elem == 2: #for falled blocks
                    pygame.draw.rect(
                        screen,
                        color_block,
                        (config.GAME_BOARD_COORDS["left"] + j * config.BLOCK_SIZE,
                         config.GAME_BOARD_COORDS["top"] + i * config.BLOCK_SIZE,
                         config.BLOCK_SIZE, config.BLOCK_SIZE)
                    )

    def add_blocks(self, tetromino):
        """Adding single blocks of falled tetromino to self.fields => setting them to value 2"""
        y, x = tetromino.current_y, tetromino.current_x
        
        for i, row in enumerate(tetromino.buffer):
            for j, elem in enumerate(row):
                if tetromino.buffer[i][j]:
                    self.fields[y + i][x + j] = 2

    def delete_lines(self):
        for i, row in enumerate(self.fields[:-1]):
            if 0 in row[1:len(row)-1]: # in i row is 0, so it isn't empty
                continue
            else:
                print(f"Linia {i} do usunięcia")