import math


def mod_inverse(a, m):  # nghịch đảo của a
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def Char2Num(c):
    return ord(c) - 65


def Num2Char(n):
    return chr(n + 65)


def decrypt_affine(ciphertext, a, b):
    m = 26
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None

    decrypted_text = ""
    for c in ciphertext:
        p = (a_inv * (Char2Num(c) - b)) % m
        decrypted_text += Num2Char(p)

    return decrypted_text


valid_a_values = {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

cipher_text = "LOLYLTQOLTHDZTDC"

for a in valid_a_values:
    for b in range(26):
        decrypted = decrypt_affine(cipher_text, a, b)
        if decrypted and "LAMUOI" in decrypted:
            print(f"🔹 Tìm thấy khóa! (a={a}, b={b})")
            print(f"Thông điệp: {decrypted}")
            exit()

