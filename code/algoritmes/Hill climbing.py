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

# class State(object):

# Random oplossing nemen als beginsituatie -> current state

	current = Random(20)

	currentState = grid
	valueCurrentState = total_value

def updateCoordinatelist(coordinate_list):

def deleteCords(grid, coordinates):


def randomChange():
	#changeOptions = [1, 2, 3, 4]
	#change = random.choice(changeOptions)
	change = 1

	if change == 1:
		draaien van random huis
		houseCords = coordinate_list
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
