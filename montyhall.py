from __future__ import division
from random import randint
def setUpGame(numberOfDoors):
#Place a car behind one door and goats behind the others.
	doors = [];
	carDoor = randint(0, numberOfDoors - 1)
	for i in range(numberOfDoors):
		if carDoor == i :
			doors.append("car");
		else: 
			doors.append("goat");
		
	
	return doors
def revealDoor(doors, currentDoor):
	#Reveal one door that is not the car and not the contestant's current choice.
	while True:
		i = randint(0, len(doors)-1)
		if ( i == currentDoor or doors[i] != "goat"):
			continue
		else:
			#print i
			return i
		
def switchDoors(doors, currentDoor, revealDoor):
#Switch the contestant's choice to a door that is not their current door and not a revealed door.
	while True:
		i = randint(0, len(doors) - 1)
		if (i == currentDoor or i == revealDoor):
			continue
		else:
			#print i
			return i
def MontyHallSim(numberOfDoors, numberOfTrials):
	wins = 0
	altWins = 0
	for i in range(numberOfTrials):
		
		doors = setUpGame(numberOfDoors)
		chosenDoor = randint(0, len(doors) - 1)
		#print doors[chosenDoor]
		revealedDoor = revealDoor(doors, chosenDoor)
		altDoor = switchDoors(doors, chosenDoor, revealedDoor)
		if doors[chosenDoor] == "car":
			#print "You win"
			wins += 1
		elif doors[altDoor] == "car":
			altWins += 1
	print "Wins when sticking = "+str(wins)
	print "Wins when switching = "+str(altWins)
	#print "Percentage= "+ str(altWins/numberOfTrials)

MontyHallSim(4, 1000)
