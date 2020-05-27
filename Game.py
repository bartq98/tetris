#!/bin/python3.8
"Simple Tetris-inspired game written with Python and PyGame"
import time
import random
import enum

import pygame

import config
import Tetromino
import Gameboard


def pre_configure_window(screen):
    """Configure whole stuff around game"""
    pygame.display.set_caption("Tetris")
    screen.fill(config.Color.DARKRED.value)


def game():
    """Runs whole game"""
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pre_configure_window(screen)

    # Drawing base of game screen
    # screen.fill(config.COLORS["darkred"])

    game_over = False

    buffer = Tetromino.Tetromino("I", 0, 0)
    gameboard = Gameboard.Gameboard()

    time_steps_done_before_fall = 0


    while not game_over:
        gameboard.draw_gameboard(screen) # only gameboard are redrawing in all frame
        time.sleep(config.GAME_SINGLE_FRAME_sec) # sleeps for every 50 miliseconds -> change to PyGame version delay() or
        buffer.move(gameboard)

        buffer.draw_buffer(screen)

        time_steps_done_before_fall += 1
        if time_steps_done_before_fall == config.TIME_STEPS_TO_FALL_BUFFER:
            has_falled = buffer.fall_down(gameboard)
            if has_falled:
                gameboard.add_blocks(buffer)
                buffer = Tetromino.Tetromino(random.choice(("I", "Z", "S")), 4, 0)
                gameboard.delete_lines()

            time_steps_done_before_fall = 0

        pygame.display.update()

# Where magic happens...
if __name__=="__main__":
    game()
