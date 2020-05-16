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
		self.current_y += 1

	def debug_x_y(self):
		print("Current coons. of buffer are [",self.current_y,"][", \
			self.current_x,"]", sep="")

	def move(self):
		"""Moves bufor by pressing keys"""
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.buffer = self.rotate_buffor(self.buffer)
				if event.key == pygame.K_LEFT:
					self.current_x -= 1
				if event.key == pygame.K_RIGHT:
					self.current_x += 1
				if event.key == pygame.K_DOWN:
					self.current_y += 1


	def detect_collision(self, board, key_pressed):
		"""Return True if buffer can move in specified direction, otherwise return False"""
		directions = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN]
		rotated = pygame.K_UP

		if key_pressed in directions:
			x_after_move = self.current_x + (1 if key_pressed == directions[0] else -1)
			y_after_move = self.current_y + (key_pressed == directions[3])
			buffer_after_move = list.copy(self.buffer)
		elif key_pressed is rotated:
			x_after_move = self.current_x
			y_after_move = self.current_y
			buffer_after_move = self.rotate_buffor(self.buffer)
		else:
			pass #if invalid key was pressed

		for i, row in enumerate(buffer_after_move):
			for j, elem in enumerate(row):
				if board[x_after_move+i][y_after_move+j] and \
					board[x_after_move+i][y_after_move+j] == buffer_after_move[i][j]:
					print("Can move!")
				else:
					print("Cannot move!")



	def draw_bufor(self, screen):
		"""Draw 4 x 4 bufor with currently falling tetromino"""
		
		# self.debug_x_y()

		# Calculate position of drawing
		rect_bufor_x = (self.current_x * block_size) + game_board_coons["left"]
		rect_bufor_y = (self.current_y * block_size) + game_board_coons["top"]
	
		for i, row in enumerate(self.buffer):
			for j, elem in enumerate(row):
				if elem == 1:
					pygame.draw.rect(screen, colors["lightblue"], \
					(rect_bufor_x+(j*block_size), rect_bufor_y+(i*block_size), block_size, block_size))