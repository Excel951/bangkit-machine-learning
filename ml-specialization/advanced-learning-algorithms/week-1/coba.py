import numpy as np
import tensorflow as tf

x = np.array([
    [200, 17]
])
layer_1 = tf.keras.layers.Dense(units=3, activation='sigmoid')
a1 = layer_1(x)

layer_2 = Dense(units=1, activation='sigmoid')
a2 = layer_2(a1)