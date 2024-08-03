import math
import pygame

from core.game import Game


class Window:

	# === Attributes ===

	__game: Game
	__cell_size: int

	__screen: pygame.Surface
	__clock: pygame.time.Clock

	__apple_header: pygame.Surface
	__apple_grid: pygame.Surface
	__eyes: pygame.Surface


	# === Constructors and Destructors ===

	def __init__(self, game: Game):
		# Initialize attributes
		self.__game = game
		self.__cell_size = min(pygame.display.Info().current_w, pygame.display.Info().current_h - 100) // (self.__game.get_size() + 1)

		# Initialize pygame
		self.__screen = pygame.display.set_mode((self.__cell_size * (self.__game.get_size() + 1), self.__cell_size * (self.__game.get_size() + 1) + 70))
		pygame.display.set_caption("Snake.py")
		self.__clock = pygame.time.Clock()

		# Load assets
		apple_image = pygame.image.load("assets/apple.png")
		self.__apple_header = pygame.transform.scale(apple_image, (40, 40))
		self.__apple_grid = pygame.transform.scale(apple_image, (self.__cell_size, self.__cell_size))
		self.__eyes = pygame.transform.scale(pygame.image.load("assets/eyes.png"), (self.__cell_size // 2, self.__cell_size))

	def __del__(self):
		pygame.quit()


	# === Public Methods ===

	def draw(self):
		self.__screen.fill("#578a34")
  
		self.__draw_header()
		self.__draw_grid()
		self.__draw_snake()

		pygame.display.flip()
		self.__clock.tick(60)


	# === Private Methods ===

	def __draw_header(self):
		self.__screen.fill("#4a752c", pygame.Rect(0, 0, self.__cell_size * (self.__game.get_size() + 1), 70))
		self.__screen.blit(self.__apple_header, (20, 15))
		self.__screen.blit(pygame.font.Font(None, 48).render(str(self.__game.get_apple_count()), True, "white"), (70, 23))

	def __draw_grid(self):
		for y in range(self.__game.get_size()):
			for x in range(self.__game.get_size()):
				color = "#aad751" if (x + y) % 2 == 0 else "#a2d149"
				self.__screen.fill(color, pygame.Rect(self.__cell_size * (x + 0.5), self.__cell_size * (y + 0.5) + 70, self.__cell_size, self.__cell_size))
				if self.__game.has_apple(x, y):
					self.__screen.blit(self.__apple_grid, (self.__cell_size * (x + 0.5), self.__cell_size * (y + 0.5) + 70))

	def __draw_snake(self):
		snake = self.__game.get_snake()

		# self.__screen.fill("#4f7ded", pygame.Rect(self.__cell_size * (snake.get_head()[0] + 0.5), self.__cell_size * (snake.get_head()[1] + 0.5) + 70, self.__cell_size, self.__cell_size))
		self.__draw_snake_head(snake)

		for i in range(1, len(snake.get_body())):
			self.__screen.fill("#4f7ded", pygame.Rect(self.__cell_size * (snake.get_body()[i][0] + 0.5), self.__cell_size * (snake.get_body()[i][1] + 0.5) + 70, self.__cell_size, self.__cell_size))

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


# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True
# dt = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill("purple")

#     pygame.draw.circle(screen, "red", player_pos, 40)

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         player_pos.y -= 300 * dt
#     if keys[pygame.K_s]:
#         player_pos.y += 300 * dt
#     if keys[pygame.K_a]:
#         player_pos.x -= 300 * dt
#     if keys[pygame.K_d]:
#         player_pos.x += 300 * dt

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     # limits FPS to 60
#     # dt is delta time in seconds since last frame, used for framerate-
#     # independent physics.
#     dt = clock.tick(60) / 1000

# pygame.quit()