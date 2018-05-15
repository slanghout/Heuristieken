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

# Hill Climbing Algorithm
currentState = Random(20)
valueCurrentState = currentState[2]

def randomChange():
	#changeOptions = [1, 2, 3, 4]
	#change = random.choice(changeOptions)
	change = 1

	# random huis draaien
	if change == 1:
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

    # random huis verplaatsen
	if change == 2:

    # random huizen wisselen
	if change == 3:

    # random water verplaatsen
	if change == 4:


def updateCoordinatelist(coordinate_list):

def deleteCords(grid, coordinates):


def HillClimbing():
while (solution not found or states left to check)
	if valueNewState >= goalValue:
		return True
	elif valueNewState >= valueCurrentState
		CurrentState = NewState
	else
		do it again