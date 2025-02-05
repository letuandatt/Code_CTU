def char2num(c):
    return ord(c) - 65

def num2char(n):
    return chr(n + 65)

def encryptAF(txt, a, b, m):
    r = ""
    for c in txt:
        e = (a * char2num(c) + b) % m
        r += num2char(e)
    return r

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0:
        x0 += temp
    return x0

def decryptAF(txt, a, b, m):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        e = (a1 * (char2num(c) - b)) % m
        r += num2char(e)
    return r


erc = encryptAF("HELLO", 3, 5, 26)
print(erc)
print(decryptAF(erc, 3, 5, 26))
