import numpy as np

from keras.src.datasets import mnist
from keras.api.utils import to_categorical
from keras.api.models import Sequential
from keras.api.layers import Flatten, Dense

# Get data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Scale
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Add dim
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

# One-hot class
num_classes = 10

y_train = to_categorical(y_train, num_classes=num_classes)
y_test = to_categorical(y_test, num_classes=num_classes)

# Model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(num_classes)
])

model.summary()

# Train
batch_size = 32
epochs = 20

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Evaluate
score = model.evaluate(X_test, y_test, verbose=0)
print(f"Test loss: {score[0]}")
print(f"Test accuracy: {score[1]}")