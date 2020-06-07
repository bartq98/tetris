#!/bin/python3.8

import config
import gameboard
import tetromino

"""
    Evaluates gameboard and chooses the next tetromino to fall
"""

class Evaluator():

    @staticmethod
    def simulate_falling(board: gameboard.Gameboard, buffer: tetromino.Tetromino):
        # if it collides at start - made for more elastic shifting tetromino of various shapes
        if buffer.will_collide(board):
            return board
        else:
            has_falled = 0
            while not has_falled:
                has_falled = buffer.fall_down(board)
            board.add_blocks(buffer)
            return board

    @staticmethod
    def caculate(board: gameboard.Gameboard, buffer: tetromino.Tetromino, x_shift):
        board_to_calculate = simulate_falling(board, buffer)
        
        score = 0

        columns_to_check = config.BOARD_COLUMNS-2
        rows_to_check    = config.BOARD_ROWS-1
        for j in range(1, columns_to_check):
            gaps_found = 0
            max_height = 0
            for i in range(0, rows_to_check): 
                # first met block within specified column determites max_height
                if max_height == 0 and board_to_calculate.fields[i][j] == config.FALLED_BLOCK:
                    max_height = 22 - j
                # for all above every empty block is interpreted as unwanted gap
                elif board_to_calculate.fields[i][j] == config.EMPTY_BLOCK:
                    gaps_found += 1
            score += max_height*config.POINTS_HEIGHT + gaps_found*config.POINTS_GAP
        
        return score
