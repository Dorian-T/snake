from typing import List


class Grid:

	# === Attributes ===

	__tab: List[List[bool]]


	# === Constructors ===

	def __init__(self, size: int):
		self.__tab = [[False for _ in range(size)] for _ in range(size)]


	# === Public Methods ===

	def has_apple(self, x: int, y: int) -> bool:
		"""
		Returns whether there is an apple at the given coordinates.

		Args:
			x (int): The x-coordinate.
			y (int): The y-coordinate.

		Returns:
			bool: Whether there is an apple at the given coordinates.
		"""
		return self.__tab[y][x]

	def add_apple(self, x: int, y: int):
		"""
		Adds an apple to the grid.

		Args:
			x (int): The x-coordinate of the apple.
			y (int): The y-coordinate of the apple.
		"""
		self.__tab[y][x] = True