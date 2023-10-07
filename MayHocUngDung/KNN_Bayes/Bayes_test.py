from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.model_selection import train_test_split

import pandas as pd
dulieu = pd.read_csv("winequality-white.csv", delimiter=";")
print(dulieu, "\n")

dulieu_x = dulieu.iloc[:,0:11]
dulieu_y = dulieu.quality

print(dulieu_x, "\n")
print(dulieu_y)

print("Số phần tử dữ liệu X:", len(dulieu_x))

X_train, X_Test, y_train, y_test = train_test_split(dulieu_x, dulieu_y, test_size=1/5.0, random_state=10)

print("Số lượng train:", len(X_train))
print("Số lượng test:", len(X_Test))

MoHinh = GaussianNB()
MoHinh.fit(X_train, y_train)

print("Thông số của mô hình:")
print("Ước lượng xác suất trước (xác suất lớp):", MoHinh.class_prior_)
print("Các nhãn lớp:", MoHinh.classes_)
print("Số lượng mẫu của mỗi lớp:", MoHinh.class_count_)
print("Xác suất của từng đặc trưng:", MoHinh.theta_)  # Trung bình của mỗi đặc trưng cho từng lớp
# print("Phương sai của từng đặc trưng:", MoHinh.sigma_)  # Phương sai của từng đặc trưng cho từng lớp

dudoan = MoHinh.predict(X_Test)
print(dudoan)

from sklearn.metrics import accuracy_score

TiLeDuDoanMoHinh = accuracy_score(y_test, dudoan) * 100
print(TiLeDuDoanMoHinh)

from sklearn.metrics import confusion_matrix

cnf_matrix_gnb = confusion_matrix(y_test, dudoan)
print(cnf_matrix_gnb)