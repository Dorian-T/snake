import pygame

from .grid import Grid
from .snake import Snake


class Game:
	"""A class representing the game state.

	Attributes:
		__SIZE (int): The size of the grid.
		__grid (Grid): The grid.
		__snake (Snake): The snake.
		__game_over (bool): Whether the game is over.
		__apple_count (int): The number of apples eaten.
	"""


	# === Attributes ===

	__SIZE: int = 15
	__grid: Grid
	__snake: Snake
	__game_over: bool
	__apple_count: int


	# === Constructors ===

	def __init__(self):
		"""
		Initializes the Game object by calling the __init method.
		"""

		self.__init()

	def __init(self):
		"""
		Initializes the Game object.
		"""

		self.__grid = Grid(self.__SIZE)
		self.__grid.add_apple(12, 7)
		self.__snake = Snake(3, 7, 3)
		self.__game_over = False
		self.__apple_count = 0


	# === Getters ===

	def get_grid(self) -> Grid:
		"""
		Returns the grid.

		Returns:
			Grid: The grid.
		"""

		return self.__grid

	def get_size(self) -> int:
		"""
		Returns the size of the grid.

		Returns:
			int: The size of the grid.
		"""
		return self.__SIZE
	
	def get_apple_count(self) -> int:
		"""
		Returns the number of apples collected in the game.

		Returns:
			int: The number of apples collected.
		"""

		return self.__apple_count
	
	def has_apple(self, x: int, y: int) -> bool:
		"""
		Returns whether the grid has an apple at the given position.

		Args:
			x (int): The x-coordinate.
			y (int): The y-coordinate.

		Returns:
			bool: Whether the grid has an apple at the given position
		"""

		return self.__grid.has_apple(x, y)
	
	def get_snake(self) -> Snake:
		"""
		Returns the snake.

		Returns:
			Snake: The snake.
		"""

		return self.__snake
	
	def is_over(self) -> bool:
		"""
		Returns whether the game is over.

		Returns:
			bool: Whether the game is over.
		"""

		return self.__game_over
		

	# === Public Methods ===

	def handle_key(self, key: int):
		"""
		Handles the key event.

		Args:
			key (int): The key event.
		"""

		if key == pygame.K_UP or key == pygame.K_z:
			self.__snake.set_direction(0)
		elif key == pygame.K_RIGHT or key == pygame.K_d:
			self.__snake.set_direction(1)
		elif key == pygame.K_DOWN or key == pygame.K_s:
			self.__snake.set_direction(2)
		elif key == pygame.K_LEFT or key == pygame.K_q:
			self.__snake.set_direction(3)

	def update(self):
		"""
		Updates the game state.
		"""

		result = self.__snake.move(self.__grid, self.__SIZE)
		if result == -1:
			self.__game_over = True
		elif result == 1:
			self.__apple_count += 1

	def reset(self):
		"""
		Resets the game state by calling the __init method.
		"""

		self.__init()