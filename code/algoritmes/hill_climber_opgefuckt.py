import csv

from houses import house
from houses import single
from houses import bungalow
from houses import maison

from grid import Area
from random_algoritme import Random

from random import randint

# Hill Climber algoritm
def HillClimber(nr_of_houses):

	# starts with running random algoritm to generate starting state
	starting_state = Random(nr_of_houses)
	current_coordinate_list = starting_state[0]
	water_coordinates = starting_state[1]
	current_value = starting_state[2]
	current_grid = starting_state[3]

	best_coordinate_list = current_coordinate_list
	best_grid = current_grid
	best_value = current_value

	with open('scores.csv', 'w', newline='') as csvfile:
		fieldnames = ['algoritme', 'score', 'housecount']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


		swaps = 0
		no_swap = 0
		# set number of changes needed to make
		while swaps < 100:

			# choose between different hill climbing methods
			change = 1 #randint(1, 3)

			# change 1 then swap two houses
			if change == 1:
				swapresults = house_swap(current_coordinate_list, nr_of_houses, current_grid)

			# change 2 then move a house by 1 m
			elif change == 2:
				swapresults = move_house(current_coordinate_list, nr_of_houses, current_grid)

			elif change == 3:
				swapresults = rotate_house(current_coordinate_list, nr_of_houses, current_grid)

			if swapresults != None:
				new_coordinate_list = swapresults[0]
				new_grid = swapresults[1]

				new_value = 0
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
						new_value += price

				# print("nieuw{} vs best {} vs nu{}" .format(new_value, best_value, current_value))
				# if new grid is worth more, accept this grid
				if new_value > best_value:
					print("ja")
					best_coordinate_list = new_coordinate_list
					best_value = new_value
					best_grid = new_grid
					swaps += 1
					no_swap = 0
					writer.writeheader()
					writer.writerow({'algoritme': 'HillClimber', 'score': new_value, 'housecount': nr_of_houses})
			
				else:
					print("nee")
					no_swap += 1
					current_coordinate_list = best_coordinate_list
					current_grid = best_grid
					current_value = best_value
					if no_swap > 100:
						break
			else:
				current_grid = best_grid
				current_value = best_value
				current_coordinate_list = best_coordinate_list

		# return the new grid
		return([best_coordinate_list, water_coordinates, best_value])

# function that swaps two houses in the grid
def house_swap(coordinate_list, nr_of_houses, grid):

	# randomly pick two houses from the coordinate list
	house_one = randint(0, (nr_of_houses -1))
	house_two = randint(0, (nr_of_houses - 1))
	if house_one != house_two:

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
		x_l_one = house_cords_two[0]
		y_u_one = house_cords_two[1]
		x_r_one = house_cords_two[0] + width_one
		y_d_one = house_cords_two[1] - height_one

		new_cord_one = [x_l_one, y_u_one, x_r_one, y_d_one, house_cords_one[4]]

		x_l_two = house_cords_one[0]
		y_u_two = house_cords_one[1]
		x_r_two = house_cords_one[0] + width_two
		y_d_two = house_cords_one[1] - height_two
		new_cord_two = [x_l_two, y_u_two, x_r_two, y_d_two, house_cords_two[4]]

		# determine the space needed for old houses
		if house_cords_one[4] == 1:
			build = single
		elif house_cords_one[4] == 2:
			build = bungalow
		elif house_cords_one[4] == 3:
			build = maison
		cord = (x_l_one, y_u_one)
		old_space_cords_one = build(cord).spacehouse(house_cords_one)

		if house_cords_two[4] == 1:
			build = single
		elif house_cords_two[4] == 2:
			build = bungalow
		elif house_cords_two[4] == 3:
			build = maison
		cord = (x_l_two, y_u_two)
		old_space_cords_two = build(cord).spacehouse(house_cords_two)

		# print(grid)
		# clear the space the houses were using
		if Area().create_space(old_space_cords_one, grid) == True:
			
			if Area().create_space(old_space_cords_two, grid) == True:

				# determine space needed for new houses
				if new_cord_one[4] == 1:
					build = single
				elif new_cord_one[4] == 2:
					build = bungalow
				elif new_cord_one[4] == 3:
					build = maison
				cord = (x_l_one, y_d_one)
				new_space_cords_one = build(cord).spacehouse(new_cord_one)
				
				if new_space_cords_one[0] > 360:
					return None
				if new_space_cords_one[3] < 0:
					return None
				if new_space_cords_one[1] > 320:
					return None
				if new_space_cords_one[2] < 0:
					return None

				build = Area().housetype(new_cord_two)
				# if new_cord_two[4] == 1:
				# 	build = single
				# elif new_cord_two[4] == 2:
				# 	build = bungalow
				# elif new_cord_two[4] == 3:
				# 	build = maison
				cord = (x_l_two, y_d_two)
				new_space_cords_two = build(cord).spacehouse(new_cord_two)
				
				if new_space_cords_two[0] > 360:
					return None
				if new_space_cords_two[3] < 0:
					return None
				if new_space_cords_two[1] > 320:
					return None
				if new_space_cords_two[2] < 0:
					return None
		
				# check if there is space to place house with extra space
				if Area().spacecheck(grid, new_space_cords_one) == True:
					if Area().spacecheck(grid, new_space_cords_two) == True:
						
						# check if there is enough space to place house
						if Area().housecheck(grid, new_cord_one) == True:
							if Area().housecheck(grid, new_cord_two) == True:

								# if everything is true swap the houses
								grid = Area().update_grid(grid, new_cord_one, "house")
								coordinate_list[house_one] = new_cord_two
								grid = Area().update_grid(grid, new_cord_two, "house")
								coordinate_list[house_two] = new_cord_one
							else:
								return None
						else:
							return None
					else:
						return None
				else:
					return None

			else:
				return None
		else:
			return None

		
		print("swap")
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
	print(cord_move_house)
	print(space_cords)

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

		if new_space_cords[0] > 360:
			return None
		if new_space_cords[3] < 0:
			return None
		if new_space_cords[1] > 320:
			return None
		if new_space_cords[2] < 0:
			return None

		# check if there is space to place house with extra space
		if Area().spacecheck(grid, new_space_cords) == True:

			# check if there is enough space to place house
			if Area().housecheck(grid, new_cord) == True:

				# if everything is true swap the houses
				grid = Area().update_grid(grid, new_cord, "house")
				coordinate_list[move_house] = new_cord
			else:
				print("nah")
				return None
		else:
			print("naah")
			return None
	else:
		print("naaah")
		return None

	print("move")
	# if the houses were swapped return the grid information
	return [coordinate_list, grid]

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

		if new_space_cords[0] > 360:
			return None
		if new_space_cords[3] < 0:
			return None
		if new_space_cords[1] > 320:
			return None
		if new_space_cords[2] < 0:
			return None

		# check if there is space to place house with extra space
		if Area().spacecheck(grid, new_space_cords) == True:
			
			# check if there is enough space to place house
			if Area().housecheck(grid, new_cord) == True:

				# if everything is true swap the houses
				grid = Area().update_grid(grid, new_cord, "house")
				print(coordinate_list[rotate_house])
				coordinate_list[rotate_house] = new_cord
				print(coordinate_list[rotate_house])
			else:
				return None

		else:
			return None
	else:
		return None

	print("rotate")
	# if the houses were swapped return the grid information
	return [coordinate_list, grid]
