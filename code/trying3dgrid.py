from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

x = [[20, 10, 20, 10], [20, 10, 20, 10]]
y = [[15, 15, 30, 30], [15, 15, 30, 30]]
z = [[10, 10, 10, 10], [2, 2, 2, 2]]

ax.scatter3D(x, y, z, "pink")

plt.show()

