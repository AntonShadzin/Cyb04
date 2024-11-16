#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
RESET='\033[0m'



validate_belarus_phone() {
    local phone_number=$1
    # Удаляем все не-цифровые символы из номера
    cleaned_number=$(echo "$phone_number" | sed 's/[^0-9]//g')
    
    # Проверяем соответствие паттерну
    if [[ $cleaned_number =~ ^(375|80)(29|25|44|33)[0-9]{7}$ ]]; then
        return 0 # Действительный номер
    else
        return 1 # Недействительный номер
    fi
}

echo -e "${BLUE}Проверка белорусских телефонных номеров${RESET}\n"
echo -e "Для выхода введите ${RED}'exit'${RESET}"

while true; do
    echo
    read -p "Введите номер телефона для проверки: " phone_number
    
    if [[ ${phone_number,,} == "exit" ]]; then
        echo -e "${RED}Программа завершена.${RESET}"
        break
    fi
    
    if validate_belarus_phone "$phone_number"; then
        echo -e "${GREEN}$phone_number - действительный белорусский номер${RESET}"
    else
        echo -e "${RED}$phone_number - недействительный белорусский номер${RESET}"
    fi
    
    echo
    echo -e "${BLUE}Примеры правильного формата:${RESET}"
    echo -e "${BLUE}+375 29 123 45 67${RESET}"
    echo -e "${BLUE}80291234567${RESET}"
    echo -e "${BLUE}375 33 1234567${RESET}"
done