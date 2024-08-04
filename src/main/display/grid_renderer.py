import pygame

from core.grid import Grid


class GridRenderer:
	"""
	A class responsible for rendering the grid.

	Attributes:
		__cell_size (int): The size of a cell.
		__screen (pygame.Surface): The screen.

		__apple_grid (pygame.Surface): The apple image for the grid.
		__apple_header (pygame.Surface): The apple image for the header.
		__trophy (pygame.Surface): The trophy image.
	"""


	# === Attributes ===

	__cell_size: int
	__screen: pygame.Surface

	__apple_grid: pygame.Surface
	__apple_header: pygame.Surface
	__trophy: pygame.Surface


	# === Constructors and Destructors ===

	def __init__(self, cell_size: int, screen: pygame.Surface):
		"""
		Initializes the grid renderer.

		Args:
			cell_size (int): The size of a cell.
			screen (pygame.Surface): The screen.
		"""

		self.__cell_size = cell_size
		self.__screen = screen

		apple_image = pygame.image.load("assets/apple.png")
		self.__apple_grid = pygame.transform.scale(apple_image, (self.__cell_size, self.__cell_size))
		self.__apple_header = pygame.transform.scale(apple_image, (40, 40))
		self.__trophy = pygame.transform.scale(pygame.image.load("assets/trophy.png"), (40, 40))


	# === Public Methods ===

	def draw(self, grid: Grid, apple_count: int, record: int):
		"""
		Draws the grid.

		Args:
			grid (Grid): The grid.
			apple_count (int): The number of apples eaten.
			record (int): The record.
		"""

		self.__draw_header(grid, apple_count, record)
		self.__draw_grid(grid)


	# === Private Methods ===

	def __draw_header(self, grid: Grid, apple_count: int, record: int):
		"""
		Draws the header.

		Args:
			grid (Grid): The grid.
			apple_count (int): The number of apples eaten.
			record (int): The record.
		"""

		self.__screen.fill("#4a752c", pygame.Rect(0, 0, self.__cell_size * (grid.get_size() + 1), 70))

		# Apple count
		self.__screen.blit(self.__apple_header, (20, 15))
		apple_font = pygame.font.Font(None, 48).render(str(apple_count), True, "white")
		apple_font_rect = apple_font.get_rect(topleft=(70, 23))
		self.__screen.blit(apple_font, apple_font_rect.topleft)

		# Record
		self.__screen.blit(self.__trophy, (apple_font_rect.right + 40, 15))
		self.__screen.blit(pygame.font.Font(None, 48).render(str(record), True, "white"), (apple_font_rect.right + 90, 23))

	def __draw_grid(self, grid: Grid):
		"""
		Draws the grid.

		Args:
			grid (Grid): The grid.
		"""

		for y in range(grid.get_size()):
			for x in range(grid.get_size()):
				color = "#aad751" if (x + y) % 2 == 0 else "#a2d149"
				self.__screen.fill(color, pygame.Rect(self.__cell_size * (x + 0.5), self.__cell_size * (y + 0.5) + 70, self.__cell_size, self.__cell_size))
				if grid.has_apple(x, y):
					self.__screen.blit(self.__apple_grid, (self.__cell_size * (x + 0.5), self.__cell_size * (y + 0.5) + 70))