import numpy as np
import matplotlib.pyplot as plt

from houses import *

class grid(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def makegrid(self, coordinatelist):
		
		# make the figure
		fig = plt.figure()

		# make plot with green background
		ax = fig.add_subplot(1, 1, 1)

		# make axes grid steps of 0.5 m
		major_ticks = np.arange(0, 200, 20)
		minor_ticks = np.arange(0, 200, 0.5)
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
		ax.fill(x, y, "g")
		
		total_value = 0
		
		# iterate over coordinate list and select coordinates
		for element in coordinatelist:
			x = [element[2], element[2], element[0], element[0]]
			y = [element[1], element[3], element[3], element[1]]
				
			# color coordinates coresponding color
			if element[4] == 1:
				ax.fill(x, y, "r")
			elif element[4] == 2:
				ax.fill(x, y, "y")
			elif element[4] == 3:
				ax.fill(x, y, "b")
		
		# set labels for the axes 
		plt.xlabel('width')
		plt.ylabel('height')
		plt.title('Amstelhaege, worth: ${}' .format(total_value))
		
		# plt.legend(loc=0)
		#for data, color, group in zip(data, colors, groups):
 		##  ax.scatter(x, y, c=color, label=group)

		#plt.scatter(x,y, label=group, c=color, s=30)
		plt.show()