class Cell:
	def __init__(self, alive):
		self.alive = alive
		self.neighbors = int()
		self.stay = bool()
		self.setAlive = bool()
		self.setDead = bool()

	def __str__(self):
		return str(int(self.alive))