import numpy as np
import matplotlib.pyplot as plt

from overlap_check import *
from houses import *
from grid import *
from water import *

class grid(object):
	def __init__(self):
		self.width = 360
		self.height = 320
		
	def makecordinatelist(self):
		cordinatelist = []
		row = []
		for i in range(self.width):
			row.append('0')
		for j in range(self.height):
			cordinatelist.append(row)

		# print((cordinatelist))
		return cordinatelist

	def updatecordinatelist(self, cordinatelist, housecords, building):	
		if building == "houses":
			print(housecords)
			for i in range(housecords[0], (housecords[2]+1)):
				for j in range(housecords[3], (housecords[1]+1)):
					# print(cordinatelist[height][width])
					if cordinatelist[j][i] != "0":
						print("no")
						# print(cordinatelist[j][i])
					else:
						print("doei")
						cordinatelist[j][i] = "h"
						
		# elif building == "water":
		# 	width = cordinate[2] - cordinate[0]
		# 	height = cordinate[3] = cordinate[1]
		# 	for i in range(cordinate[0], (cordinate[2] + 1)):
		# 		for j in range(cordinate[1], (cordinate[3]+1)):
		# 			if cordinatelist[j][i] == "0":

		# 				cordinatelist[j][i] = "w"
		# elif building == "space":
		# 	width = cordinate[2] - cordinate[0]
		# 	height = cordinate[3] = cordinate[1]
		# 	for i in range(cordinate[0], (cordinate[2] + 1)):
		# 		for j in range(cordinate[1], (cordinate[3]+1)):
		# 			if cordinatelist[i][j] == "0":
		# 				cordinatelist[i][j] = "s"

		# print(cordinatelist)
		# print(cordinatelist)
		return cordinatelist

	def overlapping(self, cordinatelist, housecords):
		for i in range(housecords[0], (housecords[2])):
			for j in range(housecords[3], (housecords[1])):
				if cordinatelist[j][i] == "0":
					print('yay')
				else:
					print(cordinatelist[j][i])
					return False
		return True

	def makegrid(self, coordinatelist, total_value):

		# make the figure
		fig = plt.figure()

		# make plot with green background
		ax = fig.add_subplot(1, 1, 1)

		# make axes grid steps of 0.5 m
		major_ticks = np.arange(0, 400, 40)
		minor_ticks = np.arange(0, 400, 1)
		# imshow

		# # makes lines for grid
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

		water_bodies = [1, 2, 3, 4]
		amount_water = random.choice(water_bodies)
		print(amount_water)
		
		elements = MakeWater(amount_water)
		for element in elements:
			x = [element[2], element[2], element[0], element[0]]
			y = [element[1], element[3], element[3], element[1]]
			ax.fill(x, y, color = "#2c7bb6")
			
		# set labels for the axes 

		# 	ax.fill(x, y, "deepskyblue")

		# set labels for the axes

		plt.xlabel('width')
		plt.ylabel('height')
		plt.title('Amstelhaege, worth: ${:,.2f}' .format(total_value))

		# plt.legend(loc=0)
		#for data, color, group in zip(data, colors, groups):
 		##  ax.scatter(x, y, c=color, label=group)

		#plt.scatter(x,y, label=group, c=color, s=30)
		plt.show()
