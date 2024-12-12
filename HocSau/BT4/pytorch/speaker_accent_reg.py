import pandas as pd
import torch as t
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics import confusion_matrix, classification_report
from torch.utils.data import DataLoader, TensorDataset

# Get data
df = pd.read_csv("../data/speaker+accent+recognition/accent-mfcc-data-1.csv")

X = df.drop("language", axis=1).values
y = df["language"].values.reshape(-1, 1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

one_hot = OneHotEncoder()
y_train = one_hot.fit_transform(y_train).toarray()
y_test = one_hot.transform(y_test).toarray()

X_train = t.tensor(X_train, dtype=t.float32)
X_test = t.tensor(X_test, dtype=t.float32)
y_train = t.tensor(y_train, dtype=t.float32)
y_test = t.tensor(y_test, dtype=t.float32)

print(f"X_train shape: {X_train.shape}", f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}", f"y_test shape: {y_test.shape}")

# Build model
n_input = X_train.shape[1]
n_hidden = 64
n_output = y_train.shape[1]

W1 = t.randn(n_input, n_hidden, dtype=t.float32, requires_grad=True)
b1 = t.zeros(n_hidden, dtype=t.float32, requires_grad=True)

W2 = t.randn(n_hidden, n_output, dtype=t.float32, requires_grad=True)
b2 = t.zeros(n_output, dtype=t.float32, requires_grad=True)

def layer1(X, W, b):
    return t.relu(t.matmul(X, W) + b)

def layer2(X, W, b):
    return t.softmax(t.matmul(X, W) + b, dim=1)

def predict(X, W1, b1, W2, b2):
    return layer2(layer1(X, W1, b1), W2, b2)

def loss_func(y, y_hat):
    y_hat = t.clamp(y_hat, 1e-7, 1 - 1e-7)
    return -t.mean(t.sum(y * t.log(y_hat), dim=1))

def to_label(y_hat):
    return t.argmax(y_hat, dim=1).to(t.int32)

# Fit model
epochs = 500
batch_size = 32
alpha = 0.1
arr_acc = []
arr_loss = []

train_data = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)

for epoch in range(epochs):
    epoch_loss = 0
    epoch_acc = 0

    for X_batch, y_batch in train_loader:
        y_hat = predict(X_batch, W1, b1, W2, b2)

        loss = loss_func(y_batch, y_hat)

        loss.backward()

        with t.no_grad():
            W1 -= alpha * W1.grad
            b1 -= alpha * b1.grad
            W2 -= alpha * W2.grad
            b2 -= alpha * b2.grad

            W1.grad.zero_()
            b1.grad.zero_()
            W2.grad.zero_()
            b2.grad.zero_()

        epoch_loss += loss.item()

        y_hat_label = to_label(y_hat)
        y_batch_label = to_label(y_batch)
        acc = (y_hat_label == y_batch_label).float().mean()
        epoch_acc += acc.item()

    num_batches = len(train_loader)
    avg_loss = epoch_loss / num_batches
    avg_acc = epoch_acc / num_batches

    if epoch % 10 == 0:
        print(f"Epoch: {epoch + 1}, Loss: {avg_loss:.4f}, Accuracy: {avg_acc:.4f}")

    arr_acc.append(avg_acc)
    arr_loss.append(avg_loss)


# Visualize training process
plt.figure(figsize=(8, 6))
plt.plot(range(1, epochs + 1), arr_loss, label='Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss over Epochs')

plt.figure(figsize=(8, 6))
plt.plot(range(1, epochs + 1), arr_acc, label='Training Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training Accuracy over Epochs')
plt.legend()
plt.show()

# Evaluation
def evaluate_model(X_test, y_test, W1, b1, W2, b2):
    y_hat_test = predict(X_test, W1, b1, W2, b2)

    test_loss = loss_func(y_test, y_hat_test).detach().numpy()

    y_hat_test_label = to_label(y_hat_test)
    y_test_label = to_label(y_test)

    test_acc = (y_hat_test_label == y_test_label).float().mean().detach().numpy()

    print(f"Test Loss: {test_loss:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")

    return y_hat_test_label, y_test_label


y_hat_test_label, y_test_label = evaluate_model(X_test, y_test, W1, b1, W2, b2)

conf_matrix = confusion_matrix(y_test_label.detach().numpy(), y_hat_test_label.detach().numpy())
print("Confusion Matrix:\n", conf_matrix)

class_report = classification_report(y_test_label.detach().numpy(), y_hat_test_label.detach().numpy(), target_names=one_hot.categories_[0])
print("Classification Report:\n", class_report)