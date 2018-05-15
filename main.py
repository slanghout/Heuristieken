# Authors: Dewi Mooij, Sylvie Langhout & Pernille Deijlen
# Amstelhaege
import os, sys
import csv
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "grid"))

from houses import*
from grid import *
from sylvie import *
from random_algoritme import *
from water import *

def main():
	nr_of_houses = input("Would you like 20, 40 or 60 houses?")
	if nr_of_houses == 20 or nr_of_houses == 40 or nr_of_houses == 60:
		print("invalid number of houses")

	with open('scores.csv', 'w', newline='') as csvfile:
		fieldnames = ['algoritme', 'score', 'housecount']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	
		best_gridvalues = []
		for repeat in range(100):
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

		# Hill_Climber(40)
		Area().makegrid(coordinate_list, water_coordinates, total_value)

		# visualizing data

	# Hill Climbing Algorithm

	# Simulated Annealing Algorithm

if __name__ == "__main__":
	main()
