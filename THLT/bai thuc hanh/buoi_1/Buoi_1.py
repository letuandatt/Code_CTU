# Ví dụ chuỗi:
# mystring = "Le Tuan Dat"
# print(len(mystring))
# print(mystring[0])
# print(mystring[-1])
# print(mystring[-2])
# print(mystring[3:8])
# print(mystring[:8])
# print(mystring[8:])
# print(mystring[::-1])
# print(mystring[::2])
# print(mystring[::-2])
# print(mystring + " B2113328")

# Ví dụ toán tử
# x = 10
# y = 4
# print(x & y)
# print(x | y)
# print(~x)
# print(x ^ y)
# print(x >> 2)
# print(y << 2)
# print(x is y)
# print(x is not y)

# Danh sách
# a = [1, 2, 3, 'India', 'Fedora']
# print(a)
# print(a[0])
# print(a[4])
# print(len(a))
# print('India' in a)
#
# for e in a:
#     print(e)
#
# L = a.copy()
#
# L.insert(3, 4)
# L.append("Linux")
# print(L.count(2))
#
# del L[1]
# print(L)
#
# L.remove(1)
# print(L)
#
# L.clear()
# print(L)
#
# L1 = [8, 5, 2, 7, 9, 1]
# print(sorted(L1, reverse=True))
#
# mynum = list(range(10))
# print(mynum)
# print([num for num in mynum if num % 2 != 0])
# print([num for num in mynum if num % 2 == 0])

# Tuple
# data = ("Tom", "England", "Python")
#
# name, country, language = data
# print(name, country, language, sep="\n")
# print(data.count("Ton"))
# print(data.count("Tom"))
# print(data.index("Python"))
#
# data += (1,)
# print(data)
#
# data += ("abc",)
# print(data)

# Set
# set1 = {"Py", 1, 2, 3, 4}
# print(set1)
#
# set2 = set(("C++", "4, 6, 8"))
# print(set2)
#
# set3 = set([4, 1, 2, 3, 1, 2, 3, 4])
# print(set3)
#
# a = set('abcthabcjwethddda')
# print(a)
# print(len(a))
#
# b = a.copy()
# for i in b:
#     print(i)
#
# b.add(3)
# print(b)
#
# b.update([1, 2], {4, 5, 7, 1})
# print(b)
#
# b.discard(1)
# print(b)
#
# b.discard("Java")
# print(b)
#
# b.remove(2)
# print(b)
#
# c = b.copy()
# d = set(b)
# del b
#
# pt = a.pop()
# print(pt)
#
# a = {1, 2, 3, 4}
# b = {2, 4, 6, 8, 10}
#
# c = a.union(b)
# d = a.intersection(b)
# e = a.difference(b)
# print(a.issubset(b))

# Dictionary
# data = {
#     'Kushal': 'Fedora',
#     'kart_': 'Debian',
#     'Jace': 'Mac'
# }
# print(data)
# print(data['kart_'])
# print('Jace' in data)
#
# print(dict((('Indian', 'Delhi'), ("Bangladesh", "Dhaka"))))
#
# for x, y in data.items():
#     print(f"{x} uses {y}")
#
# d = {0: 10, 1: 20}
# print(d)
#
# d.update({2: 30})
# print(d)
#
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = {}
#
# for d in (dic1, dic2, dic3):
#     dic4.update(d)
# print(dic4)
#
# def is_key_present(x, d):
#     if x in d:
#         print("Key is present in the dictionary")
#     else:
#         print("Key is not present in the dictionary")
#
# is_key_present(5, dic4)
# is_key_present(7, dic4)
#
# mydic = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4
# }
# print(mydic)
#
# if 'a' in mydic:
#     del mydic['a']
# print(mydic)
#
# keyys = ['red', 'green', 'blue']
# values = ['#FF0000', '#008000', '#0000FF']
# color_dict = dict(zip(keyys, values))
# print(color_dict)

# Remove duplicate elements in the dictionary
# dic = {
#     1: 10,
#     2: 20,
#     4: 40,
#     3: 30,
#     4: 40,
#     1: 10,
#     5: 50,
#     6: 60,
#     4: 40
# }
#
# dic2 = {}
#
# for i, j in dic.items():
#     if (i, j) not in dic2:
#         dic2[i] = j
#
# print(sorted(dic2))

# Viết hàm
# def tingtong(a, b):
#     return a + b
#
# print(tingtong(1, 2))

# Lớp
# class Student:
#     def __init__(self, name, branch, year):
#         self.name = name
#         self.brance = branch
#         self.year = year
#         print("A student is created!")
#
#     def printStudent(self):
#         print(f"Name: {self.name}, Branch: {self.brance}, Year: {self.year}")
#
# student = Student("Le Tuan Dat", "CSE", '2025')
# student.printStudent()

# 1.
# def swap_combine_string(string1, string2):
#     new_str1 = string2[:2] + string1[2:]
#     new_str2 = string1[:2] + string2[2:]
#     return new_str1 + ' ' + new_str2
#
# print(swap_combine_string('asdv', 'fasd'))

# 2.
# def remove_even_chars(s):
#     s_new = ""
#     for i in range(len(s)):
#         if i % 2 != 0:
#             s_new += s[i]
#     return s_new
#
# s_2 = input("Nhập chuỗi: ")
# print(remove_even_chars(s_2))

# 3.
# def count_char(s):
#     char_count = {}
#
#     for c in s.split():
#         if c in char_count:
#             char_count[c] += 1
#         else:
#             char_count[c] = 1
#
#     return char_count
#
# s_3 = input("Nhập chuỗi: ")
# print(count_char(s_3))

# 4.
# def encode_string(s):
#     s_new = ''
#     for c in s:
#         if c.isalpha():
#             c_new = chr((ord(c) - 3 - ord('a')) % 26 + ord('a'))
#             s_new += c_new
#         else:
#             s_new += c
#     return s_new
#
# s_4 = input("Nhập chuỗi: ")
# print(encode_string(s_4))

# 5.
# def valid_string(S: set, s: str) -> bool:
#     for c in s:
#         if c not in S:
#             return False
#     return True
#
#
# S = set()
#
# while True:
#     c = input("Nhập kí tự của bộ chữ cái: ")
#     S.add(c)
#     choice = input("Nhấn 'q' để kết thúc: ")
#     if choice == 'Q' or choice == 'q':
#         break
#
# s = input("Nhập chuỗi cần kiểm tra: ")
# print(valid_string(S, s))

# 6.
# a = input("Nhập chuỗi: ")
# print(a.split())

# 7.
# def char_first_not_repeating(s):
#     char_count = {}
#
#     for c in s:
#         if c in char_count:
#             char_count[c] += 1
#         else:
#             char_count[c] = 1
#
#     for c in s:
#         if char_count[c] == 1:
#             return c
#
#     return None
#
# s = input("Nhập chuỗi: ")
# print(char_first_not_repeating(s))

# 8.
# def remove_space(s):
#     s_new = ""
#
#     for c in s:
#         if c == " ":
#             continue
#         s_new += c
#
#     return s_new
#
# s_8 = input("Nhập chuỗi: ")
# print(remove_space(s_8))

# 9.
# def print_first_duplicate(s):
#     words = set()
#
#     for word in s.split():
#         if word in words:
#             return word
#         else:
#             words.add(word)
#
#     return None
#
# s_9 = input("Nhập chuỗi: ")
# print(print_first_duplicate(s_9))

# 10.
# def max_length_of_zero_substring(s):
#     max_length = 0
#     current_length = 0
#
#     for i in s:
#         if i == '0':
#             current_length += 1
#             max_length = max(max_length, current_length)
#         else:
#             current_length = 0
#
#     return max_length
#
# s_10 = input("Nhập chuỗi: ")
# print(max_length_of_zero_substring(s_10))

# BT Nang cao 1
from itertools import *

def can_generate_same_sequence(list_A, list_B):
    pass

print(can_generate_same_sequence(["110", "0011", "0110"], ["110110", "00", "110"]))
print(can_generate_same_sequence(["0011", "11", "1101"], ["101", "011", "110"]))
print(can_generate_same_sequence(["100", "0", "1"], ["1", "101", "0"]))

# BT Nang cao 2
# def is_valid_gen(s) -> str:
#     if len(s) != 9:
#         return "Không hợp lệ"
#     if s[:3] == 'ATG' and s[-3:] in ('TAA', 'TAG', 'TGA'):
#         middle = set(s[3:-3])
#         if len(middle) == 3:
#             return "Hợp lệ"
#     return "Không hợp lệ"
#
# print(is_valid_gen('ATGCCCTAG'))
# print(is_valid_gen('ATGCGTTGA'))