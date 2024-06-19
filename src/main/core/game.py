from .grid import Grid


class Game:

	# === Attributes ===

	__SIZE: int = 15
	__grid: Grid


	# === Constructors ===

	def __init__(self):
		self.__grid = Grid(self.__SIZE)
		self.__grid.add_apple(12, 7)


	# === Getters ===

	def get_size(self) -> int:
		"""
		Returns the size of the grid.

		Returns:
			int: The size of the grid.
		"""
		return self.__SIZE
	
	def get_apple_count(self) -> int: # TODO
		return 0
	
	def has_apple(self, x: int, y: int) -> bool:
		return self.__grid.has_apple(x, y)
	
	def is_over(self) -> bool: # TODO
		"""
		Returns whether the game is over.

		Returns:
			bool: Whether the game is over.
		"""
		return False
	

	# === Public Methods ===
	
	def update(self): # TODO
		"""
		Updates the game state.
		"""
		pass