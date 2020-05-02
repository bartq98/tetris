#!/bin/python3.8
import pygame
# This file provides constans of game (windows size, colos within game etc.)
# You can simply set up to your own preference

SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 720

# For board where tetrominos fall:
BOARD_COLUMNS = 10 + 2 # +2 stands for left and right border lines
BOARD_ROWS    = 22 + 1 # +1 stand for bottom border line

colors = {
    "lightblue" : (173, 216, 230),
    "red"       : (220, 20, 60),
    "darkred"   : (100, 10, 10),
    "black"     : (0, 0, 0)
}


# Sizes within game:
block_size   = 18 #in pixels
board_width  = block_size * (BOARD_COLUMNS+1) #with one border row on the bottom
board_height = block_size * (BOARD_ROWS+2) #with two borders on left and right


# For drawing screen, gameboard etc.
board_with_border_coons = {
    "left" : (SCREEN_WIDTH / 2 - board_width / 2),
    "top"  : (SCREEN_HEIGHT / 2 - board_height / 2),
}

game_board_coons = {
    "left" : board_with_border_coons["left"] + block_size,
    "top"  : board_with_border_coons["top"]
}

def pre_configure_window():
    """Configure whole stuff around game"""
    pygame.display.set_caption("Tetris")
