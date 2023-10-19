import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 4])
y = np.array([2, 3, 6])

plt.axis([0, 5, 0, 8])
plt.plot(X, y, "ro", color="blue")
plt.xlabel("Giá trị thuộc tính X")
plt.ylabel("Giá trị dự đoán y")
plt.show()

def LR1(X, y, eta, lanlap, theta0, theta1):
    m = len(X)
    for k in range(lanlap):
        print("Lần lặp: ", k)
        for i in range(m):
            h_i = theta0 + theta1 * X[i]
            theta0 += eta * (y[i] - h_i) * 1
            print("Phần tử ", i, "y=", y[i], "h=", h_i, "giá trị theta0 = ", round(theta0, 3))
            theta1 += eta * (y[i] - h_i) * X[i]
            print("Phần tử ", i, "giá trị theta1 = ", round(theta1, 3))
    return [round(theta0, 3), round(theta1, 3)]

theta = LR1(X, y, 0.2, 1, 0, 1)
print(theta)

theta2 = LR1(X, y, 0.2, 2, 0, 1)
print(theta2)

X1 = np.array([1, 6])
Y1 = theta[0] + theta[1] * X1

X2 = np.array([1, 6])
Y2 = theta2[0] + theta2[1] * X2

plt.axis([0, 7, 0, 10])
plt.plot(X, y, "ro", color="blue")

plt.plot(X1, Y1, color="violet")
plt.plot(X2, Y2, color="green")

plt.xlabel("Giá trị thuộc tính X")
plt.ylabel("Giá trị dự đoán y")
plt.show()

XX = [0, 3, 5]
for i in range(3):
    YY = theta[0] + theta[1] * XX[i]
    print(round(YY, 3))