import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Major ticks every 2, minor ticks every 0.5
#major_ticks = np.arange(0, 200, 20)
#minor_ticks = np.arange(0, 200, 0.5)

#ax.set_xticks(major_ticks)
#ax.set_xticks(minor_ticks, minor=True)
#ax.set_yticks(major_ticks)
#ax.set_yticks(minor_ticks, minor=True)

# And a corresponding grid
#ax.grid(which='both')

#ax.set_xlim(left=0, right=180, auto=False)
#ax.set_ylim(bottom=0, top=160, auto=False)

# Or if you want different settings for the grids:
#ax.grid(which='minor', alpha=0.2)
#ax.grid(which='major', alpha=0.5)

plt.xlabel('width')
plt.ylabel('height')
plt.title('Amstelhaege')

plt.grid(True)

# create blue rectangle
#x = [left, left, right, right]
#y = [bottom, top, top, bottom]
#x = [10, 10, 5, 5]
#y = [5, 10, 10, 5]
#ax.fill(x, y, "b", label="water")
#plt.legend(loc=1)


#wouter
#x = np.array[(3 kleuren)]
#x = np.array((0.0, 0.5, 0.5))
#y = np.random.random((160,180))
#im = plt.imshow(y, cmap=x)
#plt.imshow(extent=[coordinates], cmap=)
#plt.imshow(x, cmap=X)




#X = np.array(((1,2,3,4,5),(4,5,6,7,8),(7,8,9,10,11)))
#plt.imshow(X, cmap="Pastel1")
#x = ((0, 0, 180, 180), (0, 160, 160, 0))
#colormap = ("rainbow")
#plt.imshow(x, cmap=colormap)
#im = plt.imshow(x)

# filling the whole grid randomly with pastel colors

x = np.random.random((160,180))
plt.imshow(x, cmap=plt.cm.Pastel1)

# filling the whole grid with 5 colors
#blue = "dodgerblue"
#purple = "darkorchid"
#green = "lime"
#orangy = "orangered"
#redpink = "crimson"
#colormap = np.array((blue), (purple))

plt.show()