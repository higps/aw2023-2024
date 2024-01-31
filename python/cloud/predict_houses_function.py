
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df_original = pd.read_csv('kc_house_data.csv')

df_original.columns

features_name = ['sqft_living', 'bedrooms', 'sqft_lot', 'bathrooms', 'waterfront', 'grade']

label = df_original['price']
features = df_original[features_name]
y = np.c_[label]
X = np.c_[features]

linear_model = LinearRegression()
linear_model.fit(X=X, y=y)

def run_prediction(my_target_house):
    return_dict = {}
    
    return_dict["price"] = float(linear_model.predict(my_target_house)[0][0])
    return return_dict
