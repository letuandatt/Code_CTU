import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Housing_2019.csv", index_col=0)

data_X = data.iloc[:, [1, 2, 3, 4, 10]]
data_y = data.price

# plt.scatter(data.lotsize, data.price)
# plt.show()

import sklearn
from sklearn import linear_model

lm = linear_model.LinearRegression()
lm.fit(data_X[:520], data_y[:520])

print(lm.intercept_)
print(lm.coef_)

data_test_y = data_y[-20:]
data_test_X = data_X[-20:]

data_pred = lm.predict(data_test_X)

from sklearn.metrics import mean_squared_error
err = mean_squared_error(data_test_y, data_pred)
print(err)

rmse_err = np.sqrt(err)
print(round(rmse_err, 3))