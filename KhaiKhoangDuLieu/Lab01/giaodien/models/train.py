import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.utils import shuffle


def process_input(input_array, scaler_file='scaler.joblib'):
    scaler = joblib.load(scaler_file)

    input_array = np.array(input_array).reshape(1, -1)

    input_array = scaler.transform(input_array)

    return input_array

def get_data_and_process(input_file_path):
    # Load data
    df = pd.read_csv(input_file_path)

    # Encode labels
    le = LabelEncoder()
    df.iloc[:, -1] = le.fit_transform(df.iloc[:, -1])

    # Shuffle data
    df = shuffle(df, random_state=1)

    # Split data
    X = df.iloc[:, :-1].values.astype('float32')
    y = df.iloc[:, -1].values.astype('int')

    # Normalize features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    joblib.dump(scaler, 'scaler.joblib')

    # Train-validation-test split
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=1)

    print(f"X_train shape: {Xtrain.shape}", f"X_test shape: {Xtest.shape}")
    print(f"y_train shape: {ytrain.shape}", f"y_test shape: {ytest.shape}")

    return Xtrain, Xtest, ytrain, ytest

def get_best_parameter(_model_name):  # xử lí gridseach trong get_best_parameter
    model = None
    param_grid = {}

    if _model_name == 'KNN':
        # Khởi tạo model
        model = KNeighborsClassifier()

        # Tham số cần tìm kiếm
        param_grid = {
            'n_neighbors': [3, 5, 7, 9],
            "weights": ["uniform", "distance"],
            "metric": ["euclidean", "manhattan", "minkowski"]
        }

    elif _model_name == 'NaiveBayes':
        model = GaussianNB()

        param_grid = {
            'var_smoothing': np.logspace(0, -9, num=100)
        }

    elif _model_name == 'DecisionTree':
        model = DecisionTreeClassifier()

        param_grid = {
            "criterion": ["gini", "entropy"],
            "max_depth": [None, 10, 20, 30],
            "min_samples_split": [2, 5, 10],
            "min_samples_leaf": [1, 2, 4],
        }

    elif _model_name == 'RandomForest':
        model = RandomForestClassifier()

        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'bootstrap': [True, False]
        }

    elif _model_name == 'SVM':
        model = SVC()

        param_grid = {
            'C': [0.1, 1, 10, 100],
            'gamma': [1, 0.1, 0.01, 0.001],
            'kernel': ['rbf', 'linear']
        }

    elif _model_name == 'MLP':
        model = MLPClassifier()

        param_grid = {
            'hidden_layer_sizes': [(50,), (100,), (100, 50)],
            'activation': ['tanh', 'relu'],
            'solver': ['adam', 'sgd'],
            'alpha': [0.0001, 0.05],
            'learning_rate': ['constant', 'adaptive']
        }

    # GridSearchCV sau khi có model và param_grid
    grid_model = GridSearchCV(model, param_grid, cv=5, verbose=1, n_jobs=-1)
    return grid_model

def train(_model_name, Xtrain, ytrain):
    model = get_best_parameter(_model_name)
    model.fit(Xtrain, ytrain)
    return model


def show_grid_seach_results(grid_search, _model_name):
    # Lấy kết quả từ quá trình tìm kiếm
    results = pd.DataFrame(grid_search.cv_results_)

    # Chọn các cột cần xem
    results = results[['params', 'mean_fit_time', 'mean_score_time', 'mean_test_score', 'rank_test_score']]

    # Sắp xếp theo thứ hạng
    results = results.sort_values(by=['rank_test_score'], ascending=False)

    # In ra csv
    results.to_csv(f"results_{_model_name}.csv", index=False)
    print(f"All results are in results_{_model_name}.csv!")


if __name__ == '__main__':
    # file_path = "models.csv"
    # X_train, X_test, y_train, y_test = get_data_and_process(file_path)
    # print("\n")
    #
    # model_names = ["KNN", "NaiveBayes", "DecisionTree", "RandomForest", "SVM", "MLP"]
    #
    # for model_name in model_names:
    #     print(f"Training {model_name}...")
    #
    #     result = train(model_name, X_train, y_train)
    #
    #     joblib.dump(result, f"{model_name}_iris.joblib")
    #
    #     print(f"Best parameters for {model_name}: {result.best_params_}")
    #     print(f"Accuracy: {result.score(X_test, y_test)}")
    #
    #     show_grid_seach_results(result, model_name)
    #
    #     print("--------------", end="\n\n")

    input_data = [[5.1, 3.5, 1.4, 0.2]]
    input_data_processed = process_input(input_data)
    model = joblib.load('MLP_iris.joblib')
    prediction = model.predict(input_data_processed)
    print(prediction)
