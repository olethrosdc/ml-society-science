import tensorflow as tf
import numpy as np

## Toy example ##
# Create an optimizer with the desired parameters.
opt = tf.keras.optimizers.SGD(learning_rate=0.1)
var1 = tf.Variable(1.0);
var2 = tf.Variable(1.0);
# `loss` is a callable that takes no argument and returns the value
# to minimize.
loss = lambda: 3 * var1 * var1 + 2 * var2 * var2

# In eager mode, simply call minimize to update the list of variables.
n_iter=10
for i in range(n_iter):
    opt.minimize(loss, var_list=[var1, var2])
    print([var1.numpy(), var2.numpy()])
    

## Example with a more complex utility function


