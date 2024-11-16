#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
PURPLE='\033[0;35m'
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

    # Возвращаем результат
    if [ ${#errors[@]} -eq 0 ]; then
        echo -e "${GREEN}Пароль '$password' соответствует всем требованиям.${RESET}"
    else
        echo -e "${RED}Пароль '$password' не соответствует следующим требованиям:${RESET}"
        for error in "${errors[@]}"; do
            echo -e "${PURPLE}- $error${RESET}"
        done
    fi
    echo
}

# Список паролей для проверки
passwords=(
    "abcefABCEF123"
    "short"
    "nouppercase123"
    "NOLOWERCASE123"
    "NoDigits"
    "WithSpecialChar123!"
    "ValidPasswordYes123"
    "русскиеБуквы123"
)

# Проверка каждого пароля
for password in "${passwords[@]}"; do
    check_password "$password"
done