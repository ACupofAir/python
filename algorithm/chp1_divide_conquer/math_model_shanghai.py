import numpy as np
from scipy import optimize
from matplotlib import pyplot

x0=2347.46

def f(t,r):
    return x0*np.exp(r*t)

x=np.array([2347.46, 2380.43, 2415.15, 2425.68, 2415.27, 2419.7, 2418.33, 2423.78
            ])
t=np.arange(0,8,1)
# t = range(8)
fita = [0]*10
fita[0] = 0.014
# pyplot.plot(t,x,'.')
x_new=f(t,fita[0])
print(6, f(6,fita[0]), f(6, fita[0])-x[6],(f(6, fita[0])-x[6])/f(6,fita[0]))
print(7, f(7,fita[0]), f(7, fita[0])-x[7],(f(7, fita[0])-x[7])/f(7,fita[0]))

x_temp = np.arange(0, 1000, 1)
pyplot.plot(x_temp, f(x_temp, fita[0]))
# pyplot.plot(t,x_new)
pyplot.show()
pyplot.Rectangle
