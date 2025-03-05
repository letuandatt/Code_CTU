import tkinter as tk
import base64

from tkinter import ttk, filedialog, messagebox
from Crypto.Cipher import DES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256, MD5, SHA1, SHA512


# Affine Cipher (Giữ nguyên các hàm cơ bản và cải tiến giao diện)
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def char2num(c):
    if c == ' ': return 52
    if c.islower(): return ord(c) - 97 + 26
    if c.isupper(): return ord(c) - 65
    if c.isdigit(): return ord(c) - 48 + 53
    return None


def num2char(n):
    if n == 52: return ' '
    if 53 <= n <= 62: return str(n - 53)
    if n >= 26: return chr(n - 26 + 97)
    return chr(n + 65)


def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 += temp
    return x0


def encryptAF(txt, a, b, m):
    return "".join(num2char((a * char2num(c) + b) % m) for c in txt if char2num(c) is not None)


def decryptAF(txt, a, b, m):
    a1 = xgcd(a, m)
    if a1 is None:
        return "Invalid key: 'a' must be coprime with 62"
    return "".join(num2char((a1 * (char2num(c) - b)) % m) for c in txt if char2num(c) is not None)


class MAHOA_AFFINE(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mã hóa Affine")
        self.geometry("800x500")
        self.configure(bg='#f0f0f0')

        # Style
        style = ttk.Style()
        style.configure("TButton", padding=6, font=('Arial', 11))

        # Main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ AFFINE", font=("Arial Bold", 20)).grid(column=0, row=0, columnspan=2,
                                                                                  pady=10)

        # Input fields
        ttk.Label(main_frame, text="Văn bản gốc:").grid(column=0, row=1, pady=5, sticky="e")
        self.plaintxt = ttk.Entry(main_frame, width=60)
        self.plaintxt.grid(column=1, row=1, pady=5)

        ttk.Label(main_frame, text="Khóa a:").grid(column=0, row=2, pady=5, sticky="e")
        self.key_a = ttk.Entry(main_frame, width=10)
        self.key_a.grid(column=1, row=2, pady=5, sticky="w")

        ttk.Label(main_frame, text="Khóa b:").grid(column=0, row=3, pady=5, sticky="e")
        self.key_b = ttk.Entry(main_frame, width=10)
        self.key_b.grid(column=1, row=3, pady=5, sticky="w")

        ttk.Label(main_frame, text="Văn bản mã hóa:").grid(column=0, row=4, pady=5, sticky="e")
        self.ciphertxt = ttk.Entry(main_frame, width=60)
        self.ciphertxt.grid(column=1, row=4, pady=5)

        ttk.Label(main_frame, text="Văn bản giải mã:").grid(column=0, row=5, pady=5, sticky="e")
        self.dectxt = ttk.Entry(main_frame, width=60)
        self.dectxt.grid(column=1, row=5, pady=5)

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=6, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Mã hóa", command=self.mahoa_affine).grid(column=0, row=0, padx=5)
        ttk.Button(btn_frame, text="Giải mã", command=self.giaima_affine).grid(column=1, row=0, padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=2, row=0, padx=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=3, row=0, padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def mahoa_affine(self):
        try:
            a, b = int(self.key_a.get()), int(self.key_b.get())
            if mod_inverse(a, 62) is None:
                raise ValueError("Khóa 'a' phải nguyên tố cùng nhau với 62")
            entxt = encryptAF(self.plaintxt.get(), a, b, 62)
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def giaima_affine(self):
        try:
            a, b = int(self.key_a.get()), int(self.key_b.get())
            dectxt = decryptAF(self.ciphertxt.get(), a, b, 62)
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, dectxt)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def clear(self):
        self.plaintxt.delete(0, tk.END)
        self.ciphertxt.delete(0, tk.END)
        self.dectxt.delete(0, tk.END)
        self.key_a.delete(0, tk.END)
        self.key_b.delete(0, tk.END)


# DES (Thêm xử lý lỗi và cải tiến giao diện)
def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)


def unpad(s):
    return s[:-ord(s[len(s) - 1:])]


class MAHOA_DES(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mã hóa DES")
        self.geometry("800x500")
        self.configure(bg='#f0f0f0')

        style = ttk.Style()
        style.configure("TButton", padding=6, font=('Arial', 11))

        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ DES", font=("Arial Bold", 20)).grid(column=0, row=0, columnspan=2, pady=10)

        ttk.Label(main_frame, text="Văn bản gốc:").grid(column=0, row=1, pady=5, sticky="e")
        self.plaintxt = ttk.Entry(main_frame, width=60)
        self.plaintxt.grid(column=1, row=1, pady=5)

        ttk.Label(main_frame, text="Khóa (8 ký tự):").grid(column=0, row=2, pady=5, sticky="e")
        self.keytxt = ttk.Entry(main_frame, width=60)
        self.keytxt.grid(column=1, row=2, pady=5)

        ttk.Label(main_frame, text="Văn bản mã hóa:").grid(column=0, row=3, pady=5, sticky="e")
        self.ciphertxt = ttk.Entry(main_frame, width=60)
        self.ciphertxt.grid(column=1, row=3, pady=5)

        ttk.Label(main_frame, text="Văn bản giải mã:").grid(column=0, row=4, pady=5, sticky="e")
        self.dectxt = ttk.Entry(main_frame, width=60)
        self.dectxt.grid(column=1, row=4, pady=5)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=5, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Mã hóa", command=self.mahoa_DES).grid(column=0, row=0, padx=5)
        ttk.Button(btn_frame, text="Giải mã", command=self.giaima_DES).grid(column=1, row=0, padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=2, row=0, padx=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=3, row=0, padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def mahoa_DES(self):
        try:
            key = pad(self.keytxt.get())
            txt = pad(self.plaintxt.get()).encode()
            cipher = DES.new(key.encode(), DES.MODE_ECB)
            entxt = base64.b64encode(cipher.encrypt(txt)).decode()
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def giaima_DES(self):
        try:
            key = pad(self.keytxt.get())
            txt = base64.b64decode(self.ciphertxt.get())
            cipher = DES.new(key.encode(), DES.MODE_ECB)
            detxt = unpad(cipher.decrypt(txt)).decode()
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, detxt)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def clear(self):
        self.plaintxt.delete(0, tk.END)
        self.keytxt.delete(0, tk.END)
        self.ciphertxt.delete(0, tk.END)
        self.dectxt.delete(0, tk.END)


# RSA (Cải tiến với file handling và giao diện)
class MAHOA_RSA(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mã hóa RSA")
        self.geometry("900x600")
        self.configure(bg='#f0f0f0')

        style = ttk.Style()
        style.configure("TButton", padding=6, font=('Arial', 11))

        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ RSA", font=("Arial Bold", 20)).grid(column=0, row=0, columnspan=2, pady=10)

        ttk.Label(main_frame, text="Văn bản gốc:").grid(column=0, row=1, pady=5, sticky="e")
        self.plaintxt = ttk.Entry(main_frame, width=70)
        self.plaintxt.grid(column=1, row=1, pady=5)

        ttk.Label(main_frame, text="Văn bản mã hóa:").grid(column=0, row=2, pady=5, sticky="e")
        self.ciphertxt = ttk.Entry(main_frame, width=70)
        self.ciphertxt.grid(column=1, row=2, pady=5)

        ttk.Label(main_frame, text="Văn bản giải mã:").grid(column=0, row=3, pady=5, sticky="e")
        self.dectxt = ttk.Entry(main_frame, width=70)
        self.dectxt.grid(column=1, row=3, pady=5)

        ttk.Label(main_frame, text="Khóa công khai:").grid(column=0, row=4, pady=5, sticky="ne")
        self.pubtxt = tk.Text(main_frame, height=5, width=50)
        self.pubtxt.grid(column=1, row=4, pady=5)

        ttk.Label(main_frame, text="Khóa bí mật:").grid(column=0, row=5, pady=5, sticky="ne")
        self.privtxt = tk.Text(main_frame, height=5, width=50)
        self.privtxt.grid(column=1, row=5, pady=5)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=6, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Tạo khóa", command=self.generate_key).grid(column=0, row=0, padx=5)
        ttk.Button(btn_frame, text="Mã hóa", command=self.mahoa_rsa).grid(column=1, row=0, padx=5)
        ttk.Button(btn_frame, text="Giải mã", command=self.giaima_rsa).grid(column=2, row=0, padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=3, row=0, padx=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=4, row=0, padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def generate_key(self):
        try:
            key = RSA.generate(2048)
            private_key = key.exportKey('PEM')
            public_key = key.publickey().exportKey('PEM')

            if (self.save_file(private_key, "Lưu khóa bí mật") and
                    self.save_file(public_key, "Lưu khóa công khai")):
                self.privtxt.delete('1.0', tk.END)
                self.privtxt.insert('1.0', private_key.decode())
                self.pubtxt.delete('1.0', tk.END)
                self.pubtxt.insert('1.0', public_key.decode())
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def save_file(self, content, title):
        f = filedialog.asksaveasfile(mode='wb', title=title,
                                     filetypes=(("PEM files", "*.pem"), ("All files", "*.*")),
                                     defaultextension=".pem")
        if f:
            f.write(content)
            f.close()
            return True
        return False

    def load_key(self, title):
        filename = filedialog.askopenfilename(title=title,
                                              filetypes=(("PEM files", "*.pem"), ("All files", "*.*")))
        if filename:
            with open(filename, 'rb') as f:
                return RSA.import_key(f.read())
        return None

    def mahoa_rsa(self):
        try:
            public_key = self.load_key("Chọn khóa công khai")
            if not public_key:
                raise ValueError("Không chọn được khóa công khai")
            cipher = PKCS1_v1_5.new(public_key)
            entxt = base64.b64encode(cipher.encrypt(self.plaintxt.get().encode())).decode()
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def giaima_rsa(self):
        try:
            private_key = self.load_key("Chọn khóa bí mật")
            if not private_key:
                raise ValueError("Không chọn được khóa bí mật")
            cipher = PKCS1_v1_5.new(private_key)
            detxt = cipher.decrypt(base64.b64decode(self.ciphertxt.get()), "Lỗi giải mã")
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, detxt.decode() if isinstance(detxt, bytes) else detxt)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def clear(self):
        self.plaintxt.delete(0, tk.END)
        self.ciphertxt.delete(0, tk.END)
        self.dectxt.delete(0, tk.END)
        self.pubtxt.delete('1.0', tk.END)
        self.privtxt.delete('1.0', tk.END)


# Hashing
class BAM(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Hàm băm")
        self.geometry("800x500")
        self.configure(bg='#f0f0f0')

        style = ttk.Style()
        style.configure("TButton", padding=6, font=('Arial', 11))

        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="CÁC HÀM BĂM", font=("Arial Bold", 20)).grid(column=0, row=0, columnspan=2, pady=10)

        ttk.Label(main_frame, text="Văn bản đầu vào:").grid(column=0, row=1, pady=5, sticky="e")
        self.input_txt = ttk.Entry(main_frame, width=60)
        self.input_txt.grid(column=1, row=1, pady=5)

        ttk.Label(main_frame, text="Thuật toán:").grid(column=0, row=2, pady=5, sticky="e")
        self.algo_var = tk.StringVar(value="SHA256")
        algo_menu = ttk.Combobox(main_frame, textvariable=self.algo_var,
                                 values=["MD5", "SHA1", "SHA256", "SHA512"], width=20)
        algo_menu.grid(column=1, row=2, pady=5, sticky="w")

        ttk.Label(main_frame, text="Kết quả:").grid(column=0, row=3, pady=5, sticky="e")
        self.hash_txt = ttk.Entry(main_frame, width=60)
        self.hash_txt.grid(column=1, row=3, pady=5)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=4, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Tạo băm", command=self.create_hash).grid(column=0, row=0, padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=1, row=0, padx=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=2, row=0, padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_hash(self):
        try:
            text = self.input_txt.get().encode()
            algo = self.algo_var.get()
            hash_obj = {
                "MD5": MD5, "SHA1": SHA1,
                "SHA256": SHA256, "SHA512": SHA512
            }[algo].new(text)
            self.hash_txt.delete(0, tk.END)
            self.hash_txt.insert(0, hash_obj.hexdigest())
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def clear(self):
        self.input_txt.delete(0, tk.END)
        self.hash_txt.delete(0, tk.END)


# Main Window
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chương trình mã hóa")
        self.geometry("600x500")
        self.configure(bg='#f0f0f0')

        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Arial', 12))

        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(expand=True)

        ttk.Label(main_frame, text="MENU CHÍNH", font=("Arial Bold", 20)).pack(pady=20)

        ttk.Button(main_frame, text="Mã hóa Affine", command=self.affine).pack(pady=10)
        ttk.Button(main_frame, text="Mã hóa DES", command=self.des).pack(pady=10)
        ttk.Button(main_frame, text="Mã hóa RSA", command=self.rsa).pack(pady=10)
        ttk.Button(main_frame, text="Hàm băm", command=self.hashing).pack(pady=10)
        ttk.Button(main_frame, text="Thoát", command=self.quit).pack(pady=10)

    def affine(self): MAHOA_AFFINE(self)

    def des(self): MAHOA_DES(self)

    def rsa(self): MAHOA_RSA(self)

    def hashing(self): BAM(self)


if __name__ == '__main__':
    MainWindow().mainloop()