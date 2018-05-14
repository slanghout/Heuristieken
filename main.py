# Authors: Dewi Mooij, Sylvie Langhout & Pernille Deijlen
# Amstelhaege
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "grid"))

from houses import *
from grid import *
# from overlap_check import *
from random_algoritme import *
from water import *

def main():
	# nr_of_houses = input("Would you like 20, 40 or 60 houses?")
	# if nr_of_houses != 20 or nr_of_houses != 40 or nr_of_houses != 60:
	# 	Random(int(nr_of_houses))
	# else:
	# 	print("invalid number of houses")

	best_gridvalues = []
	for repeat in range(20):
		print(repeat)
		gridvalue = Random(60)
		print(gridvalue[2])
		if len(best_gridvalues) != 0:
			if best_gridvalues[2] > gridvalue[2]:
				pass
			else:
				best_gridvalues = gridvalue
		else:
			best_gridvalues = gridvalue

	# gridvalues = Random(40)

	coordinate_list = best_gridvalues[0]
	water_coordinates = best_gridvalues[1]
	total_value = best_gridvalues[2]

	Area().makegrid(coordinate_list, water_coordinates, total_value)

	Random(60)



	# placing the houses and water randomly
			# 20 houses
			# 40 houses
			# 60 houses
			# value

	# visualizing data

	# Hill Climbing Algorithm

	# Simulated Annealing Algorithm

if __name__ == "__main__":
	main()
