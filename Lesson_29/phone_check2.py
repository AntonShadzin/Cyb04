import re

GREEN="\033[32m"
RED="\033[31m"
CYAN="\033[36m"
RESET="\033[0m"

def validate_belarus_phone(phone_number):
    # Паттерн для белорусских номеров
    pattern = r'^(\+375|375|80)(29|25|44|33)(\d{3})(\d{2})(\d{2})$'
    
    # Удаляем все не-цифровые символы из номера
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Проверяем соответствие паттерну
    match = re.match(pattern, cleaned_number)
    
    return bool(match)

def main():
    print(f"{CYAN}Проверка белорусских телефонных номеров{RESET}\n")
    print(f"Для выхода введите {RED}'exit'{RESET}")
    
    while True:
        phone_number = input("\nВведите номер телефона для проверки: ").strip()
        if phone_number.lower() in ['exit']:
            print(f"{RED}Программа завершена.{RESET}")
            break
        
        if validate_belarus_phone(phone_number):
            print(f"{GREEN}{phone_number} - действительный белорусский номер{RESET}")
        else:
            print(f"{RED}{phone_number} - недействительный белорусский номер{RESET}")
        
        print(f"\n{CYAN}Примеры правильного формата{RESET}")
        print(f"{CYAN}+375 29 123 45 67{RESET}")
        print(f"{CYAN}80291234567{RESET}")
        print(f"{CYAN}375 33 1234567{RESET}")

if __name__ == "__main__":
    main()