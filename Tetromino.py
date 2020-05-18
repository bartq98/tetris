import config
import Gameboard
import pygame

class Tetromino:

    # top left corner coons. of 4x4 falling buffer
    current_x = 0
    current_y = 0

    # for holding information of type of currently falling tetromino
    buffer = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    def __init__(self, type, x, y):
        self.current_x = x
        self.current_y = y

        # capital letters refers to shape of tetromino
        if type == "I":
            self.buffer = [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0]
            ]
        elif type == "Z":
            self.buffer = [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 0]
            ]
        elif type == "S":
            self.buffer = [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0]
            ]
        elif type == "J":
            self.buffer = [
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 1],
                [0, 0, 0, 0]
            ]
        elif type == "L":
            self.buffer = [
                [0, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 1, 1, 1],
                [0, 0, 0, 0]
            ]
        elif type == "T":
            self.buffer = [
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 1, 1, 1],
                [0, 0, 0, 0]
            ]
        elif type == "O":
            self.buffer = [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]
            ]
        else:
            print("Invalid type of Tetromino!")
            print("Should throw execption!")
            self.buffer = [
                [1, 0, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 0, 0, 1]
            ],


    def rotate_buffor(self, bufor, clockwise=True):
        """Roates bufor clockwise"""
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

    def fall_down(self, board : Gameboard.Gameboard):
        """Moves buffer one block down"""
        self.current_y += 1
        if self.will_collide(board):
            self.current_y -= 1
            return True
        else:
            return False

    def move(self, board : Gameboard.Gameboard):
        """Moves bufor by pressing keys"""
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.buffer = self.rotate_buffor(self.buffer)
                    if self.will_collide(board):
                        print("Kolidują!")
                        self.buffer = self.rotate_buffor(self.buffer, clockwise=False)
                if event.key == pygame.K_LEFT:
                    self.current_x -= 1
                    if self.will_collide(board):
                        print("Kolidują!")
                        self.current_x += 1
                if event.key == pygame.K_RIGHT:
                    self.current_x += 1
                    if self.will_collide(board):
                        print("Kolidują!")
                        self.current_x -= 1
                if event.key == pygame.K_DOWN:
                    self.current_y += 1
                    if self.will_collide(board):
                        print("Kolidują!")
                        self.current_y -= 1

    def will_collide(self, board : Gameboard):
        """Return True if buffer can move in specified direction, otherwise return False"""
        for i, row in enumerate(self.buffer):
            for j, elem in enumerate(row):
                if self.buffer[j][i] == 1 and board.fields[self.current_y + j][self.current_x + i] in [-1, 2]:
                    return True
        return False


    def draw_bufor(self, screen):
        """Draw 4 x 4 bufor with currently falling tetromino"""

        rect_bufor_x = (self.current_x * config.BLOCK_SIZE) + config.GAME_BOARD_COORDS["left"]
        rect_bufor_y = (self.current_y * config.BLOCK_SIZE) + config.GAME_BOARD_COORDS["top"]
    
        for i, row in enumerate(self.buffer):
            for j, elem in enumerate(row):
                if elem == 1:
                    pygame.draw.rect(
                        screen, 
                        config.COLORS["lightblue"],
                            (rect_bufor_x+(j*config.BLOCK_SIZE), 
                            rect_bufor_y+(i*config.BLOCK_SIZE), 
                            config.BLOCK_SIZE, 
                            config.BLOCK_SIZE)
                    )

    def debug_draw_bufor(self, screen):
        rect_bufor_x = (self.current_x * config.BLOCK_SIZE) + config.GAME_BOARD_COORDS["left"]
        rect_bufor_y = (self.current_y * config.BLOCK_SIZE) + config.GAME_BOARD_COORDS["top"]
    
        for i, row in enumerate(self.buffer):
            for j, elem in enumerate(row):
                if elem == 1:
                    pygame.draw.rect(
                        screen, 
                        config.COLORS["lightblue"],
                            (rect_bufor_x+(j*config.BLOCK_SIZE), 
                            rect_bufor_y+(i*config.BLOCK_SIZE), 
                            config.BLOCK_SIZE, 
                            config.BLOCK_SIZE)
                    )
                else:
                    pygame.draw.rect(
                        screen, 
                        (255, 255, 255),
                            (rect_bufor_x+(j*config.BLOCK_SIZE), 
                            rect_bufor_y+(i*config.BLOCK_SIZE), 
                            config.BLOCK_SIZE, 
                            config.BLOCK_SIZE)
                    )
