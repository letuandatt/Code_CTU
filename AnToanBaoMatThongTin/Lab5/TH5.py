import tkinter as tk
import base64
import time
import threading
import gc
from tkinter import ttk, filedialog, messagebox
from Crypto.Cipher import AES, PKCS1_v1_5, ChaCha20
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256, MD5, SHA1, SHA512, HMAC
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Cấu hình kích thước cửa sổ
WINDOW_CONFIG = {
    "main": {"width": 600, "height": 700},
    "affine": {"width": 800, "height": 500},
    "aes": {"width": 900, "height": 600},
    "rsa": {"width": 900, "height": 600},
    "hash": {"width": 500, "height": 400},
    "chacha20": {"width": 900, "height": 500},
}

# Tách logic mã hóa
class CryptoUtils:
    @staticmethod
    def mod_inverse(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None

    @staticmethod
    def char2num(c):
        if c == ' ': return 52
        if c.islower(): return ord(c) - 97 + 26
        if c.isupper(): return ord(c) - 65
        if c.isdigit(): return ord(c) - 48 + 53
        return None

    @staticmethod
    def num2char(n):
        if n == 52: return ' '
        if 53 <= n <= 62: return str(n - 53)
        if n >= 26: return chr(n - 26 + 97)
        return chr(n + 65)

    @staticmethod
    def xgcd(a, m):
        temp = m
        x0, x1 = 1, 0
        while m != 0:
            q, a, m = a // m, m, a % m
            x0, x1 = x1, x0 - q * x1
        if x0 < 0: x0 += temp
        return x0

    @staticmethod
    def encrypt_affine(txt: str, a: int, b: int, m: int) -> str:
        """Mã hóa văn bản bằng thuật toán Affine."""
        return "".join(CryptoUtils.num2char((a * CryptoUtils.char2num(c) + b) % m)
                      for c in txt if CryptoUtils.char2num(c) is not None)

    @staticmethod
    def decrypt_affine(txt: str, a: int, b: int, m: int) -> str:
        """Giải mã văn bản bằng thuật toán Affine."""
        a1 = CryptoUtils.xgcd(a, m)
        if a1 is None:
            raise ValueError("Invalid key: 'a' must be coprime with 62")
        return "".join(CryptoUtils.num2char((a1 * (CryptoUtils.char2num(c) - b)) % m)
                      for c in txt if CryptoUtils.char2num(c) is not None)

    @staticmethod
    def encrypt_aes(text: str, key: str) -> str:
        """Mã hóa văn bản bằng AES-CBC với HMAC."""
        key = key.encode().ljust(16)[:16]
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_text = pad(text.encode(), AES.block_size)
        ciphertext = cipher.encrypt(padded_text)
        hmac = HMAC.new(key, iv + ciphertext, digestmod=SHA256).digest()
        return base64.b64encode(iv + ciphertext + hmac).decode()

    @staticmethod
    def decrypt_aes(ciphertext: str, key: str) -> str:
        """Giải mã văn bản bằng AES-CBC với xác thực HMAC."""
        key = key.encode().ljust(16)[:16]
        data = base64.b64decode(ciphertext)
        iv, ciphertext, hmac = data[:16], data[16:-32], data[-32:]
        if HMAC.new(key, iv + ciphertext, digestmod=SHA256).digest() != hmac:
            raise ValueError("Dữ liệu đã bị thay đổi!")
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        return unpad(decrypted, AES.block_size).decode()

    @staticmethod
    def encrypt_chacha20(text: str, key: str) -> str:
        """Mã hóa văn bản bằng ChaCha20."""
        key = key.encode().ljust(32)[:32]
        cipher = ChaCha20.new(key=key)
        nonce = cipher.nonce
        ciphertext = cipher.encrypt(text.encode())
        return base64.b64encode(nonce + ciphertext).decode()

    @staticmethod
    def decrypt_chacha20(ciphertext: str, key: str) -> str:
        """Giải mã văn bản bằng ChaCha20."""
        key = key.encode().ljust(32)[:32]
        data = base64.b64decode(ciphertext)
        nonce, ciphertext = data[:8], data[8:]
        cipher = ChaCha20.new(key=key, nonce=nonce)
        return cipher.decrypt(ciphertext).decode()

# Hàm hỗ trợ tooltip
def add_tooltip(widget, text):
    tooltip = ttk.Label(widget.master, text=text, background="yellow", relief="solid", borderwidth=1)
    def enter(event): tooltip.place(x=widget.winfo_x(), y=widget.winfo_y() + 25)
    def leave(event): tooltip.place_forget()
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

# Affine Cipher GUI
class MAHOA_AFFINE(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mã hóa Affine")
        config = WINDOW_CONFIG["affine"]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.configure(bg="#f0f0f0")
        self.crypto = CryptoUtils()

        style = ttk.Style()
        style.configure("TButton", padding=6, font=('Arial', 11))

        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ AFFINE", font=("Arial Bold", 20)).grid(column=0, row=0, columnspan=2, pady=10)

        ttk.Label(main_frame, text="Văn bản gốc:").grid(column=0, row=1, pady=5, sticky="e")
        self.plaintxt = ttk.Entry(main_frame, width=60)
        self.plaintxt.grid(column=1, row=1, pady=5)

        ttk.Label(main_frame, text="Khóa a:").grid(column=0, row=2, pady=5, sticky="e")
        self.key_a = ttk.Entry(main_frame, width=10, validate="key",
                              validatecommand=(self.register(self.validate_number), '%P'))
        self.key_a.grid(column=1, row=2, pady=5, sticky="w")
        add_tooltip(self.key_a, "Nhập số nguyên tố cùng nhau với 62 (VD: 3, 5, 7...)")

        ttk.Label(main_frame, text="Khóa b:").grid(column=0, row=3, pady=5, sticky="e")
        self.key_b = ttk.Entry(main_frame, width=10, validate="key",
                              validatecommand=(self.register(self.validate_number), '%P'))
        self.key_b.grid(column=1, row=3, pady=5, sticky="w")
        add_tooltip(self.key_b, "Nhập số từ 0 đến 61")

        ttk.Label(main_frame, text="Văn bản mã hóa:").grid(column=0, row=4, pady=5, sticky="e")
        self.ciphertxt = ttk.Entry(main_frame, width=60)
        self.ciphertxt.grid(column=1, row=4, pady=5)

        ttk.Label(main_frame, text="Văn bản giải mã:").grid(column=0, row=5, pady=5, sticky="e")
        self.dectxt = ttk.Entry(main_frame, width=60)
        self.dectxt.grid(column=1, row=5, pady=5)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=6, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Mã hóa", command=self.mahoa_affine).grid(column=0, row=0, padx=5)
        ttk.Button(btn_frame, text="Giải mã", command=self.giaima_affine).grid(column=1, row=0, padx=5)
        ttk.Button(btn_frame, text="Sao chép mã hóa", command=lambda: self.clipboard_append(self.ciphertxt.get())).grid(column=2, row=0, padx=5)
        ttk.Button(btn_frame, text="Sao chép giải mã", command=lambda: self.clipboard_append(self.dectxt.get())).grid(column=3, row=0, padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=4, row=0, padx=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=5, row=0, padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def validate_number(self, value):
        return value.isdigit() or value == ""

    def mahoa_affine(self):
        try:
            a = int(self.key_a.get())
            b = int(self.key_b.get())
            if not (0 <= a < 62 and 0 <= b < 62):
                raise ValueError("Khóa phải nằm trong khoảng 0-61")
            if self.crypto.mod_inverse(a, 62) is None:
                raise ValueError("Khóa 'a' phải nguyên tố cùng nhau với 62")
            entxt = self.crypto.encrypt_affine(self.plaintxt.get(), a, b, 62)
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
            self.master.log_action("Affine Encrypt", f"Input: {self.plaintxt.get()}, a: {a}, b: {b}, Output: {entxt}")
        except ValueError as ve:
            messagebox.showerror("Lỗi dữ liệu", str(ve))
        except Exception as e:
            messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {str(e)}")

    def giaima_affine(self):
        try:
            a = int(self.key_a.get())
            b = int(self.key_b.get())
            dectxt = self.crypto.decrypt_affine(self.ciphertxt.get(), a, b, 62)
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, dectxt)
            self.master.log_action("Affine Decrypt", f"Input: {self.ciphertxt.get()}, a: {a}, b: {b}, Output: {dectxt}")
        except ValueError as ve:
            messagebox.showerror("Lỗi dữ liệu", str(ve))
        except Exception as e:
            messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {str(e)}")

    def clear(self):
        self.plaintxt.delete(0, tk.END)
        self.ciphertxt.delete(0, tk.END)
        self.dectxt.delete(0, tk.END)
        self.key_a.delete(0, tk.END)
        self.key_b.delete(0, tk.END)
        gc.collect()

# AES GUI
class MAHOA_AES(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mã hóa AES")
        config = WINDOW_CONFIG["aes"]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.configure(bg="#f0f0f0")
        self.crypto = CryptoUtils()

        style = ttk.Style()
        style.configure("TButton", padding=6, font=('Arial', 11))

        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ AES", font=("Arial Bold", 20)).grid(column=0, row=0, columnspan=2, pady=10)

        ttk.Label(main_frame, text="Văn bản gốc:").grid(column=0, row=1, pady=5, sticky="e")
        self.plaintxt = ttk.Entry(main_frame, width=60)
        self.plaintxt.grid(column=1, row=1, pady=5)

        ttk.Label(main_frame, text="Khóa (≤16 ký tự):").grid(column=0, row=2, pady=5, sticky="e")
        self.keytxt = ttk.Entry(main_frame, width=60)
        self.keytxt.grid(column=1, row=2, pady=5)
        add_tooltip(self.keytxt, "Khóa tối đa 16 ký tự")

        ttk.Label(main_frame, text="Văn bản mã hóa:").grid(column=0, row=3, pady=5, sticky="e")
        self.ciphertxt = ttk.Entry(main_frame, width=60)
        self.ciphertxt.grid(column=1, row=3, pady=5)

        ttk.Label(main_frame, text="Văn bản giải mã:").grid(column=0, row=4, pady=5, sticky="e")
        self.dectxt = ttk.Entry(main_frame, width=60)
        self.dectxt.grid(column=1, row=4, pady=5)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=5, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Mã hóa", command=self.mahoa_aes).grid(column=0, row=0, padx=5)
        ttk.Button(btn_frame, text="Giải mã", command=self.giaima_aes).grid(column=1, row=0, padx=5)
        ttk.Button(btn_frame, text="Sao chép mã hóa", command=lambda: self.clipboard_append(self.ciphertxt.get())).grid(column=2, row=0, padx=5)
        ttk.Button(btn_frame, text="Sao chép giải mã", command=lambda: self.clipboard_append(self.dectxt.get())).grid(column=3, row=0, padx=5)
        ttk.Button(btn_frame, text="Tải file", command=self.load_file).grid(column=4, row=0, padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=5, row=0, padx=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=6, row=0, padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, 'r', encoding='utf-8') as f:
                self.plaintxt.delete(0, tk.END)
                self.plaintxt.insert(0, f.read())

    def mahoa_aes(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1:
                raise ValueError("Khóa không được để trống")
            if len(key) > 16:
                raise ValueError("Khóa không được dài quá 16 ký tự")
            entxt = self.crypto.encrypt_aes(self.plaintxt.get(), key)
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
            self.master.log_action("AES Encrypt", f"Input: {self.plaintxt.get()}, Key: {key}, Output: {entxt}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def giaima_aes(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1:
                raise ValueError("Khóa không được để trống")
            if len(key) > 16:
                raise ValueError("Khóa không được dài quá 16 ký tự")
            detxt = self.crypto.decrypt_aes(self.ciphertxt.get(), key)
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, detxt)
            self.master.log_action("AES Decrypt", f"Input: {self.ciphertxt.get()}, Key: {key}, Output: {detxt}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def clear(self):
        self.plaintxt.delete(0, tk.END)
        self.keytxt.delete(0, tk.END)
        self.ciphertxt.delete(0, tk.END)
        self.dectxt.delete(0, tk.END)
        gc.collect()

# RSA GUI
class MAHOA_RSA(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mã hóa RSA")
        config = WINDOW_CONFIG["rsa"]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.configure(bg="#f0f0f0")

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

        self.generate_btn = ttk.Button(btn_frame, text="Tạo khóa", command=self.generate_key)
        self.generate_btn.grid(column=0, row=0, padx=5)
        ttk.Button(btn_frame, text="Mã hóa", command=self.mahoa_rsa).grid(column=1, row=0, padx=5)
        ttk.Button(btn_frame, text="Giải mã", command=self.giaima_rsa).grid(column=2, row=0, padx=5)
        ttk.Button(btn_frame, text="Sao chép mã hóa", command=lambda: self.clipboard_append(self.ciphertxt.get())).grid(column=3, row=0, padx=5)
        ttk.Button(btn_frame, text="Sao chép giải mã", command=lambda: self.clipboard_append(self.dectxt.get())).grid(column=4, row=0, padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=5, row=0, padx=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=6, row=0, padx=5)

        self.progress = ttk.Progressbar(main_frame, mode="indeterminate")
        self.progress.grid(column=0, row=7, columnspan=2, pady=5, sticky="ew")
        self.progress.grid_remove()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def generate_key(self):
        self.generate_btn.config(state="disabled")
        self.progress.grid()
        self.progress.start()
        threading.Thread(target=self._generate_key_thread, daemon=True).start()

    def _generate_key_thread(self):
        try:
            key = RSA.generate(2048)
            private_key = key.exportKey('PEM')
            public_key = key.publickey().exportKey('PEM')
            self.after(0, lambda: self._update_keys(private_key, public_key))
            self.master.log_action("RSA Key Gen", "Generated new 2048-bit key pair")
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Lỗi", str(e)))
        finally:
            self.after(0, lambda: [self.generate_btn.config(state="normal"), self.progress.stop(), self.progress.grid_remove()])

    def _update_keys(self, private_key, public_key):
        self.privtxt.delete('1.0', tk.END)
        self.privtxt.insert('1.0', private_key.decode())
        self.pubtxt.delete('1.0', tk.END)
        self.pubtxt.insert('1.0', public_key.decode())

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
            self.master.log_action("RSA Encrypt", f"Input: {self.plaintxt.get()}, Output: {entxt}")
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
            self.master.log_action("RSA Decrypt", f"Input: {self.ciphertxt.get()}, Output: {detxt}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def clear(self):
        self.plaintxt.delete(0, tk.END)
        self.ciphertxt.delete(0, tk.END)
        self.dectxt.delete(0, tk.END)
        self.pubtxt.delete('1.0', tk.END)
        self.privtxt.delete('1.0', tk.END)
        gc.collect()

# ChaCha20 GUI
class MAHOA_CHACHA20(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mã hóa ChaCha20")
        config = WINDOW_CONFIG["chacha20"]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.configure(bg="#f0f0f0")
        self.crypto = CryptoUtils()

        style = ttk.Style()
        style.configure("TButton", padding=6, font=('Arial', 11))

        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ CHACHA20", font=("Arial Bold", 20)).grid(column=0, row=0, columnspan=2, pady=10)

        ttk.Label(main_frame, text="Văn bản gốc:").grid(column=0, row=1, pady=5, sticky="e")
        self.plaintxt = ttk.Entry(main_frame, width=60)
        self.plaintxt.grid(column=1, row=1, pady=5)

        ttk.Label(main_frame, text="Khóa (≤32 ký tự):").grid(column=0, row=2, pady=5, sticky="e")
        self.keytxt = ttk.Entry(main_frame, width=60)
        self.keytxt.grid(column=1, row=2, pady=5)
        add_tooltip(self.keytxt, "Khóa tối đa 32 ký tự")

        ttk.Label(main_frame, text="Văn bản mã hóa:").grid(column=0, row=3, pady=5, sticky="e")
        self.ciphertxt = ttk.Entry(main_frame, width=60)
        self.ciphertxt.grid(column=1, row=3, pady=5)

        ttk.Label(main_frame, text="Văn bản giải mã:").grid(column=0, row=4, pady=5, sticky="e")
        self.dectxt = ttk.Entry(main_frame, width=60)
        self.dectxt.grid(column=1, row=4, pady=5)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=5, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="Mã hóa", command=self.mahoa_chacha20).grid(column=0, row=0, padx=5)
        ttk.Button(btn_frame, text="Giải mã", command=self.giaima_chacha20).grid(column=1, row=0, padx=5)
        ttk.Button(btn_frame, text="Sao chép mã hóa", command=lambda: self.clipboard_append(self.ciphertxt.get())).grid(column=2, row=0, padx=5)
        ttk.Button(btn_frame, text="Sao chép giải mã", command=lambda: self.clipboard_append(self.dectxt.get())).grid(column=3, row=0, padx=5)
        ttk.Button(btn_frame, text="Tải file", command=self.load_file).grid(column=4, row=0, padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=5, row=0, padx=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=6, row=0, padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, 'r', encoding='utf-8') as f:
                self.plaintxt.delete(0, tk.END)
                self.plaintxt.insert(0, f.read())

    def mahoa_chacha20(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1:
                raise ValueError("Khóa không được để trống")
            if len(key) > 32:
                raise ValueError("Khóa không được dài quá 32 ký tự")
            entxt = self.crypto.encrypt_chacha20(self.plaintxt.get(), key)
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
            self.master.log_action("ChaCha20 Encrypt", f"Input: {self.plaintxt.get()}, Key: {key}, Output: {entxt}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def giaima_chacha20(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1:
                raise ValueError("Khóa không được để trống")
            if len(key) > 32:
                raise ValueError("Khóa không được dài quá 32 ký tự")
            detxt = self.crypto.decrypt_chacha20(self.ciphertxt.get(), key)
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, detxt)
            self.master.log_action("ChaCha20 Decrypt", f"Input: {self.ciphertxt.get()}, Key: {key}, Output: {detxt}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def clear(self):
        self.plaintxt.delete(0, tk.END)
        self.keytxt.delete(0, tk.END)
        self.ciphertxt.delete(0, tk.END)
        self.dectxt.delete(0, tk.END)
        gc.collect()

# Hashing GUI
class BAM(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Hàm băm")
        config = WINDOW_CONFIG["hash"]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.configure(bg="#f0f0f0")
        self.hash_cache = {}

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
        ttk.Button(btn_frame, text="Sao chép", command=lambda: self.clipboard_append(self.hash_txt.get())).grid(column=1, row=0, padx=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=2, row=0, padx=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=3, row=0, padx=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_hash(self):
        try:
            text = self.input_txt.get()
            algo = self.algo_var.get()
            cache_key = (text, algo)
            if cache_key in self.hash_cache:
                result = self.hash_cache[cache_key]
            else:
                hash_obj = {"MD5": MD5, "SHA1": SHA1, "SHA256": SHA256, "SHA512": SHA512}[algo].new(text.encode())
                result = hash_obj.hexdigest()
                self.hash_cache[cache_key] = result
            self.hash_txt.delete(0, tk.END)
            self.hash_txt.insert(0, result)
            self.master.log_action("Hash", f"Input: {text}, Algo: {algo}, Output: {result}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def clear(self):
        self.input_txt.delete(0, tk.END)
        self.hash_txt.delete(0, tk.END)
        gc.collect()

# Main Window
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chương trình mã hóa")
        config = WINDOW_CONFIG["main"]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.configure(bg="#f0f0f0")
        self.history = []
        self.theme_var = tk.StringVar(value="light")

        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Arial', 12))

        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(expand=True)

        ttk.Label(main_frame, text="MENU CHÍNH", font=("Arial Bold", 20)).pack(pady=20)

        ttk.Button(main_frame, text="Mã hóa Affine", command=self.affine).pack(pady=10)
        ttk.Button(main_frame, text="Mã hóa AES", command=self.aes).pack(pady=10)
        ttk.Button(main_frame, text="Mã hóa RSA", command=self.rsa).pack(pady=10)
        ttk.Button(main_frame, text="Mã hóa ChaCha20", command=self.chacha20).pack(pady=10)
        ttk.Button(main_frame, text="Hàm băm", command=self.hashing).pack(pady=10)
        ttk.Button(main_frame, text="Xem lịch sử", command=self.show_history).pack(pady=10)
        ttk.OptionMenu(main_frame, self.theme_var, "light", "light", "dark", command=self.change_theme).pack(pady=10)
        ttk.Button(main_frame, text="Thoát", command=self.quit).pack(pady=10)

    def change_theme(self, theme):
        bg_color = "#f0f0f0" if theme == "light" else "#2d2d2d"
        fg_color = "black" if theme == "light" else "white"
        self.configure(bg=bg_color)
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Frame):
                widget.configure(style="TFrame")
                for child in widget.winfo_children():
                    if isinstance(child, ttk.Label):
                        child.configure(foreground=fg_color)

    def log_action(self, action, data):
        self.history.append({"time": time.ctime(), "action": action, "data": data})

    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("Lịch sử")
        config = WINDOW_CONFIG["hash"]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        history_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        text = tk.Text(history_window, height=20, width=80)
        text.pack(pady=10)
        for entry in self.history:
            text.insert(tk.END, f"{entry['time']}: {entry['action']} - {entry['data']}\n")

    def affine(self): MAHOA_AFFINE(self)
    def aes(self): MAHOA_AES(self)
    def rsa(self): MAHOA_RSA(self)
    def chacha20(self): MAHOA_CHACHA20(self)
    def hashing(self): BAM(self)

if __name__ == '__main__':
    MainWindow().mainloop()