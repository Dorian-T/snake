import pygame

from core.snake import Snake


class SnakeRenderer:

	# === Attributes ===

	__cell_size: int
	__screen: pygame.Surface

	__eyes: pygame.Surface


	# === Constructors and Destructors ===

	def __init__(self, cell_size: int, screen: pygame.Surface):
		self.__cell_size = cell_size
		self.__screen = screen

		self.__eyes = pygame.transform.scale(pygame.image.load("assets/eyes.png"), (self.__cell_size // 2, self.__cell_size))


	# === Public Methods ===

	def draw(self, snake: Snake):
		# self.__screen.fill("#4f7ded", pygame.Rect(self.__cell_size * (snake.get_head()[0] + 0.5), self.__cell_size * (snake.get_head()[1] + 0.5) + 70, self.__cell_size, self.__cell_size))
		self.__draw_snake_head(snake)

		for i in range(1, len(snake.get_body())):
			self.__screen.fill("#4f7ded", pygame.Rect(self.__cell_size * (snake.get_body()[i][0] + 0.5), self.__cell_size * (snake.get_body()[i][1] + 0.5) + 70, self.__cell_size, self.__cell_size))


	# === Private Methods ===

	def __draw_snake_head(self, snake):
		head = snake.get_head()
		direction = snake.get_direction()

		self.__screen.fill("#4f7ded", pygame.Rect(self.__cell_size * (head[0] + 0.5), self.__cell_size * (head[1] + 0.5) + 70, self.__cell_size, self.__cell_size))

		if direction == 0:
			self.__screen.blit(pygame.transform.rotate(self.__eyes, 90), (self.__cell_size * (head[0] + 0.5), self.__cell_size * (head[1] + 1) + 70))
		elif direction == 1:
			self.__screen.blit(self.__eyes, (self.__cell_size * (head[0] + 0.5), self.__cell_size * (head[1] + 0.5) + 70))
		elif direction == 2:
			self.__screen.blit(pygame.transform.rotate(self.__eyes, 270), (self.__cell_size * (head[0] + 0.5), self.__cell_size * (head[1] + 0.5) + 70))
		elif direction == 3:
			self.__screen.blit(pygame.transform.rotate(self.__eyes, 180), (self.__cell_size * (head[0] + 1), self.__cell_size * (head[1] + 0.5) + 70))