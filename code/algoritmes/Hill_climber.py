from houses import *
from grid import *
from water import *
from random_algoritme import *

import random as random

# hill Climber algoritm
def Hill_Climber(nr_of_houses, repeats):
	
	# starts with running random algoritm to generate starting state
	starting_state = Random(nr_of_houses)
	current_coordinate_list = starting_state[0]
	water_coordinates = starting_state[1]
	total_value = starting_state[2]
	grid = starting_state[3]
	print(total_value)
	
	# set number of changes needed to make
	for changes in range(repeats):
		worth = 0

		# choose between different hill climbing methods
		change = 3 #randint(1, 3)
		
		# change 1 then swap two houses
		if change == 1:
			swapresults = house_swap(current_coordinate_list, nr_of_houses, grid)
			new_coordinate_list = swapresults[0]
			new_grid = swapresults[1]
		
		# change 2 then move a house by 1 m
		elif change == 2:
			swapresults = move_house(current_coordinate_list, nr_of_houses, grid)
			new_coordinate_list = swapresults[0]
			new_grid = swapresults[1]

		elif change == 3:
			swapresults = rotate_house(current_coordinate_list, nr_of_houses, grid)
			new_coordinate_list = swapresults[0]
			new_grid = swapresults[1]
		
		# determine of new grid is worth more than old grid
		for cordinate in new_coordinate_list:
			cord = (cordinate[0], cordinate[1])
			if cordinate[4] == 1:
				build = single
			elif cordinate[4] == 2:
				build = bungalow
			elif cordinate[4] == 3:
				build = maison
			price = build(cord).giveworth(cordinate, new_grid)
			if price != None:
				worth += price
		
		# if new grid is worth more, accept this grid
		if worth > total_value:
			current_coordinate_list = new_coordinate_list
			total_value = worth
			grid = new_grid
			print(changes)

	# return the new grid
	return([current_coordinate_list, water_coordinates, total_value])

# function that swaps two houses in the grid
def house_swap(coordinate_list, nr_of_houses, grid):
	
	# randomly pick two houses from the coordinate list
	house_one = randint(0, (nr_of_houses -1))
	house_two = randint(0, (nr_of_houses - 1))
	house_cords_one = coordinate_list[house_one]
	house_cords_two = coordinate_list[house_two]
	
	# determine height and width of the houses
	width_one = house_cords_one[2] - house_cords_one[0]
	height_one = house_cords_one[1] - house_cords_one[3]
	width_two = house_cords_two[2] - house_cords_two[0]
	height_two = house_cords_two[1] - house_cords_two[3]

	# create new coordinates for the houses
	# take the left upper corner
	# determine new coordinates with height and width
	x_one = house_cords_two[0]
	y_one = house_cords_two[1]
	new_cord_one = [x_one, y_one, (x_one + width_one), (y_one - height_one), house_cords_one[4]]
	x_two = house_cords_one[0]
	y_two = house_cords_one[1]
	new_cord_two = [x_two, y_two, (x_two + width_two), (y_two - height_two), house_cords_two[4]]

	# determine the space needed for old houses
	if house_cords_one[4] == 1:
		build = single
	elif house_cords_one[4] == 2:
		build = bungalow
	elif house_cords_one[4] == 3:
		build = maison
	cord = (x_one, y_one)
	space_cords_one = build(cord).spacehouse(new_cord_one)

	if house_cords_two[4] == 1:
		build = single
	elif house_cords_two[4] == 2:
		build = bungalow
	elif house_cords_two[4] == 3:
		build = maison
	cord = (x_two, y_two)
	space_cords_two = build(cord).spacehouse(new_cord_two)

	# clear the space the houses were using
	if Area().create_space(space_cords_one, grid) == True:
		if Area().create_space(space_cords_two, grid) == True:		
			
			# determine space needed for new houses
			if new_cord_one[4] == 1:
				build = single
			elif new_cord_one[4] == 2:
				build = bungalow
			elif new_cord_one[4] == 3:
				build = maison
			cord = (x_one, y_one)
			space_cords_one = build(cord).spacehouse(new_cord_one)

			if new_cord_two[4] == 1:
				build = single
			elif new_cord_two[4] == 2:
				build = bungalow
			elif new_cord_two[4] == 3:
				build = maison
			cord = (x_two, y_two)
			space_cords_two = build(cord).spacehouse(new_cord_two)
			
			# check if there is enough space to place house
			if Area().housecheck(grid, new_cord_one) == True:
				if Area().housecheck(grid, new_cord_two) == True:
					
					# check if there is space to place house with extra space
					if Area().spacecheck(grid, space_cords_one) == True:
						if Area().spacecheck(grid, space_cords_two) == True:
							
							# if everything is true swap the houses
							grid = Area().update_grid(grid, new_cord_one, "house")
							coordinate_list[house_one] = new_cord_two
							grid = Area().update_grid(grid, new_cord_two, "house")
							coordinate_list[house_two] = new_cord_one

	# if the houses were swapped return the grid information
	return [coordinate_list, grid]

# function that moves a house by 1 coordinate
def move_house(coordinate_list, nr_of_houses, grid):
	
	# randomly pick one house from the coordinate list
	move_house = randint(0, (nr_of_houses -1))
	cord_move_house = coordinate_list[move_house]

	# choose in which direction the house will move
	direction = randint(0, 3)

	# if direction is 0 move left
	if direction == 0:
		x_l = cord_move_house[0] - 2
		y_u = cord_move_house[1]
		x_r = cord_move_house[2] - 2
		y_d = cord_move_house[3]
	
	# if direction is 1 move right
	elif direction == 1:
		x_l = cord_move_house[0] + 2
		y_u = cord_move_house[1]
		x_r = cord_move_house[2] + 2
		y_d = cord_move_house[3]
	
	# if direction is 2 move up
	elif direction == 2:
		x_l = cord_move_house[0] 
		y_u = cord_move_house[1] + 2 
		x_r = cord_move_house[2] 
		y_d = cord_move_house[3] + 2
	
	# if direction is 3 move down
	elif direction == 3:
		x_l = cord_move_house[0] 
		y_u = cord_move_house[1] - 2
		x_r = cord_move_house[2] 
		y_d = cord_move_house[3] - 2

	# set new coordinates
	new_cord = [x_l, y_u, x_r, y_d, cord_move_house[4]]

	# determine space needed first
	if cord_move_house[4] == 1:
		build = single
	elif cord_move_house[4] == 2:
		build = bungalow
	elif cord_move_house[4] == 3:
		build = maison
	cord = (cord_move_house[0], cord_move_house[1])
	space_cords = build(cord).spacehouse(cord_move_house)

	# clear the space the houses were using
	if Area().create_space(space_cords, grid) == True:	
			
		# determine space needed for new houses
		if new_cord[4] == 1:
			build = single
		elif new_cord[4] == 2:
			build = bungalow
		elif new_cord[4] == 3:
			build = maison
		cord = (new_cord[0], new_cord[1])
		new_space_cords = build(cord).spacehouse(new_cord)
		
		# check if there is enough space to place house
		if Area().housecheck(grid, new_cord) == True:
				
			# check if there is space to place house with extra space
			if Area().spacecheck(grid, new_space_cords) == True:
					
				# if everything is true swap the houses
				grid = Area().update_grid(grid, new_cord, "house")
				coordinate_list[move_house] = new_cord

	# if the houses were swapped return the grid information
	return [coordinate_list, grid]

# function that rotates a house
def rotate_house(coordinate_list, nr_of_houses, grid):
	
	# randomly pick one house from the coordinate list
	rotate_house = randint(0, (nr_of_houses -1))
	cord_rotate_house = coordinate_list[rotate_house]

	# determine height and width of the houses
	width = cord_rotate_house[2] - house_cords_one[0]
	height = cord_rotate_house[1] - house_cords_one[3]

	# set coordinates for rotated house
	x_l = cord_rotate_house[0]
	y_u = cord_rotate_house[1]
	x_r = cord_rotate_house[0] + height
	y_d = cord_rotate_house[1] - width
	
	# set new coordinates
	new_cord = [x_l, y_u, x_r, y_d, cord_rotate_house[4]]

	# determine space needed first
	if cord_rotate_house[4] == 1:
		build = single
	elif cord_rotate_house[4] == 2:
		build = bungalow
	elif cord_rotate_house[4] == 3:
		build = maison
	cord = (cord_rotate_house[0], cord_rotate_house[1])
	space_cords = build(cord).spacehouse(cord_rotate_house)

	# clear the space the houses were using
	if Area().create_space(space_cords, grid) == True:	
			
		# determine space needed for new houses
		if new_cord[4] == 1:
			build = single
		elif new_cord[4] == 2:
			build = bungalow
		elif new_cord[4] == 3:
			build = maison
		cord = (new_cord[0], new_cord[1])
		new_space_cords = build(cord).spacehouse(new_cord)
		
		# check if there is enough space to place house
		if Area().housecheck(grid, new_cord) == True:
				
			# check if there is space to place house with extra space
			if Area().spacecheck(grid, new_space_cords) == True:
					
				# if everything is true swap the houses
				grid = Area().update_grid(grid, new_cord, "house")
				coordinate_list[move_house] = new_cord

	# if the houses were swapped return the grid information
	return [coordinate_list, grid]

