import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

def weight_variable_glorot(input_dim, output_dim, dtype=tf.float32, name=""):
    """Create a weight variable with Glorot & Bengio (AISTATS 2010)
    initialization.
    """
    init_range = np.sqrt(6.0 / (input_dim + output_dim))
    initial = tf.random_uniform([input_dim, output_dim], minval=-init_range,
                                maxval=init_range, dtype=dtype)
    return tf.Variable(initial, name=name)
