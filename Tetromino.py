from config import *
import pygame

class Tetromino:

	# top left corner coons. of 4x4 falling buffer
	current_x = 0
	current_y = 0

	# for holding information of type of currently falling tetromino
	buffer = [
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]
	]

	def __init__(self, type, x, y):
		self.current_x = x
		self.current_y = y

		# capital letters refers to shape of tetromino
		if type == "I":
			self.buffer = [
				[0, 0, 1, 0],
				[0, 0, 1, 0],
				[0, 0, 1, 0],
				[0, 0, 1, 0]
			]
		elif type == "Z":
			self.buffer = [
				[0, 0, 0, 0],
				[0, 1, 1, 0],
				[0, 0, 1, 1],
				[0, 0, 0, 0]
			]
		elif type == "S":
			self.buffer = [
				[0, 0, 0, 0],
				[0, 1, 1, 0],
				[1, 1, 0, 0],
				[0, 0, 0, 0]
			]
		elif type == "J":
			self.buffer = [
				[0, 0, 0, 0],
				[0, 1, 0, 0],
				[0, 1, 1, 1],
				[0, 0, 0, 0]
			]
		elif type == "L": 
			self.buffer = [
				[0, 0, 0, 0],
				[0, 0, 0, 1],
				[0, 1, 1, 1],
				[0, 0, 0, 0]
			]
		elif type == "T":
			self.buffer = [
				[0, 0, 0, 0],
				[0, 0, 1, 0],
				[0, 1, 1, 1],
				[0, 0, 0, 0]
			]
		elif type == "O":
			self.buffer = [
				[0, 0, 0, 0],
				[0, 1, 1, 0],
				[0, 1, 1, 0],
				[0, 0, 0, 0]
			]
		else:
			print("Invalid type of Tetromino!")
			print("Should throw execption!")
			self.buffer = [
				[1, 0, 0, 1],
				[0, 0, 0, 0],
				[0, 0, 0, 0],
				[1, 0, 0, 1]
			],


	def rotate_buffor(self, bufor):
		"""Roates bufor clockwise"""
		rotated_array = [
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		]

		for i in range(0, 4):
			for j in range(0, 4):
				rotated_array[i][j] = bufor[3-j][i] #12+i - (j*4)
		return rotated_array

	
	def fall_down(self):
		"""Moves buffer one block down"""
		print("Before:", self.current_y)
		self.current_y += 1
		print("After:", self.current_y)

	def debug_x_y(self):
		print("Current coons. of buffer are [",self.current_y,"][", \
			self.current_x,"]", sep="")



	def draw_bufor(self, screen):
		"""Draw 4 x 4 bufor with currently falling tetromino"""
		
		self.debug_x_y()

		# Calculate position of drawing
		rect_bufor_x = (self.current_x * block_size) + game_board_coons["left"]
		rect_bufor_y = (self.current_y * block_size) + game_board_coons["top"]
	
		for i, row in enumerate(self.buffer):
			for j, elem in enumerate(row):
				if elem == 1:
					pygame.draw.rect(screen, colors["lightblue"], \
					(rect_bufor_x+(j*block_size), rect_bufor_y+(i*block_size), block_size, block_size))