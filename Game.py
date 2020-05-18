#!/bin/python3.8
"Simple Tetris-inspired game written with Python and PyGame"
import time
import pygame
import config
import Tetromino
import Gameboard
import random

def game():
    """Runs whole game"""
    pygame.init()
    config.pre_configure_window()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

    # Drawing base of game screen
    screen.fill(config.COLORS["darkred"])

    game_over = False
    game_single_frame = 0.01
    time_steps_done_before_fall = 0
    time_steps_to_fall_bufor = 10

    bufor = Tetromino.Tetromino("I", 0, 0)
    gameboard = Gameboard.Gameboard()



    while not game_over:
        gameboard.draw_gameboard(screen)
        time.sleep(game_single_frame) # sleeps for every 50 miliseconds -> change to PyGame version delay() or
        bufor.move(gameboard)

        bufor.draw_bufor(screen)

        time_steps_done_before_fall += 1
        if time_steps_done_before_fall == time_steps_to_fall_bufor:
            has_falled = bufor.fall_down(gameboard)
            if has_falled:
                gameboard.add_blocks(bufor)
                bufor = Tetromino.Tetromino(random.choice(("I", "Z", "S")), 4, 0)
                gameboard.delete_lines()

            time_steps_done_before_fall = 0

        pygame.display.update()



game()
