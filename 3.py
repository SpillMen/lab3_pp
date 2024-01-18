import re

def extract_digits(input_string):
    digits = re.findall(r'\d', input_string)
    return digits

user_input = input("Введите строку: ")

result = extract_digits(user_input)
print("Цифры в строке:", result)
