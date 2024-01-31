import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
tf.executing_eagerly()

X_train =  np.load('train_images.npy', allow_pickle=True)
y_train =  np.load('train_labels.npy', allow_pickle=True)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# show image
data_idx = 0
plt.imshow(X_train[data_idx,:,:]/255, cmap='binary')
plt.show()
class_number = y_train[data_idx]
class_text = class_names[class_number]
print(f'This is a {class_text}')

# data prep
X_train = X_train/255
X_train = X_train.reshape(-1, 784)

c_features_names = ["age_text_high",  "age_text_low", "age_text_medium", "high_blood_pressure", "ejection_fraction_sc", "serum_creatinine_sc", "serum_sodium_sc"]
c_features = df_prepped[c_features_names]
y = np.c_[c_label]
X = np.c_[c_features]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
# create a model and train it:
age_category_encoder = OneHotEncoder(sparse_output=False)

age_category_encoder.fit(df_prepped[["age_text"]])

# prep validation data
X_val =  np.load('val_images.npy', allow_pickle=True)
# dele på 255 og reshape
# predic validation data
my_prediction = np.array([9,0,0,3,...])

# save predictions
my_name = 'Marius'
np.save(f'{my_name}_predictions.npy', my_prediction)