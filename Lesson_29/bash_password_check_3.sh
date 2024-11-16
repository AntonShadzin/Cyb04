#!/bin/bash

GREEN='\033[0;32m'
PURPLE='\033[0;35m'
RED='\033[0;31m'
BLUE='\033[0;34m'
RESET='\033[0m'


check_password() {
    local password=$1
    local errors=()

    # Проверка длины пароля
    if [[ ${#password} -lt 12 || ${#password} -gt 24 ]]; then
        errors+=("Длина пароля должна быть от 12 до 24 символов")
    fi

    # Проверка на наличие только английских букв, цифр и символов
    if [[ ! $password =~ ^[a-zA-Z0-9]+$ ]]; then
        errors+=("Пароль должен содержать только английские буквы и цифры")
    fi

    # Проверка на наличие хотя бы одной строчной буквы
    if [[ ! $password =~ [a-z] ]]; then
        errors+=("Пароль должен содержать хотя бы одну строчную букву")
    fi

    # Проверка на наличие хотя бы одной заглавной буквы
    if [[ ! $password =~ [A-Z] ]]; then
        errors+=("Пароль должен содержать хотя бы одну заглавную букву")
    fi

    # Проверка на наличие хотя бы одной цифры
    if [[ ! $password =~ [0-9] ]]; then
        errors+=("Пароль должен содержать хотя бы одну цифру")
    fi


    # Вывод ошибок
    if [ ${#errors[@]} -eq 0 ]; then
        echo -e "${GREEN}Пароль соответствует всем требованиям!${RESET}"
    else
        echo -e "${RED}Пароль не соответствует следующим требованиям:${RESET}\n"
        for error in "${errors[@]}"; do
            echo -e "${PURPLE}- $error${RESET}"
        done
    fi
}

echo -e "${BLUE}Программа проверки пароля${RESET}\n"
echo -e "${BLUE}Требования к паролю:\n${RESET}"
echo -e "${BLUE}- Длина от 12 до 24 символов${RESET}"
echo -e "${BLUE}- Только английские буквы, цифры и специальные символы${RESET}"
echo -e "${BLUE}- Минимум 1 строчная буква, 1 заглавная буква и 1 цифра${RESET}"
echo

while true; do
    read -p  "Введите пароль для проверки (или 'exit' для завершения): " password
    
    if [[ ${password,,} == "exit" ]]; then
        echo "${RED}Программа завершена.${RESET}"
        break
    fi

    check_password "$password"
    echo
done