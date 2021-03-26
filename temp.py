#%%
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace


x = [10, 30, 50, 100, 300, 500, 1000, 3000, 4000, 7000, 10000, 15000,20000]
y_insert = [0.55, 5.05, 2.71, 7.2, 23.65, 51.71,
        159.45, 1086.45, 1995.78, 6646.38, 11312.2, 24753.6,444155]
y_merge = [21.23, 27.23, 29.15, 44.12, 110.4, 180.49,
        355.47, 1195.47, 1582.27, 3206.12,  4535.58, 6833.07,11322]
y_heap = [3.86, 9, 12.74, 31.88, 146.19, 313.65,
        890.87, 2458.4, 3439.67, 6160, 8965.81, 13914,22558]
y_quick = [3.1,14.2,24.4,57.6,223.9,413.6,954.5,3718.7,5151.7,10792.6,18195.9,30960.7,49924.1]
plt.plot(x, y_insert, color='r', label="insert")
plt.plot(x, y_merge, color='#778245', label="merge")
plt.plot(x, y_heap, color='#3498db', label="heap")
plt.plot(x, y_quick, color='#34495e', label="quick")
plt.legend(loc='upper left', bbox_to_anchor=(0.2, 0.95))

plt.xlabel('NumOfElements')
plt.ylabel('Time/us')


# %%
x = np.arange(-1, 1, 0.1)

y1 = np.exp(x)
y2 = np.exp(2 * x)

plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1, label="y1")
plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1, label="y2")

plt.legend(loc='upper left', bbox_to_anchor=(0.2, 0.95))

plt.title("Figure 1")

plt.show()
# %%
