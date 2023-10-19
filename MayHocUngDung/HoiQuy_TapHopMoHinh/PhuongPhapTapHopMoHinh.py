import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn import linear_model

data = pd.read_csv("Housing_2019.csv", index_col=0)
data_X = data.iloc[:, [1, 2, 4, 10]]
data_y = data.price

data_train_X, data_test_X, data_train_y, data_test_y = train_test_split(data_X, data_y, test_size=1.0/3, random_state=100)

tree = DecisionTreeRegressor(random_state=0)

bagging_regtree = BaggingRegressor(base_estimator=tree, n_estimators=10, random_state=42)
bagging_regtree.fit(data_train_X, data_train_y)

data_pred = bagging_regtree.predict(data_test_X)
err = mean_squared_error(data_test_y, data_pred)
print(np.sqrt(err))


lm = linear_model.LinearRegression()
bagging_reg = BaggingRegressor(base_estimator=lm, n_estimators=10, random_state=42)
bagging_reg.fit(data_train_X, data_train_y)

data_pred = bagging_reg.predict(data_test_X)
err = mean_squared_error(data_test_y, data_pred)
print(np.sqrt(err))