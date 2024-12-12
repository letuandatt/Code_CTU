import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder


# Get data
df = pd.read_csv("./data/speaker+accent+recognition/accent-mfcc-data-1.csv")

X = df.drop("language", axis=1).values
y = df["language"].values.reshape(-1, 1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, shuffle=True)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

onehotencoder = OneHotEncoder(sparse_output=False)
y_train = onehotencoder.fit_transform(y_train)
y_test = onehotencoder.transform(y_test)

X_train = tf.convert_to_tensor(X_train, dtype=tf.float32)
X_test = tf.convert_to_tensor(X_test, dtype=tf.float32)
y_train = tf.convert_to_tensor(y_train, dtype=tf.float32)
y_test = tf.convert_to_tensor(y_test, dtype=tf.float32)

print(f"X_train shape: {X_train.shape}", f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}", f"y_test shape: {y_test.shape}")

# Build model
n_input = X_train.shape[1]
n_hidden = 64
n_output = y_train.shape[1]

W1 = tf.Variable(tf.random.normal((n_input, n_hidden)))
b1 = tf.Variable(tf.zeros(n_hidden, ))

W2 = tf.Variable(tf.random.normal((n_hidden, n_output)))
b2 = tf.Variable(tf.zeros(n_output, ))

@tf.function
def layer1(X, W, b):
    return tf.nn.relu(tf.matmul(X, W) + b)


@tf.function
def layer2(X, W, b):
    return tf.nn.softmax(tf.matmul(X, W) + b)


@tf.function
def predict(X, W1, b1, W2, b2):
    return layer2(layer1(X, W1, b1), W2, b2)


@tf.function
def loss_func(y, y_hat):
    y_hat = tf.clip_by_value(y_hat, 1e-7, 1 - 1e-7)
    return -tf.reduce_mean(tf.reduce_sum(y * tf.math.log(y_hat), axis=1))


@tf.function
def to_label(y_hat):
    return tf.argmax(y_hat, axis=1, output_type=tf.int32)


# Fit model
epochs = 500
batch_size = 32
alpha = 0.1
arr_acc = []
arr_loss = []

train_data = tf.data.Dataset.from_tensor_slices((X_train, y_train))

for epoch in range(epochs):
    epoch_loss = 0
    epoch_acc = 0
    batches = train_data.batch(batch_size)
    for X_batch, y_batch in batches:
        with tf.GradientTape() as tape:
            loss = loss_func(y_batch, predict(X_batch, W1, b1, W2, b2))
        dW1, db1, dW2, db2 = tape.gradient(loss, [W1, b1, W2, b2])
        W1.assign_sub(alpha*dW1)
        b1.assign_sub(alpha*db1)
        W2.assign_sub(alpha*dW2)
        b2.assign_sub(alpha*db2)
        epoch_loss += loss.numpy()

        y_hat = predict(X_batch, W1, b1, W2, b2)
        y_hat_label = to_label(y_hat)
        y_batch_label = to_label(y_batch)
        acc = tf.reduce_mean(tf.cast(tf.equal(y_batch_label, y_hat_label), tf.float32))
        epoch_acc += acc.numpy()

    print(f"Epoch: {epoch + 1}, Loss: {epoch_loss / len(batches)}, Accuracy: {epoch_acc / len(batches)}")
    arr_acc.append(epoch_acc / len(batches))
    arr_loss.append(epoch_loss / len(batches))


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