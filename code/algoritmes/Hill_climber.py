from houses import *
from grid import *
from water import *
from random_algoritme import *

import random as random

# Hill climbing
# Evaluate the initial state.
# Loop until a solution is found or there are no new operators left to be applied:
# -	select and apply an operation to the current state and get a new state
# -	evaluate the new state:
# 		compare it to the goal --> quit
# 		new state better than current state? --> update current state

def Hill_Climber(nr_of_houses):
	starting_state = Random(nr_of_houses)

	current_coordinate_list = starting_state[0]
	water_coordinates = starting_state[1]
	total_value = starting_state[2]
	grid = starting_state[3]
	print(total_value)

	
	nr_of_changes = 100
	for i in range(nr_of_changes):
		worth = 0
		swapresults = house_swap(current_coordinate_list, nr_of_houses, grid)
		new_coordinate_list = swapresults[0]
		new_grid = swapresults[1]
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
		if worth > total_value:
			current_coordinate_list = new_coordinate_list
			total_value = worth
			grid = new_grid
			print("we swap")

	Area().makegrid(current_coordinate_list, water_coordinates, total_value)

def house_swap(coordinate_list, nr_of_houses, grid):
	#changeOptions = [1, 2, 3, 4]
	#change = random.choice(changeOptions)
	house_one = randint(0, (nr_of_houses -1))
	house_two = randint(0, (nr_of_houses - 1))
	
	house_cords_one = coordinate_list[house_one]
	print(house_cords_one)
	house_cords_two = coordinate_list[house_two]
	print(house_cords_two)
	
	width_one = house_cords_one[2] - house_cords_one[0]
	height_one = house_cords_one[1] - house_cords_one[3]
	width_two = house_cords_two[2] - house_cords_two[0]
	height_two = house_cords_two[1] - house_cords_two[3]

	x_one = house_cords_two[0]
	y_one = house_cords_two[1]
	new_cord_one = [x_one, y_one, (x_one + width_one), (y_one - height_one), house_cords_one[4]]
	print(new_cord_one)

	x_two = house_cords_one[0]
	y_two = house_cords_one[1]
	new_cord_two = [x_two, y_two, (x_two + width_two), (y_two - height_two), house_cords_two[4]]
	print(new_cord_two)

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

	if Area().create_space(space_cords_one, grid) == True:
		if Area().create_space(space_cords_two, grid) == True:		
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
			
			if Area().housecheck(grid, new_cord_one) == True:
				if Area().housecheck(grid, new_cord_two) == True:
					if Area().spacecheck(grid, space_cords_one) == True:
						if Area().spacecheck(grid, space_cords_two) == True:
							grid = Area().update_grid(grid, new_cord_one, "single")
							coordinate_list[house_one] = new_cord_two
							grid = Area().update_grid(grid, new_cord_two, "single")
							coordinate_list[house_two] = new_cord_one

	return [coordinate_list, grid]

# 		randomHouse = random.choice(houseCords)
# 		width = height
# 		height = width
# 		newCords = []
# 		# deleting randomHouse (oude coordinaten)
# 		# adding newCords
# 		grid = Area().update_grid(grid, newCords, "house")
# 		NewState = grid
# 		valueNewState =
# 		return NewState, valueNewState

# # 	if change == 2:
# #	random verplaatsen van random huis
# # 	if change == 3:
# #	swapping random houses
# # 	if change == 4:
# #	changing/moving water


# def HillClimbing():
# while (solution not found or states left to check)
# 	if valueNewState >= goalValue:
# 		return True
# 	elif valueNewState >= valueCurrentState
# 		CurrentState = NewState
# 	else
# 		do it again
