from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

#Đọc data từ file
import pandas as pd
dulieu = pd.read_csv("iris_data.csv")
print(dulieu)
X = dulieu.iloc[:,0:4]
y = dulieu.nhan

#Phân chia data thành tập test và train
from sklearn.model_selection import train_test_split
X_train, X_Test, y_train, y_test = train_test_split(X, y, test_size = 1/3.0, random_state=10)

#Xây dựng mô hình dựa trên phân phối xác suất tuân theo Gausian
model = GaussianNB()
model.fit(X_train, y_train)
print(model)

#Dự đoán
thucte = y_test
dubao = model.predict(X_Test)
model.predict_proba(X_Test)
thucte
dubao

from sklearn.metrics import confusion_matrix
cnf_matrix_gnb = confusion_matrix(thucte, dubao)
print(cnf_matrix_gnb)