import matplotlib.pyplot as plt
import numpy as np

# grid = plt.imshow(np.reshape(np.random.rand(100), newshape=(10,10)),
#                     interpolation='none', vmin=0, vmax=1, aspect='equal')

grid = plt.imshow(data, extend = (0, 360, 0, 320))
