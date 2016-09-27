'''
Unit2 lesson1: Overview of Probability
'''

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

mean = 0.0
variance = 1.0
sigma = np.sqrt(variance) #standard deviation
x_values = np.linspace(-3, 3, 100)

plt.plot(x_values, mlab.normpdf(x_values, mean, sigma))
plt.show()