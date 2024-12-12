import torch

# Data
X = torch.tensor([[0.0, 0], [0, 1], [1, 0], [1, 1]], requires_grad=False)
y = torch.tensor([[0.0], [1], [1], [0]], requires_grad=False)

# Init w & b
n = 2

W1 = torch.randn(n, 8, requires_grad=True)
b1 = torch.zeros(8, requires_grad=True)

W2 = torch.randn(8, 1, requires_grad=True)
b2 = torch.zeros(1, requires_grad=True)

print(f"---Before training---")
print(f"{W1}", f"{W2}", f"{b1}", f"{b2}", sep='\n')

# Predict
def layer1(X, W, b):
    return torch.relu(torch.matmul(X, W) + b)


def layer2(X, W, b):
    return torch.sigmoid(torch.matmul(X, W) + b)


def predict(X, W1, b1, W2, b2):
    return layer2(layer1(X, W1, b1), W2, b2)


y_hat = predict(X, W1, b1, W2, b2)
print(f"Y_hat before training:\n{y_hat}")

# Loss func
def loss_func(y, y_hat):
    y_hat = torch.clamp(y_hat, 1e-7, 1 - 1e-7)
    return -torch.mean(y * torch.log(y_hat) + (1 - y) * torch.log(1 - y_hat))


loss_ = loss_func(y, y_hat)
print(f"Loss before training:\n{loss_}")

# Fit model
alpha = 0.1

for epoch in range(5000):
    y_hat = predict(X, W1, b1, W2, b2)

    loss = loss_func(y, y_hat)

    loss.backward()

    with torch.no_grad():
        W1 -= alpha * W1.grad
        b1 -= alpha * b1.grad
        W2 -= alpha * W2.grad
        b2 -= alpha * b2.grad

    W1.grad.zero_()
    b1.grad.zero_()
    W2.grad.zero_()
    b2.grad.zero_()


# After training
print("---After training---")
print(f"{W1}", f"{W2}", f"{b1}", f"{b2}", sep='\n')

y_hat_new = predict(X, W1, b1, W2, b2)
print(f"Y_hat after training:\n{y_hat_new}")
print(f"Loss after training:\n{loss_func(y, y_hat_new)}")

# Label
predictions = (y_hat_new > 0.5).float()
print(f"Predictions:\n{predictions}")