# Authors: Dewi Mooij, Sylvie Langhout & Pernille Deijlen
# Amstelhaege
import os, sys
import csv
import time

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "grid"))

from grid import Area
from kerkhof import kerkhof
from Hill_climber import hill_climber
from random_algoritme import random_algoritme
from simulated_annealing import simulated_annealing

def main():

	# ask user for nr of houses they want
	nr_of_houses = int(input("Would you like 20, 40 or 60 houses? "))
	if nr_of_houses != 20 and nr_of_houses != 40 and nr_of_houses != 60:
		print("invalid number of houses")
		exit(0)

	gridvalue = []

	# ask what algoritm they want
	alg = input("Select A for Random, B for Hill Climber, C for Simulated Annealing, D for Kerkhof ")
	if alg != "A" and alg != "B" and alg != "C" and alg != "D":
		print("this is not what I wanted")
		exit(0)

	# if uses picks A, run random algoritm
	elif alg == "A":
		distribution = input("Standard (A) or random (B) distribution of houses? ")

		if distribution != "A" and distribution != "B":
			print("Choose a distribution please")
			exit(0)

		with open('score.csv', 'w', newline='') as csvfile:
			fieldnames = ['algoritme', 'score', 'housecount', 'water']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			repeats = int(input("How many times do you want to run the algoritm? "))
			starttime = time.time()
			for repeat in range(repeats):
				print(repeat)
				new_gridvalue = random_algoritme(nr_of_houses, distribution)
				writer.writeheader()
				writer.writerow({'algoritme': 'Random', 'score': new_gridvalue[2], 'housecount': nr_of_houses, 'water' :len(new_gridvalue[1])})
				if len(gridvalue) != 0:
					if gridvalue[2] > new_gridvalue[2]:
						pass
					else:
						gridvalue = new_gridvalue
				else:
					gridvalue = new_gridvalue

		starttime = time.time()
		gridvalue = random_algoritme(nr_of_houses, distribution)

	# if uses picks B or C, choose starting grid
	elif alg == "B" or alg == "C":

		starting_state = (input("Is starting state Random(A) or Kerkhof(B)?"))

		if starting_state == "A":
			distribution = input("Standard (A) or random (B) distribution of houses? ")
			starttime = time.time()
			start = random_algoritme(nr_of_houses, distribution)

		# if startinf state is B then start with kerkhof
		elif starting_state == "B":
			starttime = time.time()
			start = kerkhof(nr_of_houses)

		else:
			print("Enter A or B for starting state")
			exit(0)

		# if B then run hill climber
		if alg == "B":
			gridvalue = hill_climber(nr_of_houses, start)

		# if C then run simulated annealing
		elif alg == "C":
			gridvalue = simulated_annealing(nr_of_houses, start)

	# if D then run kerkhof algoritm
	elif alg == "D":
		starttime = time.time()
		gridvalue = kerkhof(nr_of_houses)

	end = time.time()
	coordinate_list = gridvalue[0]
	water_coordinates = gridvalue[1]
	total_value = gridvalue[2]

	# print runtime, value of grid and grid
	print("time{}".format(end - starttime))
	print("value: {}".format(total_value))
	Area().make_grid(coordinate_list, water_coordinates, total_value)


if __name__ == "__main__":
	main()
