from houses import House, Single, Bungalow, Maison
from grid import Area
from water import make_water
from mutaties import housetype

import random as random

# function that creates crandom grid
def random_algoritme(nr_of_houses, distribution):

	# create water coordinates for the grid
	water_coordinates = None
	while water_coordinates == None:
		total_value = 0
		grid = Area().make_basic_grid()
		water_coordinates = create_water(grid)

	# after water is succesful determine house distribution
	# and build the grid
	if water_coordinates != None:
		if distribution == "A":
			coordinate_list = build_amstelhaege(nr_of_houses, grid)
			
		elif distribution == "B":
			coordinate_list = random_amstelhaege(nr_of_houses, grid)
		else:
			print("Enter A or B")

		# determine worth of the houses build
		for cordinate in coordinate_list:
			cord = (cordinate[0], cordinate[1])
			build = housetype(cordinate[4])
			price = build(cord).give_worth(cordinate, grid)
			if price != None:
				total_value += price

		# return the neighbourhood specifics
		return([coordinate_list, water_coordinates, total_value, grid])


# function to create random houses
def randomizer(amount):
	
	# max and min value of the coordinates are grid outliers
	maxX = 340
	maxY = 316
	minX = 4
	minY = 20

	# generate random x and y for left up corner
	random_x = random.randint(minX, maxX)
	random_y = random.randint(minY, maxY)
	
	# return x and y coordinate
	return [random_x, random_y]

# function to create water
def create_water(grid):
	
	# create 1-4 bodies of water
	water_options = [1, 2, 3, 4]
	water_bodies = random.choice(water_options)

	# if more than 1 water body check if all the water bodies fit
	if water_bodies > 1:
		water_coordinates = make_water(water_bodies)
		for body in range(water_bodies):
			if water_coordinates != None:
				if body == 0:
					grid = Area().update_grid(grid, water_coordinates[body],
						"water")
				elif body > 0:
					if Area().watercheck(grid, water_coordinates[body]) == True:
						grid = Area().update_grid(grid, water_coordinates[body],
							"water")
					else:
						return None

	# if only 1 water body place this
	elif water_bodies == 1:
		water_coordinates = make_water(water_bodies)
		if water_coordinates != None:
			grid = Area().update_grid(grid, water_coordinates[0], "water")

	# return the water coordinates
	return water_coordinates


# function to check if house fits and place in grid
def set_house_in_list(build, cord, coordinate_list, grid):

	# create coordinates for house
	house_coordinates = build(cord).coordinates_house()
	if house_coordinates != None:

		# if house coordinates are given create coordinates for house with space
		space_coordinates = build(cord).spacehouse(house_coordinates)

		# check room for house
		if Area().housecheck(grid, house_coordinates) == True:

			# check room for house with space around
			if Area().spacecheck(grid, space_coordinates) == True:
				coordinate_list.append(house_coordinates)

				# set house in grid
				grid = Area().update_grid(grid, house_coordinates, "house")
				grid = Area().update_grid(grid, space_coordinates, "space")
				return True

			# if not enough room for house or space return false
			elif Area().spacecheck(grid, space_coordinates) != True:
				return False
		elif Area().housecheck(grid, house_coordinates) != True:
			return False

# function to build amstelhaege according to house distribution
def build_amstelhaege(amount, grid):
	
	# set number of houses of different kinds
	build_single = int(amount*0.6)
	build_bungalow = int(amount*0.25)
	build_maison = int(amount*0.15)

	coordinate_list = []
	housecount = 0

	# place the bungalows
	while housecount < build_bungalow:
		cord = randomizer(1)
		build = Bungalow
		if set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1

	# place the maisons
	while housecount < (build_bungalow + build_maison):
		cord = randomizer(1)
		build = Maison
		if set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1

	# place the singles
	while housecount < amount:
		cord = randomizer(1)
		build = Single
		if set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1

	# return list of house coordinates
	return coordinate_list

# function to build amstelhaege with random house distribution
def random_amstelhaege(amount, grid):
	coordinate_list = []
	housecount = 0
	
	# as long as there are houses to build randomly select housetype
	# build that house
	while housecount < amount:
		house = random.randint(1, 3)
		build = housetype(house)
		cord = randomizer(1)
		if set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1

	# return list of house coordinates
	return coordinate_list

