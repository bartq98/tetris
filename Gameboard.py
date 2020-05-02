from config import *

class Gameboard:
	
	fields = [[]]

	def initialize_board(self):
		# When start all fields are set to 0 (except boundaries set which are set to -1)
		fields = [[0 for i in range(0, BOARD_COLUMNS)] for j in range(0, BOARD_ROWS)]
		# Setting bounds to -1
		for i in range(0, BOARD_ROWS-1):
			for j in range(0, BOARD_COLUMNS):
				if j in (0, BOARD_COLUMNS-1):
					fields[i][j] = -1

	def debug_board(self, print_coons):
		if print_coons:
			for i, row in enumerate(self.fields):
				for j, elem in enumerate(row):
					print("[",i,"][",j,"]=", elem, sep="", end=",")
				print("")
			print("----------------")
		else:
			for row in self.fields:
				for elem in row:
					print(elem, end=",")
				print("")
			print("----------------")