from houses import *
from grid import *
from random import *

def Overlap(new_coordinate, coordinate_list):
# check if the coordinates are overlapping
	
	if new_coordinate == None:
		return False
	else:
	
		left_x_new = new_coordinate[0]
		right_x_new = new_coordinate[2]
		up_y_new = new_coordinate[1]
		down_y_new = new_coordinate[3]
		
		# check coordinates in list
		for cords in coordinate_list:
			left_x_list = cords[0]
			right_x_list = cords[2]
			up_y_list = cords[1]
			down_y_list = cords[3]

			# check if there is overlap
			if ((left_x_new > left_x_list or left_x_new == left_x_list) and (left_x_new < right_x_list or left_x_new == right_x_list) and (up_y_new < up_y_list or up_y_new == up_y_list) and (up_y_list > down_y_list or up_y_list == down_y_list)):
				return False
			if ((right_x_new > left_x_list or right_x_new == left_x_list) and (right_x_new < right_x_list or right_x_new == right_x_list) and (up_y_new < up_y_list or up_y_new == up_y_list) and (up_y_list > down_y_list or up_y_list == down_y_list)):
				return False
			if ((left_x_new > left_x_list or left_x_new == left_x_list) and (left_x_new < right_x_list or left_x_new == right_x_list) and (down_y_new < up_y_list or down_y_new == up_y_list) and (down_y_new > down_y_list or down_y_new == down_y_list)):
				return False
			if ((right_x_new > left_x_list or right_x_new == left_x_list) and (right_x_new < right_x_list or right_x_new == right_x_list) and (down_y_new < up_y_list or down_y_new == up_y_list) and (down_y_new > down_y_list or down_y_new == down_y_list)):
				return False
				
		return True