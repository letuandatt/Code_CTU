import pandas as pd
import numpy as np
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("iris.data", header=None)
df.iloc[:, -1] = np.where(df.iloc[:, -1] == 'Iris-setosa', 0, np.where(df.iloc[:, -1] == 'Iris-versicolor', 1, 2))

# Shuffle data
df = shuffle(df, random_state=0)

# Split data
features = df.iloc[:, :-1].values.astype('float32')
target = df.iloc[:, -1].values.reshape(-1, 1).astype('float32')

# Normalize the features
scaler = StandardScaler()
features = scaler.fit_transform(features)

# One-hot encode the target labels
one_hot = OneHotEncoder(sparse_output=False)
target = one_hot.fit_transform(target).astype('float32')

# Train-validation-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

print(f"X_train.shape: {X_train.shape}")
print(f"X_test.shape: {X_test.shape}")
print(f"y_train.shape: {y_train.shape}")
print(f"y_test.shape: {y_test.shape}")

# Build model
W = torch.rand(4, 3, requires_grad=True)
b = torch.rand(3, requires_grad=True)

