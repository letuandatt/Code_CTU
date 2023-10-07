from sklearn.datasets import load_iris
iris_dt = load_iris()
iris_dt.data[1:5]
iris_dt.target[1:5]

from sklearn.model_selection import train_test_split #Nghi thức hold-out
X_train, X_test, y_train, y_test = train_test_split(iris_dt.data, iris_dt.target, test_size=1/3.0, random_state=5)

from sklearn.tree import DecisionTreeClassifier
#criterion -> Chọn cách phân hoạch, max_depth -> Độ sâu lớn nhất của cây, min_samples_leaf -> Nút nhánh ít nhất có 5 phần tử
clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)

y_pred = clf_gini.predict(X_test)
y_test
clf_gini.predict([[4, 4, 3, 3]])

from sklearn.metrics import accuracy_score,confusion_matrix
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
print("Confusion_maxtrix:\n", confusion_matrix(y_test, y_pred, labels=[2, 0, 1]))