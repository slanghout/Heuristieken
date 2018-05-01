# import os, sys
# directory = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(os.path.join(directory, "code"))
# sys.path.append(os.path.join(directory, "code", "classes"))
# sys.path.append(os.path.join(directory, "code", "algoritmes"))
# sys.path.append(os.path.join(directory, "code", "grid"))

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

	return coordinate_list

def BuildRandomHouses(amount, coordinate_list):

	build_single = int(amount*0.6)
	build_bungalow = int(amount*0.25)
	build_maison = int(amount*0.15)

	for buildsingle in range(build_single):
		cord = Randomizer(grid(180, 160))
		build = single
		coordinate_list = SetHouseInList(build, cord, coordinate_list)

	for buildmaison in range(build_maison):
		cord = Randomizer(grid(180, 160))
		build = maison
		coordinate_list = SetHouseInList(build, cord, coordinate_list)

	for buildbungalow in range(build_bungalow):
		cord = Randomizer(grid(180, 160))
		build = bungalow
		coordinate_list = SetHouseInList(build, cord, coordinate_list)

	grid(180, 160).makegrid(coordinate_list)
