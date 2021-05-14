import numpy as np
from scipy import optimize
from matplotlib import pyplot

x0=2347.46

def f(t,r,K):
    return K/(1+(K/x0-1)*np.exp(-r*t))

x=np.array([2347.46, 2380.43, 2415.15, 2425.68, 2415.27, 2419.7, 2418.33, 2423.78
])
t=np.arange(0,8,1)
fita = [0.014, 2425.4]

x_new=f(t,fita[0], fita[1])
print(fita[0], fita[1])
print(6, f(6,fita[0],fita[1]), f(6, fita[0],fita[1])-x[6],(f(6, fita[0], fita[1])-x[6])/f(6,fita[0], fita[1]))
print(7, f(7,fita[0],fita[1]), f(7, fita[0],fita[1])-x[7],(f(7, fita[0], fita[1])-x[7])/f(7,fita[0], fita[1]))
# pyplot.plot(t,x,'.')
# pyplot.plot(t,x_new)
x_temp = np.arange(0, 1000, 1)
pyplot.plot(x_temp, f(x_temp, fita[0], fita[1]))
pyplot.show()
