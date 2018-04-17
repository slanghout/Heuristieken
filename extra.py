#  grid maken matplot

import numpy as np 
import matplotlib.pyplot as plt 

x = 0
y = 50
plt.plot(x, y)

plt.xlim(0, 320)  # decreasing time
plt.ylim(0, 360)

plt.title('Our neighbourhood')
plt.grid(True)

plt.show()

#  grid maken
width = 32
height = 36
grid = []
row = []
empty = '0'
for i in range(width):
	row.append(empty)
for i in range(height):
	grid.append(row)

for i in range(len(grid)):
	print(grid[i])

# huizen

class eensgezins(Huis):
	def __init__(self):
		super().init()
		self.hoogte = 1
		self.breedte = 1
		self.prijs = 285.000
		self.vrijstaand = 2
		self.percentage = 1.03

class bungalow(Huis):
	def __init__(self):
		super().init()
		self.hoogte = 2
		self.breedte = 2
		self.prijs = 399.000
		self.vrijstaand = 3
		self.percentage = 1.04

class maison(Huis):
	def __init__(self):
		super().init()
		self.hoogte = 3
		self.breedte = 3
		self.prijs = 610.000
		self.vrijstaand = 6
		self.percentage = 1.06


def prijsverhoging(self):
		return berekeningprijsverhoging
	
	@property
	def cords(self):
		return Huis.cords