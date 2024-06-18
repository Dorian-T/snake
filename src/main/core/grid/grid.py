from typing import List
from .cell import Cell


class Grid:
	"""
	Represents a grid for the snake game.

	Attributes:
		size (int): The size of the grid.
		tab (List[List[int]]): The grid represented as a 2D list.
	"""

	size: int
	tab: List[List[Cell]]

	def __init__(self, size: int):
		self.size = size
		self.tab = [[Cell() for _ in range(size)] for _ in range(size)]

	def __str__(self):
		"""
		Returns a string representation of the grid.

		Returns:
			str: The string representation of the grid.
		"""
		return "\n".join([" ".join([str(cell) for cell in row]) for row in self.tab])
