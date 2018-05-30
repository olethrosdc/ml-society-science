## Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import scipy.io as sio

## Load a simple spectral dataset
original = sio.loadmat("../../data/micromass/data.mat")


## split data into training and test sets
n_train = 300  # number of training points
X_train, X_test, y_train, y_test = train_test_split(original['X'],
                                                    original['Y'],
                                                    train_size=n_train)
train_accuracy = {}
test_accuracy = {}
weights = ['uniform', 'distance']
n_neighbors = [1, 2, 4, 8, 16, 32, 64]

# cycle through all the parameters and see what we get
for weight in weights:
    train_accuracy[weight], test_accuracy[weight] = [], []
    for n_neighbor in n_neighbors:
        # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbor, weights=weight)
        clf.fit(X_train, y_train.ravel())
        train_accuracy[weight].append(
            accuracy_score(y_train, clf.predict(X_train)))
        test_accuracy[weight].append(
            accuracy_score(y_test, clf.predict(X_test)))
        print(n_neighbor,
              weight,
              train_accuracy[weight][-1],
              test_accuracy[weight][-1])
