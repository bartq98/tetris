#!/bin/python3.8
import pygame
import config
import tetromino
import gameboard
import time
import copy

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
            return new_board
        else:
            has_falled = 0
            while not has_falled:
                has_falled = new_buffer.fall_down(new_board)
            new_board.add_blocks(new_buffer)
            return new_board

    @staticmethod
    def calculate(board: gameboard.Gameboard, buffer: tetromino.Tetromino):
        board_to_calculate = Evaluator.simulate_falling(board, buffer)
        
        score = 0

        columns_to_check = config.BOARD_COLUMNS-1
        rows_to_check    = config.BOARD_ROWS-1
        for j in range(1, columns_to_check):
            gaps_found = 0
            max_height = 0
            for i in range(0, rows_to_check): 
                # first met block within specified column determites max_height
                if max_height == 0 and board_to_calculate.fields[i][j] == config.FALLED_BLOCK:
                    max_height = 22 - i
                # for all above every empty block is interpreted as unwanted gap
                elif max_height != 0 and board_to_calculate.fields[i][j] == config.EMPTY_BLOCK:
                    gaps_found += 1

            print(f"\nIn column no. {j}")
            print(f"max_height = {max_height}")
            print(f"gaps_found = {gaps_found}")
            score += (max_height*config.POINTS_HEIGHT) + (gaps_found*config.POINTS_GAP)
        
        return score

    