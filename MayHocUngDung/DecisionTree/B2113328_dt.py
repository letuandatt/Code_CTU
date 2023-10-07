import pandas as pd
import numpy as np

from sklearn.model_selection import KFold, train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

if __name__ == '__main__':
    dulieu = pd.read_csv("winequality-white.csv", delimiter=";")
    dulieu_X = dulieu.iloc[:, :-1]
    dulieu_y = dulieu.iloc[:, -1]

    print("Số dòng và số thuộc tính:", np.shape(dulieu), end=" ")

    print("\nCột nhãn:", dulieu_y, sep="\n")

    kf = KFold(n_splits=50, shuffle=True)

    print("------------------------------\nLặp:")

    acc_avg = 0
    cnt = 0

    for train_idx, test_idx in kf.split(dulieu_X):
        print(f"Lần lặp thứ {cnt + 1}:")

        dulieu_train_X, dulieu_test_X = dulieu_X.iloc[train_idx, ], dulieu_X.iloc[test_idx, ]
        dulieu_train_y, dulieu_test_y = dulieu_y.iloc[train_idx], dulieu_y.iloc[test_idx]

        print(f"Số phần tử trong tập train là {len(dulieu_train_X)} và tập test là {len(dulieu_test_X)}.")

        MoHinh_Cay = DecisionTreeClassifier(criterion="entropy")
        MoHinh_Cay.fit(dulieu_train_X, dulieu_train_y)

        dulieu_pred = MoHinh_Cay.predict(dulieu_test_X)

        acc = accuracy_score(dulieu_test_y, dulieu_pred) * 100

        mm = np.unique(dulieu_test_y)

        cfs_mtx = confusion_matrix(dulieu_test_y, dulieu_pred, labels=mm)

        print(f"Xác suất là {acc}")
        print(f"Ma trận nhầm lẫn:\n{cfs_mtx}\n------------------------------")

        acc_avg += acc
        cnt += 1

    print(f"Độ chính xác tổng thể trung bình {cnt} lần lặp là {acc_avg // cnt}\n============================================")

    kf = KFold(n_splits=60, shuffle=True)

    acc_avg = 0
    cnt = 0

    for train_idx, test_idx in kf.split(dulieu_X):
        dulieu_train_X, dulieu_test_X = dulieu_X.iloc[train_idx,], dulieu_X.iloc[test_idx,]
        dulieu_train_y, dulieu_test_y = dulieu_y.iloc[train_idx], dulieu_y.iloc[test_idx]

        MoHinh_KNN = KNeighborsClassifier(n_neighbors=11)
        MoHinh_KNN.fit(dulieu_train_X, dulieu_train_y)

        dulieu_pred = MoHinh_KNN.predict(dulieu_test_X)

        acc = accuracy_score(dulieu_test_y, dulieu_pred) * 100

        mm = np.unique(dulieu_test_y)

        cfs_mtx = confusion_matrix(dulieu_test_y, dulieu_pred, labels=mm)

        acc_avg += acc
        cnt += 1

    print(f"Độ chính xác tổng thể trung bình {cnt} lần lặp theo KNN là {acc_avg // cnt}\n============================================")

    acc_avg = 0
    cnt = 0

    for train_idx, test_idx in kf.split(dulieu_X):
        dulieu_train_X, dulieu_test_X = dulieu_X.iloc[train_idx,], dulieu_X.iloc[test_idx,]
        dulieu_train_y, dulieu_test_y = dulieu_y.iloc[train_idx], dulieu_y.iloc[test_idx]

        MoHinh_Bayes = BernoulliNB()
        MoHinh_Bayes.fit(dulieu_train_X, dulieu_train_y)

        dulieu_pred = MoHinh_Bayes.predict(dulieu_test_X)

        acc = accuracy_score(dulieu_test_y, dulieu_pred) * 100

        mm = np.unique(dulieu_test_y)

        cfs_mtx = confusion_matrix(dulieu_test_y, dulieu_pred, labels=mm)

        acc_avg += acc
        cnt += 1

    print(f"Độ chính xác tổng thể trung bình {cnt} lần lặp theo Bayes là {acc_avg // cnt}\n============================================")

    dulieu = pd.read_csv("text.csv", delimiter=";")
    dulieu_X = dulieu.iloc[:, :-1]
    dulieu_y = dulieu.iloc[:, -1]

    MoHinh_Cay = DecisionTreeClassifier(criterion="entropy")
    MoHinh_Cay.fit(dulieu_X, dulieu_y)

    dulieu_pred = MoHinh_Cay.predict([[135, 39, 1]])

    print(f"Phần tử mới có chiều cao {135}cm, độ dài mái tóc {39} và giọng nói {1} có nhãn là {dulieu_pred[0]}.")