import numpy as np
import matplotlib.pyplot as plt

# je kan meerdere groepen maken voor de drie huizen
#g1 = (10, 10)
#g2 = (20, 20)
#g3 = (30, 30)

# ze allemaal een eigen kleur en titel geven
#data = (g1, g2, g3)
#colors = ("red", "green", "blue")
#groups = ("eengezinswoning", "bungalow", "maison")
#markersize?
#linewidths = (1, 2, 3)
#markeredgewidths = (1, 2, 3)
#sizes = 

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Major ticks every 2, minor ticks every 0.5
major_ticks = np.arange(0, 40, 2)
minor_ticks = np.arange(0, 40, 0.5)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# And a corresponding grid
ax.grid(which='both')

ax.set_xlim(left=0, right=18, auto=false)


# Or if you want different settings for the grids:
#ax.grid(which='minor', alpha=0.2)
#ax.grid(which='major', alpha=0.5)

#for data, color, group in zip(data, colors, groups):
 ##  ax.scatter(x, y, c=color, label=group)

#plt.scatter(x,y, label=group, c=color, s=30)

plt.xlabel('width')
plt.ylabel('height')
plt.title('Amstelhaege')

# create blue rectangle
#left = 30.0
#right = left + 0.5
#bottom = 25.0
#top = bottom + 1
#x = [left, left, right, right]
#y = [bottom, top, top, bottom]
x = [10, 10, 5, 5]
y = [5, 10, 10, 5]
ax.fill(x, y, "b")
#cplt.legend(loc=2)
plt.show()

