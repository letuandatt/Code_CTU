import pandas as pd
import numpy as np

data = pd.read_csv("winequality-red.csv", delimiter=";")
data_X = data.iloc[:, 0:-1]
data_y = data.iloc[:, -1]

print("Số lượng phần tử tập dữ liệu:", len(data))
print("Các giá trị của nhãn:", np.unique(data_y))
print("Số lượng và giá trị của nhãn:", data_y.value_counts())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=4/10.0, random_state=10)

print("Số lượng phần tử tập test:", len(X_test))

from sklearn.neighbors import KNeighborsClassifier
MoHinh_KNN = KNeighborsClassifier(n_neighbors=7)
MoHinh_KNN.fit(X_train, y_train)

y_pred = MoHinh_KNN.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix
mm = np.unique(y_test)
print("Độ chính xác tổng thể: ", accuracy_score(y_test, y_pred) * 100)
print("Độ chính xác cho từng lớp:\n", confusion_matrix(y_test, y_pred, labels=mm))

X_test_8 = X_test.head(8)
y_test_8 = y_test.head(8)

y_pred_8 = MoHinh_KNN.predict(X_test_8)

print("Độ chính xác tổng thể: ", accuracy_score(y_test_8, y_pred_8) * 100)
print("Độ chính xác từng lớp:\n", confusion_matrix(y_test_8, y_pred_8))

print("-------------")

from sklearn.naive_bayes import GaussianNB, MultinomialNB
MoHinh_Bayes = GaussianNB()
MoHinh_Bayes.fit(X_train, y_train)
# print("Thông số mô hình")
# print("Xác suất lớp:", MoHinh_Bayes.class_prior_)
# print("Các nhãn lớp:", MoHinh_Bayes.classes_)
# print("Số lượng mẫu của mỗi lớp:", MoHinh_Bayes.class_count_)
# print("Xác suất của từng đặc trưng:", MoHinh_Bayes.theta_)

y_pred_Bayes = MoHinh_Bayes.predict(X_test)

print("Độ chính xác tổng thể: ", accuracy_score(y_test, y_pred_Bayes) * 100)
print("Độ chính xác từng lớp:\n", confusion_matrix(y_test, y_pred_Bayes, labels=mm))

X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=1/3.0, random_state=10)

print("\nNghi thức hold-out:")
Model_KNN = KNeighborsClassifier(n_neighbors=9)
Model_KNN.fit(X_train, y_train)
y_pred_KNN_f = Model_KNN.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred_KNN_f) * 100)

Model_Bayes = GaussianNB()
Model_Bayes.fit(X_train, y_train)
y_pred_Bayes_f = Model_Bayes.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred_Bayes_f) * 100)