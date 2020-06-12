"""Module containg Tetromino class

Tetromino class is used in main file - game.py

It is responsible for:
    - drawing buffer (currently falling tetromino)
    - detecting collision with gameboard (with borders and previously fallen blocks)
    - moving buffer (left/right/rotate/fall)
"""

import pygame

import config
import gameboard


class Tetromino:

    def __init__(self, type, times_rotated=0, x=4, y=0):
        """Initializes falling tetromino."""

        # cooridantes of [0][0] (top left element) of buffor on gameboard
        self.current_x = x
        self.current_y = y

        # self.buffer is 4x4 array which holds current shape and rotation of tetromino

        if type in config.TETROMINO_SHAPES:
            self.buffer = config.TETROMINO_SHAPES[type]
            for i in range(times_rotated):
                self.buffer = self.rotate(self.buffer)
        else: # for invalid argument of tetromino
            # below - it clearly shows the error
            self.buffer = [
                [1, 0, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 0, 0, 1]
            ],

    def rotate(self, bufor, clockwise=True):
        """Roates bufor clockwise or counterclockwise"""
        rotated_array = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        for i in range(0, 4):
            for j in range(0, 4):
                rotated_array[i][j] = bufor[3-j][i] if clockwise else bufor[j][3-i]
        return rotated_array

    def fall_down(self, board: gameboard.Gameboard):
        """Moves buffer one block down
        and returns True when the block collides with previously fallen blocks"""
        self.current_y += 1
        if self.will_collide(board):
            self.current_y -= 1
            return True
        else:
            return False

    def move(self, board: gameboard.Gameboard):
        """Moves bufor by pressing keys"""
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.buffer = self.rotate(self.buffer)
                    if self.will_collide(board):
                        self.buffer = self.rotate(self.buffer, clockwise=False)
                if event.key == pygame.K_LEFT:
                    self.current_x -= 1
                    if self.will_collide(board):
                        self.current_x += 1
                if event.key == pygame.K_RIGHT:
                    self.current_x += 1
                    if self.will_collide(board):
                        self.current_x -= 1
                if event.key == pygame.K_DOWN:
                    self.current_y += 1
                    if self.will_collide(board):
                        self.current_y -= 1

    def will_collide(self, board: gameboard):
        """Return False if buffer can move in specified direction, otherwise return False"""
        for i, row in enumerate(self.buffer):
            for j, elem in enumerate(row):
                if (self.buffer[j][i] == 1 and # if filled element within buffer...
                    board.fields[self.current_y + j][self.current_x + i] in [config.BORDER_BLOCK, config.FALLEN_BLOCK]): # ...intersects within borders or fallen blocks
                    return True
        return False

    def calculate_buffor_drawing_coordinates(self):
        """Calculates drawing coordinates necessarry while drawing single block"""
        rect_bufor_x = (self.current_x * config.BLOCK_SIZE) + config.GAME_BOARD_COORDS.left
        rect_bufor_y = (self.current_y * config.BLOCK_SIZE) + config.GAME_BOARD_COORDS.top

        return rect_bufor_x, rect_bufor_y

    def draw(self, screen):
        """Draws 4 x 4 bufor of currently falling tetromino"""

        rect_bufor_x, rect_bufor_y = self.calculate_buffor_drawing_coordinates()

        for i, row in enumerate(self.buffer):
            for j, elem in enumerate(row):
                if elem == config.BUFFER_BLOCK:
                    pygame.draw.rect(
                        screen,
                        config.Color.LIGHTBLUE.value,
                        (rect_bufor_x+(j*config.BLOCK_SIZE),
                         rect_bufor_y+(i*config.BLOCK_SIZE),
                         config.BLOCK_SIZE,
                         config.BLOCK_SIZE)
                    )

    def __str__(self):
        return f"\n {self.buffer[0]} \n {self.buffer[1]} \n {self.buffer[2]} \n {self.buffer[3]} \n"