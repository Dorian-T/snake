import pygame

from core.grid import Grid


class GridRenderer:

	# === Attributes ===

	__cell_size: int
	__screen: pygame.Surface

	__apple_grid: pygame.Surface
	__apple_header: pygame.Surface


	# === Constructors and Destructors ===

	def __init__(self, cell_size: int, screen: pygame.Surface):
		self.__cell_size = cell_size
		self.__screen = screen

		apple_image = pygame.image.load("assets/apple.png")
		self.__apple_grid = pygame.transform.scale(apple_image, (self.__cell_size, self.__cell_size))
		self.__apple_header = pygame.transform.scale(apple_image, (40, 40))


	# === Public Methods ===

	def draw(self, grid: Grid, apple_count: int):
		self.__draw_header(grid, apple_count)
		self.__draw_grid(grid)


	# === Private Methods ===

	def __draw_header(self, grid: Grid, apple_count: int):
		self.__screen.fill("#4a752c", pygame.Rect(0, 0, self.__cell_size * (grid.get_size() + 1), 70))
		self.__screen.blit(self.__apple_header, (20, 15))
		self.__screen.blit(pygame.font.Font(None, 48).render(str(apple_count), True, "white"), (70, 23))

	def __draw_grid(self, grid: Grid):
		for y in range(grid.get_size()):
			for x in range(grid.get_size()):
				color = "#aad751" if (x + y) % 2 == 0 else "#a2d149"
				self.__screen.fill(color, pygame.Rect(self.__cell_size * (x + 0.5), self.__cell_size * (y + 0.5) + 70, self.__cell_size, self.__cell_size))
				if grid.has_apple(x, y):
					self.__screen.blit(self.__apple_grid, (self.__cell_size * (x + 0.5), self.__cell_size * (y + 0.5) + 70))