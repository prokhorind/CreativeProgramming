from easygui import *
import requests


def get_exchange_rates():
    """Функція для отримання актуальних курсів валют через API ПриватБанку."""
    try:
        response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
        response.raise_for_status()
        data = response.json()  # Отримуємо список валют

        # Перетворюємо список у словник для зручності
        rates = {}
        for item in data:
            base_currency = item["ccy"]
            target_currency = item["base_ccy"]
            rates[f"{base_currency}_to_{target_currency}"] = float(item["sale"])
            rates[f"{target_currency}_to_{base_currency}"] = 1 / float(item["sale"])

        return rates
    except requests.exceptions.RequestException as e:
        msgbox(f"Error loading exchange rates: {e}")
        return None


# Завантаження курсів валют
rates = get_exchange_rates()

if rates:
    rep = True
    while rep:
        currencies = ['EUR to UAH', 'UAH to EUR', 'USD to UAH', 'UAH to USD']
        choice = buttonbox('Оберіть конверсію:', choices=currencies)

        amount = float(enterbox('Введіть суму для конвертації:'))

        # Словник для відповідності між обраною конверсією та API-курсом
        currency_mapping = {
            'EUR to UAH': rates.get('EUR_to_UAH', 'Недоступно'),
            'UAH to EUR': rates.get('UAH_to_EUR', 'Недоступно'),
            'USD to UAH': rates.get('USD_to_UAH', 'Недоступно'),
            'UAH to USD': rates.get('UAH_to_USD', 'Недоступно'),
        }

        exchange_rate = currency_mapping[choice]

        if exchange_rate == 'Недоступно':
            msgbox("Курс для цієї операції наразі недоступний.")
        else:
            result = amount * exchange_rate
            msgbox(f'Результат: {amount:.2f} {choice.split(" ")[0]} = {result:.2f} {choice.split(" ")[2]}')

        repeat = buttonbox('Ще раз?', choices=['Так', 'Ні'])
        if repeat == 'Ні':
            rep = False
