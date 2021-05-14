#%%
import numpy as np
import pylab as pl
from scipy import interpolate 
import matplotlib.pyplot as plt

x = [0, 300, 600, 1000, 1500, 2000]
y = [0.9689, 0.9322, 0.8969, 0.8519, 0.7989, 0.7491]

x_new = np.linspace(0, 2000, 100)
f_linear = interpolate.interp1d(x, y)
def p_x(x):
    return 1.0332*np.exp(-(x+500)/7756)

plt.xlabel(u'/m')
plt.ylabel(u'/p')

plt.plot(x, y, "o",  label=u"orginal")
plt.plot(x_new, f_linear(x_new), label=u"linear")
plt.plot(x_new, p_x(x_new), label=u"proposed")
#%%
for i in range(21):
    print(f'linear\t{100*i}\t{f_linear(i*100)}')
    print(f'propos\t{100*i}\t{p_x(i*100)}')

pl.legend()
pl.show()

# %%
