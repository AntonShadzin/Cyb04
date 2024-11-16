import re

GREEN="\033[32m"
PURPLE="\033[35m"
RED="\033[31m"
RESET="\033[0m"

def validate_belarus_phone(phone_number):
    # Паттерн для белорусских номеров
    pattern = r'^(\+375|375|80)(29|25|44|33)(\d{3})(\d{2})(\d{2})$'
    
    # Удаляем все не-цифровые символы из номера
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Проверяем соответствие паттерну
    match = re.match(pattern, cleaned_number)
    
    if match:
        return True
    else:
        return False

# Примеры использования
test_numbers = [
    '+375291234567',
    '375331234567',
    '80251234567',
    '+375 44 123 45 67',
    '8029-123-45-67',
    '+7 495 123 45 67',  # Российский номер
    '12345678'  # Неверный формат
]

for number in test_numbers:
    if validate_belarus_phone(number):
        print(f"{GREEN}{number} - действительный белорусский номер{RESET}")
    else:
        print(f"{RED}{number} - недействительный белорусский номер{RESET}")