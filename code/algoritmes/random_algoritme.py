# from overlap_check import *
from houses import *
from grid import *
from water import *

import random as random

def Random(nr_of_houses):
	# make empty coordinate list

	grid = Area().make_basic_grid()
	total_value = 0

	water_coordinates =  Create_water(grid)
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
			total_value += price

		Area().makegrid(coordinate_list, water_coordinates, total_value)
	else:
		exit()

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
						exit(0)
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
				if build == single:
					grid = Area().update_grid(grid, house_coordinates, "single")
				elif build == bungalow:
					grid = Area().update_grid(grid, house_coordinates, "bungalow")
				elif build == maison:
					grid = Area().update_grid(grid, house_coordinates, "maison")
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
	# total_value = 0

	while housecount < build_single:
		cord = Randomizer(1)
		build = single
		if Set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1
			# total_value += single(cord).giveworth()

	while housecount < (build_single + build_bungalow):
		cord = Randomizer(1)
		build = bungalow
		if Set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1
			# total_value += bungalow(cord).giveworth()

	while housecount < amount:
		cord = Randomizer(1)
		build = maison
		if Set_house_in_list(build, cord, coordinate_list, grid) == True:
			housecount += 1
			# total_value += maison(cord).giveworth()

	Area().fillgrid(grid)

	return coordinate_list
