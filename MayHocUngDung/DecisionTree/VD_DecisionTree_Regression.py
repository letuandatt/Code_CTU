import pandas as pd

dulieu = pd.read_csv("housing_RT.csv", index_col=0)
dulieu_X = dulieu.iloc[:, 1:]
print(dulieu_X)
dulieu_y = dulieu.iloc[:, 0]
print(dulieu_y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dulieu_X, dulieu_y, test_size=1/3.0, random_state=100)

from sklearn.tree import DecisionTreeRegressor
MoHinh_Cay = DecisionTreeRegressor(random_state=0)
MoHinh_Cay.fit(X_train, y_train)

y_pred = MoHinh_Cay.predict(X_test)

from sklearn.metrics import mean_squared_error
err = mean_squared_error(y_test, y_pred)

import numpy as np
print(np.sqrt(err))