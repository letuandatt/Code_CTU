#A. KNN
import pandas as pd
from sklearn.datasets import load_iris
iris_data = load_iris()
print("Thuộc tính:\n", iris_data.data)
print("Nhãn:\n", iris_data.target)

iris_data.data[1:5]
iris_data.target[1:5]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=1/3.0, random_state=5)

print("Thuộc tính train:\n", X_train)
print("Thuộc tính test:\n", X_test)
print("Nhãn train:\n", y_train)
print("Nhãn test:\n", y_test)

X_train[1:6]
X_train[1:6, 1:3]
y_train[1:6]
X_test[6:10]
y_test[6:10]

from sklearn.neighbors import KNeighborsClassifier
MoHinh_KNN = KNeighborsClassifier(n_neighbors=5)
MoHinh_KNN.fit(X_train, y_train)

y_pred = MoHinh_KNN.predict(X_test)
print("Nhãn dự đoán:\n", y_pred)

MoHinh_KNN.predict([[4, 4, 3, 3]])

from sklearn.metrics import accuracy_score, confusion_matrix
print("Độ chính xác theo %: ", accuracy_score(y_pred, y_test) * 100, "%", sep="")
print("Độ chính xác theo ma trận:\n", confusion_matrix(y_pred, y_test, labels=[2, 0, 1]))

print()

#B. Bayes
import pandas as pd

data = pd.read_csv("iris_data.csv")
print(data)

data_X = data.iloc[:, 0:4]
data_y = data.iloc[:, -1]

print("Thuộc tính:", data_X, sep="\n")
print("Nhãn:", data_y, sep="\n")

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.3, random_state=0)

from sklearn.naive_bayes import GaussianNB, MultinomialNB
MoHinh = GaussianNB()
MoHinh.fit(X_train, y_train)
print("Thông số mô hình")
print("Xác suất lớp:", MoHinh.class_prior_)
print("Các nhãn lớp:", MoHinh.classes_)
print("Số lượng mẫu các lớp:", MoHinh.class_count_)
print("Xác suất của từng đặc trưng:", MoHinh.theta_)

real_value = y_test
y_pred = MoHinh.predict(X_test)
print("Nhãn thực tế:", real_value, sep="\n")
print("Nhãn dự đoán:\n", y_pred)

from sklearn.metrics import confusion_matrix, accuracy_score
print("Độ chính xác theo %: ", accuracy_score(y_test, y_pred) * 100, "%", sep="")
print("Độ chính xác theo matrix:", confusion_matrix(y_test, y_pred), sep="\n")
