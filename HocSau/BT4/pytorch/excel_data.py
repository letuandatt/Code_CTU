import pandas as pd
import torch

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# Data
data = pd.read_excel("../data/data.xlsx", sheet_name='Sheet2')
data = shuffle(data)

# Get features and labels from data
X = data.iloc[:, :-1].values.astype('float32')
y = data.iloc[:, -1].values.astype('float32').reshape(-1, 1)

# Split train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

print(f"X_train: {X_train.shape}, y_train: {y_train.shape}")
print(f"X_test: {X_test.shape}, y_test: {y_test.shape}")

# Build model
n = X_train.shape[1]

W1 = torch.randn(n, 8, requires_grad=True)
b1 = torch.zeros(8, requires_grad=True)

W2 = torch.randn(8, 4, requires_grad=True)
b2 = torch.zeros(4, requires_grad=True)

W3 = torch.randn(4, 1, requires_grad=True)
b3 = torch.zeros(1, requires_grad=True)

print("------ Before training")
print(f"W1:\n{W1}", f"b1:\n{b1}", f"W2:\n{W2}", f"b2:\n{b2}", f"W3:\n{W3}", f"b3:\n{b3}", sep='\n')

def layer1(X, W, b):
    return torch.relu(torch.matmul(X, W) + b)


def layer2(X, W, b):
    return torch.relu(torch.matmul(X, W) + b)


def layer3(X, W, b):
    return torch.sigmoid(torch.matmul(X, W) + b)


def predict(X, W1, b1, W2, b2, W3, b3):
    return layer3(layer2(layer1(X, W1, b1), W2, b2), W3, b3)


def loss_func(y, y_hat):
    y_hat = torch.clamp(y_hat, 1e-7, 1 - 1e-7)
    return -torch.mean(y * torch.log(y_hat) + (1 - y) * torch.log(1 - y_hat))


y_hat = predict(X_test, W1, b1, W2, b2, W3, b3)
print(f"Y_hat:\n{y_hat}")

loss = loss_func(y_test, y_hat)
print(f"Loss: {loss}")

# Fit model
alpha = 0.01

for epoch in range(5000):
    y_hat = predict(X_train, W1, b1, W2, b2, W3, b3)

    loss = loss_func(y_train, y_hat)

    loss.backward()

    with torch.no_grad():
        W1 -= alpha * W1.grad
        b1 -= alpha * b1.grad
        W2 -= alpha * W2.grad
        b2 -= alpha * b2.grad
        W3 -= alpha * W3.grad
        b3 -= alpha * b3.grad

    W1.grad.zero_()
    b1.grad.zero_()
    W2.grad.zero_()
    b2.grad.zero_()
    W3.grad.zero_()
    b3.grad.zero_()

# Predict
print("------ After training")
print(f"W1:\n{W1}", f"b1:\n{b1}", f"W2:\n{W2}", f"b2:\n{b2}", f"W3:\n{W3}", f"b3:\n{b3}", sep='\n')

y_hat_new = predict(X_test, W1, b1, W2, b2, W3, b3)
print(f"Y_hat:\n{y_hat}")

loss = loss_func(y_test, y_hat_new)
print(f"loss: {loss}")

predictions = (y_hat_new > 0.5).float()
print(f"Predictions:\n{predictions}")
print(f"Y_true:\n{y_test}")