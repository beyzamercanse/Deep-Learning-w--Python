# GRADIENT DESCENT CODE FROM SCRATCH

import numpy as np
import matplotlib.pyplot as plt




def y_function(x):
    return x**2


def y_derivative(x):
    return x*2


x = np.arange(-100, 100, 0.1)
y = y_function(x)

current_position = (80, y_function(80))
learning_rate = 0.001

for _ in range(1000):
    new_x = current_position[0] - learning_rate * \
        y_derivative(current_position[0])
    new_y = y_function(new_x)
    current_position = (new_x, new_y)

# new_position=current_position−learning_rate×gradient
# In gradient descent, the update rule is subtracting the product of the learning rate and the gradient from the current position. This is because the gradient points in the direction of the steepest increase of the function. By subtracting the gradient, you move in the opposite direction, towards the steepest decrease, which is the direction of the minimum.


plt.plot(x, y)
plt.scatter(current_position[0], current_position[1], color="red")
plt.pause(0.001)
plt.clf()
