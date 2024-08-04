import pygame

from core.game import Game

class Menu:

	# === Attributes ===

	__screen: pygame.Surface


	# === Constructors and Destructors ===

	def __init__(self, screen: pygame.Surface):
		self.__screen = screen


	# === Public Methods ===

	def draw(self, apple_count: int, record: int) -> bool:
		x = self.__screen.get_width() // 2 - 150
		y = self.__screen.get_height() // 2 - 158

		self.__draw_background(x, y)
		self.__draw_apple_count(x, y, apple_count)
		self.__draw_record(x, y, record)
		button = self.draw_play_button(x, y)

		pygame.display.flip()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return False
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					return True
				elif event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(event.pos):
					return True

	
	# === Private Methods ===

	def __draw_background(self, x: int, y: int):
		# Background
		overlay = pygame.Surface((self.__screen.get_width(), self.__screen.get_height()), pygame.SRCALPHA)
		overlay.fill((0, 0, 0, 128))
		self.__screen.blit(overlay, (0, 0))

		# Picture
		self.__screen.fill("#4dc1f9", pygame.Rect(x, y, 300, 366))
		picture = pygame.image.load("assets/menu.png")
		self.__screen.blit(picture, (x, y))

	def __draw_apple_count(self, x: int, y: int, apple_count: int):
		# Apple
		apple = pygame.transform.scale(pygame.image.load("assets/apple.png"), (60, 60))
		self.__screen.blit(apple, (x + 60, y + 60))

		# Text
		text_surface = pygame.font.Font(None, 48).render(str(apple_count), True, "white")
		text_rect = text_surface.get_rect()
		text_rect.centerx = x + 90
		text_rect.y = y + 120
		self.__screen.blit(text_surface, text_rect)

	def __draw_record(self, x: int, y: int, record: int):
		# Trophy
		trophy = pygame.transform.scale(pygame.image.load("assets/trophy.png"), (60, 60))
		self.__screen.blit(trophy, (x + 180, y + 60))

		# Text
		text_surface = pygame.font.Font(None, 48).render(str(record), True, "white")
		text_rect = text_surface.get_rect()
		text_rect.centerx = x + 210
		text_rect.y = y + 120
		self.__screen.blit(text_surface, text_rect)

	def draw_play_button(self, x: int, y: int) -> pygame.Rect:
		# Button
		rect = pygame.Rect(x, y + 376, 300, 48)
		self.__screen.fill("#1155cc", rect)

		# Play icon
		play_button = pygame.image.load("assets/play.svg")
		play_button_rect = play_button.get_rect()
		play_button_rect.x = x + 24
		play_button_rect.centery = y + 400
		self.__screen.blit(play_button, play_button_rect)

		# Text
		text_surface = pygame.font.Font(None, 32).render("Jouer", True, "white")
		text_rect = text_surface.get_rect()
		text_rect.center = (x + 150, y + 400)
		self.__screen.blit(text_surface, text_rect)

		return rect