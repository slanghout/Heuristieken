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
	# set height and width of the land

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
