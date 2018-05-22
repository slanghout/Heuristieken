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

def kerkhof(grid, nr_of_houses, width, height):

	if nr_of_houses == 20:
		location_list = []

		# singles
		for i in range(12):
			house_next = [4 + 30 * i, 316, 4 + 16 + 30 * i, 316 - 16, 1]
			location_list.append(house_next)
			grid = Area().update_grid(grid, house_next, "house")
		print(grid)
		print(location_list)
		total_value = 100
		water_coordinates = Create_water(grid)
		Area().makegrid(location_list, water_coordinates, total_value)

		# for Area().makegrid(coordinate_list, water_coordinates, total_value)

kerkhof(grid, 20, 16, 16)
		# bungalows

		# maisons

	# 	left_x = house_coordinates[0]
	# 	up_y = house_coordinates[1]
	# 	right_x = house_coordinates[2]
	# 	down_y = house_coordinates[3]

	# if nr_of_houses == 40:

	# if nr_of_houses == 60:

	# bovenste rij
	# eerste huis 4, 360 - 4
	# 3 x volgende huizen x + 44, 360 - 4

	# onderste rij
	# eerste huis 320 - 4, 4
	# 3x volgende huizen x + 44, 4

	# linker rij
	# eerste huis 4, 360 - 4 (niet plaatsen)
	# 2x volgende huizen 320 - 4, y - 39

	# rechter rij
	# eerste huis 320 - 4, 360 - 4 (niet plaatsen)
	# 2x volgende huizen 320 - 4, y - 39

