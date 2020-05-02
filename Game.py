#!/bin/python3.8
"Simple Tetris-inspired game written with Python and PyGame"
import math
import time
import pygame
from config import *



def debug_board(buf):
    """Used in console to check if everythings is drawing fine"""
    


def draw_gameboard(screen, board, color):
    """Drawing gameboard"""
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem == 1:
                pygame.draw.rect(screen, color, (game_board_coons["left"] + j * block_size, \
                game_board_coons["top"] + i * block_size, block_size, block_size))



def draw_bufor(screen, bufor, top_y, left_x):
    """Draw 4 x 4 bufor with currently falling tetromino"""
    print("Left x = ", left_x, " block sajz", block_size)
    current_top = (top_y * block_size) + game_board_coons["top"]
    
    current_left = (left_x * block_size) + game_board_coons["left"]

    for i, row in enumerate(bufor):
        for j, elem in enumerate(row):
            if elem == 1:
                pygame.draw.rect(screen, colors["lightblue"], \
                (current_left+(j*block_size), current_top+(i*block_size), block_size, block_size))


def pre_configure_window():
    """Configure whole stuff around game"""
    pygame.display.set_caption("Tetris")
br



#--------------MAIN GAME-----------------------------------------------------
def game():
    """Runs whole game"""
    pygame.init()
    pre_configure_window()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Drawing base of game screen
    screen.fill(colors["darkred"])
    pygame.draw.rect(screen, colors["black"], \
    (board_with_border_coons["left"], board_with_border_coons["top"], board_width, board_height))
    pygame.draw.rect(screen, colors["red"], \
    (game_board_coons["left"], \
    game_board_coons["top"], board_width-2*block_size, board_height-block_size))


    game_over = False
    game_single_frame = 0.5
    time_steps_done_before_fall = 0
    time_steps_to_fall_bufor = 20

    bufor_top = 0
    bufor_left = math.floor(BOARD_COLUMNS / 2)-4

    bufor = TETROMINOS[1]
    debug_board(bufor)

    while not game_over:
        pygame.draw.rect(screen, colors["red"], (
            game_board_coons["left"], game_board_coons["top"], \
            board_width - 2 * block_size, board_height - block_size))

        time.sleep(game_single_frame) # sleeps for every 50 miliseconds
        print(bufor_top, bufor_left)
        draw_bufor(screen, bufor, bufor_top, bufor_left)

        print("game_board_coons - y=", game_board_coons["top"], ", x=", game_board_coons["left"])
        print("bufor - y = ", bufor_top, ", x= ", bufor_left)

        bufor_left, bufor_top = move(bufor_left, bufor_top)

        time_steps_done_before_fall = time_steps_done_before_fall + 1
        if time_steps_done_before_fall == time_steps_to_fall_bufor:
            bufor_top = bufor_top + 1
            time_steps_done_before_fall = 0

        #draw_gameboard(screen, gameboard, colors["lightblue"])


        pygame.display.update()



game()
print(block_size)