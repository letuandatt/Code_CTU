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


print(encryptAF("HELLO", 3, 5, 26))
