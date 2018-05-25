from random import randint, uniform
import math
import csv
from mutaties import determine_worth, house_swap, rotate_house, move_house
from mutaties import house_type, reset, move, create_change, cancel_change
from houses import House, Single, Bungalow, Maison
from grid import Area
from random_algoritme import random_algoritme

# Simulated annealing algoritm
def simulated_annealing(nr_of_houses, starting_state):

	# starts by running random algoritm to generate starting state
	current_coordinate_list = starting_state[0]
	water_coordinates = starting_state[1]
	total_value = starting_state[2]
	grid = starting_state[3]

	# set temperature at 1 and counters at 0
	temperature = 1.0
	swaps = 0
	same = 0
	no_swap = 0
	climb = 0
	coolings = 0
	heatings = 1

	# continue algoritm while temperature is above 0.01
	while temperature > 0.01:
		swaps = 0

		# after every 20 iterations reset temperature
		while climb < 20 * (coolings + 1):
			climb += 1

			# create mutation on existing grid
			swapresults = create_change(current_coordinate_list,
				nr_of_houses, grid)

			# if the change was succesful take the results
			if swapresults != None:
				new_coordinate_list = swapresults[0]
				new_grid = swapresults[1]
				old_house_cords = swapresults[2]
				old_space_cords = swapresults[3]
				coordinate_number = swapresults[4]
				new_space_cords = swapresults[5]

				# determine new price of grid after change
				worth = determine_worth(new_coordinate_list, new_grid)

				# if new grid is worth more, accept this grid
				if worth >= total_value:
					if worth > total_value:
						swaps += 1
						same = 0
						no_swap = 0
					else:
						same += 1
					current_coordinate_list = new_coordinate_list
					total_value = worth
					grid = new_grid
					swaps += 1
					no_swap = 0

				# if worth is less create acceptance and random value
				elif worth < total_value:
					randomnumber = uniform(0.5, 1.0)
					ap = acceptance(total_value, worth, temperature)

					# accept it if acceptance higher than random number
					if ap > randomnumber:
						current_coordinate_list = new_coordinate_list
						total_value = worth
						grid = new_grid
						swaps += 1
						no_swap = 0

					# else cancel the change made
					else:
						cancel = cancel_change(current_coordinate_list,
							grid, old_house_cords, old_space_cords,
							coordinate_number, new_space_cords)
						current_coordinate_list = cancel[0]
						grid = cancel[1]
						no_swap += 1
						
					# if there has been no improved change for 100 tries stop
					if no_swap > 100 or same > 100:
							temperature = 0.0001

			# after 40 temperature coolings, reset the temperature
			if coolings == 40 * heatings:
				temperature = 1.0*(0.9**heatings)
				heatings += 1

		# lower temperature after 20 iterations
		temperature = temperature * 0.95
		coolings += 1

	# return the new grid
	return([current_coordinate_list, water_coordinates, total_value])

# function to create acceptance from value and temperature
def acceptance(old, new, temperature):
	delta = (new-old)/100000
	return (math.e)**(delta/temperature)
