# GRADIENT DESCENT  CODE FROM SCRATCH
# https://www.youtube.com/watch?v=gsfbWn4Gy5Q


import numpy as np
import matplotlib.pyplot as plt


def y_function(x):
    return np.sin(x)


def y_derivative(x):
    return np.cos(x)


x = np.arange(-5, 5, 0.1)
y = y_function(x)

current_pos = (1, 5, y_function(1, 5))
# current_position is not a local minimum, but it's the starting point from which the algorithm will try to find the minimum of the quadratic function.

learning_rate = 0.01

for _ in range(1000):
    new_x = current_pos[0]-learning_rate*y_derivative(current_pos[0])
    new_y = y_function(new_x)


plt.plot(x, y)
plt.scatter(new_x, new_y, color="red")
plt.pause(0.001)
plt.clf()
