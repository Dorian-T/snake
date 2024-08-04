from typing import List, Tuple

from .grid import Grid


class Snake:
	"""
	A class representing the snake in the game.

	Attributes:
		__direction (int): The direction of the snake.
		__body (List[Tuple[int, int]]): The body of the snake.
	"""


	# === Attributes ===

	__direction: int
	__body: List[Tuple[int, int]]


	# === Constructors ===

	def __init__(self, x: int, y: int, size: int):
		"""
		Initializes the snake.

		Args:
			x (int): The x-coordinate of the head.
			y (int): The y-coordinate of the head.
			size (int): The size of the snake.
		"""

		self.__direction = 1
		self.__body = []
		for i in range(size):
			self.__body.append((
				x + i if self.__direction == 3 else x - i if self.__direction == 1 else x,
				y + i if self.__direction == 0 else y - i if self.__direction == 2 else y
			))


	# === Public Methods ===

	def get_direction(self) -> int:
		"""
		Returns the direction of the snake.

		0: up
		1: right
		2: down
		3: left

		Returns:
			int: The direction of the snake.
		"""

		return self.__direction

	def get_body(self) -> List[Tuple[int, int]]:
		"""
		Returns the body of the snake.

		Returns:
			List[Tuple[int, int]]: The body of the snake.
		"""

		return self.__body

	def get_head(self) -> Tuple[int, int]:
		"""
		Returns the head of the snake.

		Returns:
			Tuple[int, int]: The head of the snake.
		"""

		return self.__body[0]

	def set_direction(self, direction: int):
		"""
		Sets the direction of the snake.

		0: up
		1: right
		2: down
		3: left

		Args:
			direction (int): The direction of the snake.
		"""

		if direction % 2 != self.__direction % 2:
			self.__direction = direction

	def move(self, grid: Grid, size: int) -> int:
		"""
		Moves the snake.

		Args:
			grid (Grid): The grid.
			size (int): The size of the grid.

		Returns:
			int: -1 if the snake has bitten itself or hit a wall, 1 if the snake has eaten an apple, 0 otherwise.
		"""

		head = self.__body[0]
		new_head = None

		if self.__direction == 0:
			new_head = (head[0], head[1] - 1)
		elif self.__direction == 1:
			new_head = (head[0] + 1, head[1])
		elif self.__direction == 2:
			new_head = (head[0], head[1] + 1)
		elif self.__direction == 3:
			new_head = (head[0] - 1, head[1])

		# Check if the snake has bitten itself or hit a wall
		if new_head in self.__body or new_head[0] < 0 or new_head[0] >= size or new_head[1] < 0 or new_head[1] >= size:
			return -1
		else:
			self.__body.insert(0, new_head)
			# If the snake has not eaten an apple, remove the last part of its body
			if grid.has_apple(new_head[0], new_head[1]):
				grid.remove_apple(self.__body[0][0], self.__body[0][1])
				grid.add_random_apple()
				return 1
			else:
				self.__body.pop()
			return 0