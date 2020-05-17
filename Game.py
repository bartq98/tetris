#!/bin/python3.8
"Simple Tetris-inspired game written with Python and PyGame"
import math
import time
import pygame
from config import *
import Tetromino
import Gameboard

def game():
	"""Runs whole game"""
	pygame.init()
	pre_configure_window()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Drawing base of game screen
	screen.fill(COLORS["darkred"])

	# pygame.draw.rect(screen, colors["black"], \
	# (board_with_border_coons["left"], board_with_border_coons["top"], board_width, board_height))
	# pygame.draw.rect(screen, colors["red"], \
	# (game_board_coons["left"], \
	# game_board_coons["top"], board_width-2*block_size, board_height-block_size))


	game_over = False
	game_single_frame = 0.2
	time_steps_done_before_fall = 0
	time_steps_to_fall_bufor = 30

	bufor = Tetromino.Tetromino("I", 0, 0)
	
	gameboard = Gameboard.Gameboard()
	gameboard.debug_board(True)


	while not game_over:
		
		gameboard.draw_gameboard(screen)
		time.sleep(game_single_frame) # sleeps for every 50 miliseconds -> change to PyGame version delay() or 
		bufor.move(gameboard)

		bufor.debug_draw_bufor(screen)

		time_steps_done_before_fall += 1
		if time_steps_done_before_fall == time_steps_to_fall_bufor:
			bufor.fall_down()
			time_steps_done_before_fall = 0

		pygame.display.update()



game()
# print(block_size)