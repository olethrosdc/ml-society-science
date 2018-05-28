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
n_neighbors = 1

## Utility function for calculating accuracy
def Accuracy(clf, X, y):
    accuracy = 0
    prediction = clf.predict(X)
    T = y.size
    for t in range(T):
        if (prediction[t]==y[t]): accuracy+=1
    accuracy /= T
    return accuracy

k = 0
train_accuracy = [None] * 14
test_accuracy = [None] * 14
KNarray = [None] * 14
KWarray = [None] * 14

# cycle through all the parameters and see what we get
for weights in ['uniform', 'distance']:
    for n_neighbors in [1, 2, 4, 8, 16, 32, 64]:
        # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
        clf.fit(X_train, y_train.ravel())
        train_accuracy[k] = Accuracy(clf, X_train, y_train)
        test_accuracy[k] = Accuracy(clf, X_test, y_test)
        KNarray[k] = n_neighbors
        KWarray[k] = weights
        print(KNarray[k], KWarray[k], train_accuracy[k], test_accuracy[k])
        k+=1
    



