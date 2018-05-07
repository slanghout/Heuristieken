# from overlap_check import *
from houses import *
from grid import *
from water import *

import random as random

def Random(nr_of_houses):
	# make empty coordinate list

	grid = Area().make_basic_grid()
	
	water_coordinates =  Create_water(grid)
	if water_coordinates != None:
		values = Build_Amstelhaege(nr_of_houses, grid)
		total_value = values[0]
		coordinate_list = values[1]
		if total_value != None:
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

def Create_water(cordinatelist):
	water_options = [1, 2, 3, 4]

	water_bodies = 1 #random.choice(water_options)
	if water_bodies > 1:
		water_coordinates = MakeWater(water_bodies)
		for body in range(water_bodies):
			if water_coordinates != None:
				cordinatelist = Area().updatecordinatelist(cordinatelist, water_coordinates[body], "water")
			
	elif water_bodies == 1:
		water_coordinates = MakeWater(water_bodies)
		if water_coordinates != None:
			cordinatelist = Area().updatecordinatelist(cordinatelist, water_coordinates[0], "water")
	
	return water_coordinates


def Set_house_in_list(build, cord, coordinate_list, cordinatelist):

	house_coordinates = build(cord).coordinates_house()
	if house_coordinates != None:
		space_coordinates = build(cord).spacehouse(house_coordinates)
	
		if Area().housecheck(cordinatelist, house_coordinates) == True:
			if Area().spacecheck(cordinatelist, space_coordinates) == True:
				coordinate_list.append(house_coordinates)
				cordinatelist = Area().updatecordinatelist(cordinatelist, house_coordinates, "house")
				cordinatelist = Area().updatecordinatelist(cordinatelist, space_coordinates, "space")
				return True
			elif Area().spacecheck(cordinatelist, space_coordinates) != True:
				return False
		elif Area().housecheck(cordinatelist, house_coordinates) != True:
			return False

def Build_Amstelhaege(amount, cordinatelist):
	build_single = int(amount*0.6)
	build_bungalow = int(amount*0.25)
	build_maison = int(amount*0.15)

	coordinate_list = []
	housecount = 0
	total_value = 0

	while housecount < build_single:
		cord = Randomizer(1)
		build = single
		if Set_house_in_list(build, cord, coordinate_list, cordinatelist) == True:
			housecount += 1
			total_value += single(cord).giveworth()

	while housecount < (build_single + build_bungalow):
		cord = Randomizer(1)
		build = bungalow
		if Set_house_in_list(build, cord, coordinate_list, cordinatelist) == True:
			housecount += 1
			total_value += bungalow(cord).giveworth()

	while housecount < amount:
		cord = Randomizer(1)
		build = maison
		if Set_house_in_list(build, cord, coordinate_list, cordinatelist) == True:
			housecount += 1
			total_value += maison(cord).giveworth()

	Area().fillgrid(cordinatelist)

	return [total_value, coordinate_list]


