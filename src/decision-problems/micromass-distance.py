print(__doc__)

## Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
import scipy.io as sio

## Load a simple spectral dataset
original = sio.loadmat("../../data/micromass/data.mat")


## split data into training and test sets
n_train = 300 # number of training points
X_train = original['X'][:n_train]
y_train = original['Y'][:n_train]
X_test = original['X'][n_train:]
y_test = original['Y'][n_train:]
n_dim = X_train.shape[1]
mean_A = np.zeros([n_dim])
mean_B = np.zeros([n_dim])
n_A = 0
n_B = 0

## Get the most distinguishing feature
for t in range (n_train):
    if (y_train[t] == 0):
        n_A += 1
        mean_A += (X_train[t, :] - mean_A) / n_A
    else:
        n_B += 1
        mean_B += (X_train[t, :] - mean_B) / n_B

diff = mean_A - mean_B
max_features = np.argmax(abs(diff))

plt.plot(abs(diff))
plt.plot([max_features, max_features], [0,abs(diff[max_features])])
plt.show()

