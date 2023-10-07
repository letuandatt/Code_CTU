import pandas as pd
import numpy as np

from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

if __name__ == '__main__':
    dulieu = pd.read_csv("winequality-white.csv", delimiter=";")
    dulieu_X = dulieu.iloc[:, :-1]
    dulieu_y = dulieu.iloc[:, -1]

    kf = KFold(n_splits=50, shuffle=True)

    train_size = 0
    test_size = 0
    cnt = 0

    for train_index, test_index in kf.split(dulieu_X):
        train_size += len(train_index)
        test_size += len(test_index)
        cnt += 1

    print(f"Số lượng tập train là {train_size // cnt}, và tập test là {test_size // cnt}.\nLặp:")

    acc_avg = 0
    cnt = 0

    for train_index, test_index in kf.split(dulieu_X):
        dulieu_train_X, dulieu_test_X = dulieu_X.iloc[train_index,], dulieu_X.iloc[test_index,]
        dulieu_train_y, dulieu_test_y = dulieu_y.iloc[train_index], dulieu_y.iloc[test_index]

        print(f"Số lượng train: {len(dulieu_train_X)}")
        print(f"Số lượng test: {len(dulieu_test_X)}")

        MoHinh_Cay = DecisionTreeRegressor(criterion="friedman_mse")
        MoHinh_Cay.fit(dulieu_train_X, dulieu_train_y)

        dulieu_pred = MoHinh_Cay.predict(dulieu_test_X)

        acc = accuracy_score(dulieu_test_y, dulieu_pred) * 100
        print(f"Độ chính xác cho lần lặp thứ {cnt + 1} là {acc}")
        print(f"Ma trận nhầm lẫn lần lặp thứ {cnt + 1} là:\n{confusion_matrix(dulieu_test_y, dulieu_pred)}\n----------")

        acc_avg += acc
        cnt += 1

    print(f"Độ chính xác tổng thể cho 50 lần lặp: {acc_avg // cnt}\n---------------------------------")

    kf = KFold(n_splits=60, shuffle=True)

    acc_avg = 0
    cnt = 0

    for train_index, test_index in kf.split(dulieu_X):
        dulieu_train_X, dulieu_test_X = dulieu_X.iloc[train_index,], dulieu_X.iloc[test_index,]
        dulieu_train_y, dulieu_test_y = dulieu_y.iloc[train_index], dulieu_y.iloc[test_index]

        MoHinh_KNN = KNeighborsClassifier(n_neighbors=7)
        MoHinh_KNN.fit(dulieu_train_X, dulieu_train_y)

        dulieu_pred = MoHinh_KNN.predict(dulieu_test_X)

        acc = accuracy_score(dulieu_test_y, dulieu_pred) * 100
        acc_avg += acc
        cnt += 1

    print(f"Độ chính xác tổng thể KFold cho KNN là {acc_avg // cnt}\n---------------------------------")

    acc_avg = 0
    cnt = 0

    for train_index, test_index in kf.split(dulieu_X):
        dulieu_train_X, dulieu_test_X = dulieu_X.iloc[train_index,], dulieu_X.iloc[test_index,]
        dulieu_train_y, dulieu_test_y = dulieu_y.iloc[train_index], dulieu_y.iloc[test_index]

        MoHinh_Bayes = GaussianNB()
        MoHinh_Bayes.fit(dulieu_train_X, dulieu_train_y)

        dulieu_pred = MoHinh_Bayes.predict(dulieu_test_X)

        acc = accuracy_score(dulieu_test_y, dulieu_pred) * 100
        acc_avg += acc
        cnt += 1

    print(f"Độ chính xác tổng thể KFold cho Bayes là {acc_avg // cnt}\n---------------------------------")

    dulieu = pd.read_csv("text.csv", delimiter=";", index_col=0, header=None)
    dulieu_X = dulieu.iloc[:, :-1]
    dulieu_y = dulieu.iloc[:, -1]

    MoHinh_Cay = DecisionTreeClassifier(criterion="entropy")
    MoHinh_Cay.fit(dulieu_X, dulieu_y)

    dulieu_pred = MoHinh_Cay.predict([[135, 39, 1]])
    print(f"Phần tử mới có chiều cao {135}cm, độ dài mái tóc {39} và giọng nói {1} là {dulieu_pred[0]}.")