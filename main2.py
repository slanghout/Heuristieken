# Authors: Dewi Mooij, Sylvie Langhout & Pernille Deijlen
# Amstelhaege

import os, sys
import csv
import time

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from grid import Area
from kerkhof import kerkhof
from hill_climber import hill_climber
from random_algoritme import random_algoritme
from simulated_annealing import simulated_annealing

def main():
	
	# ask user for nr of houses they want
	nr_of_houses = int(input("Would you like 20, 40 or 60 houses? "))
	if nr_of_houses != 20 and nr_of_houses != 40 and nr_of_houses != 60:
		print("invalid number of houses")
		exit(0)

	# ask what algoritm they want
	alg = input("Select A for Random, B for Hill Climber, C for Simulated Annealing ")
	if alg != "A" and alg != "B" and alg != "C":
		print("this is not what I wanted")
		exit(0)

	best_gridvalues = []

	# if uses picks A, run random algoritm
	if alg == "A":
		with open('standard_verdeling.csv', 'w', newline='') as csvfile:
			fieldnames = ['algoritme', 'score', 'housecount']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			repeats = int(input("How many times do you want to run the algoritm? "))
			distribution = input("Standard (A) or random (B) distribution of houses? ")
			starttime = time.time()
			for repeat in range(repeats):
				print(repeat)
				gridvalue = random_algoritme(nr_of_houses, distribution)
				writer.writeheader()
				writer.writerow({'algoritme': 'Random', 'score': gridvalue[2], 'housecount': nr_of_houses})
				if len(best_gridvalues) != 0:
					if best_gridvalues[2] > gridvalue[2]:
						pass
					else:
						best_gridvalues = gridvalue
				else:
					best_gridvalues = gridvalue

			coordinate_list = best_gridvalues[0]
			water_coordinates = best_gridvalues[1]
			total_value = best_gridvalues[2]
			end = time.time()

	# if uses picks B, run hill climber algoritm
	if alg == "B":
		# starting_state = (input("Is starting state Random(A) or Kerkhof(B)?"))
		distribution = input("Standard (A) or random (B) distribution of houses? ")
		
		# if starting_state == "A":
		start = random_algoritme(nr_of_houses, distribution)
		# elif starting_state == "B":
		# 	start = kerkhof(nr_of_houses)
		
		starttime = time.time()
		final = hill_climber(nr_of_houses, start)

		coordinate_list = final[0]
		water_coordinates = final[1]
		total_value = final[2]
		end = time.time()

	# if uses picks C, run simulated annealing algoritm
	if alg == "C":
		starttime = time.time()
		final = simulated_annealing(nr_of_houses)

		coordinate_list = final[0]
		water_coordinates = final[1]
		total_value = final[2]
		end = time.time()

	# print runtime, value of grid and grid
	print("time{}".format(end - starttime))
	print("value: {}".format(total_value))
	Area().make_grid(coordinate_list, water_coordinates, total_value)


if __name__ == "__main__":
	main()