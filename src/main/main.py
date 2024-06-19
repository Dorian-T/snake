import sys
from pathlib import Path
import pygame
sys.path.append(str(Path(__file__).resolve().parent))

from core.game import Game
from display.window import Window


def main():
	pygame.init()
	game = Game()
	window = Window(game)

	while not game.is_over():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				game.handle_key(event.key)

		game.update()
		window.draw()

if __name__ == "__main__":
	main()