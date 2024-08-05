import pygame
from pygame import font

from core.game import Game
from .grid_renderer import GridRenderer
from .menu import Menu
from .snake_renderer import SnakeRenderer


class Window:
	"""
	A class responsible for rendering the game.

	Attributes:
		__game (Game): The game.
		__cell_size (int): The size of a cell.

		__screen (pygame.Surface): The screen.
		__clock (pygame.time.Clock): The clock.

		__snake_renderer (SnakeRenderer): The snake renderer.
		__grid_renderer (GridRenderer): The grid renderer.
		__menu (Menu): The menu.
	"""


	# === Attributes ===

	__game: Game
	__cell_size: int

	__screen: pygame.Surface
	__clock: pygame.time.Clock

	__snake_renderer: SnakeRenderer
	__grid_renderer: GridRenderer
	__menu: Menu


	# === Constructors ===

	def __init__(self, game: Game):
		"""
		Initializes the window.

		Args:
			game (Game): The game.
		"""

		# Initialize attributes
		self.__game = game
		self.__cell_size = min(pygame.display.Info().current_w, pygame.display.Info().current_h - 100) // (self.__game.get_size() + 1)

		# Initialize pygame
		self.__screen = pygame.display.set_mode((self.__cell_size * (self.__game.get_size() + 1), self.__cell_size * (self.__game.get_size() + 1) + 70))
		pygame.display.set_caption("Snake.py")
		self.__clock = pygame.time.Clock()

		# Initialize renderers
		self.__snake_renderer = SnakeRenderer(self.__cell_size, self.__screen)
		self.__grid_renderer = GridRenderer(self.__cell_size, self.__screen)
		self.__menu = Menu(self.__screen)


	# === Public Methods ===

	def draw(self, record: int):
		"""
		Draws the game.

		Args:
			record (int): The record.
		"""

		self.__screen.fill("#578a34")
  
		self.__grid_renderer.draw(self.__game.get_grid(), self.__game.get_apple_count(), record)
		self.__snake_renderer.draw(self.__game.get_snake())

		pygame.display.flip()

	def draw_menu(self, record: int) -> bool:
		"""
		Draws the menu.

		Args:
			record (int): The record.

		Returns:
			bool: Whether the game should start.
		"""

		return self.__menu.draw(self.__game.get_apple_count(), record)