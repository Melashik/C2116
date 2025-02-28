import sqlite3
import requests
import time
from datetime import datetime

# Налаштування
CITY = "Kyiv"  # Замініть на ваше місто
API_KEY = "27470e1ccffa2496829a84244be969e0"  # Отримайте безкоштовний API-ключ на https://openweathermap.org/
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
DB_NAME = "weather.db"

# Функція створення БД
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_time TEXT,
            temperature REAL
        )
    """)
    conn.commit()
    conn.close()

# Функція отримання температури з OpenWeatherMap API
def get_temperature():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        return data["main"]["temp"]  # Температура в градусах Цельсія
    else:
        print("Помилка отримання температури:", response.text)
        return None

# Функція запису даних у БД
def save_temperature(temp):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (date_time, temperature) VALUES (?, ?)", 
                   (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp))
    conn.commit()
    conn.close()

# Основний цикл оновлення погоди
def update_weather():
    while True:
        temp = get_temperature()
        if temp is not None:
            save_temperature(temp)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Температура: {temp}°C записана в БД")
        else:
            print("Не вдалося отримати температуру.")

        time.sleep(1800)  # Оновлення кожні 30 хвилин

# Запуск програми
if __name__ == "__main__":
    create_database()
    update_weather()
