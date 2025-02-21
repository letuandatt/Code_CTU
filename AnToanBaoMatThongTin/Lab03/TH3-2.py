# Le Tuan Dat
# B2113328
# 19

import random
import time

# Kiểm tra số nguyên tố bằng thuật toán Miller-Rabin
def miller_rabin_test(n, k=40):  # k là số lần kiểm tra Miller-Rabin
    if n < 2:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False

    # Tách n-1 thành (2^r) * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Thử nghiệm k lần
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Sinh số nguyên tố lớn
def generate_large_prime(bits=512):
    while True:
        num = random.getrandbits(bits)
        if num % 2 == 0:
            num += 1  # Đảm bảo là số lẻ
        if miller_rabin_test(num):
            return num

# Kiểm tra USCLN
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Hàm nghịch đảo
def mod_inverse(e, phi):
    x0, x1, y0, y1 = 1, 0, 0, 1
    a0, b0 = e, phi
    while b0:
        q = a0 // b0
        a0, b0 = b0, a0 % b0
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if a0 != 1:
        return None
    return x0 % phi

# Sinh khóa RSA
def sinh_khoa(bits=512):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    while p == q:
        q = generate_large_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

# Mã hóa
def ma_hoa(public_key, message):
    (e, n) = public_key
    return [pow(ord(char), e, n) for char in message]

# Giải mã
def giai_ma(private_key, encrypted_message):
    (d, n) = private_key
    return ''.join(chr(pow(char, d, n)) for char in encrypted_message)

# main
if __name__ == '__main__':

    start_gen_key = time.time()
    pub_key, pri_key = sinh_khoa(1024)  # Sử dụng số nguyên tố 1024-bit
    end_gen_key = time.time()
    print(f"Public_key: {pub_key}")
    print(f"Private_key: {pri_key}")
    print(f"Gen time: {end_gen_key - start_gen_key}")

    # Bản rõ
    plaintext = "LeTuanDat B2113328 19"
    print(f"plaintext: {plaintext}")

    # Mã hóa
    start_encrypt_time = time.time()
    encrypted = ma_hoa(pub_key, plaintext)
    end_encrypt_time = time.time()
    print(f"Encrypted text: {encrypted}")
    print(f"Encrypted time: {end_encrypt_time - start_encrypt_time}")

    # Giải mã
    start_decrypt_time = time.time()
    decrypted = giai_ma(pri_key, encrypted)
    end_decrypt_time = time.time()
    print(f"Decrypted text: {decrypted}")
    print(f"Decrypted time: {end_decrypt_time - start_decrypt_time}")
