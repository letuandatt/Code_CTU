#3. Các cú pháp cơ bản
a = 5
b = 3
if a > b:
    a = a * 2 + 3
    b = b - 6
    c = a / b
    print(c)

#4. Lệnh và cấu trúc điều khiển
a = 5
b = 3
if a > b:
    print("True")
    print(a)
else:
    print("False")
    print(b)

a = 1
b = 10
while a < b:
    a += 1
    print(a)

print([i for i in range(1, 10)])

def binhphuong(number):
    return number ** 2;
print(binhphuong(5))

#5. Các kiểu dữ liệu

a = 5
b = -7
c = 1.234

str1 = "Hello"
str2 = "welcome"
str3 = "abcdef12345"

cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
print(cats[2])

print(cats[-1])

print(cats[1:3])

print(cats)

cats.append('Jerry')
print(cats)

cats[-1] = 'Jerry Cat'
print(cats)

del cats[1]
print(cats)

dict1 = {'Name' : 'Zyra', 'Age' : 7, 'Class' : 'A5'}
print(dict1['Name'])

print(dict1['Age'])

dict = {'Name' : 'Zara', 'Age' : 7, 'Class' : 'First'}
dict['Age'] = 8
dict['School'] = "DPS School"
print(dict['Age'])
print(dict['School'])

#7. Ví dụ minh họa
import numpy as np

a = np.array([0, 1, 2, 3, 4, 5])

print(a)

print("Số chiều của mảng a: ", a.ndim)

print("Kích thước ma trận a là: ", a.shape)

print("In ra các phần trử có giá trị > 3 trong mảng a: ", a[a > 3])

a[a > 3] = 10

b = a.reshape((3, 2))

print("Mảng b là: ", b)

print("Số chiều của mảng b: ", b.ndim)

print("Kích thước ma trận b là: ", b.shape)

print(b[2][1])

b[2][0] = 50

print("B là: ", b)

c = b * 2

print("C là: ", c)

"""
import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 4])
Y = np.array([2, 3, 6])

plt.axis([0, 5, 0, 8])
plt.plot(X, Y, "ro", color = "red")
plt.xlabel("Giá trị thuộc tính X")
plt.ylabel("Giá trị thuộc tính Y")
plt.show()

import scipy as sp
import numpy as np

data = np.genfromtxt('web_traffic.tsv', delimiter="\t")

print(data.shape)

x = data[:,0]

y = data[:,1]

print(len(~np.isnan(y)))

x = x[~np.isnan(y)]

y = y[~np.isnan(y)]

import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hours")
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("play_tennis.csv", delimiter=",")
a = data.head(5) #lấy 5 dòng đầu
b = data.tail(5) #lấy 5 dòng cuối
d46 = data.iloc[3:7] #hàng thứ 3 đến 6, bắt đầu từ 0
c1 = data.iloc[:,0:1] #cột đầu tiên, cột 0
c15 = data.iloc[:,0:6] #cột đầu tiên (0) đến cột thứ 5
c3 = data.iloc[:,2] #cột thứ 2, bắt đầu từ 0
c453 = data.iloc[4:6,2] #giá trị dòng 4, 5 cột 2 (tính từ 0)
print(data.outlook) #In dữ liệu cột outlook
"""
"""
import pandas as pd
dt = pd.read_csv("play_tennis.csv", delimiter=',')
dt.head()
dt.tail(7)

dt.loc[3:8]
dt.iloc[:,3:6]
dt.iloc[5:10,3:4]
print(dt.outlook)
"""