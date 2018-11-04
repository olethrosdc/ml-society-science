## -*- Mode: python -*-

import scipy.io as sio
import numpy as np


class DataGenerator:
    def __init__(self, matrices="./generating_matrices.mat"):
        parameters = sio.loadmat("./generating_matrices.mat")
        self.V = parameters['V'] # the treatment effect matrix
        self.W = parameters['W'] # the feature matrix

    def generate_features(self):
        T = np.random.normal(size=(1, self.W.shape[0]))
        X = np.zeros([1,130])
        X[0,0:128] = 1*(np.matmul(T, self.W) < 0)
        X[0,0] = 1*(np.random.uniform() <0.5)
        X[0,1] = 1*(np.random.uniform() < 0.2 + 0.05 * X[0,2] + 0.1 * X[0,0])
        Z = (np.random.uniform() - 0.2 * X[0,3] + 0.2 * X[0,4] - 0.2 * X[0,5])
        X[0,127] = 1*(np.random.uniform()*0.5 + 0.5*Z<0.5)
        if (Z > 0):
            X[0,128]= 1*(np.random.uniform() < 0.5 * X[0,3] - 0.1 * X[0,4] + 0.6 * X[0,5])
            X[0,129] = 1*(np.random.uniform() < X[0,1]*X[0,3] + X[0,2])
        else:
            X[0,128] = 1*(np.random.uniform() < 0.4 * X[0,3] + 0.5 * X[0,5])
            X[0,129] = 1*(np.random.uniform() < 0.2 * X[0,1]*X[0,3] + 0.2 * X[0,4] - 0.1 * X[0,9])
        return X

    def generate_default_action(self, X):
        A = 1*(np.random.uniform() < X[0,128] * 0.4  + X[0,129] * 0.5);
        return A

    def generate_outcome(self, X, A):
        Y = 1*(np.dot(X, self.V[A]) > 0)
        return Y

    def generate_data(self, n_data):
        X = np.zeros([n_data,130])
        for t in range(n_data):
            X[t] = generate_features()
            A[t] = generate_default_action(X[t])
            Y[t] = generate_outcome(X[t], A[t])
            
if __name__ == '__main__':
    n_data = 1000

        
    
