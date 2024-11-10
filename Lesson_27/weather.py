import requests
from datetime import datetime, timedelta

def get_weather_forecast(latitude, longitude, past_days=10):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "past_days": past_days,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return process_weather_data(data)
    else:
        return "Ошибка при получении данных о погоде"

def process_weather_data(data):
    hourly_data = data['hourly']
    current_time = datetime.utcnow()
    
    # Находим индекс текущего времени
    time_index = hourly_data['time'].index(current_time.strftime("%Y-%m-%dT%H:00"))
    
    current_temp = hourly_data['temperature_2m'][time_index]
    current_humidity = hourly_data['relative_humidity_2m'][time_index]
    current_wind_speed = hourly_data['wind_speed_10m'][time_index]
    
    forecast = f"Текущая погода в Минске:\n"
    forecast += f"Температура: {current_temp}°C\n"
    forecast += f"Относительная влажность: {current_humidity}%\n"
    forecast += f"Скорость ветра: {current_wind_speed} м/с\n\n"
    
    forecast += "Прогноз на ближайшие 24 часа:\n"
    for i in range(time_index + 1, time_index + 25):
        if i < len(hourly_data['time']):
            time = datetime.fromisoformat(hourly_data['time'][i])
            temp = hourly_data['temperature_2m'][i]
            humidity = hourly_data['relative_humidity_2m'][i]
            wind_speed = hourly_data['wind_speed_10m'][i]
            forecast += f"{time.strftime('%Y-%m-%d %H:00')}: {temp}°C, {humidity}%, {wind_speed} м/с\n"
    
    return forecast

# Координаты Минска
latitude = 53.9  # Широта Минска
longitude = 27.5667  # Долгота Минска

print(get_weather_forecast(latitude, longitude))