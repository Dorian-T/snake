from .grid.grid import Grid


class Game:
	SIZE: int = 15
	grid: Grid

	def __init__(self):
		self.grid = Grid(self.SIZE)

	def __str__(self):
		"""
		Returns a string representation of the game.

		Returns:
			str: The string representation of the game.
		"""
		return str(self.grid)
	
	def is_over(self) -> bool: # TODO
		"""
		Returns whether the game is over.

		Returns:
			bool: Whether the game is over.
		"""
		return False
	
	def update(self): # TODO
		"""
		Updates the game state.
		"""
		pass