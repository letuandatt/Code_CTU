import math


def mod_inverse(a, m):  # nghịch đảo của a
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def Char2Num(c):
    if c == ' ':
        return 52  # Khoảng trắng
    if c.islower():
        return ord(c) - 97 + 26  # chữ cái thường a-z
    if c.isupper():
        return ord(c) - 65  # chữ cái hoa A-Z
    if c.isdigit():
        return ord(c) - 48 + 53  # số 0-9 (từ 53 đến 62)
    return None  # Nếu không phải ký tự hợp lệ


def Num2Char(n):
    if n == 52:
        return ' '  # Khoảng trắng
    if n == 53:
        return '0'
    if n == 54:
        return '1'
    if n == 55:
        return '2'
    if n == 56:
        return '3'
    if n == 57:
        return '4'
    if n == 58:
        return '5'
    if n == 59:
        return '6'
    if n == 60:
        return '7'
    if n == 61:
        return '8'
    if n == 62:
        return '9'
    if n >= 26:
        return chr(n - 26 + 97)  # Chữ cái thường
    return chr(n + 65)  # Chữ cái hoa


def decrypt_affine(ciphertext, a, b):
    m = 62
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None

    decrypted_text = ""
    for c in ciphertext:
        num = Char2Num(c)
        if num is None:  # Bỏ qua các ký tự không hợp lệ
            continue
        p = (a_inv * (num - b)) % m
        decrypted_text += Num2Char(p)

    return decrypted_text


valid_a_values = [a for a in range(1, 63) if math.gcd(a, 63) == 1]

cipher_text = "gAdX5d6IXpvBX3XawdSLHIXIAdXCTITwdXL6XIPXHwdvIdXLI"

for a in valid_a_values:
    for b in range(63):
        decrypted = decrypt_affine(cipher_text, a, b)
        if decrypted and "predict" in decrypted:
            decrypted = decrypted.replace('0', ' ')  # Thay '0' thành khoảng trắng
            print(f"🔹 Tìm thấy khóa! (a={a}, b={b})")
            print(f"Thông điệp: {decrypted}")
            exit()
