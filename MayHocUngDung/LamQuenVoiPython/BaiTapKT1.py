
#Bài tập buổi 1 CT294
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('baitap1.csv', delimiter=",")
print("Câu 2:\n", data)

a = data.iloc[:,2]
print("Câu 3:\n", a)

b = data.iloc[15:21,]
print("Câu 4:\n", b)

c = data.iloc[14,0:2]
print("Câu 5:\n", c)

print("Câu 7:", end=" ")

print([d for d in range(20, 71) if d % 2 != 0])

print("Câu 6:\n")

x = data.iloc[:,2]
# print(x)

y = data.iloc[:,3]
# print(y)

plt.axis([0,90,0,35])
plt.plot(x, y, "ro", color = "blue")
plt.xlabel("Data col 2")
plt.ylabel("Data col 3")
plt.show()