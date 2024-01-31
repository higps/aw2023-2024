import tensorflow as tf

from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model

#create network
input_layer = Input(shape=(3,))
first_hidden_layer = Dense(4)(input_layer)
output_layer = Dense(1)(first_hidden_layer)

my_model = Model(inputs=input_layer, outputs=output_layer)

import numpy as np

X = np.array([0.2,0.65,0.31]).reshape(1,3)
print(X.shape)
prediction = my_model.predict(X)
print("my prediction",prediction)