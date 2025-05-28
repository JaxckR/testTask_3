import requests
import json

from django.core.cache import cache

from config.settings import WEATHER_API_KEY, BASE_URL

months = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}


def parse_current_weather(data: dict, city: str) -> dict:
    '''Функция для получения погоды на данный момент. Не кешируемая

    Обязательные аргументы
        - data, type: dict - сырые необработанные данные с запроса api
        - city, type: str - Город поиска
    '''
    location = data.get('location')
    data = data.get('current')
    if data is None or location is None:
        return {
            "error": f"We haven't been able to find the city {city}"
        }
    data_condition = data.get('condition')
    result = {
        "city": location.get("name"),
        "icon": data_condition.get('icon'),
        "text": data_condition.get('text').lower(),
        "temp": data.get("temp_c"),
    }
    return result


def get_current_weather(city: str) -> dict:
    '''Функция для получения погоды на данный момент. Кешируемая

    Обязательный аргумент - city, type: str
    Возвращает словарь с ключами:
            - city,
            - icon,
            - text,
            - temp
    '''

    cached_result = cache.get(f"{city}_current")
    if cached_result is not None:
        return cached_result

    req = requests.get(f"{BASE_URL}/current.json?q={city}&key={WEATHER_API_KEY}")
    req_result = json.loads(req.text)

    result = parse_current_weather(req_result, city)

    cache.set(f"{city}_current", result, timeout=60 * 60 * 2)
    return result


def get_current_forecast_weather(city: str) -> dict:
    '''Функция для получения погоды на 7 дней. Кешируемая

    Обязательный аргумент - city, type: str
    Возвращает словарь с ключами:
            - current, type: dict с ключами city, icon, text, temp
            - forecast, type: dict с ключом day и значением dict с ключами: text, icon, mintemp, maxtemp
    '''
    cached_result = cache.get(f"{city}_forecast")
    if cached_result is not None:
        return cached_result

    req = requests.get(f"{BASE_URL}/forecast.json?q={city}&days=7&key={WEATHER_API_KEY}")
    req_result = json.loads(req.text)

    result = {
        "current": {
            **parse_current_weather(req_result, city)
        },
        "forecast": {}
    }
    if req_result.get('forecast') is None:
        return {
            "error": f"We haven't been able to find the city {city}"
        }
    for i in req_result['forecast']["forecastday"]:
        day_info = i['day']
        month = months[i["date"][-5:-3]]
        day = f"{i['date'][-2:]} {month}" if i["date"][-2] != '0' else f"{i['date'][-1]} {month}"
        result["forecast"][day] = {
            "text": day_info["condition"]["text"],
            "icon": day_info["condition"]["icon"],
            "mintemp": day_info['mintemp_c'],
            "maxtemp": day_info['maxtemp_c'],
        }

    cache.set(f"{city}_forecast", result, timeout=60 * 60 * 2)
    return result
