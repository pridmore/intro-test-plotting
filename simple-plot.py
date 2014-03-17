import numpy as np
import matplotlib.pyplot as plt

#simple tests of 2d plotting

radius = [1.0,2.0,3.0,4.0,5.0,6.0]
area = [np.pi*k*k for k in radius]
plt.plot(radius, area)
plt.show()
