from houses import *
from grid import *
from random import *

# function to check if coordinates overlap with other coordinates in list
def Overlap(new_coordinate, coordinate_list):
	
	# make sure coordinates are given
	if new_coordinate == None:
		return False
	
	# set 4 coordinates of the new coordinate
	else:
		left_x_new = new_coordinate[0]
		right_x_new = new_coordinate[2]
		up_y_new = new_coordinate[1]
		down_y_new = new_coordinate[3]
		
		# set 4 coordinates for current coordinate in the list
		for cords in coordinate_list:
			left_x_list = cords[0]
			right_x_list = cords[2]
			up_y_list = cords[1]
			down_y_list = cords[3]

			# check if there is overlap
			# check if 4 corners new house not in house in list
			if ((left_x_new > left_x_list or left_x_new == left_x_list) and (left_x_new < right_x_list or left_x_new == right_x_list) and (up_y_new < up_y_list or up_y_new == up_y_list) and (up_y_new > down_y_list or up_y_new == down_y_list)):
				return False
			if ((right_x_new > left_x_list or right_x_new == left_x_list) and (right_x_new < right_x_list or right_x_new == right_x_list) and (up_y_new < up_y_list or up_y_new == up_y_list) and (up_y_new > down_y_list or up_y_new == down_y_list)):
				return False
			if ((left_x_new > left_x_list or left_x_new == left_x_list) and (left_x_new < right_x_list or left_x_new == right_x_list) and (down_y_new < up_y_list or down_y_new == up_y_list) and (down_y_new > down_y_list or down_y_new == down_y_list)):
				return False
			if ((right_x_new > left_x_list or right_x_new == left_x_list) and (right_x_new < right_x_list or right_x_new == right_x_list) and (down_y_new < up_y_list or down_y_new == up_y_list) and (down_y_new > down_y_list or down_y_new == down_y_list)):
				return False

			# check if 4 corners house in list not in new house
			if ((left_x_list > left_x_new or left_x_list == left_x_new) and (left_x_list < right_x_new or left_x_list == right_x_new) and (up_y_list < up_y_new or up_y_list == up_y_new) and (up_y_list > down_y_new or up_y_list == down_y_new)):
				return False
			if ((right_x_list > left_x_new or right_x_list == left_x_new) and (right_x_list < right_x_new or right_x_list == right_x_new) and (up_y_list < up_y_new or up_y_list == up_y_new) and (up_y_list > down_y_new or up_y_list == down_y_new)):
				return False
			if ((left_x_list > left_x_new or left_x_list == left_x_new) and (left_x_list < right_x_new or left_x_list == right_x_new) and (down_y_list < up_y_new or down_y_list == up_y_new) and (down_y_list > down_y_new or down_y_list == down_y_new)):
				return False
			if ((right_x_list > left_x_new or right_x_list == left_x_new) and (right_x_list < right_x_new or right_x_list == right_x_new) and (down_y_list < up_y_new or down_y_list == up_y_new) and (down_y_list > down_y_new or down_y_list == down_y_new)):
				return False
				
		# if new house does not overlap with any house return true
		return True

