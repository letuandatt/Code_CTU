from sklearn.datasets import load_iris

iris_dt = load_iris()
iris_dt.data
iris_dt.target

from sklearn.model_selection import KFold
kf = KFold(n_splits=5, shuffle=True)

X = iris_dt.data
y = iris_dt.target

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

for train_idx, test_idx in kf.split(X):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    print("X_test:", len(X_test))
    print("======================")
    clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
    clf_gini.fit(X_train, y_train)
    y_pred = clf_gini.predict(X_test)
    print("Accuracy is", accuracy_score(y_test, y_pred) * 100)