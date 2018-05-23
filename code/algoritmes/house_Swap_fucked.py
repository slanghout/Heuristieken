# function that swaps two houses in the grid
def house_swap(coordinate_list, nr_of_houses, grid):

	# randomly pick two houses from the coordinate list
	house_one = randint(0, (nr_of_houses - 1))
	house_two = randint(0, (nr_of_houses - 1))
	if house_one == house_two:
		return None

	old_cords_one = coordinate_list[house_one]
	old_cords_two = coordinate_list[house_two]

	# determine height and width of the houses
	width_one_x = old_cords_one[2] - old_cords_one[0]
	height_one_x = old_cords_one[1] - old_cords_one[3]

	# determine height and width of the houses
	housetype_one = housetype(old_cords_one[4])
	cord_one = (old_cords_one[0], old_cords_one[1])
	size = housetype_one(cord_one).give_size()
	print("1st size{} and housetype{}".format(size, housetype_one))
	width_one = size[0]
	height_one = size[1]
	print("{}{}".format(width_one, width_one_x))
	print("height{}{}".format(height_one, height_one_x))

	# determine height and width of the houses
	housetype_two = housetype(old_cords_two[4])
	cord_two = (old_cords_two[0], old_cords_two[1])
	size = housetype_two(cord_two).give_size()
	print("2nd size{} and housetype{}".format(size, housetype_two))
	width_two = size[0]
	height_two = size[1]

	# create new coordinates for the houses
	# take the left upper corner
	# determine new coordinates with height and width
	
	x_l_one = old_cords_two[0]
	y_u_one = old_cords_two[1]
	x_r_one = old_cords_two[0] + width_one
	y_d_one = old_cords_two[1] - height_one
	new_cord_one = [x_l_one, y_u_one, x_r_one, y_d_one, old_cords_one[4]]

	x_l_two = old_cords_one[0]
	y_u_two = old_cords_one[1]
	x_r_two = old_cords_one[0] + width_two
	y_d_two = old_cords_one[1] - height_two
	new_cord_two = [x_l_two, y_u_two, x_r_two, y_d_two, old_cords_two[4]]

	# housetype_one = housetype(old_cords_one[4])
	# cord_one = (x_l_one, y_u_one)
	cord_one = (x_l_one, y_u_one)
	space_old_cords_one = housetype_one(cord_one).spacehouse(old_cords_one)
	print("oud{} met space {}".format(old_cords_one, space_old_cords_one))

	# build = housetype(old_cords_two[4])
	# cord_two = (x_l_two, y_u_two)
	cord_two = (x_l_two, y_u_two)
	space_old_cords_two = housetype_two(cord_two).spacehouse(old_cords_two)
	print("oud{} met space {}".format(old_cords_two, space_old_cords_two))

	build = housetype(new_cord_one[4])
	cord_one_new = (x_l_one, y_d_one)
	new_space_cords_one = build(cord_one_new).spacehouse(new_cord_one)

	if (new_space_cords_one[0] < 0 or new_space_cords_one[3] < 0 or
		new_space_cords_one[1] > 320 or new_space_cords_one[2] > 360):
		return None

	build = housetype(new_cord_two[4])
	cord_two_new = (x_l_two, y_d_two)
	new_space_cords_two = build(cord_two_new).spacehouse(new_cord_two)

	if (new_space_cords_two[0] < 0 or new_space_cords_two[3] < 0 or
		new_space_cords_two[1] > 320 or new_space_cords_two[2] > 360):
		return None

	print("space")
	# clear the space the houses were using
	grid = Area().create_space(space_old_cords_one, grid)
	print('check')
	grid = Area().create_space(space_old_cords_two, grid)
	print('doublecheck')

	# check if there is enough space to place house 1 then place
	if Area().housecheck(grid, new_cord_one) == True:
		if Area().spacecheck(grid, new_space_cords_one) == True:
			grid = reset(grid, new_cord_one, new_space_cords_one)
			coordinate_list[house_one] = new_cord_two

			# check if there is enough space to place house 2 then place
			if Area().housecheck(grid, new_cord_two) == True:
				if Area().spacecheck(grid, new_space_cords_two) == True:					
					grid = reset(grid, new_cord_two, new_space_cords_two)
					coordinate_list[house_two] = new_cord_one

				else:
					grid = Area().create_space(new_space_cords_one, grid)
					grid = reset(grid, old_cords_one, space_old_cords_one)
					grid = reset(grid, old_cords_two, space_old_cords_two)
					return None

			else:
				grid = Area().create_space(new_space_cords_one, grid)
				grid = reset(grid, old_cords_one, space_old_cords_one)
				grid = reset(grid, old_cords_two, space_old_cords_two)
				return None
		else:
			grid = reset(grid, old_cords_one, space_old_cords_one)
			grid = reset(grid, old_cords_two, space_old_cords_two)
			return None

	else:
		grid = reset(grid, old_cords_one, space_old_cords_one)
		grid = reset(grid, old_cords_two, space_old_cords_two)
		return None			

	# if the houses were swapped return the grid information
	return [coordinate_list, grid, [old_cords_one, old_cords_two], [space_old_cords_one, space_old_cords_two], [house_one, house_two], [new_space_cords_one, new_space_cords_two]]
