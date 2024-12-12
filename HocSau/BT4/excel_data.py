import pandas as pd
import tensorflow as tf

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# Data
data = pd.read_excel("./data/data.xlsx", sheet_name='Sheet2')
data = shuffle(data)

# Get features and labels from data
X = data.iloc[:, :-1].values.astype('float32')
y = data.iloc[:, -1].values.astype('float32').reshape(-1, 1)

# Split train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

print(f"X_train: {X_train.shape}, y_train: {y_train.shape}")
print(f"X_test: {X_test.shape}, y_test: {y_test.shape}")

# Build model
n = X_train.shape[1]

W1 = tf.Variable(tf.random.normal((n, 8)))
b1 = tf.Variable(tf.random.normal((8, )))

W2 = tf.Variable(tf.random.normal((8, 4)))
b2 = tf.Variable(tf.random.normal((4, )))

W3 = tf.Variable(tf.random.normal((4, 1)))
b3 = tf.Variable(tf.random.normal((1, )))

print("------ Before training")
print(f"W1:\n{W1}", f"b1:\n{b1}", f"W2:\n{W2}", f"b2:\n{b2}", f"W3:\n{W3}", f"b3:\n{b3}", sep='\n')

@tf.function
def layer1(X, W1, b1):
    return tf.nn.relu(tf.matmul(X, W1) + b1)


@tf.function
def layer2(X, W2, b2):
    return tf.nn.relu(tf.matmul(X, W2) + b2)


@tf.function
def layer3(X, W3, b3):
    return tf.nn.sigmoid(tf.matmul(X, W3) + b3)


@tf.function
def predict(X, W1, b1, W2, b2, W3, b3):
    return layer3(layer2(layer1(X, W1, b1), W2, b2), W3, b3)


@tf.function
def loss_func(y, y_hat):
    y_hat = tf.clip_by_value(y_hat, 1e-7, 1 - 1e-7)
    return -tf.reduce_mean(y * tf.math.log(y_hat) + (1 - y) * tf.math.log(1 - y_hat))


y_hat = predict(X_test, W1, b1, W2, b2, W3, b3)
print(f"Y_hat:\n{y_hat}")

loss = loss_func(y_test, y_hat)
print(f"Loss: {loss}")

# Fit model
alpha = 0.01

for epoch in range(5000):
    with tf.GradientTape() as tape:
        loss = loss_func(y_train, predict(X_train, W1, b1, W2, b2, W3, b3))
    dW1, db1, dW2, db2, dW3, db3 = tape.gradient(loss, [W1, b1, W2, b2, W3, b3])
    W1.assign_sub(alpha * dW1)
    b1.assign_sub(alpha * db1)
    W2.assign_sub(alpha * dW2)
    b2.assign_sub(alpha * db2)
    W3.assign_sub(alpha * dW3)
    b3.assign_sub(alpha * db3)


# Predict
print("------ After training")
print(f"W1:\n{W1}", f"b1:\n{b1}", f"W2:\n{W2}", f"b2:\n{b2}", f"W3:\n{W3}", f"b3:\n{b3}", sep='\n')

y_hat = predict(X_test, W1, b1, W2, b2, W3, b3)
print(f"Y_hat:\n{y_hat}")

loss = loss_func(y_test, y_hat)
print(f"loss: {loss}")

predictions = tf.cast(y_hat > 0.5, dtype=tf.float32)
print(f"Predictions:\n{predictions}")
print(f"Y_true:\n{y_test}")