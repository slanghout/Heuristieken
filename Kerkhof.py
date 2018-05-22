import os, sys
import csv
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "grid"))

from houses import house
from houses import single
from houses import bungalow
from houses import maison

from grid import Area
from random_algoritme import Random
from random_algoritme import Create_water
from water import MakeWater

grid = Area().make_basic_grid()

def kerkhof(grid, nr_of_houses):

	if nr_of_houses == 20:
		location_space = []
		location_list = []
		total_value = 0

		# singles
		for i in range(12):
			size = single([0,0]).give_size()
			print(size)
			house_next = [4 + 30 * i, 316, 4 + size[1] + 30 * i, 316 - size[0], 1]
			cords = [house_next[0], house_next[1]]
			
			if Area().housecheck(grid, house_next) == True:
				space = single(cords).spacehouse(house_next)
				print(space)
				if Area().spacecheck(grid, space) == True:
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")
					price = single(cords).giveworth(house_next, grid)
					total_value += price
					print(total_value)

		# print(grid)
		print(location_list)
		print(location_space)
		print(total_value)		
		
		# water nog bepalen
		water_coordinates = Create_water(grid)
		Area().makegrid(location_list, water_coordinates, total_value)

kerkhof(grid, 20)
		# bungalows

		# maisons

	# 	left_x = house_coordinates[0]
	# 	up_y = house_coordinates[1]
	# 	right_x = house_coordinates[2]
	# 	down_y = house_coordinates[3]

	# if nr_of_houses == 40:

	# if nr_of_houses == 60:

