import csv

from mutaties import determine_worth
from mutaties import house_swap
from mutaties import rotate_house
from mutaties import move_house
from mutaties import housetype
from mutaties import reset
from mutaties import move

from houses import house
from houses import single
from houses import bungalow
from houses import maison

from grid import Area
from random_algoritme import Random

from random import randint

# Hill Climber algoritm
def HillClimber(nr_of_houses):

	with open('scores.csv', 'w', newline='') as csvfile:
		fieldnames = ['algoritme', 'score', 'housecount', 'climb','swaps', 'change']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		# starts with running random algoritm to generate starting state
		starting_state = Random(nr_of_houses)
		current_coordinate_list = starting_state[0]
		water_coordinates = starting_state[1]
		total_value = starting_state[2]
		grid = starting_state[3]

		swaps = 0
		no_swap = 0
		climb = 0
		
		# set number of changes needed to make
		while climb < 500:
			worth = 0

			# choose between different hill climbing methods
			change = randint(2, 3)

			# change 1 then swap two houses
			if change == 1:
				swapresults = house_swap(current_coordinate_list, nr_of_houses, grid)

			# change 2 then move a house by 1 m
			elif change == 2:
				swapresults = move_house(current_coordinate_list, nr_of_houses, grid)

			elif change == 3:
				swapresults = rotate_house(current_coordinate_list, nr_of_houses, grid)

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
					print("ja")
					current_coordinate_list = new_coordinate_list
					total_value = worth
					grid = new_grid
					swaps += 1
					climb += 1
					no_swap = 0
					writer.writeheader()
					writer.writerow({'algoritme': 'HillClimber', 'score': worth, 'housecount': nr_of_houses, 'climb': climb, 'swaps' : swaps, 'change': change})
				
				else:
					grid = Area().create_space(new_space_cords, grid)
					grid = reset(grid, old_house_cords, old_space_cords)
					current_coordinate_list[coordinate_number] = old_house_cords
					print("nee")
					no_swap += 1
					climb += 1
					if no_swap > 100:
						break

		# return the new grid
		return([current_coordinate_list, water_coordinates, total_value])

