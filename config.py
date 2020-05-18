#!/bin/python3.8
"""Global variables used to configure neccessary stuff within project"""
import pygame
# This file provides constans of game (windows size, colos within game etc.)
# You can simply set up to your own preference

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# For board where tetrominos fall:
BOARD_COLUMNS = 10 + 2 # +2 stands for left and right border lines
BOARD_ROWS = 22 + 1 # +1 stand for bottom border line

COLORS = {
    "lightblue" : (173, 216, 230),
    "red"       : (220, 20, 60),
    "darkred"   : (100, 10, 10),
    "black"     : (0, 0, 0),
    "orange"    : (255, 165, 0)
}


# Sizes within game:
BLOCK_SIZE = 18 #in pixels
BOARD_WIDTH = BLOCK_SIZE * (BOARD_COLUMNS+1) #with one border row on the bottom
BOARD_HEIGHT = BLOCK_SIZE * (BOARD_ROWS+2) #with two borders on left and right


# For drawing screen, gameboard etc.
BOARD_WITH_BORDER_COORDS = {
    "left" : (SCREEN_WIDTH / 2 - BOARD_WIDTH / 2),
    "top"  : (SCREEN_HEIGHT / 2 - BOARD_HEIGHT / 2),
}

GAME_BOARD_COORDS = {
    "left" : BOARD_WITH_BORDER_COORDS["left"] + BLOCK_SIZE,
    "top"  : BOARD_WITH_BORDER_COORDS["top"]
}

def pre_configure_window():
    """Configure whole stuff around game"""
    pygame.display.set_caption("Tetris")
