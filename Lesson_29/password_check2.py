import re




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

def main():

    GREEN="\033[32m"
    PURPLE="\033[35m"
    RED="\033[31m"
    BLUE="\033[34m"
    RESET="\033[0m"

    print(f"{BLUE}Программа проверки пароля{RESET}\n\n")
    print(f"{BLUE}Требования к паролю:{RESET}\n")
    print(f"{BLUE}- Длина от 12 до 24 символов{RESET}")
    print(f"{BLUE}- Только английские буквы, цифры и специальные символы{RESET}")
    print(f"{BLUE}- Минимум 1 строчная буква, 1 заглавная буква, 1 цифра и 1 специальный символ{RESET}\n\n")


    while True:
        password = input(f"Введите пароль для проверки (или {RED}'exit'{RESET} для завершения): ")
        
        if password.lower() == 'exit':
            print(f"{RED}Программа завершена.{RESET}")
            break

        errors = check_password(password)
        
        if not errors:
            print(f"{GREEN}Пароль соответствует всем требованиям!{RESET}")
        else:
            print(f"{RED}Пароль не соответствует следующим требованиям:{RESET}")
            for error in errors:
                print(f"{PURPLE}- {error}{RESET}")
        
        print()  # Пустая строка для разделения результатов

if __name__ == "__main__":
    main()