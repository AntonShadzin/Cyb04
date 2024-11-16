import re
import dns.resolver
import socket

GREEN="\033[32m"
RED="\033[31m"
CYAN="\033[36m"
RESET="\033[0m"



def validate_email(email):
    # Базовый паттерн для проверки email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        return False, "Некорректный формат email-адреса"
    
    # Проверка длины email
    if len(email) > 254:
        return False, "Email слишком длинный"
    
    # Проверка длины локальной части (до @)
    local_part = email.split('@')[0]
    if len(local_part) > 64:
        return False, "Локальная часть email слишком длинная"
    
    # Проверка на наличие последовательных точек
    if '..' in email:
        return False, "Email содержит последовательные точки"
    
    # Проверка домена
    domain = email.split('@')[1]
    try:
        # Проверка MX-записи домена
        mx_records = dns.resolver.resolve(domain, 'MX')
        if not mx_records:
            return False, "Домен не имеет MX-записей"
        
        # Проверка A-записи домена
        socket.gethostbyname(domain)
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, socket.gaierror):
        return False, "Домен не существует или недоступен"
    
    return True, "Email-адрес корректен"

def main():
    print(f"{CYAN}Проверка email-адресов{RESET}\n")
    print(f"Для выхода введите {RED}'exit'{RESET}")
    
    while True:
        email = input("\nВведите email для проверки: ").strip()
        
        if email.lower() in ['exit']:
            print(f"{RED}Программа завершена.{RESET}")
            break
        
        is_valid, message = validate_email(email)
        if is_valid:
            print(f"{email} - {GREEN}{message}{RESET}")
        else:
            print(f"{email} - {RED}некорректный email-адрес: {CYAN}{message}{RESET}")
        
        print(f"{CYAN}\nПримеры правильного формата:{RESET}")
        print(f"{CYAN}user@example.com{RESET}")
        print(f"{CYAN}name.surname@domain.co.uk{RESET}")

if __name__ == "__main__":
    main()