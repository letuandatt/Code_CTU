# Thư viện
import tkinter as tk
import numpy as np
import tensorflow as tf
import collections

from tkinter import messagebox
from keras.api.layers import LSTM, Dense

# Đọc file và tạo từ điển
def read_data(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
    content = [x.strip().lower() for x in content]
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


# Đọc dữ liệu
data = read_data('./data_bigger.txt')
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

# Tạo mô hình LSTM
model = tf.keras.Sequential([
    LSTM(256, return_sequences=True, input_shape=(timestep, 1)),
    LSTM(128, return_sequences=False),
    Dense(128, activation='relu'),
    Dense(vocab_size)
])

model.summary()

# Compile mô hình
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Huấn luyện mô hình
model.fit(train_data, epochs=500, batch_size=128)

model.save("model_data_bigger.h5")

# Load dữ liệu và mô hình
data = read_data('./data_bigger.txt')
word2id, id2word = build_dataset(data)
model = tf.keras.models.load_model("./model_data_bigger.h5")

# Hàm mã hóa chuỗi văn bản
def encode(sent):
    words = sent.lower().split()
    return np.array([[word2id[w] for w in words]])

# Dự đoán từ tiếp theo
def predict_next_word(sentence):
    encoded_sentence = encode(sentence)
    pred = model.predict(encoded_sentence)
    pred_word = id2word[np.argmax(pred)]
    return pred_word

# Dự đoán nhiều từ
def predict_words(sentence, num_words=7):
    for _ in range(num_words):
        next_word = predict_next_word(sentence)
        sentence += " " + next_word
    return sentence

# Hàm xử lý khi nhấn nút dự đoán
def on_predict():
    sentence = entry.get()
    if len(sentence.split()) < 3:
        messagebox.showwarning("Lỗi", "Vui lòng nhập ít nhất 3 từ!")
    else:
        result = predict_words(sentence, num_words=7)
        result_label.config(text=f"Chuỗi 10 từ: {result}")

# Tạo giao diện
window = tk.Tk()
window.title("Dự đoán chuỗi từ tiếp theo")

frame = tk.Frame(window, padx=30, pady=30)
frame.pack()

label = tk.Label(frame, text="Nhập 3 từ: ")
label.pack()

entry = tk.Entry(frame, width=50)
entry.pack()

predict_button = tk.Button(frame, text="Dự đoán", command=on_predict)
predict_button.pack()

result_label = tk.Label(frame, text="", wraplength=400, pady=10)
result_label.pack()

window.mainloop()