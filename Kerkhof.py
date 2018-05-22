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
			house_next = [12 + 29 * i, 307, 12 + size[1] + 29 * i, 307 - size[0], 1]
			cords = [house_next[0], house_next[1]]
			
			if Area().housecheck(grid, house_next) == True:
				space = single(cords).spacehouse(house_next)
				if Area().spacecheck(grid, space) == True:
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")
					price = single(cords).giveworth(house_next, grid)
					total_value += price

		# bungalows
		for i in range(5):
			size = bungalow([0,0]).give_size()
			house_next = [58 + 57 * i, 250, 58 + size[1] + 57 * i, 250 - size[0], 2]
			cords = [house_next[0], house_next[1]]
			
			if Area().housecheck(grid, house_next) == True:
				space = bungalow(cords).spacehouse(house_next)
				if Area().spacecheck(grid, space) == True:
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")
					price = bungalow(cords).giveworth(house_next, grid)
					total_value += price

		# maisons
		for i in range(3):
			size = maison([0,0]).give_size()
			house_next = [58 + 99 * i, 128, 58 + size[1] + 99 * i, 128 - size[0], 3]
			cords = [house_next[0], house_next[1]]
			
			if Area().housecheck(grid, house_next) == True:
				space = maison(cords).spacehouse(house_next)
				if Area().spacecheck(grid, space) == True:
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")
					price = maison(cords).giveworth(house_next, grid)
					total_value += price

		water_coordinates = [[52, 98, 308, 8]]
		Area().makegrid(location_list, water_coordinates, total_value)

kerkhof(grid, 20)
		

	# 	left_x = house_coordinates[0]
	# 	up_y = house_coordinates[1]
	# 	right_x = house_coordinates[2]
	# 	down_y = house_coordinates[3]

	# if nr_of_houses == 40:

	# if nr_of_houses == 60:

