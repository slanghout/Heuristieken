from houses import *
from grid import *
from overlap_check import *
from random import *

# define the specifics needed to know per house
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

	# function to create x and y coordinates per house
	# depending on the height and width of house
	def coordinates_house(self):
		left_x = self.x
		down_y = self.y - self.height
		right_x = self.x + self.width
		up_y = self.y

		# set house coordinates
		house_coordinates = [left_x, up_y, right_x, down_y, self.count]
		
		# check if house coordinates do not cross sides of the grid
		if left_x < self.space:
			return None
<<<<<<< HEAD
		elif right_x > (160 - self.space):
=======
		elif right_x > (180 - self.space):
>>>>>>> 00ab623c679c3bff4daba75a7a2e6d3e34601df2
			return None
		elif up_y > (160 - self.space):
			return None
		elif down_y < self.space:
			return None
		else:
			return house_coordinates
	
	def giveworth(self):
		# bereken waarde met de vrijstand
		# geef de min ruimte tot volgende huis
		# bereken de prijs door 
		# worth_house = self.price * (self.percentage * min_space)
		return self.price

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