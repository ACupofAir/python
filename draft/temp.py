import matplotlib.pyplot as plt
import numpy as np


def w(t, c):
    return (3/2)*(t+c)**(1/2)*t


t = np.arange(0., 20., 0.2)


plt.plot(t, w(t, 1))
plt.plot(t, w(t, 2))
plt.plot(t, w(t, 4))
plt.plot(t, w(t, 8))
plt.show()


def f(x):
    return -2/(5*((1-4*x*x/25)**(1/2)))


x = np.arange(0., 20., 0.2)


plt.plot(x, f(x))
plt.show()

