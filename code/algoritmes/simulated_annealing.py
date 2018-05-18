from houses import house
from houses import single
from houses import bungalow
from houses import maison

from grid import Area
from random_algoritme import Random
from Hill_climber import house_swap
from Hill_climber import move_house
from Hill_climber import rotate_house

from random import randint
from random import uniform
import math
import csv

# Hill Climber algoritm
def SimulatedAnnealing(nr_of_houses):

	# starts with running random algoritm to generate starting state
	starting_state = Random(nr_of_houses)
	current_coordinate_list = starting_state[0]
	water_coordinates = starting_state[1]
	total_value = starting_state[2]
	grid = starting_state[3]

	temperature = 1.0

	swaps = 0
	no_swap = 0
	with open('scores.csv', 'w', newline='') as csvfile:
		fieldnames = ['algoritme', 'score', 'housecount']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


		# set number of changes needed to make
		while temperature > 0.1:
			while swaps <= 100:

				worth = 0

				# choose between different hill climbing methods
				change = randint(1, 3)

				# change 1 then swap two houses
				if change == 1:
					swapresults = house_swap(current_coordinate_list, nr_of_houses, grid)

				# change 2 then move a house by 1 m
				elif change == 2:
					swapresults = move_house(current_coordinate_list, nr_of_houses, grid)

				elif change == 3:
					swapresults = rotate_house(current_coordinate_list, nr_of_houses, grid)


				new_coordinate_list = swapresults[0]
				new_grid = swapresults[1]
				print(new_coordinate_list)
				print(current_coordinate_list)

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
					swaps += 1
					no_swap = 0
					print("yes{}".format(swaps))
					writer.writeheader()
					writer.writerow({'algoritme': 'SimAnealinghoger', 'score': worth, 'housecount': nr_of_houses})
					continue

				elif worth < total_value:
					print("nu{} vs ooit{}".format(worth, total_value))
					ap = acceptance(total_value, worth, temperature)
					randomnumber = uniform(0, 1)
					print("ap{}".format(ap))
					print(randomnumber)
					if ap > randomnumber:
						current_coordinate_list = new_coordinate_list
						total_value = worth
						grid = new_grid
						swaps += 1
						no_swap = 0
						writer.writeheader()
						writer.writerow({'algoritme': 'SimAnealing', 'score': worth, 'housecount': nr_of_houses})
						print("randoswap{}".format(temperature))

				else:
					no_swap += 1
					if no_swap > 20:
						break
					print("no{}".format(no_swap))
			
				temperature = temperature * 0.9
					
			
			print("eruot")
			# return the new grid
			return([current_coordinate_list, water_coordinates, total_value])
		
		print("kom je hier")
		# return the new grid
		return([current_coordinate_list, water_coordinates, total_value])

def acceptance(old, new, temperature):
	return math.e**((old-new)/temperature)

