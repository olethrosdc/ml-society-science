import tensorflow as tf
import numpy as np

## Define variables
var1 = tf.Variable(1.0)
var2 = tf.Variable(2.0)

loss = lambda : var1 * var2 + 2*var1*var1

opt = tf.keras.optimizers.SGD(learning_rate=0.1)
n_iter = 100
for _ in range(n_iter):
    opt.minimize(loss, [var1, var2])
    print([var1.numpy(), var2.numpy()], loss())

