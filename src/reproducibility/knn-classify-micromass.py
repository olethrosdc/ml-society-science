## Import required libraries
import numpy as np # general math
import matplotlib.pyplot as plt # plotting
from matplotlib.colors import ListedColormap # for colours
from sklearn import neighbors # for nearest neighbour
from sklearn.linear_model import LogisticRegression # for LR
from sklearn.model_selection import train_test_split # for splitting datasets
from sklearn.metrics import accuracy_score # for measuring accuracy
import scipy.io as sio # for loading data

## Load a simple spectral dataset
original = sio.loadmat("../../data/micromass/data.mat")


## split data into training and test sets
n_train = 128 # number of training points
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
        #clf = neighbors.KNeighborsClassifier(n_neighbor, weights=weight)
        clf = LogisticRegression()
        clf.fit(X_train, y_train.ravel())
        train_accuracy[weight].append(
            accuracy_score(y_train, clf.predict(X_train)))
        test_accuracy[weight].append(
            accuracy_score(y_test, clf.predict(X_test)))
        print(n_neighbor,
              weight,
              train_accuracy[weight][-1],
              test_accuracy[weight][-1])

plt.figure(1)
plt.plot(n_neighbors, train_accuracy['uniform'])
plt.plot(n_neighbors, test_accuracy['uniform'])
plt.xlabel("Number of neighbours")
plt.ylabel("Accuracy")
plt.title("Uniform")
plt.figure(2)
plt.plot(n_neighbors, train_accuracy['distance'])
plt.plot(n_neighbors, test_accuracy['distance'])
plt.xlabel("Number of neighbours")
plt.ylabel("Accuracy")
plt.title("Distance")

plt.show()

## So we have now found the best performing parameter for each method on the test set.
## However, can we use this to see which method is really better?
