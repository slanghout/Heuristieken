import csv

from mutaties import determine_worth
from mutaties import house_swap
from mutaties import rotate_house
from mutaties import move_house
from mutaties import housetype
from mutaties import reset
from mutaties import move
from mutaties import create_change
from mutaties import cancel_change

from houses import House, Single, Bungalow, Maison

from grid import Area
from random_algoritme import random

from random import randint

# Hill Climber algoritm
def hill_climber(nr_of_houses, starting_state):

	with open('hallo.csv', 'w', newline='') as csvfile:
		fieldnames = ['algoritme', 'score', 'housecount', 'climb','swaps']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		# starts by running random algoritm to generate starting state
		# starting_state = Random(nr_of_houses)
		current_coordinate_list = starting_state[0]
		water_coordinates = starting_state[1]
		total_value = starting_state[2]
		grid = starting_state[3]

		swaps = 0
		no_swap = 0
		climb = 0
		
		# set number of changes needed to make
		while (swaps < 200 and climb < 1000):
			worth = 0

			swapresults = create_change(current_coordinate_list, nr_of_houses, grid)

			if swapresults != None:
				new_coordinate_list = swapresults[0]
				new_grid = swapresults[1]
				old_house_cords = swapresults[2]
				old_space_cords = swapresults[3]
				coordinate_number = swapresults[4]
				new_space_cords = swapresults[5]

				worth = determine_worth(new_coordinate_list, new_grid)

				# if new grid is worth more, accept this grid
				if worth > total_value:
					current_coordinate_list = new_coordinate_list
					total_value = worth
					grid = new_grid
					swaps += 1
					print("ja{}".format(swaps))
					climb += 1
					no_swap = 0
					writer.writeheader()
					writer.writerow({'algoritme': 'HillClimber', 'score': worth, 'housecount': nr_of_houses, 'climb': climb, 'swaps' : swaps})
				
				else:
					cancel = cancel_change(current_coordinate_list, grid, old_house_cords, old_space_cords, coordinate_number, new_space_cords)
					current_coordinate_list = cancel[0]
					grid = cancel[1]
					no_swap += 1
					print("nee{}".format(no_swap))
					climb += 1
					
					if no_swap > 100:
						break

		# return the new grid
		print(total_value)
		return([current_coordinate_list, water_coordinates, total_value])