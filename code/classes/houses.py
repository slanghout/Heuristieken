from grid import Area

import random as random

# define the specifics needed to know per house
class House(object):
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
		height_width = [self.width, self.height]
		height = random.choice(height_width)
		if height == self.height:
			width = self.width
		elif height == self.width:
			width = self.height

		left_x = self.x
		down_y = self.y - height
		right_x = self.x + width
		up_y = self.y

		# set house coordinates
		house_coordinates = [left_x, up_y, right_x, down_y, self.count]

		# check if house coordinates do not cross sides of the grid
		if left_x < self.space:
			return None
		elif right_x > (360 - self.space):
			return None
		elif up_y > (320 - self.space):
			return None
		elif down_y < self.space:
			return None
		else:
			return house_coordinates

	# returns space coordinates for house
	def space_house(self, house_coordinates):
		left_x = house_coordinates[0]
		up_y = house_coordinates[1]
		right_x = house_coordinates[2]
		down_y = house_coordinates[3]

		left_x_space = left_x - self.space
		up_y_space = up_y + self.space
		right_x_space = right_x + self.space
		down_y_space = down_y - self.space

		space_coordinates = [left_x_space, up_y_space, right_x_space, down_y_space]

		return space_coordinates

	# returns worth of each house
	def give_worth(self, house_coordinates, grid):
		space_vertical = Area().calculate_space_vertical(house_coordinates, grid)
		space_horizontal = Area().calculate_space_horizontal(house_coordinates, grid)
		if space_horizontal != None and space_vertical != None:
			if space_horizontal < space_vertical:
				space = space_horizontal
			else:
				space = space_vertical

			extra_space = (int(space - self.space))/2
			price = self.price * (1 + (self.percentage * extra_space))

			return price

	# returns dimensions of house
	def give_size(self):
		return [self.height, self.width]

# define specifics for single house
class Single(House):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1], height = 16,
		 width = 16, price = 285000, space = 4, percentage = 0.03, count = 1)

# define specifics for bungalow house
class Bungalow(House):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1], height = 20,
		 width = 15, price = 399000, space = 6, percentage = 0.04, count = 2)

# define specifics for maison house
class Maison(House):
	def __init__(self, coordinates):
		super().__init__(x = coordinates[0], y=coordinates[1], height = 22,
		 width = 21, price = 610000, space = 12, percentage = 0.06, count = 3)
