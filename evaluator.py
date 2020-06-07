#!/bin/python3.8
import pygame
import config
import tetromino
import gameboard
import time
import copy
import random

"""
    Evaluates gameboard and chooses the next tetromino to fall
"""

class Evaluator():

    @staticmethod
    def simulate_falling(board: gameboard.Gameboard, buffer: tetromino.Tetromino):
        new_board  = copy.deepcopy(board)
        new_buffer = copy.deepcopy(buffer)

        # if it collides at start - made for more elastic shifting tetromino of various shapes
        if new_buffer.will_collide(new_board):
            return False
        else:
            has_falled = 0
            while not has_falled:
                has_falled = new_buffer.fall_down(new_board)
            new_board.add_blocks(new_buffer)
            return new_board

    @staticmethod
    def calculate(board: gameboard.Gameboard, buffer: tetromino.Tetromino):
        board_to_calculate = Evaluator.simulate_falling(board, buffer)
        
        if board_to_calculate is False:
            return False

        columns_to_check = config.BOARD_COLUMNS-1
        rows_to_check    = config.BOARD_ROWS-1
        score = 0

        for j in range(1, columns_to_check):
            
            gaps_found = 0
            max_height = 0
            
            for i in range(0, rows_to_check): 
                # first met (going from top to bottom) block within specified column determites max_height
                if max_height == 0 and board_to_calculate.fields[i][j] == config.FALLEN_BLOCK:
                    max_height = 22 - i
                # for all above max_height every empty block is interpreted as unwanted gap
                elif max_height != 0 and board_to_calculate.fields[i][j] == config.EMPTY_BLOCK:
                    gaps_found += 1

            score += (max_height*config.POINTS_HEIGHT) + (gaps_found*config.POINTS_GAP)
            print(f"Kolumna {j} dała punktów {(max_height*config.POINTS_HEIGHT) + (gaps_found*config.POINTS_GAP)}")
            
        
        return score

    @staticmethod
    def test_all_cases(board: gameboard.Gameboard):
        
        most_unwanted_tetrominos = {}
        
        start_width = 1
        rotates = 4

        for shape in config.TETROMINO_SHAPES:
            if shape == "I":
                end_width = config.BOARD_COLUMNS-2
            else:
                end_width = config.BOARD_COLUMNS-1
            for rotate in range(rotates):
                for x_shift in range(start_width, end_width):
                        testing_buffer = tetromino.Tetromino(shape, rotates, x_shift)
                        score = Evaluator.calculate(board, testing_buffer)
                        if score is False:
                            continue
                        most_unwanted_tetrominos[f"{shape}-{rotate}-{x_shift}"] = score

        return most_unwanted_tetrominos

    @staticmethod
    def generate_tetromino(board: gameboard.Gameboard, malice_level: int):
        most_unwanted_tetrominos = Evaluator.test_all_cases(board)

        # make list with tuples - first elem. of tuple is shape-rotate-x_shift str, second - score of this tetromino
        most_unwanted_tetrominos = sorted(most_unwanted_tetrominos.items(), key=lambda x: x[1], reverse=False)

        diffrent_malice_levels = 10
        size_range = len(most_unwanted_tetrominos) // diffrent_malice_levels 
        random_but_malice = malice_level*size_range - random.randint(0, size_range)

        chosed_tetromino = most_unwanted_tetrominos[random_but_malice][0] #
        shape, rotate, x_shift = chosed_tetromino.split("-")
        print(f"{shape}-{rotate}-{x_shift}")
        rotate = int(rotate)
        x_shift = int(x_shift)
        return tetromino.Tetromino(shape, times_rotated=rotate, x=x_shift)


# # to test evaluator - will be deleted soon...
# testing_board = gameboard.Gameboard()
# testing_board.fields[21][1] = 2
# testing_board.fields[21][2] = 2
# testing_board.fields[21][3] = 2
# testing_board.fields[21][4] = 2
# testing_board.fields[21][5] = 2
# testing_board.fields[21][6] = 2
# testing_board.fields[20][1] = 2
# testing_board.fields[20][2] = 2
# testing_board.fields[20][3] = 2
# testing_board.fields[0][9] = 2
# test_teto = tetromino.Tetromino("I", times_rotated=2, x=3)

# def pre_configure_window():
#     """Configure whole stuff around game"""
    
#     pygame.display.set_caption("Tetris by Bartq98")
#     screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
#     screen.fill(config.Color.DARKRED.value)
#     return screen

# screen = pre_configure_window()
# pygame.init()
# score = Evaluator.calculate(testing_board, test_teto)
# score2 = Evaluator.test_all_cases(testing_board)
# test_teto = Evaluator.generate_tetromino(testing_board, 4)
# print(test_teto.buffer)
# print(score)
# testing_board.draw_gameboard(screen)
# pygame.display.update()
# time.sleep(30)