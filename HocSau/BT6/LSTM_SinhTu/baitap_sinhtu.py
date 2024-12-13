# Thư viện
import tensorflow as tf
import numpy as np
import collections
import matplotlib.pyplot as plt

from keras.api.layers import LSTM, Dense

# Đọc file và tạo từ điển
def read_data(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    words = []
    for line in content:
        words.extend(line.split())
    return np.array(words)

def build_dataset(words):
    count = collections.Counter(words).most_common()
    word2id = {}
    for word, freq in count:
        word2id[word] = len(word2id)

    id2word = {idx: word for word, idx in word2id.items()}
    return word2id, id2word


data = read_data('./data.txt')
word2id, id2word = build_dataset(data)
vocab_size = len(word2id)
timestep = 3

# Tạo dữ liệu huấn luyện
encoded_data = [word2id[x] for x in data]
X = encoded_data[:-1]
Y = encoded_data[timestep:]

X = np.array(X)
Y = np.array(Y)

train_data = tf.keras.preprocessing.timeseries_dataset_from_array(
    X, Y, sequence_length=timestep, sampling_rate=1
)

# Tạo mô hình và huấn luyện
model = tf.keras.Sequential([
    LSTM(512, return_sequences=True, input_shape=(timestep, 1)),
    LSTM(512, return_sequences=False),
    Dense(vocab_size)
])

model.summary()

model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

history = model.fit(train_data, epochs=500)

model.save("model_data.h5")

# Visualize
def visualize_metrics(history, title="Training and Validation Metrics"):
    loss = history.history['loss']
    val_loss = history.history['validation_loss']
    accuracy = history.history['accuracy']
    val_accuracy = history.history['validation_accuracy']

    epochs = range(1, len(loss) + 1)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss, 'b', label='Training Loss')
    plt.plot(epochs, val_loss, 'r', label='Validation Loss')
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(epochs, accuracy, 'b', label='Training Accuracy')
    plt.plot(epochs, val_accuracy, 'r', label='Validation Accuracy')
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.suptitle(title)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig("./training_sinhtu.png")


visualize_metrics(history)

# Dự báo
def encode(sent):
    return np.array([[word2id[w] for w in sent.split()]])


model = tf.keras.models.load_model("model_data.h5")

pred = model.predict(encode("had a general"))
pred_word = id2word[np.argmax(pred)]
print(pred_word)

pred = model.predict(encode("a general council"))
pred_word = id2word[np.argmax(pred)]
print(pred_word)