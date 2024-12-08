import torch

# Data
X = torch.tensor([[0.0, 0], [0, 1], [1, 0], [1, 1]], requires_grad=False)
y = torch.tensor([[1.0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]], requires_grad=False)

# Init w & b
W = torch.randn(2, 3, requires_grad=True)
b = torch.tensor([0.0, 0.0, 0.0], requires_grad=True)

print(f"--- W and b before training:")
print(f"W:\n{W}", f"b:\n{b}", sep='\n')

# Predict
def predict(x, w, b_):
    return torch.softmax(torch.matmul(x, w) + b_, dim=1)


y_hat = predict(X, W, b)
print(f"--- Y_hat before training:\n{y_hat}")

# Loss func
def loss_func(y, y_hat):
    return -torch.mean(torch.sum(y * torch.log(y_hat), dim=1))


loss_be4 = loss_func(y, y_hat)
print(f"--- Loss before training: {loss_be4}")

# Fit data
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

# After training:
print(f"--- W and b after training:")
print(f"W:\n{W}", f"b:\n{b}", sep='\n')

y_hat_new = predict(X, W, b)
print(f"--- Y_hat after training:\n{y_hat_new}")

loss_after = loss_func(y, y_hat_new)
print(f"--- Loss before training: {loss_after}")

agrmax_predictions = torch.argmax(y_hat_new, dim=-1)
predictions = torch.nn.functional.one_hot(agrmax_predictions, num_classes=3)
print(f"--- Predictions:\n{predictions}")