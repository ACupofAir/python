import numpy as np
from __future__ division
import matplotlib.pyplot as plt
from IPython import display


# generate a length-128 vector with 5 non-zero coefficients and permute them
# randomly
x = np.array([0.2, 0.5, 0.6, 0.8, 1]+[0]*(128-5))
x = x[np.random.permutation(128)-1]

plt.stem(x)
plt.show()


# add gaussian noise with standard deviation = 0.05 to the signal
y = x + 0.05 * np.random.randn(128)
plt.plot(x, y)
plt.show()


# denoising and regularization
lmda = [0.01, 0.05, 0.1, 0.2]

plt.figure()
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.title(f'lamda = {i}')
    plt.axis([0, 130, -0.5, 1])
    x_hat = y/(1+lmda[i])
    plt.stem(x_hat)
plt.show()
