# from overlap_check import *
from houses import house
from houses import single
from houses import bungalow
from houses import maison
from grid import Area
from water import MakeWater

import random as random

def Random(nr_of_houses):
	# make empty coordinate list

	water_coordinates = None
	while water_coordinates == None:
		total_value = 0
		grid = Area().make_basic_grid()
		water_coordinates = Create_water(grid)
	
	if water_coordinates != None:
		coordinate_list = Build_Amstelhaege(nr_of_houses, grid)
		for cordinate in coordinate_list:
			cord = (cordinate[0], cordinate[1])
			if cordinate[4] == 1:
				build = single
			elif cordinate[4] == 2:
				build = bungalow
			elif cordinate[4] == 3:
				build = maison
			price = build(cord).giveworth(cordinate, grid)
			if price != None:
				total_value += price
		
		return([coordinate_list, water_coordinates, total_value, grid])


# Random coordinate generation after grid boundaries are given
def Randomizer(amount):
	# max and min value of the coordinates are grid outliers
	maxX = 320
	maxY = 360
	minX = 0
	minY = 0

	# generate random x and y for left up corner
	random_x = random.randint(minX, maxX)
	random_y = random.randint(minY, maxY)
	return [random_x, random_y]

def Create_water(grid):
	water_options = [1, 2, 3, 4]

	water_bodies = random.choice(water_options)

	if water_bodies > 1:
		water_coordinates = MakeWater(water_bodies)
		for body in range(water_bodies):
			if water_coordinates != None:
				if body == 0:
					grid = Area().update_grid(grid, water_coordinates[body], "water")
				elif body > 0:
					if Area().watercheck(grid, water_coordinates[body]) == True:
						grid = Area().update_grid(grid, water_coordinates[body], "water")
					else:
						return None

	elif water_bodies == 1:
		water_coordinates = MakeWater(water_bodies)
		if water_coordinates != None:
			grid = Area().update_grid(grid, water_coordinates[0], "water")

	return water_coordinates


def Set_house_in_list(build, cord, coordinate_list, grid):

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

def Build_Amstelhaege(amount, grid):
	build_single = int(amount*0.6)
	build_bungalow = int(amount*0.25)
	build_maison = int(amount*0.15)

	coordinate_list = []
	housecount = 0
	# while housecount < amount:
	# 	housetype = random.randint(1, 3)

	# 	if housetype == 1:
	# 		build = single
	# 	if housetype == 2:
	# 		build = bungalow
	# 	if housetype == 3:
	# 		build = maison
	# 	cord = Randomizer(1)
	# 	if Set_house_in_list(build, cord, coordinate_list, grid) == True:
	# 		housecount += 1

	while housecount < build_bungalow:
		cord = Randomizer(1)
		build = bungalow
		if Set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1

	while housecount < (build_bungalow + build_maison):
		cord = Randomizer(1)
		build = maison
		if Set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1

	while housecount < amount:
		cord = Randomizer(1)
		build = single
		if Set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1

	# Area().fillgrid(grid)

	return coordinate_list
