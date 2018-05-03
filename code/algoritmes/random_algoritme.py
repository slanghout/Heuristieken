from overlap_check import *
from houses import *
from grid import *

import random as random

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

def SetHouseInList(build, cord, coordinate_list):
	housecords = build(cord).coordinates_house()

	if housecords != None:
		if len(coordinate_list) == 0:
				coordinate_list.append(housecords)

		elif Overlap(housecords, coordinate_list) == True:
			coordinate_list.append(housecords)
			return True
		elif Overlap(housecords, coordinate_list) != True:
			return False

def BuildRandomHouses(amount):
	build_single = int(amount*0.6)
	build_bungalow = int(amount*0.25)
	build_maison = int(amount*0.15)

	coordinate_list = []
	housecount = 0
	total_value = 0

	while housecount < build_single:
		cord = Randomizer(grid(180, 160))
		build = single
		if SetHouseInList(build, cord, coordinate_list) == True:
			housecount += 1
			total_value += single(cord).giveworth()

	while housecount < (build_single + build_bungalow):
		cord = Randomizer(grid(180, 160))
		build = bungalow
		if SetHouseInList(build, cord, coordinate_list) == True:
			housecount += 1
			total_value += bungalow(cord).giveworth()

	while housecount < amount:
		cord = Randomizer(grid(180, 160))
		build = maison
		if SetHouseInList(build, cord, coordinate_list) == True:
			housecount += 1
			total_value += maison(cord).giveworth()

	grid(180, 160).makegrid(coordinate_list, total_value)
