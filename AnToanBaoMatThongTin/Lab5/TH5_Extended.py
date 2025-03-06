import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import base64
import time
import json
import os
from Crypto.Cipher import AES, Salsa20, Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from ecies import encrypt as ecc_encrypt, decrypt as ecc_decrypt
from ecies.utils import generate_key

# Cấu hình giao diện
WINDOW_CONFIG = {
    "main": {"width": 700, "height": 750},
    "aes": {"width": 1000, "height": 600},
    "ecc": {"width": 1000, "height": 700},
    "salsa20": {"width": 1000, "height": 600},
    "blowfish": {"width": 1000, "height": 600},
}

HISTORY_FILE = "history_encrypted.txt"
MASTER_KEY = "masterkey12345678901234567890123"  # Khóa mặc định để mã hóa file lịch sử (32 byte)

# Lớp mã hóa
class CryptoUtils:
    @staticmethod
    def encrypt_aes_cbc(text: str, key: str) -> tuple[str, bytes]:
        key = key.encode().ljust(32)[:32]
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_text = pad(text.encode(), 16)
        ciphertext = cipher.encrypt(padded_text)
        return base64.b64encode(iv + ciphertext).decode(), iv

    @staticmethod
    def decrypt_aes_cbc(ciphertext: str, key: str) -> str:
        key = key.encode().ljust(32)[:32]
        data = base64.b64decode(ciphertext)
        iv, ciphertext = data[:16], data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext), 16).decode()

    @staticmethod
    def encrypt_ecc(text: str, pubkey: bytes) -> str:
        return base64.b64encode(ecc_encrypt(pubkey, text.encode())).decode()

    @staticmethod
    def decrypt_ecc(ciphertext: str, privkey: bytes) -> str:
        return ecc_decrypt(privkey, base64.b64decode(ciphertext)).decode()

    @staticmethod
    def encrypt_salsa20(text: str, key: str) -> tuple[str, bytes]:
        key = key.encode().ljust(32)[:32]
        cipher = Salsa20.new(key=key)
        ciphertext = cipher.encrypt(text.encode())
        return base64.b64encode(cipher.nonce + ciphertext).decode(), cipher.nonce

    @staticmethod
    def decrypt_salsa20(ciphertext: str, key: str) -> str:
        key = key.encode().ljust(32)[:32]
        data = base64.b64decode(ciphertext)
        nonce, ciphertext = data[:8], data[8:]
        cipher = Salsa20.new(key=key, nonce=nonce)
        return cipher.decrypt(ciphertext).decode()

    @staticmethod
    def encrypt_blowfish(text: str, key: str) -> tuple[str, bytes]:
        key = key.encode().ljust(32)[:32]
        iv = get_random_bytes(8)
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        padded_text = pad(text.encode(), 8)
        ciphertext = cipher.encrypt(padded_text)
        return base64.b64encode(iv + ciphertext).decode(), iv

    @staticmethod
    def decrypt_blowfish(ciphertext: str, key: str) -> str:
        key = key.encode().ljust(32)[:32]
        data = base64.b64decode(ciphertext)
        iv, ciphertext = data[:8], data[8:]
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext), 8).decode()

    @staticmethod
    def encrypt_history(data: str, master_key: str) -> str:
        key = master_key.encode().ljust(32)[:32]
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(data.encode(), 16)
        ciphertext = cipher.encrypt(padded_data)
        return base64.b64encode(iv + ciphertext).decode()

    @staticmethod
    def decrypt_history(ciphertext: str, master_key: str) -> str:
        key = master_key.encode().ljust(32)[:32]
        data = base64.b64decode(ciphertext)
        iv, ciphertext = data[:16], data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext), 16).decode()

# Hàm hỗ trợ
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                encrypted_data = f.read()
            decrypted_data = CryptoUtils.decrypt_history(encrypted_data, MASTER_KEY)
            return json.loads(decrypted_data)
        except Exception as e:
            return []
    return []

def save_history(history):
    data = json.dumps(history, ensure_ascii=False, indent=4)
    encrypted_data = CryptoUtils.encrypt_history(data, MASTER_KEY)
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        f.write(encrypted_data)

class BaseWindow(tk.Toplevel):
    def __init__(self, parent, title, window_type):
        super().__init__(parent)
        self.title(title)
        self.center_window(window_type)
        self.apply_theme(parent.theme_var.get())
        self.crypto = CryptoUtils()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        style = ttk.Style()
        style.configure("TButton", padding=8, font=('Helvetica', 12))
        style.configure("TLabel", font=('Helvetica', 11))

    def center_window(self, window_type):
        config = WINDOW_CONFIG[window_type]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def apply_theme(self, theme):
        bg_color = "#ffffff" if theme == "light" else "#1e1e1e"
        fg_color = "#333333" if theme == "light" else "#ffffff"
        self.configure(bg=bg_color)
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Frame) or isinstance(widget, tk.Frame):
                widget.configure(style=f"{theme}.TFrame")
                for child in widget.winfo_children():
                    if isinstance(child, ttk.Label):
                        child.configure(foreground=fg_color)

    def create_common_widgets(self, frame, key_label, key_tip):
        ttk.Label(frame, text="Văn bản gốc:").grid(column=0, row=1, pady=10, sticky="e")
        self.plaintxt = ttk.Entry(frame, width=80, font=('Helvetica', 11))
        self.plaintxt.grid(column=1, row=1, pady=10)
        ttk.Label(frame, text=key_label).grid(column=0, row=2, pady=10, sticky="e")
        self.keytxt = ttk.Entry(frame, width=80, font=('Helvetica', 11), show="*")
        self.keytxt.grid(column=1, row=2, pady=10)
        ttk.Label(frame, text="Văn bản mã hóa:").grid(column=0, row=3, pady=10, sticky="e")
        self.ciphertxt = ttk.Entry(frame, width=80, font=('Helvetica', 11))
        self.ciphertxt.grid(column=1, row=3, pady=10)
        ttk.Label(frame, text="Văn bản giải mã:").grid(column=0, row=4, pady=10, sticky="e")
        self.dectxt = ttk.Entry(frame, width=80, font=('Helvetica', 11))
        self.dectxt.grid(column=1, row=4, pady=10)

    def create_buttons(self, frame, encrypt_cmd, decrypt_cmd):
        ttk.Button(frame, text="Mã hóa", command=encrypt_cmd).grid(column=0, row=0, padx=5, pady=5)
        ttk.Button(frame, text="Giải mã", command=decrypt_cmd).grid(column=1, row=0, padx=5, pady=5)
        ttk.Button(frame, text="Sao chép mã hóa", command=lambda: self.clipboard_append(self.ciphertxt.get())).grid(column=2, row=0, padx=5, pady=5)
        ttk.Button(frame, text="Sao chép giải mã", command=lambda: self.clipboard_append(self.dectxt.get())).grid(column=3, row=0, padx=5, pady=5)
        ttk.Button(frame, text="Tải file", command=self.load_file).grid(column=4, row=0, padx=5, pady=5)
        ttk.Button(frame, text="Xóa", command=self.clear).grid(column=5, row=0, padx=5, pady=5)
        ttk.Button(frame, text="Quay lại", command=self.destroy).grid(column=6, row=0, padx=5, pady=5)

    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, 'r', encoding='utf-8') as f:
                self.plaintxt.delete(0, tk.END)
                self.plaintxt.insert(0, f.read())
            self.update_status("Đã tải file thành công", "green")

    def clear(self):
        self.plaintxt.delete(0, tk.END)
        self.keytxt.delete(0, tk.END)
        self.ciphertxt.delete(0, tk.END)
        self.dectxt.delete(0, tk.END)
        self.update_status("Sẵn sàng", "green")

    def update_status(self, text, color):
        self.status_label.config(text=text, foreground=color)
        self.progress_bar["value"] = 100 if "thành công" in text else 0

    def on_close(self):
        self.clear()
        self.destroy()

class MAHOA_AES_CBC(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, "Mã hóa AES-256-CBC", "aes")
        main_frame = ttk.Frame(self, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ AES-256-CBC", font=("Helvetica", 24, "bold")).grid(column=0, row=0, columnspan=2, pady=20)
        self.create_common_widgets(main_frame, "Khóa (≤32 ký tự):", "Khóa tối đa 32 ký tự")

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=5, columnspan=2, pady=20)
        self.create_buttons(btn_frame, self.mahoa_aes_cbc, self.giaima_aes_cbc)

        status_frame = ttk.Frame(main_frame)
        status_frame.grid(column=0, row=6, columnspan=2, pady=10, sticky="ew")
        self.status_label = ttk.Label(status_frame, text="Sẵn sàng", foreground="green", font=('Helvetica', 11))
        self.status_label.grid(row=0, column=0)
        self.progress_bar = ttk.Progressbar(status_frame, length=200, mode="determinate")
        self.progress_bar.grid(row=0, column=1, padx=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def mahoa_aes_cbc(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1: raise ValueError("Khóa không được để trống")
            if len(key) > 32: raise ValueError("Khóa không được dài quá 32 ký tự")
            entxt, iv = self.crypto.encrypt_aes_cbc(self.plaintxt.get(), key)
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
            self.update_status("Mã hóa thành công", "green")
            self.master.log_action("AES-256-CBC Encrypt", f"Input: {self.plaintxt.get()}, Output: {entxt}", key=key, iv_nonce=iv)
        except Exception as e:
            self.update_status("Lỗi mã hóa", "red")
            self.master.log_action("AES-256-CBC Encrypt", f"Input: {self.plaintxt.get()}", key=key, error=str(e))
            messagebox.showerror("Lỗi", str(e))

    def giaima_aes_cbc(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1: raise ValueError("Khóa không được để trống")
            if len(key) > 32: raise ValueError("Khóa không được dài quá 32 ký tự")
            detxt = self.crypto.decrypt_aes_cbc(self.ciphertxt.get(), key)
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, detxt)
            self.update_status("Giải mã thành công", "green")
            self.master.log_action("AES-256-CBC Decrypt", f"Input: {self.ciphertxt.get()}, Output: {detxt}", key=key)
        except Exception as e:
            self.update_status("Lỗi giải mã", "red")
            self.master.log_action("AES-256-CBC Decrypt", f"Input: {self.ciphertxt.get()}", key=key, error=str(e))
            messagebox.showerror("Lỗi", str(e))

class MAHOA_ECC(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, "Mã hóa ECC", "ecc")
        self.keypair = None

        main_frame = ttk.Frame(self, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ ECC", font=("Helvetica", 24, "bold")).grid(column=0, row=0, columnspan=2, pady=20)
        ttk.Label(main_frame, text="Văn bản gốc:").grid(column=0, row=1, pady=10, sticky="e")
        self.plaintxt = ttk.Entry(main_frame, width=80, font=('Helvetica', 11))
        self.plaintxt.grid(column=1, row=1, pady=10)
        ttk.Label(main_frame, text="Văn bản mã hóa:").grid(column=0, row=2, pady=10, sticky="e")
        self.ciphertxt = ttk.Entry(main_frame, width=80, font=('Helvetica', 11))
        self.ciphertxt.grid(column=1, row=2, pady=10)
        ttk.Label(main_frame, text="Văn bản giải mã:").grid(column=0, row=3, pady=10, sticky="e")
        self.dectxt = ttk.Entry(main_frame, width=80, font=('Helvetica', 11))
        self.dectxt.grid(column=1, row=3, pady=10)
        ttk.Label(main_frame, text="Khóa công khai:").grid(column=0, row=4, pady=10, sticky="ne")
        self.pubtxt = tk.Text(main_frame, height=5, width=60, font=('Helvetica', 11))
        self.pubtxt.grid(column=1, row=4, pady=10)
        ttk.Label(main_frame, text="Khóa bí mật:").grid(column=0, row=5, pady=10, sticky="ne")
        self.privtxt = tk.Text(main_frame, height=5, width=60, font=('Helvetica', 11))
        self.privtxt.grid(column=1, row=5, pady=10)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=6, columnspan=2, pady=20)
        ttk.Button(btn_frame, text="Tạo khóa", command=self.generate_key).grid(column=0, row=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Mã hóa", command=self.mahoa_ecc).grid(column=1, row=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Giải mã", command=self.giaima_ecc).grid(column=2, row=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Sao chép mã hóa", command=lambda: self.clipboard_append(self.ciphertxt.get())).grid(column=3, row=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Sao chép giải mã", command=lambda: self.clipboard_append(self.dectxt.get())).grid(column=4, row=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Xóa", command=self.clear).grid(column=5, row=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Quay lại", command=self.destroy).grid(column=6, row=0, padx=5, pady=5)

        status_frame = ttk.Frame(main_frame)
        status_frame.grid(column=0, row=7, columnspan=2, pady=10, sticky="ew")
        self.status_label = ttk.Label(status_frame, text="Sẵn sàng", foreground="green", font=('Helvetica', 11))
        self.status_label.grid(row=0, column=0)
        self.progress_bar = ttk.Progressbar(status_frame, length=200, mode="determinate")
        self.progress_bar.grid(row=0, column=1, padx=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def generate_key(self):
        try:
            self.keypair = generate_key()
            pubkey = base64.b64encode(self.keypair.public_key.format()).decode()
            privkey = base64.b64encode(self.keypair.secret).decode()
            self.pubtxt.delete('1.0', tk.END)
            self.pubtxt.insert('1.0', pubkey)
            self.privtxt.delete('1.0', tk.END)
            self.privtxt.insert('1.0', privkey)
            self.update_status("Khóa đã được tạo", "green")
            self.master.log_action("ECC Key Gen", f"Public Key: {pubkey}, Private Key: {privkey}")
        except Exception as e:
            self.update_status("Lỗi tạo khóa", "red")
            self.master.log_action("ECC Key Gen", "Failed", error=str(e))

    def mahoa_ecc(self):
        try:
            if not self.keypair: raise ValueError("Chưa tạo khóa!")
            entxt = self.crypto.encrypt_ecc(self.plaintxt.get(), self.keypair.public_key.format())
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
            self.update_status("Mã hóa thành công", "green")
            self.master.log_action("ECC Encrypt", f"Input: {self.plaintxt.get()}, Output: {entxt}", key=base64.b64encode(self.keypair.secret).decode())
        except Exception as e:
            self.update_status("Lỗi mã hóa", "red")
            self.master.log_action("ECC Encrypt", f"Input: {self.plaintxt.get()}", error=str(e))
            messagebox.showerror("Lỗi", str(e))

    def giaima_ecc(self):
        try:
            if not self.keypair: raise ValueError("Chưa tạo khóa!")
            detxt = self.crypto.decrypt_ecc(self.ciphertxt.get(), self.keypair.secret)
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, detxt)
            self.update_status("Giải mã thành công", "green")
            self.master.log_action("ECC Decrypt", f"Input: {self.ciphertxt.get()}, Output: {detxt}", key=base64.b64encode(self.keypair.secret).decode())
        except Exception as e:
            self.update_status("Lỗi giải mã", "red")
            self.master.log_action("ECC Decrypt", f"Input: {self.ciphertxt.get()}", error=str(e))
            messagebox.showerror("Lỗi", str(e))

class MAHOA_SALSA20(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, "Mã hóa Salsa20", "salsa20")
        main_frame = ttk.Frame(self, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ SALSA20", font=("Helvetica", 24, "bold")).grid(column=0, row=0, columnspan=2, pady=20)
        self.create_common_widgets(main_frame, "Khóa (≤32 ký tự):", "Khóa tối đa 32 ký tự")

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=5, columnspan=2, pady=20)
        self.create_buttons(btn_frame, self.mahoa_salsa20, self.giaima_salsa20)

        status_frame = ttk.Frame(main_frame)
        status_frame.grid(column=0, row=6, columnspan=2, pady=10, sticky="ew")
        self.status_label = ttk.Label(status_frame, text="Sẵn sàng", foreground="green", font=('Helvetica', 11))
        self.status_label.grid(row=0, column=0)
        self.progress_bar = ttk.Progressbar(status_frame, length=200, mode="determinate")
        self.progress_bar.grid(row=0, column=1, padx=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def mahoa_salsa20(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1: raise ValueError("Khóa không được để trống")
            if len(key) > 32: raise ValueError("Khóa không được dài quá 32 ký tự")
            entxt, nonce = self.crypto.encrypt_salsa20(self.plaintxt.get(), key)
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
            self.update_status("Mã hóa thành công", "green")
            self.master.log_action("Salsa20 Encrypt", f"Input: {self.plaintxt.get()}, Output: {entxt}", key=key, iv_nonce=nonce)
        except Exception as e:
            self.update_status("Lỗi mã hóa", "red")
            self.master.log_action("Salsa20 Encrypt", f"Input: {self.plaintxt.get()}", key=key, error=str(e))
            messagebox.showerror("Lỗi", str(e))

    def giaima_salsa20(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1: raise ValueError("Khóa không được để trống")
            if len(key) > 32: raise ValueError("Khóa không được dài quá 32 ký tự")
            detxt = self.crypto.decrypt_salsa20(self.ciphertxt.get(), key)
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, detxt)
            self.update_status("Giải mã thành công", "green")
            self.master.log_action("Salsa20 Decrypt", f"Input: {self.ciphertxt.get()}, Output: {detxt}", key=key)
        except Exception as e:
            self.update_status("Lỗi giải mã", "red")
            self.master.log_action("Salsa20 Decrypt", f"Input: {self.ciphertxt.get()}", key=key, error=str(e))
            messagebox.showerror("Lỗi", str(e))

class MAHOA_BLOWFISH(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, "Mã hóa Blowfish", "blowfish")
        main_frame = ttk.Frame(self, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MẬT MÃ BLOWFISH", font=("Helvetica", 24, "bold")).grid(column=0, row=0, columnspan=2, pady=20)
        self.create_common_widgets(main_frame, "Khóa (≤32 ký tự):", "Khóa tối đa 32 ký tự")

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=5, columnspan=2, pady=20)
        self.create_buttons(btn_frame, self.mahoa_blowfish, self.giaima_blowfish)

        status_frame = ttk.Frame(main_frame)
        status_frame.grid(column=0, row=6, columnspan=2, pady=10, sticky="ew")
        self.status_label = ttk.Label(status_frame, text="Sẵn sàng", foreground="green", font=('Helvetica', 11))
        self.status_label.grid(row=0, column=0)
        self.progress_bar = ttk.Progressbar(status_frame, length=200, mode="determinate")
        self.progress_bar.grid(row=0, column=1, padx=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def mahoa_blowfish(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1: raise ValueError("Khóa không được để trống")
            if len(key) > 32: raise ValueError("Khóa không được dài quá 32 ký tự")
            entxt, iv = self.crypto.encrypt_blowfish(self.plaintxt.get(), key)
            self.ciphertxt.delete(0, tk.END)
            self.ciphertxt.insert(0, entxt)
            self.update_status("Mã hóa thành công", "green")
            self.master.log_action("Blowfish Encrypt", f"Input: {self.plaintxt.get()}, Output: {entxt}", key=key, iv_nonce=iv)
        except Exception as e:
            self.update_status("Lỗi mã hóa", "red")
            self.master.log_action("Blowfish Encrypt", f"Input: {self.plaintxt.get()}", key=key, error=str(e))
            messagebox.showerror("Lỗi", str(e))

    def giaima_blowfish(self):
        try:
            key = self.keytxt.get()
            if len(key) < 1: raise ValueError("Khóa không được để trống")
            if len(key) > 32: raise ValueError("Khóa không được dài quá 32 ký tự")
            detxt = self.crypto.decrypt_blowfish(self.ciphertxt.get(), key)
            self.dectxt.delete(0, tk.END)
            self.dectxt.insert(0, detxt)
            self.update_status("Giải mã thành công", "green")
            self.master.log_action("Blowfish Decrypt", f"Input: {self.ciphertxt.get()}, Output: {detxt}", key=key)
        except Exception as e:
            self.update_status("Lỗi giải mã", "red")
            self.master.log_action("Blowfish Decrypt", f"Input: {self.ciphertxt.get()}", key=key, error=str(e))
            messagebox.showerror("Lỗi", str(e))

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chương trình mã hóa - Advanced")
        config = WINDOW_CONFIG["main"]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.history = load_history()
        self.theme_var = tk.StringVar(value="light")

        style = ttk.Style()
        style.configure("TButton", padding=12, font=('Helvetica', 12))
        style.configure("light.TFrame", background="#ffffff")
        style.configure("dark.TFrame", background="#1e1e1e")

        main_frame = ttk.Frame(self, padding="30", style=f"{self.theme_var.get()}.TFrame")
        main_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(main_frame, text="MENU CHÍNH", font=("Helvetica", 28, "bold")).grid(row=0, column=0, columnspan=2, pady=30)
        ttk.Button(main_frame, text="Mã hóa AES-256-CBC", command=self.aes_cbc).grid(row=1, column=0, pady=15, sticky="ew")
        ttk.Button(main_frame, text="Mã hóa ECC", command=self.ecc).grid(row=2, column=0, pady=15, sticky="ew")
        ttk.Button(main_frame, text="Mã hóa Salsa20", command=self.salsa20).grid(row=3, column=0, pady=15, sticky="ew")
        ttk.Button(main_frame, text="Mã hóa Blowfish", command=self.blowfish).grid(row=4, column=0, pady=15, sticky="ew")
        ttk.Button(main_frame, text="Xem lịch sử", command=self.show_history).grid(row=5, column=0, pady=15, sticky="ew")
        ttk.OptionMenu(main_frame, self.theme_var, "light", "light", "dark", command=self.change_theme).grid(row=6, column=0, pady=15, sticky="ew")
        ttk.Button(main_frame, text="Thoát", command=self.quit).grid(row=7, column=0, pady=15, sticky="ew")

        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=8, column=0, columnspan=2, pady=20, sticky="ew")
        self.status_label = ttk.Label(status_frame, text="Sẵn sàng", foreground="green", font=('Helvetica', 11))
        self.status_label.grid(row=0, column=0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def change_theme(self, theme):
        bg_color = "#ffffff" if theme == "light" else "#1e1e1e"
        fg_color = "#333333" if theme == "light" else "#ffffff"
        self.configure(bg=bg_color)
        self.status_label.configure(foreground=fg_color)
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Frame):
                widget.configure(style=f"{theme}.TFrame")
                for child in widget.winfo_children():
                    if isinstance(child, ttk.Label):
                        child.configure(foreground=fg_color)

    def log_action(self, action, data, key=None, iv_nonce=None, error=None):
        entry = {
            "time": time.ctime(),
            "action": action,
            "data": data,
            "key": key if key else None,
            "iv_nonce": base64.b64encode(iv_nonce).decode() if iv_nonce else None,
            "error": error if error else None
        }
        self.history.append(entry)
        save_history(self.history)
        self.status_label.config(text=f"Đã ghi: {action}", foreground="green")

    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("Lịch sử")
        config = WINDOW_CONFIG["main"]
        window_width, window_height = config["width"], config["height"]
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        history_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        text = tk.Text(history_window, height=25, width=90, font=('Helvetica', 11))
        text.pack(pady=20, padx=20)
        for entry in self.history:
            text.insert(tk.END, f"{entry['time']}: {entry['action']} - {entry['data']}\n")
            if entry['key']:
                text.insert(tk.END, f"  Key: {entry['key']}\n")
            if entry['iv_nonce']:
                text.insert(tk.END, f"  IV/Nonce: {entry['iv_nonce']}\n")
            if entry['error']:
                text.insert(tk.END, f"  Error: {entry['error']}\n")
            text.insert(tk.END, "-" * 50 + "\n")

    def aes_cbc(self): self.last_window = MAHOA_AES_CBC(self)
    def ecc(self): self.last_window = MAHOA_ECC(self)
    def salsa20(self): self.last_window = MAHOA_SALSA20(self)
    def blowfish(self): self.last_window = MAHOA_BLOWFISH(self)

if __name__ == '__main__':
    MainWindow().mainloop()