import csv
from random import randint
from mutaties import determine_worth, house_swap, rotate_house, move_house
from mutaties import housetype, reset, move, create_change, cancel_change
from houses import House, Single, Bungalow, Maison
from grid import Area
from random_algoritme import random

# Hill Climber algoritm
def hill_climber(nr_of_houses, starting_state):

	with open('hallo.csv', 'w', newline='') as csvfile:
		fieldnames = ['algoritme', 'score', 'housecount', 'climb','swaps']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		# starts by running random algoritm to generate starting state
		current_coordinate_list = starting_state[0]
		water_coordinates = starting_state[1]
		total_value = starting_state[2]
		grid = starting_state[3]

		# set counters at 0
		swaps = 0
		no_swap = 0
		climb = 0

		# climb until 200 changes are made or 1000 tries
		while (swaps < 200 and climb < 1000):

			# create a mutation on the grid
			swapresults = create_change(current_coordinate_list, nr_of_houses, grid)

			# if the change was succesful take the results
			if swapresults != None:
				new_coordinate_list = swapresults[0]
				new_grid = swapresults[1]
				old_house_cords = swapresults[2]
				old_space_cords = swapresults[3]
				coordinate_number = swapresults[4]
				new_space_cords = swapresults[5]

				# determine worth new grid
				worth = determine_worth(new_coordinate_list, new_grid)

				# if new grid is worth more, accept this grid
				if worth > total_value:
					current_coordinate_list = new_coordinate_list
					total_value = worth
					grid = new_grid
					swaps += 1
					climb += 1
					no_swap = 0
					writer.writeheader()
					writer.writerow({'algoritme': 'HillClimber',
						'score': worth, 'housecount': nr_of_houses,
						'climb': climb, 'swaps' : swaps})

				# if new grid is worth less cancel the changes
				else:
					cancel = cancel_change(current_coordinate_list,
						grid, old_house_cords, old_space_cords,
						coordinate_number, new_space_cords)
					current_coordinate_list = cancel[0]
					grid = cancel[1]
					no_swap += 1
					climb += 1

					# if there has been no change for 100 tries stop
					if no_swap > 100:
						break

		# return the new grid
		print(total_value)
		return([current_coordinate_list, water_coordinates, total_value])
