import pygame
from pygame import font

from core.game import Game
from .grid_renderer import GridRenderer
from .menu import Menu
from .snake_renderer import SnakeRenderer


class Window:

	# === Attributes ===

	__game: Game
	__cell_size: int

	__screen: pygame.Surface
	__clock: pygame.time.Clock

	__snake_renderer: SnakeRenderer
	__grid_renderer: GridRenderer
	__menu: Menu


	# === Constructors and Destructors ===

	def __init__(self, game: Game):
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

	def __del__(self):
		pygame.quit()


	# === Public Methods ===

	def draw(self):
		self.__screen.fill("#578a34")
  
		self.__grid_renderer.draw(self.__game.get_grid(), self.__game.get_apple_count())
		self.__snake_renderer.draw(self.__game.get_snake())

		pygame.display.flip()
		self.__clock.tick(60)

	def draw_menu(self) -> bool:
		return self.__menu.draw(0, 0) # TODO: Add record

	def draw_game_over(self) -> bool:
		return self.__menu.draw(self.__game.get_apple_count(), 0) # TODO: Add record