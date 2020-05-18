import pygame
import config


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

    def debug_board(self, print_coons):
        if print_coons:
            for i, row in enumerate(self.fields):
                for j, elem in enumerate(row):
                    print("[", i, "][", j, "]=", elem, sep="", end=",")
                print("")
            print("----------------")
        else:
            for row in self.fields:
                for elem in row:
                    print(elem, end=",")
                print("")
            print("----------------")


    def draw_gameboard(self, screen):
        """Drawing gameboard"""
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
