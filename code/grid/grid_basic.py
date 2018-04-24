
class grid(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def makegrid(self):
		grid = []
		row = []
		for i in range(self.width):
			row.append('0')
		for i in range(self.height):
			grid.append(row)
		for i in range(len(grid)):
			print(grid[i])

class Huis(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.position = [x,y]

class woning(Huis):
	def __init__(self, hoogte, breedte, prijs, vrijstaand, percentage):
		super().__init__(x = 0, y = 0)
		self.hoogte = hoogte
		self.breedte = breedte
		self.prijs = prijs
		self.vrijstaand = vrijstaand
		self.percentage = percentage

	def printhuis(self):
		print("The house is {} by {} and worth {}".format(self.hoogte, self.breedte, self.prijs))

def build_house(grid, woning):
	for i in range(grid.width):
		for j in range(grid.height):
			if [i][j] == '0':
				for i in range(self.hoogte):
					for j in range(self.breedte):
						[i][j] = 'x'



eensgezins = woning(2, 2, 285000, 2, 1.03)
eensgezins.printhuis()

land = grid(32, 36)
land.makegrid()

build_house(land, eensgezins)
