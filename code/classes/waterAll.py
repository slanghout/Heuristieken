import random as random

# CHECK IF WATER BODIES OVERLAP!!!
# alles in 1 ipv apart? Dus voor 4 bodies maken maar dan mag je ook 0 als grootte kiezen maar minimaal eentje > 0

# details grid and water
total_width = 180
total_height = 160
water_percentage = 0.2
total_water_size = total_width * total_height * water_percentage
print(total_water_size)

water_cords = []
while not water_cords:

	# choose random height and width
	height_1 = random.randint(1, total_height)
	width_1 = random.randint(1, total_width)
	water_size_1 = height_1 * width_1

	# if water body 1 is equal to total water
	if water_size_1 == total_water_size:
		# check ratio height and width
		if height_1 / width_1 > 1 and height_1 / width_1 < 4 or width_1 / height_1 > 1 and width_1 / height_1 < 4:
			# choose random coordinates
			left_x = random.randint(0, total_width)
			up_y = random.randint(0, total_height)
			right_x = left_x + width_1
			down_y = up_y - height_1
			
			if right_x >= 0 and down_y >= 0:
				water_coordinates_1 = [left_x, up_y, right_x, down_y]
				water_cords = [water_coordinates_1]
				print(water_cords)

	# if water body 1 is smaller than total water
	elif water_size_1 < total_water_size:
		# choose random height and width
		height_2 = random.randint(1, total_height)
		width_2 = random.randint(1, total_width)
		water_size_2 = height_2 * width_2
		
		# if water body 1 and 2 are equal to total water
		if water_size_2 == total_water_size - water_size_1:
			# check ratio height and width
			if (height_1 / width_1 > 1 and height_1 / width_1 < 4 or width_1 / height_1 > 1 and width_1 / height_1 < 4) and (height_2 / width_2 > 1 and height_2 / width_2 < 4 or width_2 / height_2 > 1 and width_2 / height_2 < 4):
				
				# choose random coordinates
				left_x1 = random.randint(0, total_width)
				up_y1 = random.randint(0, total_height)
				right_x1 = left_x1 + width_1
				down_y1 = up_y1 - height_1

				left_x2 = random.randint(0, total_width)
				up_y2 = random.randint(0, total_height)
				right_x2 = left_x2 + width_2
				down_y2 = up_y2 - height_2

				if right_x1 >= 0 and right_x2 >= 0 and down_y1 >= 0 and down_y2 >= 0:
							water_coordinates_1 = [left_x1, up_y1, right_x1, down_y1]
							water_coordinates_2 = [left_x2, up_y2, right_x2, down_y2]
							water_cords = [water_coordinates_1, water_coordinates_2]
							print(water_cords)

		# if water body 1 and 2 are smaller than total water
		elif water_size_2 < total_water_size - water_size_1:
			height_3 = random.randint(1, total_height)
			width_3 = random.randint(1, total_width)
			water_size_3 = height_3 * width_3
					
			# if water body 1, 2 and 3 are equal to total water
			if water_size_3 == total_water_size - water_size_1 - water_size_2:
				# check ratio height and width
				if (height_1 / width_1 > 1 and height_1 / width_1 < 4 or width_1 / height_1 > 1 and width_1 / height_1 < 4) and (height_2 / width_2 > 1 and height_2 / width_2 < 4 or width_2 / height_2 > 1 and width_2 / height_2 < 4) and (height_3 / width_3 > 1 and height_3 / width_3 < 4 or width_3 / height_3 > 1 and width_3 / height_3 < 4):
					
					# choose random coordinates
					left_x1 = random.randint(0, total_width)
					up_y1 = random.randint(0, total_height)
					right_x1 = left_x1 + width_1
					down_y1 = up_y1 - height_1

					left_x2 = random.randint(0, total_width)
					up_y2 = random.randint(0, total_height)
					right_x2 = left_x2 + width_2
					down_y2 = up_y2 - height_2

					left_x3 = random.randint(0, total_width)
					up_y3 = random.randint(0, total_height)
					right_x3 = left_x3 + width_3
					down_y3 = up_y3 - height_3

					if right_x1 >= 0 and right_x2 >= 0 and right_x3 >= 0 and down_y1 >= 0 and down_y2 >= 0 and down_y3 >= 0:
						water_coordinates_1 = [left_x1, up_y1, right_x1, down_y1]
						water_coordinates_2 = [left_x2, up_y2, right_x2, down_y2]
						water_coordinates_3 = [left_x3, up_y3, right_x3, down_y3]
						water_cords = [water_coordinates_1, water_coordinates_2, water_coordinates_3]
						print(water_cords)

			# if water body 1, 2 and 3 are smaller than total water
			elif water_size_3 < total_water_size - water_size_1 - water_size_2:
				height_4 = random.randint(1, total_height)
				width_4 = random.randint(1, total_width)
				water_size_4 = height_4 * width_4
						
				# if water body 1, 2, 3 and 4 are equal to total water (while loop until is gelijk?)
				if water_size_4 == total_water_size - water_size_1 - water_size_2 - water_size_3:
					# check ratio height and width
					if (height_1 / width_1 > 1 and height_1 / width_1 < 4 or width_1 / height_1 > 1 and width_1 / height_1 < 4) and (height_2 / width_2 > 1 and height_2 / width_2 < 4 or width_2 / height_2 > 1 and width_2 / height_2 < 4) and (height_3 / width_3 > 1 and height_3 / width_3 < 4 or width_3 / height_3 > 1 and width_3 / height_3 < 4) and (height_4 / width_4 > 1 and height_4 / width_4 < 4 or width_4 / height_4 > 1 and width_4 / height_4 < 4):

						# choose random coordinates
						left_x1 = random.randint(0, total_width)
						up_y1 = random.randint(0, total_height)
						right_x1 = left_x1 + width_1
						down_y1 = up_y1 - height_1

						left_x2 = random.randint(0, total_width)
						up_y2 = random.randint(0, total_height)
						right_x2 = left_x2 + width_2
						down_y2 = up_y2 - height_2

						left_x3 = random.randint(0, total_width)
						up_y3 = random.randint(0, total_height)
						right_x3 = left_x3 + width_3
						down_y3 = up_y3 - height_3

						left_x4 = random.randint(0, total_width)
						up_y4 = random.randint(0, total_height)
						right_x4 = left_x4 + width_4
						down_y4 = up_y4 - height_4

						if right_x1 >= 0 and right_x2 >= 0 and right_x3 >= 0 and right_x4 >= 0 and down_y1 >= 0 and down_y2 >= 0 and down_y3 >= 0 and down_y4 >= 0:
							water_coordinates_1 = [left_x1, up_y1, right_x1, down_y1]
							water_coordinates_2 = [left_x2, up_y2, right_x2, down_y2]
							water_coordinates_3 = [left_x3, up_y3, right_x3, down_y3]
							water_coordinates_4 = [left_x4, up_y4, right_x4, down_y4]
							water_cords = [water_coordinates_1, water_coordinates_2, water_coordinates_3, water_coordinates_4]
							print(water_cords)

				else:
					print("water 4 is too big or small")
			else:
				print("water 3 is too big")
		else:
			print("water 2 is too big")
	else:
		print("water 1 is too big")