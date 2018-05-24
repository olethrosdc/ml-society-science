print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
import scipy.io as sio

original = sio.loadmat("../../data/micromass/data.mat")

n_train = 300
X_train = original['X'][:n_train]
y_train = original['Y'][:n_train]
X_test = original['X'][n_train:]
y_test = original['Y'][n_train:]

### Create color maps
### Now we can classify

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X_train, y_train.ravel())
    accuracy = 0
    prediction = clf.predict(X_train)
    T = y.size
    for t in range(1, T):
        if (prediction[t]==y[t]): accuracy+=1
    accuracy /= T

        
    



