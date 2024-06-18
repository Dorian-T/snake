from core.game import Game
from display.window import Window

def main():
	game = Game()
	window = Window(game)

	while not game.is_over() and window.is_open():
		game.update()
		window.draw()

if __name__ == "__main__":
	main()