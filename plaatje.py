import matplotlib.pyplot as plt
import numpy as np

x = np.arange(28800).reshape((160, 180))

fig, axs = plt.subplots(sharex=False)

axs.imshow(x, cmap = None, origin='lower', interpolation=None)
plt.show()

kleurenarray geven in een float
3 dimentionale array; array in array in array
voor een array met een 4 bij 4 array heeft elke array erin (16) een 3 kleuren array, rgb(0.,0.,0.) 1 is max, 0 is geen rood,
punt achter de puntjes
array met kleuren, elke kleur een nummer aangeven, rood is 1, geel is 2, blauw is 3.
aangeven welk vakje welke kleur wordt
numpy:nieuwe image met 


Presentatie: als een eindpresentatie
