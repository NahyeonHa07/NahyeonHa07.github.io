# velocity_acceleration_plot.py
# This script calculates and visualizes a function's graph, its velocity (1st derivative), and acceleration (2nd derivative).

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. Define the function to analyze
# -------------------------------
def func(x):
    # Define the function you want here
    # Example: y = x**2
    y = x**2
    return y

# -------------------------------
# 2. Numerical derivative: 1st derivative (velocity)
# -------------------------------
def numerical_derivative1(x, h):
    y = []
    for each_x in x:
        tangent = (func(each_x + h) - func(each_x)) / h
        y.append(tangent)
    return y

# -------------------------------
# 3. Numerical derivative: 2nd derivative (acceleration)
# -------------------------------
def numerical_derivative2(x, h):
    d1 = numerical_derivative1(x, h)
    y = []
    for i in range(0, len(d1)-1):
        tangent = (d1[i+1] - d1[i]) / h
        y.append(tangent)
    # Append the last value to keep the list the same length
    y.append(y[len(y)-1])
    return y

# -------------------------------
# 4. Set graph range and step size
# -------------------------------
h = 1e-3          # Step size for numerical derivative
A = 0             # Start of the graph
B = 10            # End of the graph
x = np.arange(A, B, h)

# -------------------------------
# 5. Plot the graph
# -------------------------------
line1, = plt.plot(x, func(x), label='Function')
line2, = plt.plot(x, numerical_derivative1(x, h), color='orange', label='Velocity')
line3, = plt.plot(x, numerical_derivative2(x, h), color='green', label='Acceleration')

plt.legend(handles=(line1, line2, line3))
plt.grid()
plt.xlabel('x')
plt.ylabel('y / Velocity / Acceleration')
plt.title('Function, Velocity, and Acceleration')
plt.show()
