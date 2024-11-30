import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data and take only first 100 samples (Iris-setosa and Iris-versicolor)
df = pd.read_csv("../iris/iris.data", header=None).iloc[:100]
df.iloc[:, -1] = np.where(df.iloc[:, -1] == 'Iris-setosa', 0, 1)

# Shuffle data
df = df.iloc[np.random.permutation(len(df))].reset_index(drop=True)

# Split data
features = df.iloc[:, :-1].values
target = df.iloc[:, -1].values.astype(float)

# Normalize the features
scaler = StandardScaler()
features = scaler.fit_transform(features)

# Train-validation-test split (60% train, 20% validation, 20% test)
X_train, X_temp, y_train, y_temp = train_test_split(features, target, test_size=0.4, random_state=0)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=0)

# Convert to torch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_val = torch.tensor(X_val, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
y_val = torch.tensor(y_val, dtype=torch.float32).unsqueeze(1)
y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

# Create DataLoader for batch processing
train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)  # Mini-batch size of 16

# Build model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(4, 1)  # 4 input features, 1 output (binary classification)

    def forward(self, x):
        return torch.sigmoid(self.fc1(x))  # Sigmoid activation for binary classification


model = SimpleNN()

# Loss function and optimizer
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Store training and validation loss for visualization
train_losses = []
val_losses = []

# Training loop
num_epochs = 150
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0

    # Training step
    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()  # Zero the gradients
        outputs = model(batch_X)  # Forward pass
        loss = criterion(outputs, batch_y)  # Compute loss
        loss.backward()  # Backward pass
        optimizer.step()  # Update weights
        running_loss += loss.item()

    # Calculate validation loss
    model.eval()
    with torch.no_grad():
        val_outputs = model(X_val)
        val_loss = criterion(val_outputs, y_val).item()  # Validation loss

    # Average loss for the epoch
    avg_train_loss = running_loss / len(train_loader)
    train_losses.append(avg_train_loss)  # Store training loss
    val_losses.append(val_loss)  # Store validation loss

    if (epoch + 1) % 10 == 0:  # Print loss every 10 epochs
        print(f"Epoch [{epoch+1}/{num_epochs}], Train Loss: {avg_train_loss:.4f}, Val Loss: {val_loss:.4f}")

# Plot the training and validation loss
plt.figure(figsize=(8, 6))
plt.plot(range(1, num_epochs + 1), train_losses, label='Training Loss')
plt.plot(range(1, num_epochs + 1), val_losses, label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training and Validation Loss over Epochs')
plt.legend()
plt.show()

# Evaluate model on the test set
model.eval()
with torch.no_grad():
    outputs = model(X_test)
    test_loss = criterion(outputs, y_test)
    predicted = (outputs >= 0.5).float()
    accuracy = (predicted == y_test).sum().item() / y_test.size(0)

# Print the results
print(f"Test loss: {test_loss.item():.4f}")
print(f"Test accuracy: {accuracy * 100:.2f}%")
