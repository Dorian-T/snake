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
	clock = pygame.time.Clock()

	frame_counter = 0

	while not game.is_over():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				game.handle_key(event.key)

		frame_counter += 1
		if frame_counter == 8:
			game.update()
			window.draw()
			frame_counter = 0

		clock.tick(60) # 15 cases en 2 secondes
	
	print("Game Over")
	pygame.quit()

if __name__ == "__main__":
	main()