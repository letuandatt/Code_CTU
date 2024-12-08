import pandas as pd
import numpy as np
import tensorflow as tf
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

# Build model (initialize weights and bias)
W = tf.Variable(tf.random.normal((4, 3)))
b = tf.Variable(tf.random.normal((3, )))

# Define the prediction function
@tf.function
def predict(x, w, b_):
    return tf.nn.softmax(tf.matmul(x, w) + b_)

# Define cross-entropy loss function
@tf.function
def loss_func(y, y_hat):
    y_hat = tf.clip_by_value(y_hat, 1e-7, 1 - 1e-7)  # Clip to avoid log(0)
    return -tf.reduce_mean(tf.reduce_sum(y * tf.math.log(y_hat), axis=1))

# Training parameters
alpha = 0.01
epochs = 500
batch_size = 32

# Create a TensorFlow dataset for batch processing
train_data = tf.data.Dataset.from_tensor_slices((X_train, y_train)).batch(batch_size)

# Initialize arrays for accuracy and loss tracking
arr_acc = []
arr_loss = []

# Training loop
for epoch in range(epochs):
    for batch_X, batch_y in train_data:
        with tf.GradientTape() as tape:
            loss = loss_func(batch_y, predict(batch_X, W, b))
        dW, db = tape.gradient(loss, [W, b])
        W.assign_sub(alpha * dW)
        b.assign_sub(alpha * db)

    # Calculate training loss and accuracy after each epoch
    train_y_hat = predict(X_train, W, b)
    train_loss = loss_func(y_train, train_y_hat)
    train_predictions = tf.argmax(train_y_hat, axis=1)
    train_actuals = tf.argmax(y_train, axis=1)
    train_acc = tf.reduce_mean(tf.cast(train_predictions == train_actuals, tf.float32))

    arr_acc.append(train_acc.numpy())
    arr_loss.append(train_loss.numpy())

# Plot training loss over epochs
plt.figure(figsize=(8, 6))
plt.plot(range(1, epochs + 1), arr_loss, label='Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss over Epochs')
plt.legend()
plt.show()

# Evaluate the model on the test set
y_hat_test = predict(X_test, W, b)

# Calculate predictions and accuracy
predictions = tf.argmax(y_hat_test, axis=1)
actuals = tf.argmax(y_test, axis=1)

# Calculate accuracy
acc = tf.reduce_mean(tf.cast(predictions == actuals, tf.float32)).numpy()

# Confusion matrix
confusion_matrix = tf.math.confusion_matrix(actuals, predictions)

# Print results
print(f"Accuracy: {acc * 100:.2f}%")
print(f"Confusion Matrix:\n{confusion_matrix}")
