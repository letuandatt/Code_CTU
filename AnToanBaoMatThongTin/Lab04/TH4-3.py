# Lê Tuấn Đạt - B2113328 - 19
import csv
import os
import tkinter as tk

from tkinter import messagebox
from Crypto.Hash import MD5, SHA1, SHA256, SHA512


class LoginApp:
    def __init__(self):
        # Khởi tạo cửa sổ chính
        self.window = tk.Tk()
        self.window.title("Welcome to Demo AT&BMTT")
        self.window.geometry("400x200")

        # Tạo giao diện
        self._setup_ui()

    def _setup_ui(self):
        """Thiết lập giao diện người dùng"""
        # Khoảng trống
        tk.Label(self.window, text=" ", font=("Arial Bold", 14)).grid(column=0, row=0)

        # Tiêu đề
        tk.Label(self.window, text="Đăng nhập", font=("Arial Bold", 20)).grid(column=1, row=1)

        # Username
        tk.Label(self.window, text="Username", font=("Arial Bold", 11)).grid(column=0, row=2)
        self.username_entry = tk.Entry(self.window, width=50)
        self.username_entry.grid(column=1, row=2)

        # Password
        tk.Label(self.window, text="Password", font=("Arial Bold", 11)).grid(column=0, row=3)
        self.password_entry = tk.Entry(self.window, width=50, show="*")
        self.password_entry.grid(column=1, row=3)

        # Button
        tk.Button(self.window, text="Đăng nhập", command=self.login).grid(column=1, row=4)

    def hash_password(self, password):
        """Tạo danh sách các giá trị hash từ mật khẩu"""
        password = password.encode()
        hash_functions = [MD5, SHA1, SHA256, SHA512]
        return [func.new(password).hexdigest().upper() for func in hash_functions]

    def login(self):
        """Xử lý đăng nhập"""
        filename = 'accounts.csv'
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Kiểm tra đầu vào
        if not username or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ username và password!")
            return

        try:
            # Kiểm tra file tồn tại và đọc dữ liệu
            if not os.path.isfile(filename):
                messagebox.showerror("Lỗi", "Không tìm thấy tài khoản!")
                return

            with open(filename, mode='r', newline='') as file:
                users = csv.reader(file)
                stored_password = next((row[1] for row in users if row[0] == username), None)

            # Kiểm tra thông tin đăng nhập
            if stored_password:
                password_hashes = self.hash_password(password)
                if stored_password in password_hashes:
                    messagebox.showinfo("Thành công", "Đăng nhập thành công!")
                    self._clear_entries()
                else:
                    messagebox.showerror("Lỗi", "Mật khẩu không đúng!")
            else:
                messagebox.showerror("Lỗi", "Tài khoản không tồn tại!")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    def _clear_entries(self):
        """Xóa nội dung các trường nhập liệu"""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def run(self):
        """Chạy ứng dụng"""
        self.window.mainloop()


if __name__ == "__main__":
    app = LoginApp()
    app.run()