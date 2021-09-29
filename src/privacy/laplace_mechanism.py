import numpy as np

def laplace_mechanism(data: np.array, epsilon: np.float, function: Callable, sensitivity: np.float):
    '''
    Laplace mechanism for calculating the value of a function in a differentially-private manner.

    Given a specific value for epsilon, and the sensitivity of the function, it returns a differentially private version of the function's output by adding an appropriate amount of Laplace noise.

    Parameters:
        data: An np.array with data.shape[0] records to which local DP is applied. The data must be binary.
        epsilon: the privacy parameter.
        function: the real-valued function :math:`f : X \to \mathbb{R}` to compute on the data x.
        sensitivity: the sensitivity of the function :math:`\max{xNy}|f(x)-f(y)|` where xNy denotes neighbouring datasets

    Returns:
        value: the value of f with Laplace noise added
    '''
    # Dummy implementation. You must also add the appropriate amount of noise .
    return function(data)






