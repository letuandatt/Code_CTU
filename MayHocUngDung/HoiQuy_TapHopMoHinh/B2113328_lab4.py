import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, KFold
from sklearn.ensemble import *
from sklearn.tree import *
from sklearn.metrics import mean_squared_error, accuracy_score
from spicy import stats

print("Câu 1")

X = np.array([150, 147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183])
Y = np.array([90, 49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

plt.axis([140, 190, 0, 100])
plt.plot(X, Y, "ro", color="red")
plt.xlabel("Giá trị thuộc tính X")
plt.ylabel("Giá trị dự đoán Y")
plt.grid(True)
plt.show()

plt.axis([140, 190, 0, 100])
plt.scatter(X, Y, label="Dữ liệu thực tế")

slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
line = slope * X + intercept

plt.plot(X, line, label=f"Hồi quy: y = {slope:.2f}x + {intercept:.2f}", color="red")
plt.xlabel("Giá trị X")
plt.ylabel("Giá trị Y")
plt.legend()
plt.grid(True)
plt.title("Biểu đồ hồi quy tuyến tính")
plt.show()

print("\nCâu 2")

data = pd.read_csv("Housing_2019.csv", index_col=0)
data_X = data.iloc[:, [1, 2, 4, 10]]
data_y = data.price

data_train_X, data_test_X, data_train_y, data_test_y = train_test_split(data_X, data_y, test_size=1.0/3, random_state=100)

tree = DecisionTreeRegressor(random_state=0)

bagging_regtree = BaggingRegressor(base_estimator=tree, n_estimators=10, random_state=42)
bagging_regtree.fit(data_train_X, data_train_y)

data_pred = bagging_regtree.predict(data_test_X)
err = mean_squared_error(data_test_y, data_pred)
print("Err:", np.sqrt(err))

rmse_err = np.sqrt(err)
print("RMSE:",round(rmse_err, 3))

print("\nCâu 3")

pic = pd.read_csv("Wood.csv", index_col=0)
hamluonggo = pic.iloc[:, 0]
docangmanh = pic.iloc[:, 1]

plt.axis([0, 20, 0, 60])
plt.plot(hamluonggo, docangmanh, "ro", color="green")
plt.xlabel("Hàm lượng gỗ cứng")
plt.ylabel("Độ căng mạnh")
plt.show()

plt.axis([0, 20, 0, 60])
plt.scatter(hamluonggo, docangmanh, label="Dữ liệu thực tế")

slope, intercept, r_value, p_value, std_err = stats.linregress(hamluonggo, docangmanh)
line = slope * hamluonggo + intercept

plt.plot(hamluonggo, line, label=f"Hồi quy: y = {slope:.2f}x + {intercept:.2f}", color="red")
plt.xlabel("Hàm lượng gỗ")
plt.ylabel("Độ căng mạnh")
plt.legend()
plt.grid(True)
plt.title("Biểu đồ hồi quy tuyến tính")
plt.show()

print(f"Phương trình hồi quy: y = {slope:.2f}x + {intercept:.2f}")

print("\nCâu 4")

X = np.array([0.1, 0.2, 0.2, 0.3, 0.4, 0.4, 0.5, 0.6, 0.9, 0.9]).reshape(-1, 1)
Y = np.array([1, 1, 1, 1, -1, -1, -1, -1, 1, 1])

kf = KFold(n_splits=10, shuffle=True)

avg_acc = 0
cnt = 0

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = Y[train_index], Y[test_index]

    Model_Tree = DecisionTreeClassifier(criterion="entropy")
    Model_Tree.fit(X_train, y_train)

    y_pred = Model_Tree.predict(X_test)

    acc = accuracy_score(y_test, y_pred) * 100
    avg_acc += acc
    cnt += 1

print(f"Độ chính xác trung bình DT: {avg_acc // cnt}")

avg_acc = 0
cnt = 0

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = Y[train_index], Y[test_index]

    Model_Tree = AdaBoostClassifier(estimator=DecisionTreeClassifier(criterion="entropy"))
    Model_Tree.fit(X_train, y_train)

    y_pred = Model_Tree.predict(X_test)

    acc = accuracy_score(y_test, y_pred) * 100
    avg_acc += acc
    cnt += 1

print(f"Độ chính xác trung bình RF: {avg_acc // cnt}")

print("\nCâu 5")

data = pd.read_csv("winequality-white.csv", delimiter=";")
data_X = data.drop("quality", axis=1)
data_y = data.quality

avg_acc = 0

for i in range(10):
    data_train_X, data_test_X, data_train_y, data_test_y = train_test_split(data_X, data_y, test_size=1/3.0)

    Model_Tree = DecisionTreeClassifier(criterion="entropy")
    Model_Tree.fit(data_train_X, data_train_y)

    data_pred = Model_Tree.predict(data_test_X)

    acc = accuracy_score(data_test_y, data_pred) * 100
    avg_acc += acc

print(f"Giá trị trung bình DecisionTree: {avg_acc // 10}")

avg_acc = 0

for i in range(10):
    data_train_X, data_test_X, data_train_y, data_test_y = train_test_split(data_X, data_y, test_size=1/3.0)

    random_forest = RandomForestClassifier(criterion="entropy")
    random_forest.fit(data_train_X, data_train_y)

    data_pred = random_forest.predict(data_test_X)

    acc = accuracy_score(data_test_y, data_pred) * 100
    avg_acc += acc

print(f"Giá trị trung bình RandomForestClassifier: {avg_acc // 10}")

avg_acc = 0
cnt = 0

kf = KFold(n_splits=50, shuffle=True)

for train_idx, test_idx in kf.split(data_X):
    data_train_X, data_test_X = data_X.iloc[train_idx,], data_X.iloc[test_idx,]
    data_train_y, data_test_y = data_y.iloc[train_idx], data_y.iloc[test_idx]

    Model_Tree = AdaBoostClassifier(estimator=DecisionTreeClassifier(criterion="entropy") ,n_estimators=50, learning_rate=0.1)
    Model_Tree.fit(data_train_X, data_train_y)

    data_pred = Model_Tree.predict(data_test_X)

    acc = accuracy_score(data_test_y, data_pred) * 100
    avg_acc += acc
    cnt += 1

print(f"Giá trị trung bình AdaBoostClassifier: {avg_acc // cnt}")

plt.figure(figsize=(10, 6))
plt.barh(Model_Tree.feature_names_in_, Model_Tree.feature_importances_)
plt.ylabel("Tên đặc trưng")
plt.xlabel("Độ quan trọng")
plt.title("Biểu đồ độ quan trọng")
plt.show()