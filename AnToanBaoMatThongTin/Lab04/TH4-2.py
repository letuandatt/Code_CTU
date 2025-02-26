# Lê Tuấn Đạt - B2113328 - 19
import csv
import os
import random
import tkinter as tk

from tkinter import messagebox
from Crypto.Hash import MD5, SHA1, SHA256, SHA512


class AccountCreator:
    def __init__(self):
        # Khởi tạo cửa sổ chính
        self.window = tk.Tk()
        self.window.title("Welcome to Demo AT&BMTT")
        self.window.geometry("400x200")

        # Tạo các control
        self._setup_ui()

    def _setup_ui(self):
        """Thiết lập giao diện người dùng"""
        tk.Label(self.window, text=" ", font=("Arial Bold", 14)).grid(column=0, row=0)

        # Tiêu đề
        tk.Label(self.window, text="Tạo tài khoản", font=("Arial Bold", 20)).grid(column=1, row=1)

        # Username
        tk.Label(self.window, text="Username", font=("Arial Bold", 11)).grid(column=0, row=2)
        self.username_entry = tk.Entry(self.window, width=50)
        self.username_entry.grid(column=1, row=2)

        # Password
        tk.Label(self.window, text="Password", font=("Arial Bold", 11)).grid(column=0, row=3)
        self.password_entry = tk.Entry(self.window, width=50, show="*")  # Ẩn mật khẩu
        self.password_entry.grid(column=1, row=3)

        # Button
        tk.Button(self.window, text="Tạo tài khoản", command=self.create_account).grid(column=1, row=4)

    def hash_password(self, password):
        """Hàm băm mật khẩu với thuật toán ngẫu nhiên"""
        hash_functions = [MD5, SHA1, SHA256, SHA512]
        hash_func = random.choice(hash_functions)
        return hash_func.new(password.encode()).hexdigest().upper()

    def create_account(self):
        """Xử lý tạo tài khoản"""
        filename = 'accounts.csv'
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Kiểm tra đầu vào
        if not username or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ username và password!")
            return

        # Kiểm tra tài khoản tồn tại
        try:
            if os.path.isfile(filename):
                with open(filename, mode='r', newline='') as file:
                    users = csv.reader(file)
                    if any(row[0] == username for row in users):
                        messagebox.showerror("Lỗi", "Tài khoản đã tồn tại!")
                        return

            # Tạo tài khoản mới
            hashed_password = self.hash_password(password)
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, hashed_password])

            messagebox.showinfo("Thành công", "Tạo tài khoản thành công!")
            self._clear_entries()

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
    app = AccountCreator()
    app.run()