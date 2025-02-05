from tkinter import *

# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")

# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ AFFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)

plainlb3 = Label(window, text="PLAIN TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)

cipherlb4 = Label(window, text="CIPHER TEXT",font=("Arial", 14))
cipherlb4.grid(column=0, row=4)

plaintxt = Entry(window, width=20)
plaintxt.grid(column=1, row=3)

ciphertxt = Entry(window, width=20)
ciphertxt.grid(column=1, row=4)

KEYlb4 = Label(window, text="KEY PAIR",font=("Arial", 14))
KEYlb4.grid(column=2, row=3)

KEYA1 = Entry(window, width=3)
KEYA1.grid(column=3, row=3)

KEYB1 = Entry(window, width=5)
KEYB1.grid(column=4, row=3)

DECRTXT = Entry(window, width=20)
DECRTXT.grid(column=3, row=4)

def char2num(c):
    if c == ' ':
        return 52
    if c.islower():
        return ord(c) - 97 + 26
    return ord(c) - 65

def num2char(n):
    if n == 52:
        return ' '
    if n >= 26:
        return chr(n - 26 + 97)
    return chr(n + 65)

def encryptAF(txt, a, b, m):
    r = ""
    for c in txt:
        e = (a * char2num(c) + b) % m
        r += num2char(e)
    return r

def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 53
    entxt = encryptAF(plaintxt.get(), a, b, m)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)


AFbtn = Button(window, text="Mã Hóa", command=mahoa)
AFbtn.grid(column=5, row=3)

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0:
        x0 += temp
    return x0

def decryptAF(txt, a, b, m):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        e = (a1 * (char2num(c) - b)) % m
        r += num2char(e)
    return r

def giaima():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    cipher = ciphertxt.get()
    m = 53
    dectxt = decryptAF(cipher, a, b, m)
    DECRTXT.delete(0, END)
    DECRTXT.insert(INSERT, dectxt)


deAFbtn = Button(window, text="Giải mã", command=giaima)
deAFbtn.grid(column=2, row=4)

window.geometry('800x400')
window.mainloop()
