import csv

from houses import house
from houses import single
from houses import bungalow
from houses import maison

from grid import Area
from random_algoritme import Random

from random import randint

# determine of new grid is worth more than old grid
def determine_worth(coordinate_list, grid):
	worth = 0
	for cordinate in coordinate_list:
		build = housetype(cordinate[4])
		cord = (cordinate[0], cordinate[1])
		price = build(cord).giveworth(cordinate, grid)
		if price != None:
			worth += price

	return worth

# function that swaps two houses in the grid
def house_swap(coordinate_list, nr_of_houses, grid):

	# randomly pick two houses from the coordinate list
	house_one = randint(0, (nr_of_houses -1))
	house_two = randint(0, (nr_of_houses - 1))
	old_cords_one = coordinate_list[house_one]
	old_cords_two = coordinate_list[house_two]

	# determine height and width of the houses
	width_one = old_cords_one[2] - old_cords_one[0]
	height_one = old_cords_one[1] - old_cords_one[3]
	width_two = old_cords_two[2] - old_cords_two[0]
	height_two = old_cords_two[1] - old_cords_two[3]

	# create new coordinates for the houses
	# take the left upper corner
	# determine new coordinates with height and width
	x_l_one = old_cords_two[0]
	y_u_one = old_cords_two[1]
	x_r_one = old_cords_two[0] + width_one
	y_d_one = old_cords_two[1] - height_one
	new_cord_one = [x_l_one, y_u_one, x_r_one, y_d_one, old_cords_one[4]]

	x_l_two = old_cords_one[0]
	y_u_two = old_cords_one[1]
	x_r_two = old_cords_one[0] + width_two
	y_d_two = old_cords_one[1] - height_two
	new_cord_two = [x_l_two, y_u_two, x_r_two, y_d_two, old_cords_two[4]]

	# determine the space needed for old houses
	if old_cords_one[4] == 1:
		build = single
	elif old_cords_one[4] == 2:
		build = bungalow
	elif old_cords_one[4] == 3:
		build = maison
	cord_one = (x_l_one, y_u_one)
	space_old_cords_one = build(cord_one).spacehouse(old_cords_one)

	build = housetype(old_chords_two[4])
	cord_two = (x_l_two, y_u_two)
	space_old_cords_two = build(cord_two).spacehouse(old_cords_two)

	# clear the space the houses were using
	grid = Area().create_space(space_old_cords_one, grid)
	grid = Area().create_space(space_old_cords_two, grid)

	# determine space needed for new houses
	if new_cord_one[4] == 1:
		build = single
	elif new_cord_one[4] == 2:
		build = bungalow
	elif new_cord_one[4] == 3:
		build = maison
	cord_one_new = (x_l_one, y_d_one)
	new_space_cords_one = build(cord_one_new).spacehouse(new_cord_one)

	if (new_space_cords_one[0] < 0 or new_space_cords_one[3] < 0 or
		new_space_cords_one[1] > 320 or new_space_cords_one[2] > 360):
		grid = reset(grid, old_cords_one, space_old_cords_one)
		return [coordinate_list, grid]

	if new_cord_two[4] == 1:
		build = single
	elif new_cord_two[4] == 2:
		build = bungalow
	elif new_cord_two[4] == 3:
		build = maison
	cord_two_new = (x_l_two, y_d_two)
	new_space_cords_two = build(cord_two_new).spacehouse(new_cord_two)

	if (new_space_cords_two[0] < 0 or new_space_cords_two[3] < 0 or
		new_space_cords_two[1] > 320 or new_space_cords_two[2] > 360):
		grid = reset(grid, old_cords_two, space_old_cords_two)
		return [coordinate_list, grid]

	# check if there is enough space to place house
	if (Area().housecheck(grid, new_cord_one) == True and
		Area().housecheck(grid, new_cord_two) == True):

		# check if there is space to place house with extra space
		if (Area().spacecheck(grid, new_space_cords_one) == True and
			Area().spacecheck(grid, new_space_cords_two) == True):

			# if everything is true swap the houses
			grid = reset(grid, new_cord_one, new_space_cords_one)
			coordinate_list[house_one] = new_cord_two
			grid = reset(grid, new_cord_two, new_space_cords_two)
			coordinate_list[house_two] = new_cord_one
		
		else:
			grid = reset(grid, old_cords_one, space_old_cords_one)
			grid = reset(grid, old_cords_two, space_old_cords_two)

	else:
		grid = reset(grid, old_cords_one, space_old_cords_one)
		grid = reset(grid, old_cords_two, space_old_cords_two)			
# else:
# 	grid = reset(grid, old_cords_one, space_old_cords_one)
# 	grid = reset(grid, old_cords_two, space_old_cords_two)

	# if the houses were swapped return the grid information
	return [coordinate_list, grid]

# function that moves a house by 1 coordinate
def move_house(coordinate_list, nr_of_houses, grid):

	# randomly pick one house from the coordinate list
	move_house = randint(0, (nr_of_houses -1))
	cord_move_house = coordinate_list[move_house]

	new_cord = move(cord_move_house)

	# determine space needed first
	build = housetype(cord_move_house[4])
	cord = (cord_move_house[0], cord_move_house[1])
	space_cords = build(cord).spacehouse(cord_move_house)

	# determine space needed after move
	build = housetype(new_cord[4])
	cord = (new_cord[0], new_cord[1])
	new_space_cords = build(cord).spacehouse(new_cord)

	if (new_space_cords[0] < 0 or new_space_cords[3] < 0 or
		new_space_cords[1] > 320 or new_space_cords[2] > 360):
		return None
	
	# clear the space the houses were using
	grid = Area().create_space(space_cords, grid)

	# check if there is enough space to place house
	if Area().housecheck(grid, new_cord) == True:

		# check if there is space to place house with extra space
		if Area().spacecheck(grid, new_space_cords) == True:

			# if everything is true move the house
			grid = reset(grid, new_cord, new_space_cords)
			coordinate_list[move_house] = new_cord

		else:
			grid = reset(grid, cord_move_house, space_cords)
			return None

	else:
		grid = reset(grid, cord_move_house, space_cords)
		return None

	# if the houses were swapped return the grid information
	return [coordinate_list, grid, cord_move_house, space_cords, move_house, new_space_cords]

# function that rotates a house
def rotate_house(coordinate_list, nr_of_houses, grid):

	# randomly pick one house from the coordinate list
	rotate_house = randint(0, (nr_of_houses -1))
	cord_rotate_house = coordinate_list[rotate_house]

	# determine height and width of the houses
	width = cord_rotate_house[2] - cord_rotate_house[0]
	height = cord_rotate_house[1] - cord_rotate_house[3]

	# set coordinates for rotated house
	x_l = cord_rotate_house[0]
	y_u = cord_rotate_house[1]
	x_r = cord_rotate_house[0] + height
	y_d = cord_rotate_house[1] - width

	# set new coordinates
	new_cord = [x_l, y_u, x_r, y_d, cord_rotate_house[4]]

	build = housetype(cord_rotate_house[4])
	cord = (cord_rotate_house[0], cord_rotate_house[1])
	space_cords = build(cord).spacehouse(cord_rotate_house)

	build = housetype(new_cord[4])
	cord = (new_cord[0], new_cord[1])
	new_space_cords = build(cord).spacehouse(new_cord)

	if (new_space_cords[0] < 0 or new_space_cords[3] < 0 or
		new_space_cords[1] > 320 or new_space_cords[2] > 360):
		return None

	# clear the space the houses were using
	grid = Area().create_space(space_cords, grid)

	# check if there is enough space to place house
	if Area().housecheck(grid, new_cord) == True:

		# check if there is space to place house with extra space
		if Area().spacecheck(grid, new_space_cords) == True:

			# if everything is true swap the houses
			grid = reset(grid, new_cord, new_space_cords)
			coordinate_list[rotate_house] = new_cord

		else:
			grid = reset(grid, cord_rotate_house, space_cords)
			return None

	else:
		grid = reset(grid, cord_rotate_house, space_cords)
		return None

	# if the houses were swapped return the grid information
	return [coordinate_list, grid, cord_rotate_house, space_cords, rotate_house, new_space_cords]

def reset(grid, house_coordinates, space_coordinates):
	grid = Area().update_grid(grid, house_coordinates, "house")
	grid = Area().update_grid(grid, space_coordinates, "space")
	return grid

def move(coordinates):

	# choose in which direction the house will move
	direction = randint(0, 3)
	distance = randint(1, 10)

	# if direction is 0 move left
	if direction == 0:
		x_l = coordinates[0] - distance
		y_u = coordinates[1]
		x_r = coordinates[2] - distance
		y_d = coordinates[3]

	# if direction is 1 move right
	elif direction == 1:
		x_l = coordinates[0] + distance
		y_u = coordinates[1]
		x_r = coordinates[2] + distance
		y_d = coordinates[3]

	# if direction is 2 move up
	elif direction == 2:
		x_l = coordinates[0]
		y_u = coordinates[1] + distance
		x_r = coordinates[2]
		y_d = coordinates[3] + distance

	# if direction is 3 move down
	elif direction == 3:
		x_l = coordinates[0]
		y_u = coordinates[1] - distance
		x_r = coordinates[2]
		y_d = coordinates[3] - distance

	# set new coordinates
	new_cord = [x_l, y_u, x_r, y_d, coordinates[4]]

	return new_cord

def housetype(housenumber):
		if housenumber == 1:
			build = single
		elif housenumber == 2:
			build = bungalow
		elif housenumber == 3:
			build = maison

		return build
