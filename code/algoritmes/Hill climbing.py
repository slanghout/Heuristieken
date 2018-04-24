Hill climbing
Evaluate the initial state.
Loop until a solution is found or there are no new operators left to be applied:
-	select and apply an operation to the current state and get a new state
-	evaluate the new state:
		compare it to the goal --> quit
		new state better than current state? --> update current state


first of all we need a State class 

class State(object):
	stores the current state
	store the value of this state

define operator methods which gets us a new state
- moving a house
- swapping a house

def HillClimbing():
while (solution not found or states left to check)
	getNewState
	if (value.getnewstate => goal)
		quit/return
	elif (value.getnewstate => value.currentstate)
		getnewstate = currentstate
	else
		do it again
