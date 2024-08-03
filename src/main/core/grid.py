from typing import List
import random


class Grid:

	# === Attributes ===

	__tab: List[List[bool]]


	# === Constructors ===

	def __init__(self, size: int):
		"""
		Initializes the grid.

		Args:
			size (int): The size of the grid.
		"""
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

	def remove_apple(self, x: int, y: int):
		"""
		Removes an apple from the grid.

		Args:
			x (int): The x-coordinate of the apple.
			y (int): The y-coordinate of the apple.
		"""
		self.__tab[y][x] = False

	def add_random_apple(self):
		"""
		Adds an apple to a random empty cell of the grid.
		"""
		self.add_apple(random.randint(0, len(self.__tab[0]) - 1), random.randint(0, len(self.__tab) - 1))