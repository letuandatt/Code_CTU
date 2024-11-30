import torch

# Data
X = torch.tensor([[0.0, 0], [0, 1], [1, 0], [1, 1]], requires_grad=False)
y = torch.tensor([[0.0], [0], [0], [1]], requires_grad=False)

# Init w & b
W = torch.randn(2, 1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

print("--- W & b before training:")
print(f"W:\n{W}")
print(f"b:\n{b}")

print()

# Predict
def predict(x, w, b_):
    return torch.sigmoid(torch.matmul(x, w) + b_)


y_hat = predict(X, W, b)
print(f"---Y_hat before training:\n{y_hat}")

print()

# Loss func
def loss_func(y, y_hat):
    y_hat = torch.clamp(y_hat, 1e-7, 1 - 1e-7)
    return -torch.mean(y * torch.log(y_hat) + (1 - y) * torch.log(1 - y_hat))


print(f"---Loss before training:\n{loss_func(y, y_hat)}")

print()

# Gradient Descent
alpha = 0.1

for epoch in range(500):
    y_hat = predict(X, W, b)

    loss = loss_func(y, y_hat)

    loss.backward()

    with torch.no_grad():
        W -= alpha * W.grad
        b -= alpha * b.grad

    W.grad.zero_()
    b.grad.zero_()


# Predict after training
print("--- W & b after training:")
print(f"W:\n{W}")
print(f"b:\n{b}")

y_hat_new = predict(X, W, b)
print(f"---Y_hat after training:\n{y_hat_new}")
print(f"---Loss after training:\n{loss_func(y, y_hat_new)}")

predictions = (y_hat_new > 0.5).float()
print(f"---Predictions:\n{predictions.detach().numpy()}")