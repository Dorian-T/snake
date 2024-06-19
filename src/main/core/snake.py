from typing import List, Tuple


class Snake:
	# === Attributes ===

	__direction: int
	__x: int
	__y: int
	__body: List[Tuple[int, int]]

	# === Constructors ===

	def __init__(self, x: int, y: int, size: int):
		self.__direction = 1
		self.__x = x
		self.__y = y
		self.__body = []
		for i in range(size):
			self.__body.append((
				self.__x + i if self.__direction == 3 else self.__x - i if self.__direction == 1 else self.__x,
				self.__y + i if self.__direction == 0 else self.__y - i if self.__direction == 2 else self.__y
			))

	# === Public Methods ===

	def get_direction(self) -> int:
		return self.__direction

	def get_body(self) -> List[Tuple[int, int]]:
		return self.__body

	def get_head(self) -> Tuple[int, int]:
		return self.__body[0]

	def set_direction(self, direction: int):
		if direction % 2 != self.__direction % 2:
			self.__direction = direction

	def move(self, grow: bool):
		head = self.__body[0]
		if self.__direction == 0:
			self.__body.insert(0, (head[0] - 1, head[1]))
		elif self.__direction == 1:
			self.__body.insert(0, (head[0], head[1] - 1))
		elif self.__direction == 2:
			self.__body.insert(0, (head[0] + 1, head[1]))
		elif self.__direction == 3:
			self.__body.insert(0, (head[0], head[1] + 1))

		if not grow:
			self.__body.pop()