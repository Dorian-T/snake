import pygame

from .grid import Grid
from .snake import Snake


class Game:

	# === Attributes ===

	__SIZE: int = 15
	__grid: Grid
	__snake: Snake


	# === Constructors ===

	def __init__(self):
		self.__grid = Grid(self.__SIZE)
		self.__grid.add_apple(12, 7)
		self.__snake = Snake(3, 7, 3)


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
	
	def get_snake(self) -> Snake:
		return self.__snake
	
	def is_over(self) -> bool: # TODO
		"""
		Returns whether the game is over.

		Returns:
			bool: Whether the game is over.
		"""
		return False
	

	# === Public Methods ===

	def handle_key(self, key: int):
		if key == pygame.K_UP or key == pygame.K_z:
			self.__snake.set_direction(0)
			print("up")
		elif key == pygame.K_RIGHT or key == pygame.K_d:
			self.__snake.set_direction(1)
			print("right")
		elif key == pygame.K_DOWN or key == pygame.K_s:
			self.__snake.set_direction(2)
			print("down")
		elif key == pygame.K_LEFT or key == pygame.K_q:
			self.__snake.set_direction(3)
			print("left")
	
	def update(self): # TODO
		"""
		Updates the game state.
		"""
		pass