import requests
from datetime import datetime, timezone
import sys

# ANSI-коды для цветов
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

def get_weather_forecast(latitude, longitude, past_days=10):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "past_days": past_days,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Вызовет исключение для неуспешных статус-кодов
    except requests.RequestException as e:
        print(f"{RED}Ошибка: Сервер недоступен.{RESET}")
        sys.exit(1)  # Завершаем выполнение скрипта с кодом ошибки

    data = response.json()
    return process_weather_data(data)

def process_weather_data(data):
    hourly_data = data['hourly']
    current_time = datetime.now(timezone.utc)
    
    time_index = hourly_data['time'].index(current_time.strftime("%Y-%m-%dT%H:00"))
    
    current_temp = hourly_data['temperature_2m'][time_index]
    current_humidity = hourly_data['relative_humidity_2m'][time_index]
    current_wind_speed = hourly_data['wind_speed_10m'][time_index]
    
    forecast = f"{BLUE}Текущая погода в Минске:{RESET}\n\n"
    forecast += f"{BLUE}Температура: {GREEN}{current_temp}°C{RESET}\n"
    forecast += f"{BLUE}Относительная влажность: {GREEN}{current_humidity}%{RESET}\n"
    forecast += f"{BLUE}Скорость ветра: {GREEN}{current_wind_speed} м/с{RESET}\n\n"
    
    forecast += f"{BLUE}Прогноз на ближайшие 24 часа:{RESET}\n"
    for i in range(time_index + 1, time_index + 25):
        if i < len(hourly_data['time']):
            time = datetime.fromisoformat(hourly_data['time'][i])
            temp = hourly_data['temperature_2m'][i]
            humidity = hourly_data['relative_humidity_2m'][i]
            wind_speed = hourly_data['wind_speed_10m'][i]
            forecast += f"{time.strftime('%Y-%m-%d %H:00')}: {GREEN}{temp}°C, {humidity}%, {wind_speed} м/с{RESET}\n"
    
    return forecast

# Координаты Минска
latitude = 53.9
longitude = 27.5667

try:
    print(get_weather_forecast(latitude, longitude))
except Exception as e:
    print(f"{RED}Произошла непредвиденная ошибка: {e}{RESET}")
    sys.exit(1)