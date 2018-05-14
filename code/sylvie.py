from houses import *
from grid import *
from water import *
from random_algoritme import *

import random as random

# Hill climbing
# Evaluate the initial state.
# Loop until a solution is found or there are no new operators left to be applied:
# -	select and apply an operation to the current state and get a new state
# -	evaluate the new state:
# 		compare it to the goal --> quit
# 		new state better than current state? --> update current state

def Hill_Climber(nr_of_houses):
	starting_state = Random(nr_of_houses)

	coordinate_list = starting_state[0]
	water_coordinates = starting_state[1]
	total_value = starting_state[2]

	nr_of_changes = 5
	for i in range(nr_of_changes):
		randomChange(coordinate_list, nr_of_houses)

def updateCoordinatelist(coordinate_list):

def deleteCords(grid, coordinates):


def randomChange(coordinate_list, nr_of_houses):
	#changeOptions = [1, 2, 3, 4]
	#change = random.choice(changeOptions)
	house_one = randint(0, nr_of_houses)
	house_two = randint(0, nr_of_houses)
	change = 1

	if change == 1:
		house_cords_one = coordinate_list[house_one]
		house_cords_two = coordinate_list[house_two]
		
		randomHouse = random.choice(houseCords)
		width = height
		height = width
		newCords = []
		# deleting randomHouse (oude coordinaten)
		# adding newCords
		grid = Area().update_grid(grid, newCords, "house")
		NewState = grid
		valueNewState =
		return NewState, valueNewState

# 	if change == 2:
#	random verplaatsen van random huis
# 	if change == 3:
#	swapping random houses
# 	if change == 4:
#	changing/moving water


def HillClimbing():
while (solution not found or states left to check)
	if valueNewState >= goalValue:
		return True
	elif valueNewState >= valueCurrentState
		CurrentState = NewState
	else
		do it again
