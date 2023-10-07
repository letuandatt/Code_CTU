
#Khởi tạo
l = [1, 2, 3, 4, 5]
print(l)
print(type(l))

#Truy xuất phần tử
print("Phần tử đầu tiên:", l[0])
print("Phần tử cuối cùng:", l[-5])

l[2] = 6
print(l)

l[2] = "Hello"
print(l)

#Phần tử trong 1 List cũng có thể là 1 List
l[2] = [2, 3]
print(l)

#Độ dài của list
print(len(l))


#Cắt list - Slicing => Đầu ra luôn là list
l = [1, 2, 3, 4, 5]
print(l)

#Slice từ đầu đến phần tử thứ 3
 # Cách 1
print(l[0:3])
 # Cách 2
print(l[:3])

#Slice từ pt thứ 3 đến cuối
print(l[2:])

#Slice từ pt thứ 2 đến pt thứ 4
print(l[1:4])

#Slice từ đầu đến cuối
print(l[:]) # == print(l)

#Sự khác nhau
print(l[0]) # => Trả về 1 con số
print(l[0:1]) # => Trả về 1 list

#Phần tử thứ 2 của slice_list từ pt thứ 2 đến thứ 4
print(l[1:4][1])

#Slice từ đầu tới cuối, nhảy 2 bước
print(l[::2])

#Slice đảo ngược lại list
print(l[::-1])

#Slice phần tử thứ 2 đến 4, thay nó bằng [6, 7]
l[1:3] = [6,7]
print(l)

#Slice phần tử thứ 2 đến 4, thay nó bằng [8, 9, 10, 11, "Apple"] => Tự chèn vào list
l[1:3] = [8, 9, 10, 11, "Apple"]
print(l)

#Slice lấy n phần tử cuối cùng
print(l[-2:])
"""
"""
#Các thao tác với list
l = [1, 2, 3, 4, 5]
print(l)

#. Kiểm tra một giá trị có trong list hay không
print(1 in l)
print(99 in l)

#. Nối 2 list thành 1 list
l2 = [1, -3, 8]
print(l2 + l)

#. Tạo 1 list mới = cách replicate pt của list có sẵn
l3 = [1, 2]
l4 = l3 * 3
print(l3)
print(l4)

#. Sắp xếp 1 list (nếu được)
print(l4)
print(sorted(l4))
print(sorted(l4, reverse=True))

#. Delete phần tử thứ 2
print(l4)
del l4[1]
print(l4)

#. Unpack list
l5 = [2020, 1, 25]
y, m, d = l5
print(y)
print(m)
print(d)

#. Unpack list (3)
l6 = l5
y, *_ = l6
print(y)
print(_)

#. Tìm phần tử nhỏ nhất
l7 = [10,11, 14, 6, 8]
print(sorted(l7)[0])
"""
"""
#Các phương thức của list
l = [1, 2, 3, 4, 5, 3]
print(l)

#. Đếm số lần xuất hiện của 1 pt
print(l.count(3))

#. Lấy index của 1 phần tử xuất hiện lần đầu
print(l.index(5))

#. Thêm pt vào cuối list
l.append(10)
print(l)

#. Extend list vào list ban đầu
l.extend(["A", "B", "C"]["A", "B", "C"] )
print(l)

l.append(["A", "B", "C"]) #Xem ["A", "B", "C"] là một pt
print(l)

#. Remove phần tử 'value' được tìm thấy đầu tiên
l.remove(3)
print(l)

#. Pop pt cuối cùng, save giá trị vào biến last_value
last_value = l.pop()
print(l)
print(last_value)

#. Pop pt chỉ định, save giá trị vào biến first_value
first_value = l.pop(0)
print(l)
print(first_value)

#. Xóa sạch list
l.clear()
print(l)
