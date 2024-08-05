import sys
from pathlib import Path
import pygame
sys.path.append(str(Path(__file__).resolve().parent))

from core.game import Game
from display.window import Window


def main():
	"""
	The main function of the game.
	"""
	pygame.init()
	game = Game()
	window = Window(game)
	run(game, window)

def run(game: Game, window: Window):
	"""
	Runs the game.

	Args:
		game (Game): The game.
		window (Window): The window.
	"""

	record = 0
	running = True

	while running:
		# Main menu
		window.draw(record)
		if not window.draw_menu(record):
			break

		# Game
		game.reset()
		clock = pygame.time.Clock()
		frame_counter = 0
		start_to_move = False
		window.draw(record)
		while not game.is_over():
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					break
				elif event.type == pygame.KEYDOWN:
					start_to_move = True
					game.handle_key(event.key)

			if not running:
				break
			
			if start_to_move:
				frame_counter += 1
				if frame_counter == 8:
					game.update()
					window.draw(record)
					frame_counter = 0

			clock.tick(60) # 15 cases en 2 secondes

		# Game over
		record = max(game.get_apple_count(), record)

	# Quit
	pygame.quit()


if __name__ == "__main__":
	main()