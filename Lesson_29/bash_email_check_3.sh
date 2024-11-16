#!/bin/bash

GREEN='\033[0;32m'
CYAN='\033[0;36m' 
RED='\033[0;31m'
PURPLE='\033[0;35m'
RESET='\033[0m'


validate_email() {
    local email="$1"
    
    # Базовая проверка формата email
    if ! echo "$email" | grep -E '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' >/dev/null 2>&1; then
        echo "Некорректный формат email-адреса"
        return 1
    fi
    
    # Проверка длины email
    if [ ${#email} -gt 254 ]; then
        echo "Email слишком длинный"
        return 1
    fi
    
    # Проверка длины локальной части
    local local_part="${email%%@*}"
    if [ ${#local_part} -gt 64 ]; then
        echo "Локальная часть email слишком длинная"
        return 1
    fi
    
    # Проверка на последовательные точки
    if echo "$email" | grep -E '\.\.' >/dev/null 2>&1; then
        echo "Email содержит последовательные точки"
        return 1
    fi
    
    # Проверка домена
    local domain="${email#*@}"
    
    # Проверка MX-записи
    if ! dig +short MX "$domain" | grep -E '^[0-9]+ [a-zA-Z0-9.-]+\.$' >/dev/null 2>&1; then
        echo "Домен не имеет действительных MX-записей"
        return 1
    fi
    
    # Проверка A-записи
    if ! dig +short A "$domain" | grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$' >/dev/null 2>&1; then
        echo "Домен не имеет действительных A-записей"
        return 1
    fi
    
    echo "Email-адрес корректен"
    return 0
}

main() {
    echo -e "${CYAN}Проверка email-адресов${RESET}\n"
    echo -e "${CYAN}Для выхода введите ${RED}'exit'${RESET}"
    
    while true; do
        echo
        read -p "Введите email для проверки: " email
        
        if [[ "${email,,}" == "exit" ]]; then
            echo -e "${RED}Программа завершена.${RESET}"
            break
        fi
        
        result=$(validate_email "$email")
        status=$?
        
        if [ $status -eq 0 ]; then
            echo -e "${GREEN}$email - $result${RESET}"
        else
            echo -e "$email ${RED}- некорректный email-адрес: ${PURPLE}$result${RESET}"
        fi
        
        echo
        echo -e "${CYAN}Примеры правильного формата:${RESET}"
        echo -e "${CYAN}user@example.com${RESET}"
        echo -e "${CYAN}name.surname@domain.co.uk${RESET}"
    done
}

main