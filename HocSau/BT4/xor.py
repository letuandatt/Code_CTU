import tensorflow as tf

# Data
X = tf.constant([[0.0, 0], [0, 1], [1, 0], [1, 1]])
y = tf.constant([[0.0], [1], [1], [0]])

# Init w & b
n = 2

W1 = tf.Variable(tf.random.normal((n, 8)))
b1 = tf.Variable(tf.zeros((8, )))

W2 = tf.Variable(tf.random.normal((8, 1)))
b2 = tf.Variable(tf.zeros((1, )))

print("---Before training:")
print(f"{W1}", f"{W2}", f"{b1}", f"{b2}", sep='\n')

# Predict
@tf.function
def layer1(X, W1, b1):
    return tf.nn.relu(tf.matmul(X, W1) + b1)


@tf.function
def layer2(X, W2, b2):
    return tf.nn.sigmoid(tf.matmul(X, W2) + b2)


@tf.function
def predict(X, W1, b1, W2, b2):
    return layer2(layer1(X, W1, b1), W2, b2)


y_hat = predict(X, W1, b1, W2, b2)
print(f"---Y_hat before training:\n{y_hat}")

# Loss func
def loss_func(y, y_hat):
    y_hat = tf.clip_by_value(y_hat, 1e-7, 1 - 1e-7)
    return -tf.reduce_mean(y * tf.math.log(y_hat) + (1 - y) * tf.math.log(1 - y_hat))

# Fit model
alpha = 0.1

for epoch in range(5000):
    with tf.GradientTape() as tape:
        loss = loss_func(y, predict(X, W1, b1, W2, b2))
    dW1, db1, dW2, db2 = tape.gradient(loss, [W1, b1, W2, b2])
    W1.assign_sub(alpha * dW1)
    b1.assign_sub(alpha * db1)
    W2.assign_sub(alpha * dW2)
    b2.assign_sub(alpha * db2)


# After fitting
print("---After training:")
print(f"{W1}", f"{W2}", f"{b1}", f"{b2}", sep='\n')

y_hat_new = predict(X, W1, b1, W2, b2)
print(f"---Y_hat after training:\n{y_hat_new}")

# Label
predictions = tf.cast(y_hat_new > 0.5, dtype=tf.float32)
print(f"---Predictions:\n{predictions}")