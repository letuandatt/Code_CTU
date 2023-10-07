fruits = ("apple", "banana", "guava", "kiwi", [i for i in range(1, 5)], 8);
print("Các phần tử trong tuple:", fruits)

print("----------")
#Số lượng phần tử
print("Số lượng phần tử:", len(fruits))

#Truy cập các giá trị trong tuple trong Python
print("Giá trị thứ 2 trong tuple:", fruits[1])

#Chỉ mục âm
print("Phần tử cuối cùng của tuple:", fruits[-1])

#Phạm vi chỉ mục
print("Các giá trị thứ 3 đến thứ 5:", fruits[2:5])

#Phạm vi chỉ mục âm
print("Các giá trị thứ 3 đến thứ 5 từ phía sau:", fruits[-5:-2])

#Tuple không thể thay đổi giá trị

#Duyệt giá trị trong tuple
for x in fruits:
    print(x)

#Kiểm tra giá trị tồn tại = "in"
print("Banana có tồn tại trong tuple không?", "banana" in fruits)

#Kiểm tra kiểu dữ liệu
print("Fruits đang mang kiểu dữ liệu:", type(fruits))

#Nối 2 Tuple
tuple_2 = ("monkey", "dog", "cat")
fruits += tuple_2
print("Các phần tử trong tuple sau khi nối: ", fruits)
print("Số lượng phần tử sau khi nối:", len(fruits))

print("----------")
#Các phương thức
tuple_3 = (1, 7, 9, 3, 4, 3, 5, 6, 8)
print("Giá trị lớn nhất trong tuple_3 là:", max(tuple_3))
print("Giá trị nhỏ nhất trong tuple_3 là:", min(tuple_3))