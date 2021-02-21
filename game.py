import time

from cell import Cell

class Game:
	def __init__(self, size, delay):
		self.size = size
		self.running = True
		self.ticks = int()
		self.delay = delay
		self._generateEmptyGrid()

	# Y is the array (1st index)
	# X is value in the array (2nd index)

	def _generateEmptyGrid(self):
		self.cells = [[Cell(False) for x in range(self.size)] for y in range(self.size)] 

	def _updateCells(self):
		for y in range(self.size):
			for x in range(self.size):
				currentCell = self.cells[y][x]
				currentCell.neighbors = 0
				self._updateVerticalNeighbors(x, y)
				self._updateHorizontalNeighbors(x, y)
				self._updateDiagonalNeighbors(x, y)
				if currentCell.neighbors < 2 or currentCell.neighbors > 3:
					currentCell.setDead = True

				elif currentCell.neighbors == 3:
					currentCell.setAlive = True

				elif currentCell.neighbors == 2:
					currentCell.stay = True

		for y in range(self.size):
			for x in range(self.size):
				currentCell = self.cells[y][x]
				if not self.cells[y][x].stay:
					if self.cells[y][x].setAlive:
						self.cells[y][x].alive = True
						self.cells[y][x].setAlive = False
					if self.cells[y][x].setDead:
						self.cells[y][x].alive = False
						self.cells[y][x].setDead = False
				else:
					self.stay = False

					

	def _updateVerticalNeighbors(self, x, y):
		currentCell = self.cells[y][x]	
		if y != 0:
			if self.cells[y - 1][x].alive:
				currentCell.neighbors += 1

		if y != self.size - 1:
			if self.cells[y + 1][x].alive:
				currentCell.neighbors += 1

	def _updateHorizontalNeighbors(self, x, y):
		currentCell = self.cells[y][x]
		if x != 0:
			if self.cells[y][x - 1].alive:
				currentCell.neighbors += 1

		if x != self.size - 1:
			if self.cells[y][x + 1].alive:
				currentCell.neighbors += 1

	def _updateDiagonalNeighbors(self, x, y):
		currentCell = self.cells[y][x]
		if y != 0 and x != 0:
			if self.cells[y - 1][x - 1].alive:
				currentCell.neighbors += 1
		if y != 0 and x != self.size - 1:
			if self.cells[y - 1][x + 1].alive:
				currentCell.neighbors += 1
		if y != self.size - 1 and x != 0:
			if self.cells[y + 1][x - 1].alive:
				currentCell.neighbors += 1
		if y != self.size - 1 and x != self.size - 1:
			if self.cells[y + 1][x + 1].alive:
				currentCell.neighbors += 1
		

	def showCells(self):
		for y in range(self.size):
			print()
			for x in range(self.size):
				print(self.cells[y][x], end=' ')
		print("\n\n")

	def setCellAlive(self, x, y):
		self.cells[y][x].alive = True 


	def run(self):
		while self.running:
			self.ticks += 1
			self._updateCells()
			self.showCells()
			currentCell = self.cells[2][2]
			time.sleep(self.delay)

				
if __name__ == '__main__':
	game = Game(10, 2)
	game.setCellAlive(1, 1)
	game.setCellAlive(2, 1)
	game.setCellAlive(1, 2)
	game.setCellAlive(4, 3)
	game.setCellAlive(4, 4)
	game.setCellAlive(3, 4)
	game.setCellAlive(7, 2)
	game.setCellAlive(7, 3)
	game.setCellAlive(7, 4)
	game.showCells()
	game.run()