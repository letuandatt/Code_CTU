import pandas as pd
import keras as kr

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

data, target = iris.data, iris.target

df = pd.DataFrame(data, columns=iris.feature_names)
df['target'] = target

df = df.iloc[:100].values

train, test = train_test_split(df, test_size=0.2, random_state=0)

model = kr.models.Sequential([
    kr.layers.Dense(1, activation='sigmoid', input_shape=(4, )),
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train[:, 0:4], train[:, -1], epochs=150, batch_size=32, verbose=0)

score = model.evaluate(test[:, :-1], test[:, -1], verbose=0)
print(f"Test loss: {score[0]}")
print(f"Test accuracy: {score[1]}")
