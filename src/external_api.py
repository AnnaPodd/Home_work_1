import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data"


def get_exchange_rate(currency):
    """Получает текущий курс валюты к рублю."""
    url = f"{BASE_URL}/convert?from={currency}&to=RUB&amount=1"
    headers = {
        "apikey": API_KEY
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('result')  # Возвращаем курс в рублях
    else:
        raise Exception("Ошибка при получении курса валют.")