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