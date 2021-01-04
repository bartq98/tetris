#!/bin/env python
"Simple Tetris-inspired game written with Python and PyGame"
import random
import time

import pygame

import config
import tetromino
import gameboard
import evaluator


def pre_configure_window():
    """Configure whole stuff around game"""
    
    pygame.display.set_caption("Tetris by Bartq98")
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    screen.fill(config.Color.DARKRED.value)
    return screen


def game():
    """Runs whole game"""
    pygame.init()
    screen = pre_configure_window()

    buffer = tetromino.Tetromino("I", times_rotated=0, x=3, y=0)
    actuall_gameboard = gameboard.Gameboard()

    time_steps_done_before_fall = 0
    game_over = False

    # main gameloop
    while not game_over:

        actuall_gameboard.draw_gameboard(screen) # only gameboard are redrawing in all frame
        time.sleep(config.GAME_SINGLE_FRAME_SEC) # sleeps for every 50 miliseconds

        buffer.move(actuall_gameboard) # controlled from keyboard

        buffer.draw(screen)

        time_steps_done_before_fall += 1
        if time_steps_done_before_fall == config.TIME_STEPS_TO_FALL_BUFFER:
            has_falled = buffer.fall_down(actuall_gameboard)
            
            if has_falled:
                actuall_gameboard.add_blocks(buffer)
                buffer = evaluator.Evaluator.generate_tetromino(actuall_gameboard, config.MALICIOUS_LEVEL)
                if buffer.fall_down(actuall_gameboard): # while newly added tetromino instantly touching fallen blocks
                    game_over = True
                    print(f"Thank You for your play - waiting to see u next time!")
                actuall_gameboard.delete_lines()

            time_steps_done_before_fall = 0

        pygame.display.update()


# Where magic happens...
if __name__ == "__main__":
    game()
