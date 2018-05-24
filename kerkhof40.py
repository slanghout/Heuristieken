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

	# if nr_of_houses == 20:
	location_space = []
	location_list = []
	total_value = 0

	# SINGLES
	for i in range(8):
		size = single([0,0]).give_size()
		house_next = [20 + (size[1] + 27) * i, 310, 20 + size[1] + (27 + size[1]) * i, 310 - size[0], 1]
		cords = [house_next[0], house_next[1]]

		if Area().housecheck(grid, house_next) == True:
			space = single(cords).spacehouse(house_next)
			if Area().spacecheck(grid, space) == True:
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

	for i in range(8):
		size = single([0,0]).give_size()
		house_next = [20 + (size[1] + 27) * i, 30, 20 + size[1] + (27 + size[1]) * i, 30 - size[0], 1]
		cords = [house_next[0], house_next[1]]

		if Area().housecheck(grid, house_next) == True:
			space = single(cords).spacehouse(house_next)
			if Area().spacecheck(grid, space) == True:
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

	for i in range(4):
		size = single([0,0]).give_size()
		house_next = [20, 280 - (size[0] + 55) * i , 20 + size[1], 280 - size[0] - (55 + size[0]) * i, 1]
		cords = [house_next[0], house_next[1]]

		if Area().housecheck(grid, house_next) == True:
			space = single(cords).spacehouse(house_next)
			if Area().spacecheck(grid, space) == True:
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

	for i in range(4):
		size = single([0,0]).give_size()
		house_next = [324, 280 - (size[0] + 55) * i , 324 + size[1], 280 - size[0] - (55 + size[0]) * i, 1]
		cords = [house_next[0], house_next[1]]

		if Area().housecheck(grid, house_next) == True:
			space = single(cords).spacehouse(house_next)
			if Area().spacecheck(grid, space) == True:
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

	# BUNGLOWS
	for i in range(3):
		size = bungalow([0,0]).give_size()
		house_next = [324, 250 - (size[0] + 55) * i , 324 + size[1], 250 - size[0] - (55 + size[0]) * i, 2]
		cords = [house_next[0], house_next[1]]

		if Area().housecheck(grid, house_next) == True:
			space = bungalow(cords).spacehouse(house_next)
			if Area().spacecheck(grid, space) == True:
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

	for i in range(3):
		size = bungalow([0,0]).give_size()
		house_next = [20, 250 - (size[0] + 55) * i , 20 + size[1], 250 - size[0] - (55 + size[0]) * i, 2]
		cords = [house_next[0], house_next[1]]

		if Area().housecheck(grid, house_next) == True:
			space = bungalow(cords).spacehouse(house_next)
			if Area().spacecheck(grid, space) == True:
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

	for i in range(6):
		size = maison([0,0]).give_size()
		house_next = [60 + (size[1] + 30) * i, 60 + (size[0] + 30) * i, 60 + size[1] + (30 + size[1]) * i, 60 - size[0] + (30 + size[0]) * i, 3]
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
		# print(price)
		if price != None:
			total_value += price

	# print(total_value)

	water_coordinates = [[36, 294, 184, 204], [176, 120, 324, 30]]
	# if Area().watercheck(grid, water_coordinates[body]) == True:
	# 	grid = Area().update_grid(grid, water_coordinates[body], "water")

	Area().makegrid(location_list, water_coordinates, total_value)

kerkhof(grid, 40)