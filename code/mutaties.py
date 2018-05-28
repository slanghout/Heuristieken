import csv
from houses import House, Single, Bungalow, Maison
from grid import Area
from random import randint

# function to determine what mutation to be made on grid
def create_change(current_coordinate_list, nr_of_houses, grid):
	change = randint(1, 3)

	# change 1 then swap two houses
	if change == 1:
		swapresults = house_swap(current_coordinate_list, nr_of_houses, grid)

	# change 2 then move a house
	elif change == 2:
		swapresults = move_house(current_coordinate_list, nr_of_houses, grid)

	# change 3 then rotate house
	elif change == 3:
		swapresults = rotate_house(current_coordinate_list, nr_of_houses, grid)

	return swapresults

# function to determine if new grid is worth more than old grid
def determine_worth(coordinate_list, grid):
	worth = 0
	for cordinate in coordinate_list:
		build = house_type(cordinate[4])
		cord = (cordinate[0], cordinate[1])
		price = build(cord).give_worth(cordinate, grid)
		if price != None:
			worth += price

	return worth

# function that swaps two houses in the grid
def house_swap(coordinate_list, nr_of_houses, grid):

	# randomly pick two houses from the coordinate list
	house_one = randint(0, (nr_of_houses -1))
	house_two = randint(0, (nr_of_houses - 1))
	if house_one == house_two:
		return None

	# look at old coordinates
	old_cords_one = coordinate_list[house_one]
	old_cords_two = coordinate_list[house_two]

	# create new coordinates
	new_cord_one = create_coordinates(old_cords_two, old_cords_one[4], 1, 0)
	new_cord_two = create_coordinates(old_cords_one, old_cords_two[4], 1, 0)

	# create space coordinates of old coordinates
	build = house_type(old_cords_one[4])
	cord_one = (old_cords_one[0], old_cords_one[1])
	space_old_cords_one = build(cord_one).space_house(old_cords_one)
	
	build = house_type(old_cords_two[4])
	cord_two = (old_cords_two[0], old_cords_two[1])
	space_old_cords_two = build(cord_two).space_house(old_cords_two)

	# create coordinates with space for new coordinates
	build = house_type(new_cord_one[4])
	cord_one_new = (new_cord_one[0], new_cord_one[1])
	new_space_cords_one = build(cord_one_new).space_house(new_cord_one)

	# check if space is in grid
	if (new_space_cords_one[0] < 0 or new_space_cords_one[3] < 0 or
		new_space_cords_one[1] > 320 or new_space_cords_one[2] > 360):
		return None

	# also for the second house
	build = house_type(new_cord_two[4])
	cord_two_new = (new_cord_two[0], new_cord_two[1])
	new_space_cords_two = build(cord_two_new).space_house(new_cord_two)

	if (new_space_cords_two[0] < 0 or new_space_cords_two[3] < 0 or
		new_space_cords_two[1] > 320 or new_space_cords_two[2] > 360):
		return None

	# clear the space the houses were using
	grid = Area().create_space(space_old_cords_one, grid)
	grid = Area().create_space(space_old_cords_two, grid)

	# check if there is enough space to place house
	if Area().house_check(grid, new_cord_one) == True:
		if Area().space_check(grid, new_space_cords_one) == True:
			grid = reset(grid, new_cord_one, new_space_cords_one)
			coordinate_list[house_one] = new_cord_two
			
			if Area().house_check(grid, new_cord_two) == True:
				if Area().space_check(grid, new_space_cords_two) == True:
					grid = reset(grid, new_cord_two, new_space_cords_two)
					coordinate_list[house_two] = new_cord_one

				else:
					cancel = cancel_change(coordinate_list, grid,
					[old_cords_one, old_cords_two], [space_old_cords_one, space_old_cords_two],
					[house_one, house_two], [new_space_cords_one])
					coordinate_list = cancel[0]
					grid = cancel[1]
					return None
			else:
				cancel = cancel_change(coordinate_list, grid,
				[old_cords_one, old_cords_two], [space_old_cords_one, space_old_cords_two],
				[house_one, house_two], [new_space_cords_one])
				coordinate_list = cancel[0]
				grid = cancel[1]
				return None
		
		else:
			grid = reset(grid, old_cords_one, space_old_cords_one)
			grid = reset(grid, old_cords_two, space_old_cords_two)
			return None
	else:
		grid = reset(grid, old_cords_one, space_old_cords_one)
		grid = reset(grid, old_cords_two, space_old_cords_two)
		return None			

	# if the houses were swapped return the grid information
	return [coordinate_list, grid, [old_cords_one, old_cords_two], [space_old_cords_one, space_old_cords_two], [house_one, house_two], [new_space_cords_one, new_space_cords_two]]

# function that moves a house by 1 coordinate
def move_house(coordinate_list, nr_of_houses, grid):

	# randomly pick one house from the coordinate list
	move_house = randint(0, (nr_of_houses -1))
	cord_move_house = coordinate_list[move_house]

	new_cord = move(cord_move_house)

	# determine space needed first
	build = house_type(cord_move_house[4])
	cord = (cord_move_house[0], cord_move_house[1])
	space_cords = build(cord).space_house(cord_move_house)

	# determine space needed after move
	build = house_type(new_cord[4])
	cord = (new_cord[0], new_cord[1])
	new_space_cords = build(cord).space_house(new_cord)

	if (new_space_cords[0] < 0 or new_space_cords[3] < 0 or
		new_space_cords[1] > 320 or new_space_cords[2] > 360):
		return None
	
	# clear the space the house was using
	grid = Area().create_space(space_cords, grid)

	# check if there is enough space to place house
	if Area().house_check(grid, new_cord) == True:

		# check if there is space to place house with extra space
		if Area().space_check(grid, new_space_cords) == True:

			# if everything is true move the house
			grid = reset(grid, new_cord, new_space_cords)
			coordinate_list[move_house] = new_cord

		else:
			grid = reset(grid, cord_move_house, space_cords)
			return None

	else:
		grid = reset(grid, cord_move_house, space_cords)
		return None

	# if the house was moved return the grid information
	return [coordinate_list, grid, cord_move_house, space_cords, move_house, new_space_cords]

# function that rotates a house
def rotate_house(coordinate_list, nr_of_houses, grid):

	# randomly pick one house from the coordinate list
	rotate_house = randint(0, (nr_of_houses -1))
	cord_rotate_house = coordinate_list[rotate_house]

	new_cord = create_coordinates(cord_rotate_house, cord_rotate_house[4], 0, 1)
	build = house_type(cord_rotate_house[4])
	cord = (cord_rotate_house[0], cord_rotate_house[1])
	space_cords = build(cord).space_house(cord_rotate_house)

	cord = (new_cord[0], new_cord[1])
	new_space_cords = build(cord).space_house(new_cord)

	if (new_space_cords[0] < 0 or new_space_cords[3] < 0 or
		new_space_cords[1] > 320 or new_space_cords[2] > 360):
		return None

	# clear the space the house was using
	grid = Area().create_space(space_cords, grid)

	# check if there is enough space to rotate house
	if Area().house_check(grid, new_cord) == True:

		# check if there is space to place house with extra space
		if Area().space_check(grid, new_space_cords) == True:

			# if everything is true rotate house
			grid = reset(grid, new_cord, new_space_cords)
			coordinate_list[rotate_house] = new_cord

		else:
			grid = reset(grid, cord_rotate_house, space_cords)
			return None

	else:
		grid = reset(grid, cord_rotate_house, space_cords)
		return None

	# if the house was rotated return the grid information
	return [coordinate_list, grid, cord_rotate_house, space_cords, rotate_house, new_space_cords]

# function that resets grid
def reset(grid, house_coordinates, space_coordinates):
	grid = Area().update_grid(grid, house_coordinates, "house")
	grid = Area().update_grid(grid, space_coordinates, "space")
	return grid

# function to move houses
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

# function that defines which type the house is
def house_type(housenumber):
		if housenumber == 1:
			build = Single
		elif housenumber == 2:
			build = Bungalow
		elif housenumber == 3:
			build = Maison

		return build

# function to go back to previous state
def cancel_change(current_coordinate_list, grid, old_house_cords, old_space_cords, coordinate_number, new_space_cords):
	if len(old_house_cords) == 2 and len(new_space_cords) == 2:
		grid = Area().create_space(new_space_cords[0], grid)
		grid = Area().create_space(new_space_cords[1], grid)
		grid = reset(grid, old_house_cords[0], old_space_cords[0])
		grid = reset(grid, old_house_cords[1], old_space_cords[1])
		current_coordinate_list[coordinate_number[0]] = old_house_cords[0]
		current_coordinate_list[coordinate_number[1]] = old_house_cords[1]
	
	elif len(new_space_cords) == 1:
		grid = Area().create_space(new_space_cords[0], grid)
		grid = reset(grid, old_house_cords[0], old_space_cords[0])
		grid = reset(grid, old_house_cords[1], old_space_cords[1])
		current_coordinate_list[coordinate_number[0]] = old_house_cords[0]
		current_coordinate_list[coordinate_number[1]] = old_house_cords[1]
		
	else:
		grid = Area().create_space(new_space_cords, grid)
		grid = reset(grid, old_house_cords, old_space_cords)
		current_coordinate_list[coordinate_number] = old_house_cords
	
	return [current_coordinate_list, grid]

# function that returns new coordinates
def create_coordinates(coordinates, i, j):
	build = house_type(coordinates[4])

# function that makes coordinates
def create_coordinates(coordinates, housenumber, i, j):
	build = house_type(housenumber)
	cords = (coordinates[0], coordinates[1])
	size = build(cords).give_size()
	height = size[i]
	width = size[j]

	x_l = coordinates[0]
	y_u = coordinates[1]
	x_r = coordinates[0] + width
	y_d = coordinates[1] - height

	new_coordinates = [x_l, y_u, x_r, y_d, housenumber]

	return new_coordinates
