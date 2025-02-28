import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        url = "https://bank.gov.ua/ua/markets/exchangerates"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # Знаходимо курс долара США (код валюти 840)
            usd_row = soup.find("td", text="840").find_parent("tr")
            exchange_rate = float(usd_row.find_all("td")[4].text.replace(",", "."))
            return exchange_rate
        else:
            raise Exception("Не вдалося отримати курс валют!")

    def uah_to_usd(self, uah_amount):
        return uah_amount / self.exchange_rate

if __name__ == "__main__":
    converter = CurrencyConverter()
    
    print(f"Курс USD/UAH: {converter.exchange_rate}")
    
    try:
        uah_amount = float(input("Введіть кількість гривень: "))
        usd_amount = converter.uah_to_usd(uah_amount)
        print(f"{uah_amount} грн = {usd_amount:.2f} доларів США")
    except ValueError:
        print("Будь ласка, введіть коректне числове значення.")
