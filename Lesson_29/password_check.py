import re

GREEN="\033[32m"
PURPLE="\033[35m"
RED="\033[31m"
RESET="\033[0m"




def check_password(password):
    errors = []

    # Проверка длины пароля
    if not 12 <= len(password) <= 24:
        errors.append("Длина пароля должна быть от 12 до 24 символов")
    
    # Проверка на наличие только английских букв, цифр и символов
    if not re.match(r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:\'",.<>?]+$', password):
        errors.append("Пароль должен содержать только английские буквы, цифры и специальные символы")
    
    # Проверка на наличие хотя бы одной строчной буквы
    if not re.search(r'[a-z]', password):
        errors.append("Пароль должен содержать хотя бы одну строчную букву")
    
    # Проверка на наличие хотя бы одной заглавной буквы
    if not re.search(r'[A-Z]', password):
        errors.append("Пароль должен содержать хотя бы одну заглавную букву")
    
    # Проверка на наличие хотя бы одной цифры
    if not re.search(r'\d', password):
        errors.append("Пароль должен содержать хотя бы одну цифру")
    
    # Проверка на наличие хотя бы одного специального символа
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?]', password):
        errors.append("Пароль должен содержать хотя бы один специальный символ")
    
    return errors

# Пример использования
passwords = [
    "abcABC123!@#",  # Правильный пароль
    "short",         # Слишком короткий
    "nouppercase123!",  # Нет заглавной буквы
    "NOLOWERCASE123!",  # Нет строчной буквы
    "NoDigits!@#",   # Нет цифры
    "NoSpecialChar123",  # Нет специального символа
    "ValidPassword123!",  # Правильный пароль
    "русскиеБуквы123!", # Содержит не английские буквы
]

for password in passwords:
    errors = check_password(password)
    if not errors:
        print(f"{GREEN}Пароль '{password}' соответствует всем требованиям.{RESET}")
    else:
        print(f"{RED}Пароль '{password}' не соответствует следующим требованиям:{RESET}")
        for error in errors:
            print(f"{PURPLE}- {error}{RESET}")
    print()  # Пустая строка для разделения результатов