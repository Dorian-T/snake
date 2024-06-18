class Cell:
	apple: bool

	def __init__(self):
		self.apple = False

	def __str__(self):
		return "O" if self.apple else "."