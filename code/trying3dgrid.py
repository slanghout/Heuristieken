from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

a = [[16, 16, 0, 0], [16, 16, 0, 0]]
b = [[16, 0, 16, 0], [16, 0, 16, 0]]
c = [[10, 10, 10, 10], [0, 0, 0, 0]]


x = np.array(a)
y = np.array(b)
z = np.array(c)

# hele surface een kleur
ax.plot_surface(x, y, z, color="pink")

# lijnen tussen de punten
# ax.plot_wireframe(x, y, z, color='black')

plt.show()