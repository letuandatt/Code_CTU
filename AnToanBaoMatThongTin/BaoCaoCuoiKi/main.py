import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Import ttk for improved widgets
from PIL import Image, ImageTk
import numpy as np

# Bước 1: Chuyển đổi thông điệp thành dạng nhị phân với UTF-8
def text_to_binary(message):
    binary_message = ''.join(format(byte, '08b') for byte in message.encode('utf-8'))
    return binary_message

# Chuyển đổi nhị phân thành văn bản UTF-8
def binary_to_text(binary_message):
    byte_list = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    byte_array = bytearray(int(byte, 2) for byte in byte_list if len(byte) == 8)
    try:
        return byte_array.decode('utf-8')
    except UnicodeDecodeError:
        return "Lỗi giải mã thông điệp!"


# Bước 2: Thêm marker vào thông điệp
def add_marker(binary_message):
    marker = '1111111111111110'  # 16-bit marker
    return binary_message + marker

# Bước 3: Mã hóa thông điệp vào ảnh
def encode_image(image_path, message, output_image_path):
    # Chuyển đổi thông điệp thành nhị phân và thêm marker
    binary_message = text_to_binary(message)
    binary_message_with_marker = add_marker(binary_message)
    
    # Mở ảnh và chuyển đổi thành mảng numpy
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Biến đổi ảnh thành chuỗi bit (LSB của mỗi pixel)
    pixel_index = 0
    bit_index = 0
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # RGB channels
                if bit_index < len(binary_message_with_marker):
                    pixels[i, j, k] = (pixels[i, j, k] & 0xFE) | int(binary_message_with_marker[bit_index])
                    bit_index += 1

    # Lưu ảnh đã mã hóa
    encoded_image = Image.fromarray(pixels)
    encoded_image.save(output_image_path)

# Bước 4: Giải mã thông điệp từ ảnh
def decode_image(image_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    binary_message = "".join(str(pixels[i, j, k] & 1) for i in range(pixels.shape[0]) for j in range(pixels.shape[1]) for k in range(3))
    
    marker = '1111111111111110'
    message_end_index = binary_message.find(marker)

    if message_end_index == -1:
        return "Không tìm thấy thông điệp"

    binary_message = binary_message[:message_end_index]
    return binary_to_text(binary_message)

# Trang chủ điều hướng
class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Trang chủ Steganography")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')

        # Label trang chủ
        self.label = ttk.Label(root, text="Steganography: Mã hóa và Giải mã", font=("Arial", 18, 'bold'), background='#f0f0f0', foreground='#2C3E50')
        self.label.pack(pady=50)

        # Frame for buttons
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10)

        # Button để đi tới cửa sổ mã hóa
        self.encode_button = ttk.Button(self.button_frame, text="Mã hóa thông điệp", command=self.open_encode_window, style="Encode.TButton")
        self.encode_button.grid(row=0, column=0, padx=10)

        # Button để đi tới cửa sổ giải mã
        self.decode_button = ttk.Button(self.button_frame, text="Giải mã thông điệp", command=self.open_decode_window, style="Decode.TButton")
        self.decode_button.grid(row=0, column=1, padx=10)

        # Apply styles
        self.style = ttk.Style()
        self.style.configure("Encode.TButton", font=("Arial", 12), padding=10, background='#2980B9', foreground='black', relief="solid")
        self.style.configure("Decode.TButton", font=("Arial", 12), padding=10, background='#27AE60', foreground='black', relief="solid")

    def open_encode_window(self):
        self.root.destroy()
        self.new_root = tk.Tk()
        self.app = EncodeWindow(self.new_root)

    def open_decode_window(self):
        self.root.destroy()
        self.new_root = tk.Tk()
        self.app = DecodeWindow(self.new_root)

# Cửa sổ mã hóa
class EncodeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Mã hóa thông điệp")
        self.root.geometry("800x600")
        self.root.configure(bg='#ECF0F1')

        # Label cho hướng dẫn
        self.label = ttk.Label(root, text="Mã hóa thông điệp vào ảnh", font=("Arial", 16, 'bold'), background='#ECF0F1', foreground='#2C3E50')
        self.label.pack(pady=20)

        # Textbox để nhập thông điệp
        self.message_label = ttk.Label(root, text="Thông điệp cần giấu:", font=("Arial", 12), background='#ECF0F1', foreground='#2C3E50')
        self.message_label.pack(pady=5)

        self.message_entry = ttk.Entry(root, width=50, font=("Arial", 12))
        self.message_entry.pack(pady=10)

        # Frame for buttons
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10)

        # Button chọn ảnh đầu vào
        self.choose_image_button = ttk.Button(self.button_frame, text="Chọn ảnh đầu vào", command=self.choose_input_image, style="Input.TButton")
        self.choose_image_button.grid(row=0, column=0, padx=10)

        # Button chọn ảnh đầu ra
        self.choose_output_button = ttk.Button(self.button_frame, text="Chọn địa chỉ lưu ảnh", command=self.choose_output_image, style="Output.TButton")
        self.choose_output_button.grid(row=0, column=1, padx=10)

        self.output_path_label = ttk.Label(root, text="Đường dẫn ảnh mã hóa:", font=("Arial", 12), background='#ECF0F1', foreground='#2C3E50')
        self.output_path_label.pack(pady=5)

        self.output_path_display = ttk.Label(root, text="", font=("Arial", 10), background='#ECF0F1', foreground='blue')
        self.output_path_display.pack(pady=5)


        # Button để mã hóa
        self.encode_button = ttk.Button(self.button_frame, text="Mã hóa thông điệp", command=self.encode_message, style="Encode.TButton")
        self.encode_button.grid(row=0, column=2, padx=10)

        # Button trở về trang chủ
        self.back_button = ttk.Button(self.button_frame, text="Trở về trang chủ", command=self.back_to_main, style="Back.TButton")
        self.back_button.grid(row=0, column=3, padx=10)

        # Frame để chứa ảnh gốc và ảnh mã hóa
        self.image_frame = ttk.Frame(root)
        self.image_frame.pack(pady=20)

        # Hiển thị ảnh gốc
        self.input_image_label = ttk.Label(self.image_frame, text="Ảnh gốc:", font=("Arial", 12), background='#ECF0F1', foreground='#2C3E50')
        self.input_image_label.grid(row=0, column=0, padx=10)

        self.input_image_display = ttk.Label(self.image_frame)
        self.input_image_display.grid(row=1, column=0, padx=10)

        # Hiển thị ảnh mã hóa
        self.encoded_image_label = ttk.Label(self.image_frame, text="Ảnh mã hóa:", font=("Arial", 12), background='#ECF0F1', foreground='#2C3E50')
        self.encoded_image_label.grid(row=0, column=1, padx=10)

        self.encoded_image_display = ttk.Label(self.image_frame)
        self.encoded_image_display.grid(row=1, column=1, padx=10)

        # Variables để lưu đường dẫn ảnh
        self.input_image_path = ""
        self.output_image_path = ""

        # Apply styles
        self.style = ttk.Style()
        self.style.configure("Input.TButton", font=("Arial", 12), padding=10, background='#3498DB', foreground='black', relief="solid")
        self.style.configure("Output.TButton", font=("Arial", 12), padding=10, background='#E67E22', foreground='black', relief="solid")
        self.style.configure("Encode.TButton", font=("Arial", 12), padding=10, background='#2980B9', foreground='black', relief="solid")
        self.style.configure("Back.TButton", font=("Arial", 12), padding=10, background='#E74C3C', foreground='black', relief="solid")

    # Chọn ảnh đầu vào
    def choose_input_image(self):
        self.input_image_path = filedialog.askopenfilename(title="Chọn ảnh đầu vào", filetypes=[("Image files", "*.png;*.bmp;*.jpg")])
        if self.input_image_path:
            self.display_input_image()

    # Cập nhật khi người dùng chọn nơi lưu
    def choose_output_image(self):
        self.output_image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("BMP files", "*.bmp")])
        if self.output_image_path:
            self.output_path_display.config(text=self.output_image_path)

    # Mã hóa thông điệp
    def encode_message(self):
        message = self.message_entry.get()
        if not message or not self.input_image_path or not self.output_image_path:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin (thông điệp và ảnh)")
            return
        encode_image(self.input_image_path, message, self.output_image_path)
        messagebox.showinfo("Thành công", "Thông điệp đã được mã hóa vào ảnh!")
        self.display_encoded_image()

    # Hiển thị ảnh gốc
    def display_input_image(self):
        img = Image.open(self.input_image_path)
        img.thumbnail((250, 250))  # Resize ảnh cho vừa với giao diện
        img_tk = ImageTk.PhotoImage(img)
        self.input_image_display.config(image=img_tk)
        self.input_image_display.image = img_tk

    # Hiển thị ảnh mã hóa
    def display_encoded_image(self):
        img = Image.open(self.output_image_path)
        img.thumbnail((250, 250))  # Resize ảnh cho vừa với giao diện
        img_tk = ImageTk.PhotoImage(img)
        self.encoded_image_display.config(image=img_tk)
        self.encoded_image_display.image = img_tk

    # Trở về trang chủ
    def back_to_main(self):
        self.root.destroy()
        self.new_root = tk.Tk()
        self.app = MainPage(self.new_root)

# Cửa sổ giải mã
class DecodeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Giải mã thông điệp")
        self.root.geometry("800x600")
        self.root.configure(bg='#ECF0F1')

        # Label cho hướng dẫn
        self.label = ttk.Label(root, text="Giải mã thông điệp từ ảnh", font=("Arial", 16, 'bold'), background='#ECF0F1', foreground='#2C3E50')
        self.label.pack(pady=20)

        # Frame for buttons
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10)

        # Button chọn ảnh đầu vào
        self.choose_image_button = ttk.Button(self.button_frame, text="Chọn ảnh đầu vào", command=self.choose_input_image, style="Input.TButton")
        self.choose_image_button.grid(row=0, column=0, padx=10)

        # Button giải mã
        self.decode_button = ttk.Button(self.button_frame, text="Giải mã thông điệp", command=self.decode_message, style="Decode.TButton")
        self.decode_button.grid(row=0, column=1, padx=10)

        # Button trở về trang chủ
        self.back_button = ttk.Button(self.button_frame, text="Trở về trang chủ", command=self.back_to_main, style="Back.TButton")
        self.back_button.grid(row=0, column=2, padx=10)

        # Hiển thị ảnh đã chọn
        self.input_image_label = ttk.Label(root, text="Ảnh đã chọn:", font=("Arial", 12), background='#ECF0F1', foreground='#2C3E50')
        self.input_image_label.pack(pady=5)
        
        self.input_image_display = ttk.Label(root)
        self.input_image_display.pack(pady=10)

        # Output giải mã
        # Frame chứa Text widget và Scrollbar
        self.output_frame = ttk.Frame(root)
        self.output_frame.pack(pady=10, fill="both", expand=True)

        # Widget Text để hiển thị thông điệp giải mã
        self.output_text = tk.Text(self.output_frame, font=("Arial", 12), wrap="word", height=10, width=60)
        self.output_text.pack(side="left", fill="both", expand=True)

        # Scrollbar cho Text widget
        self.scrollbar = ttk.Scrollbar(self.output_frame, orient="vertical", command=self.output_text.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.output_text.config(yscrollcommand=self.scrollbar.set)


        # Variables để lưu đường dẫn ảnh
        self.input_image_path = ""

        # Apply styles
        self.style = ttk.Style()
        self.style.configure("Input.TButton", font=("Arial", 12), padding=10, background='#3498DB', foreground='black', relief="solid")
        self.style.configure("Decode.TButton", font=("Arial", 12), padding=10, background='#27AE60', foreground='black', relief="solid")
        self.style.configure("Back.TButton", font=("Arial", 12), padding=10, background='#E74C3C', foreground='black', relief="solid")

    # Chọn ảnh đầu vào
    def choose_input_image(self):
        self.input_image_path = filedialog.askopenfilename(title="Chọn ảnh đầu vào", filetypes=[("Image files", "*.png;*.bmp;*.jpg")])
        if self.input_image_path:
            self.display_input_image()

    # Giải mã thông điệp
    def decode_message(self):
        if not self.input_image_path:
            messagebox.showerror("Lỗi", "Vui lòng chọn ảnh đầu vào")
            return
        decoded_message = decode_image(self.input_image_path)
        if decoded_message:
            self.output_text.delete("1.0", tk.END)  # Xóa nội dung cũ
            self.output_text.insert(tk.END, decoded_message)  # Hiển thị thông điệp mới

        else:
            self.output_label.config(text="Không tìm thấy thông điệp")

    # Hiển thị ảnh đầu vào
    def display_input_image(self):
        img = Image.open(self.input_image_path)
        img.thumbnail((250, 250))  # Resize ảnh cho vừa với giao diện
        img_tk = ImageTk.PhotoImage(img)
        self.input_image_display.config(image=img_tk)
        self.input_image_display.image = img_tk

    # Trở về trang chủ
    def back_to_main(self):
        self.root.destroy()
        self.new_root = tk.Tk()
        self.app = MainPage(self.new_root)

# Main loop để chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = MainPage(root)
    root.mainloop()
