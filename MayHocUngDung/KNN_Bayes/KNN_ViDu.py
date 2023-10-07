#Lấy file iris trực tiếp từ sklearn
from sklearn.datasets import load_iris
import pandas as pd

iris_dt = load_iris()
iris_dt.data[1:5] #Thuộc tính tập iris
iris_dt.target[1:5] #Giá trị của nhãn / clas

#Phân chia tập data để build mô hình và check theo nghi thức Hold-out
from sklearn.model_selection import train_test_split

X_train, X_Test, y_train, y_test = train_test_split(iris_dt.data, iris_dt.target, test_size = 1/3.0, random_state=5)
#4 data đầu vào hàm train_test_split(Thuộc tính tập data cần phân chia, Nhãn tập data cần chia, kích thước tập data cần phân chia, <mặc định>)
#thuộc tính tập train, thuộc tính tập test, nhãn tập train, nhãn tập test

X_train[1:6]
X_train[1:6,1:3]
y_train[1:6]
X_Test[6:10]
y_test[6:10]

#Xây dựng mô hình K láng giềng KNN với 5 láng giềng
from sklearn.neighbors import KNeighborsClassifier
Mohinh_KNN = KNeighborsClassifier(n_neighbors=5)
Mohinh_KNN.fit(X_train, y_train) #Xây dựng mô hình

#Dự đoán nhãn cho các phần tử trong tập kiểm tra
y_pred = Mohinh_KNN.predict(X_Test)
y_test
print(y_pred)
print(y_test)
Mohinh_KNN.predict([[4, 4, 3, 3]])

#Tính độ chính xác cho giá trị dự đoán của phần tử trong tập kiểm tra
from sklearn.metrics import accuracy_score
print("Accuracy is", accuracy_score(y_test, y_pred) * 100)

#Tính độ chính xác cho giá trị dự đoán thông qua ma trận con
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred, labels=[2, 0, 1]))