
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

	
	def overlapping(self, cordinatelist, housecords):
		for i in range(housecords[0], (housecords[2])):
			for j in range(housecords[3], (housecords[1])):
				if cordinatelist[j][i] == "0":
					cordinatelist[j][i] = "y"
				else:
					# print(cordinatelist[j][i])
					return False
		return True

grids = makegrid()

cord = [1, 4, 3, 2]

overlaping(grids, cord)

print(grids)
