
class grid(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def hoimakegrid(self):
		grid = [["0"]*self.width for x in range(self.height)]
		# grid = []
		# row = []
		# for x in range(self.width):
		# 	grid.append([])
		# for li in range(gird)

		# for y in range(self.height):
		# 	grid.append(row)
		# # for i in range(len(grid)):
		# # 	print(grid[i])
		return grid

	
	def hoioverlaping(self, cordinatelist, housecords):
		for i in range(housecords[0], (housecords[2])):
			for j in range(housecords[3], (housecords[1])):
				print(cordinatelist[j][i], j, i)
				if cordinatelist[j][i] == "0":
					cordinatelist[j][i] = "y"
				else:
					print("vol{}{}".format(j, i))
		return True

grids = grid(40, 50).hoimakegrid()

cord = [5, 20, 15, 10]

grid(40, 50).hoioverlaping(grids, cord)

print(grids)
