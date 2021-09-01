import numpy as np
import abc
import scipy.stats

# This is a base class for generating classification problems
class BaseClassificationGenerator:
    @abc.abstractmethod
    ## generate n_points (x,y) pairs
    def generate(self, n_points):
        pass
    ## generate an (x,y) at x.
    def generate_at_point(self, x):
        pass

# Generates data where $X|Y=i~Normal(\mu_i, \Sigma_i)$
class GaussianClassificationGenerator(BaseClassificationGenerator):
    # Initialise the class centers
    def __init__(self, n_dimensions, class_proportions):
        self.n_dimensions = n_dimensions
        self.class_proportions = class_proportions
        self.n_classes = class_proportions.shape[0]
        self.means = np.zeros([self.n_classes, self.n_dimensions])
        self.covariances = np.zeros([self.n_classes, self.n_dimensions, self.n_dimensions])
        # Generate means   $\mu_i \sim Uniform([0,1]^n)$
        # and covariances  $\Sigma_i \sim Gamma(1)$
        for i in range(self.n_classes):
            self.means[i] = np.random.uniform(size=self.n_dimensions)
            self.covariances[i] = scipy.stats.wishart.rvs(self.n_dimensions, np.identity(self.n_dimensions))
    # generate data
    def generate(self, n_points):
        Y = np.random.choice(self.n_classes, p=self.class_proportions, size=n_points)
        X = np.zeros([n_points, self.n_dimensions])
        for t in range(n_points):
            X[t]= np.random.multivariate_normal(self.means[Y[t]], self.covariances[Y[t]])
        return [X, Y]
