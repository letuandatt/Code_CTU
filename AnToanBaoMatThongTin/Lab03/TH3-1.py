# Lê Tuấn Đạt
# B2113328
# 19

import base64
import os

from tkinter import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from tkinter import filedialog

# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")

# Them cac control
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

# Tiêu đề
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ BẤT ĐỐI XỨNG RSA", font=("Arial Bold", 15), justify="center")
lb2.grid(column=1, row=2)

# Phần văn bản gốc
original_word = Label(window, text="Văn bản gốc", font=("Arial", 14), justify="center")
original_word.grid(column=0, row=3)

original_txt = Entry(window, width=95)
original_txt.grid(column=1, row=3)

# Phần VB mã hóa
encrypt_word = Label(window, text="Văn bản được mã hóa", font=("Arial", 14))
encrypt_word.grid(column=0, row=4)

encrypt_txt = Entry(window, width=95)
encrypt_txt.grid(column=1, row=4)

# Phần VB giải mã
decrypt_word = Label(window, text="Văn bản được giải mã", font=("Arial", 14))
decrypt_word.grid(column=0, row=5)

decrypt_txt = Entry(window, width=95)
decrypt_txt.grid(column=1, row=5)

# Phần khóa cá nhân
private_key= Label(window, text="Khóa cá nhân", font=("Arial", 14))
private_key.grid(column=0, row=6)

private_key_txt = Text(window, width=70, height=10)
private_key_txt.grid(column=1, row=6)

# Phần khóa công khai
public_key = Label(window, text='Khóa công khai', font=("Arial", 14))
public_key.grid(column=0, row=7)

public_key_txt = Text(window, width=70, height=10)
public_key_txt.grid(column=1, row=7)

# Tạo khóa
def save_file(content, _mode, _title, _filetypes, _defaultExtension):
    f = filedialog.asksaveasfile(mode = _mode, initialdir=os.getcwd(), filetypes=_filetypes,
                                 defaultextension=_defaultExtension)
    if f is None:
        return

    f.write(content)
    f.close()

def generate_key():
    key = RSA.generate(1024)
    save_file(key.exportKey('PEM'), 'wb', 'Lưu khóa cá nhân', (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")
    save_file(key.public_key().exportKey('PEM'), 'wb', 'Lưu khóa cá nhân', (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")
    private_key_txt.delete('1.0', END)
    private_key_txt.insert(END, key.exportKey('PEM'))
    public_key_txt.delete('1.0', END)
    public_key_txt.insert(END, key.publickey().exportKey('PEM'))


gen_key = Button(window, text="Tạo khóa", command=generate_key)
gen_key.grid(column=1, row=8)

# Mã hóa
def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          filetypes=(("PEM files", "*.pem"), ('All files', '*.*')),
                                          title="Open " + key_style)
    if filename is None:
        return

    file = open(filename, 'rb')
    key = file.read()
    file.close()
    return RSA.importKey(key)

def mahoa_rsa():
    txt = original_txt.get().encode()
    public_key = get_key("Public Key")
    cipher = PKCS1_v1_5.new(public_key)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    encrypt_txt.delete(0, END)
    encrypt_txt.insert(END, entxt)

encr_button = Button(window, text="Mã hóa", command=mahoa_rsa)
encr_button.grid(column=1, row=9)

# Giải mã
def giaima_rsa():
    txt = encrypt_txt.get().encode()
    try:
        pri_key = get_key("Private Key")
        if pri_key is None:
            decrypt_txt.delete(0, END)
            decrypt_txt.insert(END, "No private key selected.")
            return

        cipher = PKCS1_v1_5.new(pri_key)
        sentinel_value = b'[DECRYPTION ERROR]'
        decr_txt = cipher.decrypt(base64.b64decode(txt), sentinel=sentinel_value)

        if decr_txt == sentinel_value:
            decrypt_txt.delete(0, END)
            decrypt_txt.insert(END, "Decryption failed or incorrect private key.")
        else:
            decrypt_txt.delete(0, END)
            decrypt_txt.insert(END, decr_txt.decode())

    except ValueError as e:
        decrypt_txt.delete(0, END)
        decrypt_txt.insert(END, str(e))
    except Exception as e:
        decrypt_txt.delete(0, END)
        decrypt_txt.insert(END, f"Error: {str(e)}")


decr_button = Button(window, text='Giải mã', command=giaima_rsa)
decr_button.grid(column=1, row=10)


# Main
window.geometry("800x600")
window.mainloop()
