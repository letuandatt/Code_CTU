import tensorflow as tf

# Data
X = tf.constant([[0.0, 0], [0, 1], [1, 0], [1, 1]])
y = tf.constant([[0.0], [0], [0], [1]])

# Init w & b
W = tf.Variable(tf.random.normal((2, 1)))
b = tf.Variable(tf.random.normal((1,)))

print("--- W & b before training")
print(W, b, sep='\n')

# Predict
@tf.function
def predict(x, w, b_):
    return tf.nn.sigmoid(tf.matmul(x, w) + b_)


y_hat = predict(X, W, b)
print(f"---Y_hat before training:\n{y_hat}")

# Loss func
@tf.function
def loss_func(y, y_hat):
    return tf.reduce_mean(tf.square(y - y_hat))


print(f"---Loss before training:\n{loss_func(y, y_hat)}")

# Gradient Descent
alpha = 0.1

for epoch in range(500):
    with tf.GradientTape() as tape:
        loss = loss_func(y, predict(X, W, b))
    dW, db = tape.gradient(loss, [W, b])
    W.assign_sub(alpha * dW)
    b.assign_sub(alpha * db)


# Predict after training
print("--- W & b after training")
print(W, b, sep='\n')

y_hat_new = predict(X, W, b)
print(f"---Y_hat after training:\n{y_hat_new}")
print(f"---Loss after training:\n{loss_func(y, y_hat_new)}")

predictions = tf.cast(y_hat_new >= 0.5, tf.float32)
print(f"---Predictions:\n{predictions}")
