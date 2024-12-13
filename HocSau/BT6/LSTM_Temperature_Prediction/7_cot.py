# Thêm các thư viện cần thiết
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from keras.api.layers import LSTM, Dense

# Đọc dữ liệu
df = pd.read_csv("./climate.csv", sep=',')
print(df.columns)

# Lấy 7 cột
columns_to_use = ["p (mbar)", "T (degC)", "rh (%)", "VPact (mbar)",
                  "VPdef (mbar)", "sh (g/kg)", "rho (g/m**3)"]
data = df[columns_to_use]

# Chuẩn hóa và tách dữ liệu huấn luyện
train_split = int(0.715 * int(df.shape[0]))
print(train_split)

def normalize(data, train_split):
    mean = data[:train_split].mean(axis=0)
    std = data[:train_split].std(axis=0)
    return (data - mean) / std


print(data.head())
data = normalize(data, train_split)
print(data.head())

train_data = data[:train_split]
val_data = data[train_split:]

# Xác định phương thức dự báo
past = 720
future = 72
step = 6
batch_size = 256

start = past + future
end = start + train_split

X_train = train_data
y_train = data[start:end]
sequence_length = int(past / step)


x_end = len(val_data) - past - future

label_start = past + future + train_split

X_val = val_data[:x_end]
y_val = data[label_start:]

# Tạo dữ liệu huấn luyện
dataset_train = tf.keras.preprocessing.timeseries_dataset_from_array(
    X_train, y_train, sequence_length=sequence_length,
    sampling_rate=step, batch_size=batch_size
)

data_val = tf.keras.preprocessing.timeseries_dataset_from_array(
    X_val, y_val, sequence_length=sequence_length,
    sampling_rate=step, batch_size=batch_size
)

# Tạo mô hình
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(sequence_length, len(columns_to_use))),
    LSTM(64, return_sequences=True),
    LSTM(32, return_sequences=False),
    Dense(32, activation='relu'),
    Dense(1)
])


model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.004),
    loss='mse',
)

model.summary()

# Huấn luyện
epochs = 10
history = model.fit(dataset_train, epochs=epochs, validation_data=data_val)

model.save("model_7cot.h5")

# Vẽ đồ thị
def visualize_loss(history, title):
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(len(loss))
    plt.figure()
    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'r', label='Validation loss')
    plt.title(title)
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig("./training_loss_7cot.png")
    plt.show()


visualize_loss(history, "Training and Validation Loss")