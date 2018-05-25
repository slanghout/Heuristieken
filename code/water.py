import random as random

total_width = 360
total_height = 320
water_percentage = 0.2
total_water_size = total_width * total_height * water_percentage

# function that makes water
def make_water(amount_water):
	if amount_water == 1:
		# choose random height and width
		water_1 = choose_height_width()
		water_size_1 = water_1[0]

		if water_size_1 == total_water_size:
			height_1 = water_1[1]
			width_1 = water_1[2]

			# check ratio height and width
			if check_ratio(height_1, width_1) == True:
			
				# choose random coordinates
				water_coordinates_1 = choose_random_coordinates(height_1, width_1)

				if water_coordinates_1 == None:
					return None
				else:
					return [water_coordinates_1]


	if amount_water == 2:
		# choose random height and width
		water_1 = choose_height_width()
		water_size_1 = water_1[0]

		if water_size_1 < total_water_size - 1:
			water_size_2 = total_water_size - water_size_1
			water_2 = choose_height(water_size_2)
			height_2 = water_2[0]
			width_2 = water_2[1]
			height_1 = water_1[1] 
			width_1 = water_1[2] 

			# check ratio height and width
			if (check_ratio(height_1, width_1) and check_ratio(height_2, width_2)) == True:

				# choose random coordinates
				water_coordinates_1 = choose_random_coordinates(height_1, width_1)
				water_coordinates_2 = choose_random_coordinates(height_2, width_2)

				if water_coordinates_1 == None or water_coordinates_2 == None:
					return None
				else:
					return [water_coordinates_1, water_coordinates_2]


	if amount_water == 3:
		# choose random height and width
		water_1 = choose_height_width()
		water_size_1 = water_1[0]
		height_1 = water_1[1]
		width_1 = water_1[2]

		if water_size_1 < total_water_size - 2:
			water_2 = choose_height_width()
			water_size_2 = water_2[0]
			height_2 = water_2[1]
			width_2 = water_2[2]

			if water_size_2 < total_water_size - water_size_1 - 1:
				water_size_3 = total_water_size - water_size_1 - water_size_2
				water_3 = choose_height(water_size_3)
				height_3 = water_3[0]
				width_3 = water_3[1]

				# check ratio height and width
				if (check_ratio(height_1, width_1) and check_ratio(height_2, width_2) \
					and check_ratio(height_3, width_3)) == True:

					# choose random coordinates
					water_coordinates_1 = choose_random_coordinates(height_1, width_1)
					water_coordinates_2 = choose_random_coordinates(height_2, width_2)
					water_coordinates_3 = choose_random_coordinates(height_3, width_3)
					
					if water_coordinates_1 == None or water_coordinates_2 == None or water_coordinates_3 == None:
						return None
					else:		
						return [water_coordinates_1, water_coordinates_2, water_coordinates_3]

	if amount_water == 4:
		# choose random height and width
		water_1 = choose_height_width()
		water_size_1 = water_1[0]
		height_1 = water_1[1]
		width_1 = water_1[2]

		if water_size_1 < total_water_size - 3:
			water_2 = choose_height_width()
			water_size_2 = water_2[0]
			height_2 = water_2[1]
			width_2 = water_2[2]

			if water_size_2 < total_water_size - water_size_1 - 2:
				water_3 = choose_height_width()
				water_size_3 = water_3[0]
				height_3 = water_3[1]
				width_3 = water_3[2]

				if water_size_3 < total_water_size - water_size_1 - water_size_2 - 1:
					water_size_4 = total_water_size - water_size_1 - water_size_2 - water_size_3
					water_4 = choose_height(water_size_4)
					height_4 = water_4[0]
					width_4 = water_4[1]

					# check ratio height and width
					if (check_ratio(height_1, width_1) and check_ratio(height_2, width_2) \
						and check_ratio(height_3, width_3) and check_ratio(height_4, width_4)) == True:

						# choose random coordinates
						water_coordinates_1 = choose_random_coordinates(height_1, width_1)
						water_coordinates_2 = choose_random_coordinates(height_2, width_2)
						water_coordinates_3 = choose_random_coordinates(height_3, width_3)
						water_coordinates_4 = choose_random_coordinates(height_4, width_4)

						if water_coordinates_1 == None or water_coordinates_2 == None \
							or water_coordinates_3 == None or water_coordinates_4 == None:
							return None
						else:
							return [water_coordinates_1, water_coordinates_2, water_coordinates_3, water_coordinates_4]

def choose_height_width(): 
	height = random.randint(1, total_height)
	width = random.randint(1, total_width)
	size = height * width
	return [size, height, width]

def choose_height(water_size):
	height = random.randint(1, total_height)
	width = water_size / height
	return [height, width]

def check_ratio(height, width):
	if height / width > 1 and height / width < 4 or width / height > 1 \
		and width / height < 4:
			return True

def choose_random_coordinates(height, width):
	left_x = random.randint(0, total_width)
	up_y = random.randint(0, total_height)
	right_x = int(left_x + width)
	down_y = int(up_y - height)

	if right_x <= total_width and down_y >= 0:
		return [left_x, up_y, right_x, down_y]

	else:
		return None
		





