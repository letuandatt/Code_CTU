# Lê Tuấn Đạt
# B2113328
# 19

import base64
from Crypto.Cipher import DES


# Hàm pad để thêm padding cho văn bản
def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)


# Hàm unpad để loại bỏ padding sau khi giải mã
def unpad(s):
    return s[:-ord(s[len(s) - 1:])]


# Mã hóa DES
def mahoa_DES(text, key):
    text = pad(text).encode("utf-8")
    key = key.encode("utf-8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(text)
    return base64.b64encode(entxt).decode('utf-8')


# Giải mã DES
def giaima_DES(encoded_text, key):
    decoded_text = base64.b64decode(encoded_text)
    key = key.encode("utf-8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(decoded_text)).decode("utf-8")
    return detxt


# Đọc văn bản từ tệp tin
def doc_tap_tin(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Ghi văn bản ra tệp tin
def ghi_tap_tin(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    input_file = "vanbangoc.txt"
    original_text = doc_tap_tin(input_file)
    print(f"Văn bản gốc: {original_text}")

    # Nhận khóa từ người dùng
    key = input("Nhập khóa (8 ký tự): ")
    if len(key) != 8:
        print("Khóa phải dài đúng 8 ký tự!")
        exit(1)

    # Mã hóa
    encrypted_text = mahoa_DES(original_text, key)
    print(f"Văn bản sau khi mã hóa: {encrypted_text}")

    # Lưu văn bản đã mã hóa vào tệp tin
    output_encrypted_file = "vanbanmahoa.txt"
    ghi_tap_tin(output_encrypted_file, encrypted_text)
    print(f"Văn bản đã mã hóa được lưu tại: {output_encrypted_file}")

    # Giải mã
    encrypted_file_path = "vanbanmahoa.txt"
    encrypted_text_from_file = doc_tap_tin(encrypted_file_path)
    decrypted_text = giaima_DES(encrypted_text_from_file, key)
    print(f"Văn bản sau khi giải mã: {decrypted_text}")

    # Lưu văn bản sau khi giải mã vào tệp tin
    output_decrypted_file = "vanbangiaima.txt"
    ghi_tap_tin(output_decrypted_file, decrypted_text)
    print(f"Văn bản đã giải mã được lưu tại: {output_decrypted_file}")
