# %%
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

my_target_house = [
    [1000, 3, 0, 2, 1, 13],
    [1500, 4, 0, 2, 0, 13]
]

linear_model.predict(my_target_house)

y_pred = linear_model.predict(X)

mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'R2: {r2}')

mean_price = np.mean(y)
y_pred_naive = np.full(y.shape, mean_price)

mae_naive = mean_absolute_error(y, y_pred_naive)
mse_naive = mean_squared_error(y, y_pred_naive)
r2_naive = r2_score(y, y_pred_naive)
print(f'MAE naive: {mae_naive}')
print(f'MSE naive: {mse_naive}')
print(f'R2 naive: {r2_naive}')

# %%
print(f'Improvments over naive: {(mse_naive-mse)/mse_naive*100:.02f}%')

# %%
knn_model = KNeighborsRegressor(n_neighbors=1)
knn_model.fit(X, y)

y_pred_knn = knn_model.predict(X)

mae_knn = mean_absolute_error(y, y_pred_knn)
mse_knn = mean_squared_error(y, y_pred_knn)
r2_knn = r2_score(y, y_pred_knn)
print(f'MAE: {mae_knn}')
print(f'MSE: {mse_knn}')
print(f'R2: {r2_knn}')



