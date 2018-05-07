import random as random

total_width = 360
total_height = 320
water_percentage = 0.2
total_water_size = total_width * total_height * water_percentage
print(total_water_size)


def MakeWater(amount_water):	
	if amount_water == 1:
		water_coordinates_1 = []
		while not water_coordinates_1:
			
			# choose random height and width
			height_1 = random.randint(0, total_height)
			width_1 = random.randint(0, total_width)
			water_size_1 = height_1 * width_1

			if water_size_1 == total_water_size:
			
				# check ratio height and width
				if height_1 / width_1 > 1 and height_1 / width_1 < 4 or width_1 / height_1 > 1 and width_1 / height_1 < 4:
					
					# choose random coordinates
					left_x1 = random.randint(0, total_width)
					up_y1 = random.randint(0, total_height)
					right_x1 = int(left_x1 + width_1)
					down_y1 = int(up_y1 - height_1)
					
					# check coordinates
					if right_x1 <= total_width and down_y1 >= 0:
						water_coordinates_1 = [left_x1, up_y1, right_x1, down_y1]
						print(water_coordinates_1)	
		return [water_coordinates_1] 


	if amount_water == 2:
		water_coordinates_1 = []
		water_coordinates_2 = []
		while not water_coordinates_1 and not water_coordinates_2:
		
			# choose random height and width
			height_1 = random.randint(1, total_height)
			width_1 = random.randint(1, total_width)
			water_size_1 = height_1 * width_1
			
			if water_size_1 < total_water_size - 1:
				water_size_2 = total_water_size - water_size_1
				height_2 = random.randint(1, total_height)
				width_2 = water_size_2 / height_2

				# check ratio height and width
				if width_2 == int(width_2) and (height_1 / width_1 > 1 and height_1 / width_1 < 4 or width_1 / height_1 > 1 and width_1 / height_1 < 4) and (height_2 / width_2 > 1 and height_2 / width_2 < 4 or width_2 / height_2 > 1 and width_2 / height_2 < 4):
				
					# choose random coordinates
					left_x1 = random.randint(0, total_width)
					up_y1 = random.randint(0, total_height)
					right_x1 = int(left_x1 + width_1)
					down_y1 = int(up_y1 - height_1)

					left_x2 = random.randint(0, total_width)
					up_y2 = random.randint(0, total_height)
					right_x2 = int(left_x2 + width_2)
					down_y2 = int(up_y2 - height_2)

					# check coordinates
					if right_x1 <= total_width and right_x2 <= total_width and down_y1 >= 0 and down_y2 >= 0:
						water_coordinates_1 = [left_x1, up_y1, right_x1, down_y1]
						water_coordinates_2 = [left_x2, up_y2, right_x2, down_y2]
						print(water_coordinates_1)
						print(water_coordinates_2)
		return [water_coordinates_1, water_coordinates_2]


	if amount_water == 3:
		water_coordinates_1 = []
		water_coordinates_2 = []
		water_coordinates_3 = []
		while not water_coordinates_1 and not water_coordinates_2 and not water_coordinates_3:
			
			# choose random height and width
			height_1 = random.randint(1, total_height)
			width_1 = random.randint(1, total_width)
			water_size_1 = height_1 * width_1
			
			if water_size_1 < total_water_size - 2:
				height_2 = random.randint(1, total_height)
				width_2 = random.randint(1, total_width)
				water_size_2 = height_2 * width_2

				if water_size_2 < total_water_size - water_size_1 - 1:
					water_size_3 = total_water_size - water_size_1 - water_size_2
					height_3 = random.randint(1, total_height)
					width_3 = water_size_3 / height_3

					# check ratio height and width
					if width_3 == int(width_3) and (height_1 / width_1 > 1 and height_1 / width_1 < 4 or width_1 / height_1 > 1 and width_1 / height_1 < 4) and (height_2 / width_2 > 1 and height_2 / width_2 < 4 or width_2 / height_2 > 1 and width_2 / height_2 < 4) and (height_3 / width_3 > 1 and height_3 / width_3 < 4 or width_3 / height_3 > 1 and width_3 / height_3 < 4):

						# choose random coordinates		
						left_x1 = random.randint(0, total_width)
						up_y1 = random.randint(0, total_height)
						right_x1 = int(left_x1 + width_1)
						down_y1 = int(up_y1 - height_1)

						left_x2 = random.randint(0, total_width)
						up_y2 = random.randint(0, total_height)
						right_x2 = int(left_x2 + width_2)
						down_y2 = int(up_y2 - height_2)

						left_x3 = random.randint(0, total_width)
						up_y3 = random.randint(0, total_height)
						right_x3 = int(left_x3 + width_3)
						down_y3 = int(up_y3 - height_3)

						# check coordinates
						if right_x1 <= total_width and right_x2 <= total_width and right_x3 <= total_width and down_y1 >= 0 and down_y2 >= 0 and down_y3 >= 0:
							water_coordinates_1 = [left_x1, up_y1, right_x1, down_y1]
							water_coordinates_2 = [left_x2, up_y2, right_x2, down_y2]
							water_coordinates_3 = [left_x3, up_y3, right_x3, down_y3]
							print(water_coordinates_1)
							print(water_coordinates_2)
							print(water_coordinates_3)
		return [water_coordinates_1, water_coordinates_2, water_coordinates_3]	

	if amount_water == 4:
		water_coordinates_1 = []
		water_coordinates_2 = []
		water_coordinates_3 = []
		water_coordinates_4 = []
		while not water_coordinates_1 and not water_coordinates_2 and not water_coordinates_3 and not water_coordinates_4:
			
			# choose random height and width
			height_1 = random.randint(1, total_height)
			width_1 = random.randint(1, total_width)
			water_size_1 = height_1 * width_1
			
			if water_size_1 < total_water_size - 3:
				height_2 = random.randint(1, total_height)
				width_2 = random.randint(1, total_width)
				water_size_2 = height_2 * width_2
				
				if water_size_2 < total_water_size - water_size_1 - 2:
					height_3 = random.randint(1, total_height)
					width_3 = random.randint(1, total_width)
					water_size_3 = height_3 * width_3
					
					if water_size_3 < total_water_size - water_size_1 - water_size_2 - 1:
						water_size_4 = total_water_size - water_size_1 - water_size_2 - water_size_3
						height_4 = random.randint(1, total_height)
						width_4 = water_size_4 / height_4

						# check ratio height and width
						if width_4 == int(width_4) and (height_1 / width_1 > 1 and height_1 / width_1 < 4 or width_1 / height_1 > 1 and width_1 / height_1 < 4) and (height_2 / width_2 > 1 and height_2 / width_2 < 4 or width_2 / height_2 > 1 and width_2 / height_2 < 4) and (height_3 / width_3 > 1 and height_3 / width_3 < 4 or width_3 / height_3 > 1 and width_3 / height_3 < 4) and (height_4 / width_4 > 1 and height_4 / width_4 < 4 or width_4 / height_4 > 1 and width_4 / height_4 < 4):
				
							# choose random coordinates
							left_x1 = random.randint(0, total_width)
							up_y1 = random.randint(0, total_height)
							right_x1 = int(left_x1 + width_1)
							down_y1 = int(up_y1 - height_1)

							left_x2 = random.randint(0, total_width)
							up_y2 = random.randint(0, total_height)
							right_x2 = int(left_x2 + width_2)
							down_y2 = int(up_y2 - height_2)

							left_x3 = random.randint(0, total_width)
							up_y3 = random.randint(0, total_height)
							right_x3 = int(left_x3 + width_3)
							down_y3 = int(up_y3 - height_3)

							left_x4 = random.randint(0, total_width)
							up_y4 = random.randint(0, total_height)
							right_x4 = int(left_x4 + width_4)
							down_y4 = int(up_y4 - height_4)

							# check coordinates
							if right_x1 <= total_width and right_x2 <= total_width and right_x3 <= total_width and right_x4 <= total_width and down_y1 >= 0 and down_y2 >= 0 and down_y3 >= 0 and down_y4 >= 0:
								water_coordinates_1 = [left_x1, up_y1, right_x1, down_y1]
								water_coordinates_2 = [left_x2, up_y2, right_x2, down_y2]
								water_coordinates_3 = [left_x3, up_y3, right_x3, down_y3]
								water_coordinates_4 = [left_x4, up_y4, right_x4, down_y4]
								print(water_coordinates_1)
								print(water_coordinates_2)
								print(water_coordinates_3)
								print(water_coordinates_4)
		return [water_coordinates_1, water_coordinates_2, water_coordinates_3, water_coordinates_4]