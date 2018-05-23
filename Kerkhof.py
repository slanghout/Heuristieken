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


def kerkhof(nr_of_houses):
	
	grid = Area().make_basic_grid()

	if nr_of_houses == 20:
		location_space = []
		location_list = []
		total_value = 0

		# singles
		for i in range(9):
			size = single([0,0]).give_size()
			house_next = [24 + (21 + size[1]) * i, 300, 24 + size[1] + (21 + size[1]) * i, 300 - size[0], 1]
			cords = [house_next[0], house_next[1]]
			
			if Area().housecheck(grid, house_next) == True:
				space = single(cords).spacehouse(house_next)
				if Area().spacecheck(grid, space) == True:
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		for i in range(3):
			size = single([0,0]).give_size()
			house_next = [24 + (21 + size[1]) * i, 36, 24 + size[1] + (21 + size[1]) * i, 36 - size[0], 1]
			cords = [house_next[0], house_next[1]]
			
			if Area().housecheck(grid, house_next) == True:
				space = single(cords).spacehouse(house_next)
				if Area().spacecheck(grid, space) == True:
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		# bungalows
		size = bungalow([0,0]).give_size()
		house_next = [28, 170, 28 + size[1], 170 - size[0], 2]
		cords = [house_next[0], house_next[1]]
		
		if Area().housecheck(grid, house_next) == True:
			space = bungalow(cords).spacehouse(house_next)
			if Area().spacecheck(grid, space) == True:
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

		for i in range(2):
			size = bungalow([0,0]).give_size()
			house_next = [71, 105 + size[0] + (70 + size[0]) * i, 71 + size[1], 105 + (70 + size[0]) * i, 2]
			cords = [house_next[0], house_next[1]]
			
			if Area().housecheck(grid, house_next) == True:
				space = bungalow(cords).spacehouse(house_next)
				if Area().spacecheck(grid, space) == True:
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		for i in range(2):
			size = bungalow([0,0]).give_size()
			house_next = [295, 30 + size[0] + (size[0] + 82) * i, 295 + size[1], 30 + (size[0] + 82) * i, 2]
			cords = [house_next[0], house_next[1]]
			
			if Area().housecheck(grid, house_next) == True:
				space = bungalow(cords).spacehouse(house_next)
				if Area().spacecheck(grid, space) == True:
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		# maisons
		size = maison([0,0]).give_size()
		house_next = [135 - size[1], 149 + size[0], 135, 171 - size[0], 3]
		cords = [house_next[0], house_next[1]]
		
		if Area().housecheck(grid, house_next) == True:
			space = maison(cords).spacehouse(house_next)
			if Area().spacecheck(grid, space) == True:
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

		for i in range(2):
			size = maison([0,0]).give_size()
<<<<<<< HEAD
			house_next = [70 + 99 * i, 128, 70 + size[1] + 99 * i, 128 - size[0], 3]
			# print(house_next)
=======
			house_next = [225, 80 + size[0] + (size[0] + 80) * i, 225 + size[1], 80 + (size[0] + 80) * i, 3]
>>>>>>> f74b15a97440e8f6f92d3fc8863a6a8b0a3309e2
			cords = [house_next[0], house_next[1]]
			
			if Area().housecheck(grid, house_next) == True:
				space = maison(cords).spacehouse(house_next)
				if Area().spacecheck(grid, space) == True:
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		for coordinate in location_list:
			cords = [coordinate[0], coordinate[1]]
			if coordinate[4] == 1:
				build = single
			elif coordinate[4] == 2:
				build = bungalow
			elif coordinate[4] == 3:
				build = maison
			price = build(cords).giveworth(coordinate, grid)
<<<<<<< HEAD
			# print(price)
			if price != None:
				total_value += price

		# print(total_value)

		water_coordinates = [[52, 98, 308, 8]]
		return([location_list, water_coordinates, total_value, grid])
		# Area().makegrid(location_list, water_coordinates, total_value)
=======
			if price != None:
				total_value += price

		water_coordinates = [[135, 270, 225, 14]]
		Area().makegrid(location_list, water_coordinates, total_value)
>>>>>>> f74b15a97440e8f6f92d3fc8863a6a8b0a3309e2

# kerkhof(grid, 20)
		

	# 	left_x = house_coordinates[0]
	# 	up_y = house_coordinates[1]
	# 	right_x = house_coordinates[2]
	# 	down_y = house_coordinates[3]

	# if nr_of_houses == 40:

	# if nr_of_houses == 60:

