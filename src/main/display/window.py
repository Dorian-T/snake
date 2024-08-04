import pygame
from pygame import font

from core.game import Game
from .grid_renderer import GridRenderer
from .snake_renderer import SnakeRenderer


class Window:

	# === Attributes ===

	__game: Game
	__cell_size: int

	__screen: pygame.Surface
	__clock: pygame.time.Clock

	__snake_renderer: SnakeRenderer
	__grid_renderer: GridRenderer


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

	def __del__(self):
		pygame.quit()


	# === Public Methods ===

	def draw(self):
		self.__screen.fill("#578a34")
  
		self.__grid_renderer.draw(self.__game.get_grid(), self.__game.get_apple_count())
		self.__snake_renderer.draw(self.__game.get_snake())

		pygame.display.flip()
		self.__clock.tick(60)

	def draw_game_over(self): # TODO: move into a Menu class
		x = self.__screen.get_width() // 2 - 150
		y = self.__screen.get_height() // 2 - 158

		self.__screen.fill("#4dc1f9", pygame.Rect(x, y, 300, 366))
		picture = pygame.image.load("assets/menu.png")
		self.__screen.blit(picture, (x, y))

		apple = pygame.transform.scale(pygame.image.load("assets/apple.png"), (60, 60))
		self.__screen.blit(apple, (x + 60, y + 60))
		text_surface = pygame.font.Font(None, 48).render(str(self.__game.get_apple_count()), True, "white")
		text_rect = text_surface.get_rect()
		text_rect.centerx = x + 90
		text_rect.y = y + 120
		self.__screen.blit(text_surface, text_rect)

		pygame.display.flip()

		pygame.time.wait(3000)