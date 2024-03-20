
import requests
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Функція для отримання поточної ціни криптовалюти
def get_crypto_price(crypto_symbol):
    # Створення URL запиту до API
    api_url = f'https://api.coinbase.com/v2/prices/{crypto_symbol}-USD/spot'
    try:
        # Виконання HTTP GET запиту до API
        response = requests.get(api_url)

        # Перевірка статусу відповіді
        response.raise_for_status()

        # Парсинг отриманої відповіді у форматі JSON
        data = response.json()

        # Перевірка наявності необхідних даних у відповіді
        if 'data' in data and 'amount' in data['data']:
            price = data['data']['amount']
            # Отримання поточної дати та часу
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Відображення ціни та часу останнього оновлення у віджеті
            result_label.config(text=f'Поточний курс {crypto_symbol}: ${price}\nОновлено: {now}')
        else:
            # Відображення повідомлення про помилку, якщо дані відсутні
            result_label.config(text='Хибний формат відповіді від API')
    except requests.exceptions.RequestException as e:
        # Обробка винятків при виконанні HTTP запиту
        result_label.config(text=f'Помилка запиту: {e}')

# Функція, яка викликається при виборі криптовалюти
def on_crypto_selected(event):
    # Отримання вибраної криптовалюти
    selected_crypto = crypto_combobox.get()
    # Виклик функції для отримання ціни вибраної криптовалюти
    get_crypto_price(selected_crypto)

# Створення головного вікна програми
root = tk.Tk()
root.title("Криптовалютний трекер")

# Створення та налаштування віджетів
crypto_label = tk.Label(root, text="Виберіть криптовалюту:")
crypto_label.pack(pady=10)

# Список символів криптовалют для вибору
crypto_symbols = ["BTC", "ETH", "LTC", "XRP"]
crypto_combobox = ttk.Combobox(root, values=crypto_symbols)
crypto_combobox.pack(pady=10)
crypto_combobox.set(crypto_symbols[0])  # Задання значення за замовчуванням

# Кнопка для отримання курсу вибраної криптовалюти
get_price_button = tk.Button(root, text="Отримати курс")
get_price_button.pack(pady=10)
# Прив'язка події натискання на кнопку до відповідної функції
get_price_button.bind("<Button-1>", lambda event: on_crypto_selected(event))

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запуск головного циклу Tkinter
root.mainloop()
