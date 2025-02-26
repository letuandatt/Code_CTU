# Lê Tuấn Đạt
# B2113328
# 19

import tkinter as tk

from tkinter import messagebox
from Crypto.Hash import MD5, SHA1, SHA256, SHA512


class HashingApp:
    def __init__(self):
        # Khởi tạo cửa sổ chính
        self.window = tk.Tk()
        self.window.title("Welcome to Demo AT&BMTT")
        self.window.geometry("700x400")

        # Biến lưu lựa chọn hàm băm
        self.hashmode = tk.IntVar(value=-1)

        # Thiết lập giao diện
        self._setup_ui()

    def _setup_ui(self):
        """Thiết lập giao diện người dùng"""
        # Khoảng trống
        tk.Label(self.window, text=" ", font=("Arial Bold", 14)).grid(column=0, row=0)

        # Tiêu đề
        tk.Label(self.window, text="CHƯƠNG TRÌNH BĂM", font=("Arial Bold", 20)).grid(column=1, row=1)

        # Phần văn bản
        tk.Label(self.window, text="Văn bản", font=("Arial Bold", 14)).grid(column=0, row=2, padx=10, pady=5)
        self.text_entry = tk.Entry(self.window, width=85)
        self.text_entry.grid(column=1, row=2, padx=10, pady=5)

        # Nhóm radio buttons
        radio_group = tk.LabelFrame(self.window, text="Hàm băm", font=("Arial Bold", 12))
        radio_group.grid(column=1, row=3, padx=10, pady=10, sticky="ew")

        hash_options = [
            ("Hash MD5", 0),
            ("Hash SHA1", 1),
            ("Hash SHA256", 2),
            ("Hash SHA512", 3)
        ]

        for idx, (text, value) in enumerate(hash_options):
            tk.Radiobutton(
                radio_group,
                text=text,
                font=("Times New Roman", 11),
                variable=self.hashmode,
                value=value,
                command=self.hash_content
            ).grid(column=1, row=idx + 4, sticky="w", padx=5, pady=2)

        # Phần giá trị băm
        tk.Label(self.window, text="Giá trị băm", font=("Arial Bold", 14)).grid(column=0, row=8, padx=10, pady=5)
        self.hash_value_entry = tk.Entry(self.window, width=85)
        self.hash_value_entry.grid(column=1, row=8, padx=10, pady=5)

    def hash_content(self):
        """Thực hiện băm nội dung với hàm được chọn"""
        try:
            content = self.text_entry.get().strip()
            if not content:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản để băm!")
                return

            func = self.hashmode.get()
            if func == -1:
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn một hàm băm!")
                return

            hash_functions = [MD5, SHA1, SHA256, SHA512]
            result = hash_functions[func].new(content.encode()).hexdigest().upper()

            self.hash_value_entry.delete(0, tk.END)
            self.hash_value_entry.insert(0, result)

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    def run(self):
        """Chạy ứng dụng"""
        self.window.mainloop()


if __name__ == "__main__":
    app = HashingApp()
    app.run()