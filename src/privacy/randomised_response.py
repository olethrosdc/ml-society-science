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
    '''


    # Basic implementation
    n_people = data.shape[0]
    n_features = data.shape[1]

    ## TODO: set p correctly depending on features
    p = 1.0 / (1.0 + np.exp(epsilon)) # should be calculated based on epsilon
    mask = np.random.choice(2, size=n_people, p=[1-p, p])
    # fix this so it works for multiple features as well
    private_data = mask^data
    return private_data


def rp_float(data: np.array, epsilon: np.float, bounds: np.array):
    '''
    Random-Response mechanism for local DP on floating data.

    Given a specific value for epsilon, adds Laplace noise to the features
    so that epsilon-differential privacy is preserved. The noise is tuned according to the number of features and the epsilon

    Parameters:
        data: An np.array with data.shape[0] records to which local DP is applied. The data must be binary.
        epsilon: the privacy parameter.
        bounds: lower and upper on the range of each feature. In particular, x[t,i] must be in the range [bounds[0,i], bounds[1,i]].

    Returns:
        private_data: data modified with randomised response.
    '''
    # Dummy implementation
    private_data = data
    return private_data






