# Lê Tuấn Đạt
# B2113328
# 19

import base64

from tkinter import *
from Crypto.Cipher import DES

# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")

# Them cac control
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

# Tiêu đề
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG DES", font=("Arial Bold", 15), justify="center")
lb2.grid(column=1, row=2)

# Phần văn bản gốc
original_word = Label(window, text="Văn bản gốc", font=("Arial", 14), justify="center")
original_word.grid(column=0, row=3)

original_txt = Entry(window, width=95)
original_txt.grid(column=1, row=3)

# Phần khóa
key = Label(window, text="Khóa", font=("Arial", 14))
key.grid(column=0, row=4)

key_txt = Entry(window, width=95)
key_txt.grid(column=1, row=4)

# Phần VB mã hóa
encrypt_word = Label(window, text="Văn bản được mã hóa", font=("Arial", 14))
encrypt_word.grid(column=0, row=5)

encrypt_txt = Entry(window, width=95)
encrypt_txt.grid(column=1, row=5)

# Phần VB giải mã
decrypt_word = Label(window, text="Văn bản được giải mã", font=("Arial", 14))
decrypt_word.grid(column=0, row=6)

decrypt_txt = Entry(window, width=95)
decrypt_txt.grid(column=1, row=6)

# Mã hóa
def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def mahoa_DES():
    txt = pad(original_txt.get())
    key = pad(key_txt.get())
    if len(key) != 8:
        encrypt_txt.delete(0, END)
        encrypt_txt.insert(0, "Khóa phải dài đúng 8 ký tự!")
        return

    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    entxt = cipher.encrypt(txt.encode('utf-8'))
    entxt = base64.b64encode(entxt).decode('utf-8')  # Chuyển sang chuỗi UTF-8 để hiển thị
    encrypt_txt.delete(0, END)
    encrypt_txt.insert(0, entxt)

Encrbtn = Button(window, text="Mã Hóa", command=mahoa_DES)
Encrbtn.grid(column=0, row=7)

# Giải mã
def giaima_DES():
    try:
        txt = base64.b64decode(encrypt_txt.get())
        key = pad(key_txt.get())
        if len(key) != 8:
            decrypt_txt.delete(0, END)
            decrypt_txt.insert(0, "Khóa phải dài đúng 8 ký tự!")
            return

        cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        detxt = unpad(cipher.decrypt(txt)).decode("utf-8")  # Chuyển lại thành UTF-8 sau khi giải mã
        decrypt_txt.delete(0, END)
        decrypt_txt.insert(0, detxt)
    except Exception as e:
        decrypt_txt.delete(0, END)
        decrypt_txt.insert(0, f"Lỗi giải mã: {str(e)}")

deAFbtn = Button(window, text="Giải mã", command=giaima_DES)
deAFbtn.grid(column=1, row=7)

window.geometry('800x400')
window.mainloop()
