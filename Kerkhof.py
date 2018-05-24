import os, sys
import csv
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "grid"))

from houses import House, Single, Bungalow, Maison

from grid import Area
from random_algoritme import random, create_water
from water import make_water


# creating a state we think has a high worth
def kerkhof(nr_of_houses):

	# initialising empty grid
	grid = Area().make_basic_grid()

	# if 20 houses are chosen
	if nr_of_houses == 20:
		location_space = []
		location_list = []
		total_value = 0

		# placing 9 singles
		for i in range(9):
			size = Single([0,0]).give_size()

			# choosing coordinates
			house_next = [24 + (21 + size[1]) * i, 300, 24 + size[1] + (21 + size[1]) * i, 300 - size[0], 1]
			cords = [house_next[0], house_next[1]]

			# checking if there is place for house
			if Area().housecheck(grid, house_next) == True:
				space = Single(cords).spacehouse(house_next)
			
				# checking if there is place for space
				if Area().spacecheck(grid, space) == True:
			
					# if all true place house and space
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		# placing 3 singles
		for i in range(3):
			size = Single([0,0]).give_size()
			
			# choosing coordinates
			house_next = [24 + (21 + size[1]) * i, 36, 24 + size[1] + (21 + size[1]) * i, 36 - size[0], 1]
			cords = [house_next[0], house_next[1]]

			# checking if there is place for house		
			if Area().housecheck(grid, house_next) == True:
				space = Single(cords).spacehouse(house_next)
			
				# checking if there is place for space
				if Area().spacecheck(grid, space) == True:
			
					# if all true place house and space
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		# placing 1 bungalow
		size = Bungalow([0,0]).give_size()
		
		# choosing coordinates		
		house_next = [28, 170, 28 + size[1], 170 - size[0], 2]
		cords = [house_next[0], house_next[1]]

		# checking if there is place for house	
		if Area().housecheck(grid, house_next) == True:
			space = Bungalow(cords).spacehouse(house_next)
		
			# checking if there is place for space
			if Area().spacecheck(grid, space) == True:
		
				# if all true place house and space
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

		# placing 2 bungalows
		for i in range(2):
			size = Bungalow([0,0]).give_size()

			# choosing coordinates	
			house_next = [71, 105 + size[0] + (70 + size[0]) * i, 71 + size[1], 105 + (70 + size[0]) * i, 2]
			cords = [house_next[0], house_next[1]]

			# checking if there is place for house	
			if Area().housecheck(grid, house_next) == True:
				space = Bungalow(cords).spacehouse(house_next)
			
				# checking if there is place for space
				if Area().spacecheck(grid, space) == True:
			
					# if all true place house and space
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		# placing 2 bungalows
		for i in range(2):
			size = Bungalow([0,0]).give_size()
			
			# choosing coordinates	
			house_next = [295, 30 + size[0] + (size[0] + 82) * i, 295 + size[1], 30 + (size[0] + 82) * i, 2]
			cords = [house_next[0], house_next[1]]
			
			# checking if there is place for house
			if Area().housecheck(grid, house_next) == True:
				space = Bungalow(cords).spacehouse(house_next)
				
				# checking if there is place for space
				if Area().spacecheck(grid, space) == True:
				
					# if all true place house and space
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		# placing 1 maison
		size = Maison([0,0]).give_size()
		
		# choosing coordinates		
		house_next = [135 - size[1], 149 + size[0], 135, 171 - size[0], 3]
		cords = [house_next[0], house_next[1]]
		
		# checking if there is place for house	
		if Area().housecheck(grid, house_next) == True:
			space = Maison(cords).spacehouse(house_next)
		
			# checking if there is place for space
			if Area().spacecheck(grid, space) == True:
		
				# if all true place house and space
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")
		
		# placing 2 maisons
		for i in range(2):
			size = Maison([0,0]).give_size()
			
			# choosing coordinates	
			house_next = [225, 80 + size[0] + (size[0] + 80) * i, 225 + size[1], 80 + (size[0] + 80) * i, 3]
			cords = [house_next[0], house_next[1]]
			
			# checking if there is place for house		
			if Area().housecheck(grid, house_next) == True:
				space = Maison(cords).spacehouse(house_next)
			
				# checking if there is place for space
				if Area().spacecheck(grid, space) == True:
			
					# if all true place house and space
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		# determining worth
		for coordinate in location_list:
			cords = [coordinate[0], coordinate[1]]
			if coordinate[4] == 1:
				build = Single
			elif coordinate[4] == 2:
				build = Bungalow
			elif coordinate[4] == 3:
				build = Maison
			price = build(cords).give_worth(coordinate, grid)
			if price != None:
				total_value += price

		# placing water
		water = 1
		water_coordinates = [[135, 272, 225, 14]]
		
		# checking if there is place for water
		for body in range(water):
			if Area().watercheck(grid, water_coordinates[body]) == True:
					grid = Area().update_grid(grid, water_coordinates[body], "water")

		return([location_list, water_coordinates, total_value, grid])

	# if 40 houses are chosen
	if nr_of_houses == 40:
		location_space = []
		location_list = []
		total_value = 0
		
		# placing 16 singles
		for i in range(8):
			for j in range(2):
				size = Single([0,0]).give_size()
				
				# choosing coordinates
				house_next = [20 + (size[1] + 27) * i, 310 - 280 * j, 20 + size[1] + (27 + size[1]) * i, 310 - size[0] - 280 * j, 1]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house			
				if Area().housecheck(grid, house_next) == True:
					space = Single(cords).spacehouse(house_next)
				
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
				
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 8 singles
		for i in range(4):
			for j in range(2):
				size = Single([0,0]).give_size()
				
				# choosing coordinates
				house_next = [20 + 301 * j, 280 - (size[0] + 55) * i, 20 + size[1] + 301 * j, 280 - size[0] - (55 + size[0]) * i, 1]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house			
				if Area().housecheck(grid, house_next) == True:
					space = Single(cords).spacehouse(house_next)
				
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
				
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 6 bungalows
		for i in range(3):
			for j in range(2):
				size = Bungalow([0,0]).give_size()
				
				# choosing coordinates
				house_next = [321 - 300 * j, 250 - (size[0] + 55) * i , 321 + size[1] - 300 * j, 250 - size[0] - (55 + size[0]) * i, 2]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house
				if Area().housecheck(grid, house_next) == True:
					space = Bungalow(cords).spacehouse(house_next)
				
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
						
						# if all true place house and space
						location_list.append(house_next)	
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 2 bungalows
		for i in range (2):
				size = Bungalow([0,0]).give_size()
				
				# choosing coordinates
				house_next = [101 + 140 * i, 204 - 64 * i, 101 + size[1] + 140 * i, 204 - size[0] - 64 * i, 2]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house			
				if Area().housecheck(grid, house_next) == True:
					space = Bungalow(cords).spacehouse(house_next)
				
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
				
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 6 maisons
		for i in range(6):
			size = Maison([0,0]).give_size()
			
			# choosing coordinates
			house_next = [65 + (size[1] + 20) * i, 65 + (size[0] + 20) * i, 65 + size[1] + (20 + size[1]) * i, 65 - size[0] + (20 + size[0]) * i, 3]
			cords = [house_next[0], house_next[1]]

			# checking if there is place for house	
			if Area().housecheck(grid, house_next) == True:
				space = Maison(cords).spacehouse(house_next)
			
				# checking if there is place for space
				if Area().spacecheck(grid, space) == True:
					
					# if all true place house and space
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		# determining worth
		for coordinate in location_list:
			cords = [coordinate[0], coordinate[1]]
			if coordinate[4] == 1:
				build = Single
			elif coordinate[4] == 2:
				build = Bungalow
			elif coordinate[4] == 3:
				build = Maison
			price = build(cords).give_worth(coordinate, grid)
			if price != None:
				total_value += price

		# placing water
		water = 2
		water_coordinates = [[36, 294, 164, 204], [193, 120, 321, 30]]

		# checking if there is place for water
		for body in range(water):
			if Area().watercheck(grid, water_coordinates[body]) == True:
				grid = Area().update_grid(grid, water_coordinates[body], "water")

		return([location_list, water_coordinates, total_value, grid])	

	# if 60 houses are chosen
	if nr_of_houses == 60:
		location_space = []
		location_list = []
		total_value = 0

		# placing 24 singles
		for i in range(12):
			for j in range(2):
				size = Single([0,0]).give_size()
				
				# choosing coordinates
				house_next = [12 + 29 * i, 307 - 278 * j, 12 + size[1] + 29 * i, 307 - 278 * j - size[0], 1]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house			
				if Area().housecheck(grid, house_next) == True:
					space = Single(cords).spacehouse(house_next)
					
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:			
					
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 12 singles
		for i in range(6):
			for j in range(2):
				size = Single([0,0]).give_size()
				
				# choosing coordinates
				house_next = [331 - 319 * j, 29 + 26 + size[0] + (23 + size[0]) * i, 331 - 319 * j + size[1], 29 + 26 + (size[0] + 23) * i, 1]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house			
				if Area().housecheck(grid, house_next) == True:
					space = Single(cords).spacehouse(house_next)
					
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
					
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 4 bungalows
		for i in range(2):
			for j in range(2):
				size = Bungalow([0,0]).give_size()

				# choosing coordinates
				house_next = [244 + 44 * j, 224 + size[0] + (14 + size[0]) * i, 244 + 44 * j + size[1], 224 + (14 + size[0]) * i, 2]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house				
				if Area().housecheck(grid, house_next) == True:
					space = Bungalow(cords).spacehouse(house_next)
				
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
				
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 4 bungalows
		for i in range(2):
			for j in range(2):
				size = Bungalow([0,0]).give_size()
				
				# choosing coordinates
				house_next = [244 + 44 * j, 29 + 13 + size[0] + (14 + size[0]) * i, 244 + 44 * j + size[1], 29 + 13 + (14 + size[0]) * i, 2]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house		
				if Area().housecheck(grid, house_next) == True:
					space = Bungalow(cords).spacehouse(house_next)
					
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
					
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 4 bungalows
		for i in range(2):
			for j in range(2):
				size = Bungalow([0,0]).give_size()
				
				# choosing coordinates
				house_next = [57 + (29 + size[1]) * i, 96 - (14 + size[0]) * j, 57 + size[1] + (29 + size[1]) * i, 96 - size[0] - (14 + size[0]) * j, 2]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house
				if Area().housecheck(grid, house_next) == True:
					space = Bungalow(cords).spacehouse(house_next)
				
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
				
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 2 bungalows
		for i in range(2):
			size = Bungalow([0,0]).give_size()
			
			# choosing coordinates
			house_next = [57 + (29 + size[1]) * i, 244, 57 + size[1] + (29 + size[1]) * i, 244 - size[0], 2]
			cords = [house_next[0], house_next[1]]

			# checking if there is place for house			
			if Area().housecheck(grid, house_next) == True:
				space = Bungalow(cords).spacehouse(house_next)
			
				# checking if there is place for space
				if Area().spacecheck(grid, space) == True:
			
					# if all true place house and space
					location_list.append(house_next)
					grid = Area().update_grid(grid, house_next, "house")
					location_space.append(space)
					grid = Area().update_grid(grid, space, "space")

		# placing 1 bungalow
		size = Bungalow([0,0]).give_size()
		
		# choosing coordinates				
		house_next = [86 + size[1], 278, 86 + size[1] + size[1], 278 - size[0], 2]
		cords = [house_next[0], house_next[1]]

		# checking if there is place for house
		if Area().housecheck(grid, house_next) == True:
			space = Bungalow(cords).spacehouse(house_next)
			
			# checking if there is place for space
			if Area().spacecheck(grid, space) == True:
			
				# if all true place house and space
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

		# placing 1 maison
		size = Maison([0,0]).give_size()
		
		# choosing coordinates	
		house_next = [170, 171, 170 + size[1], 171 -  size[0], 3]
		cords = [house_next[0], house_next[1]]
		
		# checking if there is place for house
		if Area().housecheck(grid, house_next) == True:
			space = Maison(cords).spacehouse(house_next)
			
			# checking if there is place for space
			if Area().spacecheck(grid, space) == True:
			
				# if all true place house and space
				location_list.append(house_next)
				grid = Area().update_grid(grid, house_next, "house")
				location_space.append(space)
				grid = Area().update_grid(grid, space, "space")

		# placing 4 maisons
		for i in range(2):
			for j in range(2):
				size = Maison([0,0]).give_size()

				# choosing coordinates
				house_next = [145 + (size[1] + 28) * i, 246 - 150 * j, 145 + size[1] + (size[1] + 28) * i, 246 - size[0] - 150 * j, 3]
				cords = [house_next[0], house_next[1]]
				
				# checking if there is place for house
				if Area().housecheck(grid, house_next) == True:
					space = Maison(cords).spacehouse(house_next)
					
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
						
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# placing 4 maisons
		for i in range(2):
			for j in range(2):
				size = Maison([0,0]).give_size()
				
				# choosing coordinates
				house_next = [73 + 192 * j, 196 - (size[0] + 28) * i, 73 + size[1] + 192 * j, 196 - size[0] - (size[0] + 28) * i, 3]
				cords = [house_next[0], house_next[1]]

				# checking if there is place for house
				if Area().housecheck(grid, house_next) == True:
					space = Maison(cords).spacehouse(house_next)
					
					# checking if there is place for space
					if Area().spacecheck(grid, space) == True:
						
						# if all true place house and space
						location_list.append(house_next)
						grid = Area().update_grid(grid, house_next, "house")
						location_space.append(space)
						grid = Area().update_grid(grid, space, "space")

		# determining worth
		for coordinate in location_list:
			cords = [coordinate[0], coordinate[1]]
			if coordinate[4] == 1:
				build = Single
			elif coordinate[4] == 2:
				build = Bungalow
			elif coordinate[4] == 3:
				build = Maison
			price = build(cords).give_worth(coordinate, grid)
			if price != None:
				total_value += price
		
		# placing water
		water = 4
		water_coordinates = [[28, 224, 73, 96], [286, 224, 331, 96], [116, 74, 244, 29], [116, 291, 244, 246]]
		
		# checking if there is place for water
		for body in range(water):
			if Area().watercheck(grid, water_coordinates[body]) == True:
					grid = Area().update_grid(grid, water_coordinates[body], "water")

		return([location_list, water_coordinates, total_value, grid])
