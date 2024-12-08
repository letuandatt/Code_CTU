import tensorflow as tf


# Data
X = tf.constant([[0.0, 0], [0, 1], [1, 0], [1, 1]])
y = tf.constant([[1.0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]])

# Init w & b
W = tf.Variable(tf.random.normal((2, 3)))
b = tf.Variable([0.0, 0.0, 0.0])

print(f"--- W and b before training:")
print(f"W:\n{W}", f"b:\n{b}", sep='\n')

# Predict
@tf.function
def predict(x, w, b_):
    return tf.nn.softmax(tf.matmul(x, w) + b_)


y_hat = predict(X, W, b)
print(f"--- Y_hat before training:\n{y_hat}")

# Loss func
@tf.function
def loss_func(y, y_hat):
    return -tf.reduce_mean(tf.reduce_sum(y * tf.math.log(y_hat), axis=1))


loss_be4 = loss_func(y, y_hat)
print(f"--- Loss before training: {loss_be4}")

# Fit data
alpha = 0.1

for epoch in range(500):
    with tf.GradientTape() as tape:
        loss = loss_func(y, predict(X, W, b))
    dW, db = tape.gradient(loss, [W, b])
    W.assign_sub(alpha * dW)
    b.assign_sub(alpha * db)


# After training:
print(f"--- W and b after training:")
print(f"W:\n{W}", f"b:\n{b}", sep='\n')

y_hat_new = predict(X, W, b)
print(f"--- Y_hat after training:\n{y_hat_new}")

loss_after = loss_func(y, y_hat_new)
print(f"--- Loss before training: {loss_after}")

predictions = tf.one_hot(tf.argmax(y_hat, axis=-1), 3)
print(f"--- Predictions:\n{predictions}")