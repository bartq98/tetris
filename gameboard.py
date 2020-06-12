"""Module containg Gameboard class

Gameboard class is used in main file - game.py

It is responsible for:
    - drawing board
    - holding falling tetromino (buffer)
    - holding information about blocks that had fallen earlier
    - detecting which rows should be deleted (and then moving all above one block down)
"""

import pygame

import config
import tetromino


class Gameboard:
    """Implementing board when tetrominos falls and whole game happend"""

    # self.fields are where tetromino falls

    def __init__(self):
        self.initialize_board()


    def initialize_board(self):
        """Set proper values of self.fields - 0 when buffer can move and -1 which are borders (undeletable)"""

        # When start all fields are set to 0 (except borders set which are set to -1)
        self.fields = [[0 for i in range(0, config.BOARD_COLUMNS)] for j in range(0, config.BOARD_ROWS)]

        for i in range(0, config.BOARD_ROWS-1): # except the last row
            # set first and last column of i row as border
            self.fields[i][0] = config.BORDER_BLOCK
            self.fields[i][config.BOARD_COLUMNS-1] = config.BORDER_BLOCK

        for i in range(0, config.BOARD_COLUMNS):
            self.fields[config.BOARD_ROWS-1][i] = config.BORDER_BLOCK


    def draw_single_block(self, screen, color, x_rect, y_rect):
        """Function responsible for drawing single block of gameboard"""
        pygame.draw.rect(
            screen,
            color,
             (config.GAME_BOARD_COORDS.left + x_rect * config.BLOCK_SIZE,
              config.GAME_BOARD_COORDS.top  + y_rect * config.BLOCK_SIZE,
              config.BLOCK_SIZE, config.BLOCK_SIZE)
        )


    def draw_gameboard(self, screen):
        """Drawing gameboard within screen"""

        # used colors can be simply changed
        color_block  = config.Color.ORANGE.value
        color_border = config.Color.BLACK.value
        color_empty  = config.Color.RED.value

        for i, row in enumerate(self.fields):
            for j, board_elem in enumerate(row):
                if board_elem == config.EMPTY_BLOCK:
                    self.draw_single_block(screen, color_empty, j, i)
                elif board_elem == config.BORDER_BLOCK:
                    self.draw_single_block(screen, color_border, j, i)
                elif board_elem == config.FALLEN_BLOCK:
                    self.draw_single_block(screen, color_block, j, i)


    def add_blocks(self, tetromino):
        """Adding single blocks of falled tetromino to self.fields => setting them to value 2"""
        y, x = tetromino.current_y, tetromino.current_x

        for i, row in enumerate(tetromino.buffer):
            for j, elem in enumerate(row):
                if tetromino.buffer[i][j] == config.BUFFER_BLOCK:
                    self.fields[y + i][x + j] = config.FALLEN_BLOCK


    def delete_lines(self):
        """Check if specified row is empty; if yes deletes it and moves all block down."""
        rows_to_detele = [] # holds indexes of filled rows
        for i, row in enumerate(self.fields[:-1]):
            if 0 in row[1:len(row)-1]: # in i row is 0, so it isn't empty
                continue
            else:
                rows_to_detele.append(i)

        for row_index in rows_to_detele:
            for i in range(1, len(row)-1):
                self.fields[row_index][i] = 0 # delete row

            for i in range(row_index-1, 0, -1): # from bottom to up
                for j in range(1, len(row)-1):
                    self.fields[i+1][j] = self.fields[i][j] # moves all blocks within row one row lower
