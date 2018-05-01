from houses import *
from grid import *
from overlap_check import *
from random import *

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