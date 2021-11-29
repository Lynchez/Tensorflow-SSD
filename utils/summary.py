import tensorflow as tf
from tensorflow.keras.applications.densenet import DenseNet121

net = DenseNet121()
net.summary()