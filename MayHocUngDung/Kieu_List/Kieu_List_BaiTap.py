"""
#Python3 program to swap first and last element of a list
test = [3, 10, 6, 5, 20]
print(test)

test[0], test[-1] = test[-1], test[0]

print(test)

#Python 3 program to replace elements at given positions (user input)
i = int(input("Nhập chỉ số: "))
n = int(input("Nhập giá trị mới: "))
test[i] = n
print(test)

test[3] = 12
print(test)
"""

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(List[3:9:2])
print(List[::2])
print(List[::])
print(List[::-1])
print(List[::-3])
print(List[:1:-2])

print(List[-3:][::-1])
List[-2:] = [1, 2]
print(List)