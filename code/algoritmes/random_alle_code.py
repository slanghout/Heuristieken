import numpy as np
import matplotlib.pyplot as plt
import random as random

class grid(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def makegrid(self, coordinatelist):
		# make the figure
		fig = plt.figure()

		# make plot with green background
		ax = fig.add_subplot(1, 1, 1)

		# make axes grid steps of 0.5 m
		major_ticks = np.arange(0, 200, 20)
		minor_ticks = np.arange(0, 200, 0.5)
		# imshow
		
		# # makes lines for grid 
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
		
		# make background grid green
		x = [180, 180, 0, 0]
		y = [0, 160, 160, 0]
		ax.fill(x, y, "g")
		
		# iterate over coordinate list and select coordinates
		for element in coordinatelist:
			x = [element[2], element[2], element[0], element[0]]
			y = [element[1], element[3], element[3], element[1]]
				
			# color coordinates coresponding color
			if element[4] == 1:
				ax.fill(x, y, "r")
			elif element[4] == 2:
				ax.fill(x, y, "y")
			elif element[4] == 3:
				ax.fill(x, y, "b")
	
		# plt.legend(loc=0)
		#for data, color, group in zip(data, colors, groups):
 		##  ax.scatter(x, y, c=color, label=group)

		#plt.scatter(x,y, label=group, c=color, s=30)
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
		self.count = count

	def coordinates_house(self):
		left_x = self.x
		down_y = self.y - self.height
		right_x = self.x + self.width
		up_y = self.y
		count = self.count
		house_coordinates = [left_x, up_y, right_x, down_y, count]
		if left_x < self.space:
			print("does not fit left: {}".format(house_coordinates))
		elif right_x > (160 - self.space):
			print("does not fit right: {}".format(house_coordinates))
		elif up_y > (160 - self.space):
			print("does not fit on top: {}".format(house_coordinates))
		elif down_y < self.space:
		 	print("does not fit on the bottom: {}".format(house_coordinates))
		else:
			# print(house_coordinates)
			return house_coordinates

# define specifics for single house
class single(house):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1], height = 8,
		 width = 8, price = 285000, space = 2, percentage = 1.03, count = 1)

# define specifics for bungalow house
class bungalow(house):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1], height = 10,
		 width = 7.5, price = 399000, space = 3, percentage = 1.04, count = 2)

# define specifics for maison house
class maison(house):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1], height = 11,
		 width = 10.5, price = 610000, space = 6, percentage = 1.06, count = 3)
  
# Random coordinate generation after grid boundaries are given
def Randomizer(grid):

	# max and min value of the coordinates are grid outliers
	maxX = grid.width
	maxY = grid.height
	minX = 0
	minY = 0
	
	# generate random x and y for left up corner
	random_x = random.randint(minX, maxX)
	random_y = random.randint(minY, maxY)
	return [random_x, random_y]

def Overlap(new_coordinate, coordinatelist):
# check if the coordinates are overlapping
	
	if new_coordinate == None:
		return False
	else:
	
		left_x_new = new_coordinate[0]
		right_x_new = new_coordinate[2]
		up_y_new = new_coordinate[1]
		down_y_new = new_coordinate[3]
		
		# check coordinates in list
		for cords in coordinate_list:
			left_x_list = cords[0]
			right_x_list = cords[2]
			up_y_list = cords[1]
			down_y_list = cords[3]

			# check if there is overlap
			if ((left_x_new > left_x_list or left_x_new == left_x_list) and (left_x_new < right_x_list or left_x_new == right_x_list) and (up_y_new < up_y_list or up_y_new == up_y_list) and (up_y_list > down_y_list or up_y_list == down_y_list)):
				return False
			if ((right_x_new > left_x_list or right_x_new == left_x_list) and (right_x_new < right_x_list or right_x_new == right_x_list) and (up_y_new < up_y_list or up_y_new == up_y_list) and (up_y_list > down_y_list or up_y_list == down_y_list)):
				return False
			if ((left_x_new > left_x_list or left_x_new == left_x_list) and (left_x_new < right_x_list or left_x_new == right_x_list) and (down_y_new < up_y_list or down_y_new == up_y_list) and (down_y_new > down_y_list or down_y_new == down_y_list)):
				return False
			if ((right_x_new > left_x_list or right_x_new == left_x_list) and (right_x_new < right_x_list or right_x_new == right_x_list) and (down_y_new < up_y_list or down_y_new == up_y_list) and (down_y_new > down_y_list or down_y_new == down_y_list)):
				return False
				
		return True

# set height and width of the land
land = grid(180, 160)

# create empty coordinate list
coordinate_list = []

def BuildRandomHouses(amount)

for houses in range(amount):
	cord = Randomizer(land)
	
	# build_single = amount*0.6
	# build_bungalow = amount*0.25
	# build_maison = amount*0.15

	# for building in range(build_single)
	# 	build = single

	# create either single, bungalow or maison
	housenr = random.randint(1, 3)
	if housenr == 1:
		build = single
	elif housenr == 2:
		build = bungalow
	elif housenr == 3:
		build = maison
	
	housecords = build(cord).coordinates_house()
	if housecords != None:
		if len(coordinate_list) == 0:
				coordinate_list.append(housecords)
		
		elif Overlap(housecords, coordinate_list) == True:
			coordinate_list.append(housecords)
			# print(coordinate_list)
		

# make a grid of the coordinates in coordinate list
land.makegrid(coordinate_list) 


