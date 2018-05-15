# Authors: Dewi Mooij, Sylvie Langhout & Pernille Deijlen
# Amstelhaege
import os, sys
import csv
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "grid"))

from houses import house
from houses import single
from houses import bungalow
from houses import maison

from grid import Area
from Hill_climber import HillClimber
from random_algoritme import Random
from water import MakeWater

def main():
	nr_of_houses = int(input("Would you like 20, 40 or 60 houses?"))
	if nr_of_houses != 20 and nr_of_houses != 40 and nr_of_houses != 60:
		print("invalid number of houses")
		exit(0)

	alg = input("Select A for Random, B for Hill Climber")
	if alg != "A" and alg != "B":
		print("this is not what I wanted")
		exit(0)

	repeats = int(input("How many times do you want to run the algoritm?"))

	with open('scores.csv', 'w', newline='') as csvfile:
		fieldnames = ['algoritme', 'score', 'housecount']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		if alg == "A":
			best_gridvalues = []
			for repeat in range(repeats):
				gridvalue = Random(int(nr_of_houses))
				writer.writeheader()
				writer.writerow({'algoritme': 'Random', 'score': gridvalue[2], 'housecount': nr_of_houses})
				print(repeat)
				if len(best_gridvalues) != 0:
					print("best {} vs now {}".format(best_gridvalues[2], gridvalue[2]))
					if best_gridvalues[2] > gridvalue[2]:
						pass
					else:
						best_gridvalues = gridvalue
				else:
					best_gridvalues = gridvalue

			coordinate_list = best_gridvalues[0]
			water_coordinates = best_gridvalues[1]
			total_value = best_gridvalues[2]
			Area().makegrid(coordinate_list, water_coordinates, total_value)

		if alg == "B":
			final = HillClimber(nr_of_houses, repeats)
			coordinate_list = final[0]
			water_coordinates = final[1]
			total_value = final[2]
			writer.writeheader()
			writer.writerow({'algoritme': 'HillClimber', 'score': final[2], 'housecount': nr_of_houses})
			Area().makegrid(coordinate_list, water_coordinates, total_value)


if __name__ == "__main__":
	main()
