#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
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

# Список тестовых номеров
test_numbers=(
    "+375291234567"
    "375331234567"
    "8 (025) 123 45 67"
    "+375 44 123 45 67"
    "8029-123-45-67"
    "+7 495 123 45 67"
    "12345678"
)

for number in "${test_numbers[@]}"; do
    if validate_belarus_phone "$number"; then
        echo -e "${GREEN}$number - действительный белорусский номер${RESET}"
    else
        echo -e "${RED}$number - недействительный белорусский номер${RESET}"
    fi
done