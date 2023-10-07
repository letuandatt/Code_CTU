#Tạo một từ điển
Dict = {}
print(Dict)

#Dict với key là số nguyên
Dict = {1: 'lập', 2: 'trình', 3: 'không khó'}
print(Dict)

#Dict với key hỗn hợp
Dict = {'Name': 'dict', 1: [1, 2, 3, 4]}
print(Dict)

#Tạo một dict sử dụng dict()
Dict = dict({1: 'ví dụ', 2: 'về', 3: 'dict()'})
print(Dict)

#Tạo một dict với mỗi cặp
Dict = dict([(1, 'Gun'), (2, 'Gim')])
print(Dict)

print("-------")

#Thuộc tính
##Khóa k đc trùng
##Value bất kể kiểu dữ liệu, khóa chỉ có thể là "int" hoặc "String"
##Khóa có phân biệt chữ hoa chữ thường

d = dict()

#Thêm các giá trị vào từ điển (Khóa ch có, thêm khóa vào; else, cập nhật lại value tại khóa đó)
d[0] = 'Welcome'
d[1] = 'Lê Tuấn Đạt'
print(d)

d[2] = 'Máy học ứng dụng'
d[3] = 'Cờ vua 2'
d[4] = 'Python'
d[5] = 'OOP'
d[6] = 'Cơ sở dữ liệu MySQL'
print(d)

print("-------")

#Truy cập giá trị của từ điển (cách thường)
print("Giá trị tại key = 4 là:", d[4])

#Truy cập giá trị thông qua hàm get(<key>)
print("Giá trị tại key = 4 cách 2:", d.get(4))

#Xóa một giá trị khỏi dict
del d[6]
print("Dict sau khi xóa 1 phần tử:", d)

#Lấy độ dài
print("Độ dài dict là:", len(d))

#Chuyển từ điển thành chuỗi
print("Biểu diễn chuỗi tương đuương là:", str(d))

#Copy từ điển
d_2 = d.copy()
print("Từ điển copy d_2:", d_2)

#Cập nhật giá trị
##Nếu key đã tồn tại, cập nhật value tại key đó
##Hoặc tạo ra key mới với value đi kèm
d.update({3: 'Nguyên lý hệ điều hành'})
d.update({6: 'Trí tuệ nhân tạo'})
print("Dict sau update:", d)

#Trả về danh sách các cặp key: value
print("Các cặp giá trị key-value:", d.items())

#Trả về list key/value
print("Danh sách các key của d:", d.keys())
print("Danh sách các value của d:", d.values())

#Xóa toàn bộ dict
d.clear()
print(d)