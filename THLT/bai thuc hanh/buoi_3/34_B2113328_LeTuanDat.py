import re

# # 1. Phương thức findall()
### VD1
# string = 'Computer science 2020 and Software Engineering 2023'
# pattern = r'\d+'
# result = re.findall(pattern, string)
# print(result)
#
# ### VD2
# wood = 'How much wood would you woodchuck chuck if a woodchuck could chuck wood?'
# print(re.findall(r'wo\w+', wood))
#
# ### VD3
# print(re.findall(r'o+', wood))
# print(re.findall(r'e+', wood))
#
# foo = 'This and that and those'
# print(re.findall(r'th\w+', foo))
# print(re.findall(r'th\w+', foo, re.IGNORECASE))
#
# # 2. Phương thức re.sub()
# ### VD1
# string = 'Computer Science, Software Engineering'
# pattern = r'\s+'
# replace = '_'
# new_string = re.sub(pattern, replace, string)
# print(new_string)
#
# ### VD2
# string, pattern
# replace = ""
# new_string = re.sub(pattern, replace, string, 2)
# print(new_string)
#
# ### VD3
# wood
# print(re.sub(r'[aeiou]+', '-', wood))
#
# # 3. Phương thức re.search()
# ### VD1
# string = 'Computer science 2020 and Software Engineering 2023'
# pattern = r'\d+'
# result = re.search(pattern, string)
# print(result)
#
#
# ### VD2
# string = 'Colorless green ideas sleep furiously'
# result = re.search(r'e+', string)
# print(result)
#
# ### VD3
# string = 'Colorless green ideas sleep furiously'
# pattern = r're+'
# result = re.search(pattern, string)
# print(result)
#
# # 4. Phương thức re.split()
# ### VD1
# string = 'Computer science 2020 and Software Engineering 2023'
# pattern = r'\s'
# result = re.split(pattern, string)
# print(result)
#
# ### VD2
# string = 'Computer science 2020 and Software Engineering 2023'
# pattern = r'\s'
# result = re.split(pattern, string, 2)
# print(result)
#
# # 5. Phương thức re.compile()
# myre = re.compile(r"\w+ou\w+")
# print(myre.findall(wood))
# print(myre.findall('Colorless green ideas sleep furiously'))
# print(myre.findall('The thirty-three thieves thought that they thrilled'
#                    'the throne throughout Thursday.'))

# BT
## A
### 1.
def lines_start_with_t_or_h_and_contain_re(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            print(line)
            if re.search(r'^[h].*re', line):
                result.append(line)
    return result

### 2.
def string_min_length_20(lines):
    result = []
    result.append([line.strip() for line in lines if len(line.strip() >= 20)])
    return result

### 3.
def string_end_with_question_exclamation_mark(lines):
    result = []
    result.append([line.strip() for line in lines if re.search(r'!\?$', line.strip())])
    return result

### 4.
def string_contain_arsml(lines):
    result = []
    result.append([line.strip() for line in lines if re.search(r'[arsml]', line)])
    return result

### 5.
def string_with_no_comma_period(lines):
    result = []
    result.append([line.strip() for line in lines if not any(char in line for char in ',.')])
    return result

### 6.
def string_contain_mouse(lines):
    result = []
    for line in lines:
        if 'mouse' in line:
            result.append(line.strip())
    return result

### 7.
def string_contain_a_followed_by_b(lines):
    result = []
    for line in lines:
        words = line.split()
        for word in words:
            if re.search(r'a.*b', word):
                result.append(word.strip())
    return result

### 8.
def find_email_domains(lines):
    result = []
    for line in lines:
        domains = re.findall(r'@([^. ]+\.[^ ]+)', line.strip())
        for domain in domains:
            result.append(domain)
    return result

### 9.
print(lines_start_with_t_or_h_and_contain_re("data.txt"))