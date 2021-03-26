# %%
import numpy as np
# from __future__ division
import matplotlib.pyplot as plt
from IPython import display


# %%
# generate a length-128 vector with 5 non-zero coefficients and permute them
# randomly
x = np.array([0.2, 0.5, 0.6, 0.8, 1]+[0]*(128-5))
x = x[np.random.permutation(128)-1]

plt.stem(x)
plt.show()


# %%
# add gaussian noise with standard deviation = 0.05 to the signal
y = x + 0.05 * np.random.randn(128)
plt.plot(x, y)
plt.show()

# %%
# denoising and regularization
lmda = [0.01, 0.05, 0.1, 0.2]

plt.figure()
for i in range(len(lmda)):
    plt.subplot(2, 2, i+1)
    plt.title(f'lamda = {i}')
    plt.axis([0, 130, -0.5, 1])
    x_hat = y/(1+lmda[i])
    plt.stem(x_hat)
plt.show()

# %%
def SoftThresh(y, lmda):
    if y > lmda:
        return y - lmda
    elif y < -lmda:
        return y + lmda
    else:
        return 0

def norm_l1(x_hat, y, lmda):
    for i in range(x_hat.size):
        x_hat[i] = SoftThresh(y[i], lmda)
    return x_hat
x_hat_l1 = norm_l1(x_hat, y, 2)
plt.stem(x_hat_l1)
plt.show()


# %%
plt.figure()
for i in range(len(lmda)):
    plt.subplot(2, 2, i+1)
    plt.title(f'lamda = {lmda[i]}')
    x_hat_temp = norm_l1(x_hat, y, lmda[i])
    plt.stem(x_hat_temp)
plt.show()


# %%
# Compute the unitary Discrete Fourier transform of the sparse signal
X = np.fft.fft(x)


# %%
# Undersample X by 4 by taking 32 equispaced
# Compute the inverse Fourier Transform filling the missing data 
# with zeros, and multipy by 4 to correct for the fact that we 
# only have 1/4 of the samples.
Xu = np.zeros(128, dtype='complex')
Xu[::4] = X[::4]
Xu = np.fft.ifft(Xu)
plt.stem(Xu)
plt.show()


# %%
# Reconstruct the original signal from this minimum-norm solution
# Undersample the data by taking 32 random samples, 
# compute the zero-filled inverse Fourier transform and multiply 4
Xr = np.zeros(128, dtype='complex')
prm = np.random.permutation(128) - 1
Xr[[prm[:32]]] = X[prm[:32]]
xr = np.fft.ifft(Xr) * 4
plt.stem(xr)
plt.show
# %%
