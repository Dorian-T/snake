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
	run(game, window)

def run(game: Game, window: Window):
	record = 0

	while True:
		# Main menu
		window.draw()
		if not window.draw_menu(record):
			break

		# Game
		game.reset()
		clock = pygame.time.Clock()
		frame_counter = 0
		start_to_move = False
		window.draw()
		while not game.is_over():
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					start_to_move = True
					game.handle_key(event.key)
			
			if start_to_move:
				frame_counter += 1
				if frame_counter == 8:
					game.update()
					window.draw()
					frame_counter = 0

			clock.tick(60) # 15 cases en 2 secondes

		# Game over
		record = game.get_apple_count() if game.get_apple_count() > record else record

	# Quit
	pygame.quit()
	sys.exit()


if __name__ == "__main__":
	main()