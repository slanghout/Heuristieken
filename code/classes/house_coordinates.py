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
	def __init__(self, x, y, height, width, price, space, percentage, count):
		self.x = x
		self.y = y
		self.coordinates = [x,y]
		self.height = height
		self.width = width
		self.price = price
		self.space = space
		self.percentage = percentage
		# self.color = color
		self.count = count

	def coordinates_house(self):
		leftup = [self.x, self.y]
		leftdown = [self.x, (self.y - self.height)]
		rightup = [(self.x + self.width), self.y]
		rightdown = [(self.x+self.width), (self.y - self.height)]
		if leftup[0] < self.space or rightup[0] > (180 - self.space):
			print("House too wide")
		if leftdown[1] > (160 - self.space):
			print("House too tall")
		else:
			house_coordinates = [leftup, leftdown, rightup, rightdown]
			print(house_coordinates)
			return house_coordinates

class single(house):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1], height = 8,
		 width = 8, price = 285000, space = 2, percentage = 1.03, count = 1)

class bungalow(house):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1], height = 10,
		 width = 7.5, price = 399000, space = 3, percentage = 1.04, count = 2)

class maison(house):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1], height = 11,
		 width = 10.5, price = 610000, space = 6, percentage = 1.06, count = 3)


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

coordinates_t = Randomizer(land)
coordinates_h = Randomizer(land)
house1 = single(coordinates_t)
house2 = maison(coordinates_h)
print("Coordinates are {}".format(coordinates_t))
print("Coordinates are {}".format(coordinates_h))
house1.coordinates_house()
house2.coordinates_house()
# def build_house(grid, woning):
# 	#  iterate over the width of the grid
# 	# if there is an empty block, check if there are enough empty blocks to make house
# 	# if true check if this is the case for height of the house
# 	# if true, plot the house, change value of blocks to 1, 2, 3

