
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


# STOND EERST IN GRID.PY MAAR WORDT NIET GEBRUIKT

		# iterate over coordinate list and select coordinates
		# for i in range(360):
		# 	for j in range(320):
		# 		if grid[j][i] == 'h':
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color = "#ffffbf")
		# 		elif grid[j][i] == 's':
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color = "#2c7bb6")
		# 		elif grid[j][i] == 'w':
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color ="#abd9e9")
		# 		else:
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color ="#fdae61")
