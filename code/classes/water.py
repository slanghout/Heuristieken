import random as random

total_width = 180
total_height = 160
water_percentage = 0.2
total_water_size = total_width * total_height * water_percentage
print(total_water_size)

# water_bodies = [1, 2, 3, 4]
# amount_water = random.choice(water_bodies)
amount_water = 1
print(amount_water)

if amount_water == 1:
	# choose random height and width
	height_1 = random.choice(range(0, total_height))
	width_1 = int(total_water_size / height_1)
	print(height_1)
	print(width_1)

	# check ratio height and width
	if height_1 / width_1 > 1 and height_1 / width_1 < 4 or width_1 / height_1 > 1 and width_1 / height_1 < 4:
		print("okay")
	else:
		print("wrong ratio!")
	
	# choose random coordinates
	left_x = random.choice(range(0, total_width))
	up_y = random.choice(range(0, total_height))
	right_x = left_x + width_1
	down_y = up_y - height_1
	if right_x < 0 or down_y < 0:
		print("coordinates can't be negative")
	else:
		water_coordinates = [left_x, up_y, right_x, down_y]
		print(water_coordinates)
	
	
if amount_water == 2:
	# choose random height and weight
	water_size_1 = random.choice(range(0, total_water_size))
	water_size_2 = total_water_size - water_size_1

	height_1 = random.choice(range(0, total_height))
	width_1 = 
	height_2
	width_2
	if height_1 * width_1 + height_2 * width_2 != total_water_size:
		print("wrong")
	
	

	# check ratio height and weight

	# choose random coordinates

# if amount_water == 3:
# 	water_size[1] = random.choice()
# 	water_size[2] = random.choice()
# 	water_size[3] = random.choice()

# if amount_water == 4:
# 	water_size[1] = random.choice()
# 	water_size[2] = random.choice()
# 	water_size[3] = random.choice()
# 	water_size[4] = random.choice()