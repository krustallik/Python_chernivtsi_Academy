import requests
import json
import tkinter as tk
from tkinter import ttk
from datetime import datetime

def get_crypto_price(crypto_symbol):
    api_url = f'https://api.coinbase.com/v2/prices/{crypto_symbol}-USD/spot'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'amount' in data['data']:
            price = data['data']['amount']
            # Тут ми використовуємо datetime для отримання поточного часу
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result_label.config(text=f'Поточний курс {crypto_symbol}: ${price}\nОновлено: {now}')
        else:
            result_label.config(text='Хибний формат відповіді від API')
    except requests.exceptions.RequestException as e:
        result_label.config(text=f'Помилка запиту: {e}')

def on_crypto_selected(event):
    selected_crypto = crypto_combobox.get()
    get_crypto_price(selected_crypto)

# Створення головного вікна
root = tk.Tk()
root.title("Криптовалютний трекер")

# Створення та налаштування віджетів
crypto_label = tk.Label(root, text="Виберіть криптовалюту:")
crypto_label.pack(pady=10)

crypto_symbols = ["BTC", "ETH", "LTC", "XRP"]  # Додайте інші символи за потребою
crypto_combobox = ttk.Combobox(root, values=crypto_symbols)
crypto_combobox.pack(pady=10)
crypto_combobox.set(crypto_symbols[0])  # Задайте значення за замовчуванням

get_price_button = tk.Button(root, text="Отримати курс")
get_price_button.pack(pady=10)
get_price_button.bind("<Button-1>", lambda event: on_crypto_selected(event))

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запуск головного циклу Tkinter
root.mainloop()
