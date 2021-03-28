# %%
import numpy as np
# from __future__ division
import matplotlib.pyplot as plt
from IPython import display


# %p
# generate a length-128 vector with 5 non-zero coefficients and permute them
# randomly
x = np.array([0.2, 0.5, 0.6, 0.8, 1]+[0]*(128-5))
x = x[np.random.permutation(128)-1]

plt.stem(x)
plt.show()


# %%
# add gaussian noise with standard deviation = 0.05 to the signal
y = x + 0.05 * np.random.randn(128)
plt.stem(y)
plt.show()

# %%
# denoising and regularization
lmda = [0.01, 0.05, 0.1, 0.2]

plt.figure()
for i in range(len(lmda)):
    plt.subplot(2, 2, i+1)
    plt.title(f'lamda = {lmda[i]}')
    plt.axis([0, 130, -0.5, 1.2])
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


def norm_l1(y, lmda):
    x_hat_l1 = np.zeros(y.size)
    for i in range(y.size):
        x_hat_l1[i] = SoftThresh(y[i], lmda)
    return x_hat_l1


x_hat_l1 = norm_l1(y, 2)
plt.stem(x_hat_l1)
plt.show()


# %%
plt.figure()
for i in range(len(lmda)):
    plt.subplot(2, 2, i+1)
    plt.title(f'lamda = {lmda[i]}')
    x_hat_temp = norm_l1(y, lmda[i])
    plt.stem(x_hat_temp)
plt.show()


# %%
# Compute the unitary Discrete Fourier transform of the sparse signal
X = np.fft.fft(x)
plt.stem(X)
plt.show()


# %%
# Undersample X by 4 by taking 32 equispaced
# Compute the inverse Fourier Transform filling the missing data
# with zeros, and multipy by 4 to correct for the fact that we
# only have 1/4 of the samples.
Xu = np.zeros(128, dtype='complex')
Xu[::4] = X[::4]
xu = np.fft.ifft(Xu)*4
plt.stem(Xu)
plt.show()

plt.stem(xu.real)
plt.show()

# %%
# Reconstruct the original signal from this minimum-norm solution
# Undersample the data by taking 32 random samples,
# compute the zero-filled inverse Fourier transform and multiply 4
Xr = np.zeros(128, dtype='complex')
prm = np.random.permutation(128) - 1
Xr[[prm[:32]]] = X[prm[:32]]
xr = np.fft.ifft(Xr) * 4
plt.stem(xr.real)
plt.show()


# %%
# Reconstruction from Randomly Sampled Frequency Domain Data


Y = Xr
Xi = Y
plt.figure()
for i in range(36):
    plt.subplot(6, 6, i+1)
    xi = np.fft.ifft(Xi)
    xi_st = norm_l1(xi.real, lmda[2])
    Xi = np.fft.fft(xi_st)
    Xi = Xi * (Y == 0) + Y
    plt.stem(xi.real)
    plt.title('Iteration %d' % i)
plt.show()

Y = Xu
Xi = Y
plt.figure()
for i in range(36):
    plt.subplot(6, 6, i+1)
    xi = np.fft.ifft(Xi)
    xi_st = norm_l1(xi.real, lmda[2])
    Xi = np.fft.fft(xi_st)
    Xi = Xi * (Y == 0) + Y
    plt.stem(xi.real)
    plt.title('Iteration %d' % i)
plt.show()
