import numpy as np


def rp_binary(data: np.array, epsilon: np.float):
    '''
    Random-Response mechanism for local DP on binary data.

    Given a specific value for epsilon, flips individual bits in the features
    so that epsilon-differential privacy is preserved.

    Parameters:
        data: An np.array with data.shape[0] records to which local DP is applied. The data must be binary.
        epsilon: the privacy parameter.

    Returns:
        private_data: data modified with randomised response.
        p: the flipping probability
    '''

    # Basic implementation
    n_people = data.shape[0]
    n_features = data.shape[1]

    ## TODO: set p correctly depending on features
    ## Let p be the probability with which you change somebody's answer for a feature.
    ## So, p = 1 / (1 + exp(epsilon)), i.e. the sigmoid of (-epsilon), just set p = 1/2 - epsilon
    ## However, we want to take into account multiple features. If we want a total privacy loss of epsilon.
    ## That means a privacy loss of epsilon / n_features for each one of the features
    p = 1/(1 + np.exp(epsilon / n_features))
    #print("Using a p of ", p)
    private_data = data.copy()
    flip_bits = np.random.choice(2, p=[1 -p, p], size=[n_people, n_features])
    private_data = private_data ^ flip_bits                                    
    return private_data, p


def rp_float(data: np.array, epsilon: np.float, bound: np.array):
    '''
    Random-Response mechanism for local DP on floating data.

    Given a specific value for epsilon, adds Laplace noise to the features
    so that epsilon-differential privacy is preserved. The noise is tuned according to the number of features and the epsilon

    Parameters:
        data: An np.array with data.shape[0] records to which local DP is applied. The data must be binary.
        epsilon: the privacy parameter.
        bound: a bound on the range of each feature.

    Returns:
        private_data: data modified with randomised response.
    '''
    # Dummy implementation
    # Basic implementation
    n_people = data.shape[0]
    n_features = data.shape[1]
    private_data = data.copy()
    epsilon_i = epsilon / n_features # we lose epsilon_i for each feature, so total privacy loss is epsilon.
    sensitivity = bound
    for t in range(n_people):
        for i in range(n_features):
            private_data[t,i] += np.random.laplace(0, sensitivity[i] / epsilon_i)
            
    return private_data



