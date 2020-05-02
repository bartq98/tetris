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
		self.