import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from overlap_check import *
from houses import *
from water import *
# from opslaan2 import *

class grid(object):
	def __init__(self):
		self.width = 360
		self.height = 320
		
	def makecordinatelist(self):
		basic_grid = [["0"]*self.width for x in range(self.height)]

		return basic_grid

	def updatecordinatelist(self, cordinatelist, housecords, thing):	
		if thing == "house":
			for i in range(housecords[0], (housecords[2])):
				for j in range(housecords[3], (housecords[1])):
					if cordinatelist[j][i] == "0":
						cordinatelist[j][i] = "h"
					else:
						print("cannot build house")

		elif thing == "water":
			for i in range(housecords[0], (housecords[2])):
				for j in range(housecords[3], (housecords[1])):
					if cordinatelist[j][i] == "0":
						cordinatelist[j][i] = "w"
					else:
						print("cannot")
		# voor vrijstand: 4kant met huis erin meegeven, waar 0 staat en geen h een s zetten
		elif thing == "space":
			for i in range(housecords[0], (housecords[2])):
				for j in range(housecords[3], (housecords[1])):
					if cordinatelist[j][i] == "0" or cordinatelist[j][i] == "s":
						cordinatelist[j][i] = "s"
					elif cordinatelist[j][i] == "w":
						print("water")
					else:
						print("cannot, must be h")

		return cordinatelist

	# check if around house enough space for free space
	def spacecheck(self, cordinatelist, housecords):
		for i in range(housecords[0], (housecords[2])):
			for j in range(housecords[3], (housecords[1])):
				# print(j,i)
				if (cordinatelist[j][i] == "0" or cordinatelist[j][i] == "s"
					or cordinatelist[j][i] == "w"):
					x = 5
				else:
					return False
		return True


	# check if there is enough space to buid a house
	def housecheck(self, cordinatelist, housecords):
		for i in range(housecords[0], (housecords[2])):
			for j in range(housecords[3], (housecords[1])):
				# print(j,i)
				if cordinatelist[j][i] == "0":
					x = 5
				else:
					return False
		return True

	def makegrid(self, coordinatelist, water, total_value):

		# make the figure
		fig = plt.figure()

		# make plot
		ax = fig.add_subplot(1, 1, 1)

		# make axes grid
		major_ticks = np.arange(0, 320, 40)
		minor_ticks = np.arange(0, 400, 1)
		
		# makes lines for grid
		# ax.set_xticks(major_ticks)
		# ax.set_xticks(minor_ticks, minor=True)
		# ax.set_yticks(major_ticks)
		# ax.set_yticks(minor_ticks, minor=True)
		# ax.grid(which='both')

		# set limits for the plot
		ax.set_xlim(left=0, right=self.width, auto=False)
		ax.set_ylim(bottom=0, top=self.height, auto=False)
		
		# make background grid green
		x = [self.width, self.width, 0, 0]
		y = [0, self.height, self.height, 0]
		ax.fill(x, y, color ="#abd9e9")

	
		# iterate over coordinate list and select coordinates
		# for i in range(360):
		# 	for j in range(320):
		# 		if cordinatelist[j][i] == 'h':
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color = "#ffffbf")
		# 		elif cordinatelist[j][i] == 's':
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color = "#2c7bb6")
		# 		elif cordinatelist[j][i] == 'w':
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color ="#abd9e9")
		# 		else:
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color ="#fdae61")	


		for element in coordinatelist:
			x = [element[2], element[2], element[0], element[0]]
			y = [element[1], element[3], element[3], element[1]]

			# color coordinates coresponding color
			if element[4] == 1:
				ax.fill(x, y, color = "#ffffbf")
			elif element[4] == 2:
				# total_value += bungalow(element).giveworth()
				ax.fill(x, y, color = "#fdae61")
			elif element[4] == 3:
				# total_value += maison(element).giveworth()
				ax.fill(x, y, color = "#d7191c")

		if len(water) > 1:
			print(water)
			print(len(water))
			for body in range(len(water)):
				element = (water[body])
				x = [element[2], element[2], element[0], element[0]]
				y = [element[1], element[3], element[3], element[1]]
				ax.fill(x, y, color = "#2c7bb6")

			
		plt.xlabel('width')
		plt.ylabel('height')
		plt.title('Amstelhaege, worth: ${:,.2f}' .format(total_value))

		# bij deze beide manieren gaat de grid een beetje uit proporsie
		#plt.subplots_adjust(right = 0.75)
		plt.tight_layout(rect=[0,0,0.75,1])

		legend_single = mpatches.Patch(color = "#ffffbf", label = "single")
		legend_bungalow = mpatches.Patch(color = "#fdae61", label = "bungalow")
		legend_maison = mpatches.Patch(color = "#d7191c", label = "maison")
		legend_water = mpatches.Patch(color = "#2c7bb6", label = "water")		
		plt.legend(handles=[legend_single, legend_bungalow, legend_maison, legend_water], bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0.)

		plt.show()
