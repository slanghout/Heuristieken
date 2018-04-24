import numpy as np
import matplotlib.pyplot as plt
import random as random

class grid(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def makegrid(self):
		# make the figure
		fig = plt.figure()

		# make plot with green background
		ax = fig.add_subplot(1, 1, 1)

		# make axes grid steps of 0.5 m
		major_ticks = np.arange(0, 200, 20)
		minor_ticks = np.arange(0, 200, 0.5)
		# imshow
		
		# makes lines for grid 
		# ax.set_xticks(major_ticks)
		# ax.set_xticks(minor_ticks, minor=True)
		# ax.set_yticks(major_ticks)
		# ax.set_yticks(minor_ticks, minor=True)
		# ax.grid(which='both')

		# set limits for the plot
		ax.set_xlim(left=0, right=self.width, auto=False)
		ax.set_ylim(bottom=0, top=self.height, auto=False)
		
		# set labels for the axes 
		plt.xlabel('width')
		plt.ylabel('height')
		plt.title('Amstelhaege')
		
		# # set value of plots to 0
		# for i in range(self.width):
  #  	 		for j in range(self.height):
  #  	 			plt.text(i, j, '0')

		# dit zijn dus de coordinaten van het huis
		# property?
		# linken aan classes van de soorten huizen
		# algoritme dat deze coordinaten bepaalt
		# dit zijn dus de coordinaten van het huis
		x = [180, 180, 0, 0]
		y = [0, 160, 160, 0]
		# kleur aan huis aanpassen
		ax.fill(x, y, "g") #per huis de legenda erachter
		
		x = [15, 15, 7, 7]
		y = [7, 15, 15, 7]
		ax.fill(x, y, "r") #per huis de legenda erachter
		
		
		# plt.legend(loc=0)
		plt.show()

class house(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.coordinates = [x,y]		

	@property
	def leftupper(self):
		return self.coordinates

	@property
	def rightupper(self):
		return [self.coordinates[0] + self.width, self.coordinates[1]]

	@property
	def leftlower(self):
		return [self.coordinates[0], self.coordinates[1] + self.height]

	@property
	def rightlower(self):
		return [self.coordinates[0] + self.width, self.coordinates[1] + self.height]

	# def print_coordinates(self):
	# 	print("House coordinates are {}{}{}{}".format(house.leftlower(), house.leftupper(), house.rightlower(), house.rightupper()))

class single(house):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1])
		self.height = 8
		self.width = 8
		self.price = 285.000
		self.space = 2
		self.percentage = 1.03
		# self.color = 
		self.count = 1

class bungalow(house):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1])
		self.height = 10
		self.width = 7.5
		self.price = 399.000
		self.space= 3
		self.percentage = 1.04
		# self.color = 
		self.count = 2

class maison(house):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1])
		self.height = 11
		self.width = 10.5
		self.price = 610.000
		self.space = 6
		self.percentage = 1.06
		# self.color = 
		self.count = 3

	def printhuis(self):
		print("The house is {} by {} and worth {}".format(self.height, self.width, self.price))

land = grid(180, 160)
land.makegrid()

  
# Random coordinates generation
def Randomizer(grid):
	maxX = grid.width
	maxY = grid.height
	minX = 0
	minY = 0
	random_x = random.randint(minX, maxX)
	random_y = random.randint(minY, maxY)
	return [random_x, random_y]
#  als coordinaten leeg zijn; kijken of @property allemaal leeg zijn: dan huis planten

coordinates = Randomizer(land)
house1 = single(coordinates)
# house1.print_coordinates()
print("Coordinates are {}".format(coordinates))
print("House coordinates are {}".format(house1.leftlower()))






# def build_house(grid, woning):
# 	#  iterate over the width of the grid
# 	# if there is an empty block, check if there are enough empty blocks to make house
# 	# if true check if this is the case for height of the house
# 	# if true, plot the house, change value of blocks to 1, 2, 3


# 	for i in range(grid.width):
# 		if [i] =

# 		for j in range(grid.height):
# 			if [i][j] == Null:
# 				x = [i, i, (i + woning.breedte), (i + woning.breedte)]
# 				y = [j, (j + woning.hoogte), (j+ woning.hoogte), j]
# 				[i][j] = woning.count
# 				ax.fill(x, y, woning.color)
# 	plt.show()


		# property?
		# linken aan classes van de soorten huizen
		# algoritme dat deze coordinaten bepaalt
		# x = [10, 10, 5, 5] 
		# y = [5, 10, 10, 5]
		# # kleur aan huis aanpassen
# 		# ax.fill(x, y, "r") #per huis de legenda erachter
# vila = woning(10,10,10,2,1.03,'green',123)
# print(vila.linkerbovenhoek) 

# eensgezins = woning(2, 2, 285000, 2, 1.03, "r", "1")
# eensgezins.printhuis()

# land = grid(180, 160)
# land.makegrid()

# build_house(land, eensgezins)
